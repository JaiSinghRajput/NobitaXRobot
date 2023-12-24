"""
pyromod - A monkeypatcher add-on for Pyrogram
Copyright (C) 2020 Cezar H. <https://github.com/usernein>

This file is part of pyromod.

pyromod is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pyromod is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pyromod.  If not, see <https://www.gnu.org/licenses/>.
"""
from contextlib import asynccontextmanager, contextmanager
from inspect import iscoroutinefunction
from logging import getLogger
from typing import Callable

from pyrogram.sync import async_to_sync

logger = getLogger("nobita")


class PyromodConfig:
    timeout_handler = None
    stopped_handler = None
    throw_exceptions = True
    unallowed_click_alert = True
    unallowed_click_alert_text = "[pyromod] You're not expected to click this button."


def patch(obj):
    def is_patchable(item):
        return getattr(item[1], "patchable", False)

    def wrapper(container):
        for name, func in filter(is_patchable, container.__dict__.items()):
            old = getattr(obj, name, None)
            if old is not None:  # Not adding 'old' to new func
                setattr(obj, f"old{name}", old)

            # Worse Code
            tempConf = {
                i: getattr(func, i, False)
                for i in ["is_property", "is_static", "is_context"]
            }

            async_to_sync(container, name)
            func = getattr(container, name)

            for tKey, tValue in tempConf.items():
                setattr(func, tKey, tValue)

            if func.is_property:
                func = property(func)
            elif func.is_static:
                func = staticmethod(func)
            elif func.is_context:
                if iscoroutinefunction(func.__call__):
                    func = asynccontextmanager(func)
                else:
                    func = contextmanager(func)

            logger.info(
                f"Patch Attribute To {obj.__name__} From {container.__name__} : {name}"
            )
            setattr(obj, name, func)
        return container

    return wrapper


def patchable(
    is_property: bool = False, is_static: bool = False, is_context: bool = False
) -> Callable:
    """
    A decorator that marks a function as patchable.

    Usage:

        @patchable(is_property=True)
        def my_property():
            ...

        @patchable(is_static=True)
        def my_static_method():
            ...

        @patchable(is_context=True)
        def my_context_manager():
            ...

        @patchable(is_property=False, is_static=False, is_context=False)
        def my_function():
            ...

        @patchable()
        def default_usage():
            ...

    Parameters:
        - is_property (bool): whether the function is a property. Default is False.
        - is_static (bool): whether the function is a static method. Default is False.
        - is_context (bool): whether the function is a context manager. Default is False.

    Returns:
        - A callable object that marks the function as patchable.
    """

    def wrapper(func: Callable) -> Callable:
        func.patchable = True
        func.is_property = is_property
        func.is_static = is_static
        func.is_context = is_context
        return func

    return wrapper

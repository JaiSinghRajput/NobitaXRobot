import asyncio
from typing import Union

from pyrogram import Client


async def edit_message_text(
    self,
    chat_id: Union[int, str],
    message_id: int,
    text: str,
    del_in: int = 0,
    *args,
    **kwargs
) -> Union["Message", bool]:
    """\nExample:
            message.edit_text("hello")
    Parameters:
        chat_id (``int`` | ``str``):
            Unique identifier (int) or username (str) of the target chat.
            For your personal cloud (Saved Messages)
            you can simply use "me" or "self".
            For a contact that exists in your Telegram address book
            you can use his phone number (str).
        message_id (``int``):
            Message identifier in the chat specified in chat_id.
        text (``str``):
            New text of the message.
        del_in (``int``):
            Time in Seconds for delete that message.
        parse_mode (:obj:`enums.ParseMode`, *optional*):
            By default, texts are parsed using
            both Markdown and HTML styles.
            You can combine both syntaxes together.
            Pass "markdown" or "md" to enable
            Markdown-style parsing only.
            Pass "html" to enable HTML-style parsing only.
            Pass None to completely disable style parsing.
        entities (List of :obj:`~pyrogram.types.MessageEntity`):
            List of special entities that appear in message text,
            which can be specified instead of *parse_mode*.
        disable_web_page_preview (``bool``, *optional*):
            Disables link previews for links in this message.
        reply_markup (:obj:`InlineKeyboardMarkup`, *optional*):
            An InlineKeyboardMarkup object.
    Returns:
        On success, the edited
        :obj:`Message` or True is returned.
    Raises:
        RPCError: In case of a Telegram RPC error.
    """
    msg = await self.edit_message_text(
        chat_id=chat_id, message_id=message_id, text=text, *args, **kwargs
    )
    if del_in == 0:
        return msg
    await asyncio.sleep(del_in)
    return bool(await msg.delete())


Client.edit_msg_text = edit_message_text

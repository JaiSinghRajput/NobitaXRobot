"""
MIT License

Copyright (c) 2023 TheHamkerCat

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import re
from datetime import datetime, timedelta

from pyrogram import filters
from pyrogram.types import ChatPermissions
from pyrogram.errors import ChatAdminRequired

from database.blacklist_db import (
    delete_blacklist_filter,
    get_blacklisted_words,
    save_blacklist_filter,
)
from nobita import app
from nobita.core.decorator.errors import capture_err
from nobita.core.decorator.permissions import adminsOnly, list_admins
from nobita.vars import SUDO

__MODULE__ = "Blacklist"
__HELP__ = """
/blacklisted - Get All The Blacklisted Words In The Chat.
/blacklist [WORD|SENTENCE] - Blacklist A Word Or A Sentence.
/whitelist [WORD|SENTENCE] - Whitelist A Word Or A Sentence.
"""


@app.on_message(filters.command("blacklist") & ~filters.private)
@adminsOnly("can_restrict_members")
async def save_filters(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/blacklist [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("**Usage**\n__/blacklist [WORD|SENTENCE]__")
    chat_id = message.chat.id
    await save_blacklist_filter(chat_id, word)
    await message.reply_text(f"__**Blacklisted {word}.**__")


@app.on_message(filters.command("blacklisted") & ~filters.private)
@capture_err
async def get_filterss(_, message):
    data = await get_blacklisted_words(message.chat.id)
    if not data:
        await message.reply_text("**No blacklisted words in this chat.**")
    else:
        msg = f"List of blacklisted words in {message.chat.title} :\n"
        for word in data:
            msg += f"**-** `{word}`\n"
        await message.reply_text(msg)


@app.on_message(filters.command("whitelist") & ~filters.private)
@adminsOnly("can_restrict_members")
async def del_filter(_, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage:\n/whitelist [WORD|SENTENCE]")
    word = message.text.split(None, 1)[1].strip()
    if not word:
        return await message.reply_text("Usage:\n/whitelist [WORD|SENTENCE]")
    chat_id = message.chat.id
    deleted = await delete_blacklist_filter(chat_id, word)
    if deleted:
        return await message.reply_text(f"**Whitelisted {word}.**")
    await message.reply_text("**No such blacklist filter.**")


@app.on_message(filters.text & ~filters.private, group=8)
@capture_err
async def blacklist_filters_re(self, message):
    text = message.text.lower().strip()
    if not text:
        return
    chat_id = message.chat.id
    user = message.from_user
    if not user:
        return
    if user.id in SUDO:
        return
    list_of_filters = await get_blacklisted_words(chat_id)
    for word in list_of_filters:
        pattern = r"( |^|[^\w])" + re.escape(word) + r"( |$|[^\w])"
        if re.search(pattern, text, flags=re.IGNORECASE):
            if user.id in await list_admins(chat_id):
                return
            try:
                await message.delete_msg()
                await message.chat.restrict_member(
                    user.id,
                    ChatPermissions(all_perms=False),
                    until_date=datetime.now() + timedelta(hours=1),
                )
            except ChatAdminRequired:
                return await message.reply("Please give me admin permissions to blacklist user", quote=False)
            except Exception as err:
                self.log.info(f"ERROR Blacklist Chat: ID = {chat_id}, ERR = {err}")
                return
            await app.send_message(
                chat_id,
                f"Muted {user.mention} [`{user.id}`] for 1 hour "
                + f"due to a blacklist match on {word}.",
            )

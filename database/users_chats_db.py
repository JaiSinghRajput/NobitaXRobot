from async_pymongo import AsyncClient

from nobita.vars import DATABASE_NAME, DATABASE_URI


class UsersData:
    def __init__(self, uri, database_name):
        self._client = AsyncClient(uri)
        self.db = self._client[database_name]
        self.col = self.db["userlist"]
        self.grp = self.db["groups"]

    @staticmethod
    def new_user(id, name):
        return dict(
            id=id,
            name=name,
            ban_status=dict(
                is_banned=False,
                ban_reason="",
            ),
        )

    @staticmethod
    def new_group(id, title):
        return dict(
            id=id,
            title=title,
            chat_status=dict(
                is_disabled=False,
                reason="",
            ),
        )

    async def add_user(self, id, name):
        user = self.new_user(id, name)
        await self.col.insert_one(user)

    async def is_user_exist(self, id):
        user = await self.col.find_one({"id": int(id)})
        return bool(user)

    async def total_users_count(self):
        return await self.col.count_documents({})

    async def remove_ban(self, id):
        return await self.col.delete_one({"_id": id})

    async def ban_user(self, user_id, ban_reason="No Reason"):
        return await self.col.insert_one({"_id": user_id, "reason": ban_reason})

    async def get_ban_status(self, id):
        user = await self.col.find_one({"_id": int(id)})
        if user:
            return True, user
        return False, None

    async def get_all_users(self):
        return self.col.find({})

    async def delete_user(self, user_id):
        await self.col.delete_many({"id": int(user_id)})

    async def is_chat_exist(self, id):
        user = await self.grp.find_one({"id": int(id)})
        return bool(user)

    async def get_banned(self):
        users = self.col.find({"ban_status.is_banned": True})
        chats = self.grp.find({"chat_status.is_disabled": True})
        b_chats = [chat["id"] async for chat in chats]
        b_users = [user["id"] async for user in users]
        return b_users, b_chats

    async def add_chat(self, chat, title):
        chat = self.new_group(chat, title)
        await self.grp.insert_one(chat)

    async def get_chat(self, chat):
        chat = await self.grp.find_one({"id": int(chat)})
        return chat.get("chat_status") if chat else False

    async def re_enable_chat(self, id):
        chat_status = dict(
            is_disabled=False,
            reason="",
        )
        await self.grp.update_one(
            {"id": int(id)}, {"$set": {"chat_status": chat_status}}
        )

    async def disable_chat(self, chat, reason="No Reason"):
        chat_status = dict(
            is_disabled=True,
            reason=reason,
        )
        await self.grp.update_one(
            {"id": int(chat)}, {"$set": {"chat_status": chat_status}}
        )

    async def total_chat_count(self):
        return await self.grp.count_documents({})

    async def get_all_chats(self):
        return self.grp.find({})

    async def get_db_size(self):
        return (await self.db.command("dbstats"))["dataSize"]


db = UsersData(DATABASE_URI, DATABASE_NAME)

# * @author        nobi Aris M <jaisinghmitrc+bot@gmail.com>
# * @date          2024-11-21 22:12:27
# * @projectName   NobitaXRobot
# * Copyright ©Nobi-Pro All rights reserved
import time, os, uvloop
from asyncio import get_event_loop
from faulthandler import enable as faulthandler_enable
from logging import ERROR, INFO, StreamHandler, basicConfig, getLogger, handlers

from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from async_pymongo import AsyncClient
from pymongo import MongoClient
from pyrogram import Client

from nobita.vars import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    DATABASE_NAME,
    DATABASE_URI,
    TZ,
    USER_SESSION,
)

basicConfig(
    level=INFO,
    format="[%(levelname)s] - [%(asctime)s - %(name)s - %(message)s] -> [%(module)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        handlers.RotatingFileHandler("nobitaLogs.txt", mode="w+", maxBytes=5242880, backupCount=1),
        StreamHandler(),
    ],
)
getLogger("pyrogram").setLevel(ERROR)
getLogger("openai").setLevel(ERROR)
getLogger("httpx").setLevel(ERROR)
getLogger("iytdl").setLevel(ERROR)

MOD_LOAD = []
MOD_NOLOAD = ["subscene_dl"]
HELPABLE = {}
cleanmode = {}
botStartTime = time.time()
nobita_version = "v2.12.2 - Stable"

uvloop.install()
faulthandler_enable()
from nobita.core import nobita_patch

# Pyrogram Bot Client
app = Client(
    "nobitaBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    mongodb=dict(connection=AsyncClient(DATABASE_URI), remove_peers=False),
    sleep_threshold=180,
    app_version="NobitaXRobot Stable",
    workers=50,
    max_concurrent_transmissions=20,
)
app.db = AsyncClient(DATABASE_URI)
app.log = getLogger("nobita")

# Pyrogram UserBot Client
user = Client(
    "nobiUBot",
    session_string=USER_SESSION,
    mongodb=dict(connection=AsyncClient(DATABASE_URI), remove_peers=False),
    sleep_threshold=180,
)

jobstores = {
    "default": MongoDBJobStore(
        client=MongoClient(DATABASE_URI), database=DATABASE_NAME, collection="nightmode"
    )
}
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=TZ)

app.start()
BOT_ID = app.me.id
BOT_NAME = app.me.first_name
BOT_USERNAME = app.me.username
if USER_SESSION:
    user.start()
    UBOT_ID = user.me.id
    UBOT_NAME = user.me.first_name
    UBOT_USERNAME = user.me.username
else:
    UBOT_ID = None
    UBOT_NAME = None
    UBOT_USERNAME = None

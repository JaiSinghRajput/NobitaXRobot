"""
 * @author        nobi <jaisinghmitrc+bot@gmail.com>
 * @date          2022-09-06 10:12:09
 * @projectName   NobitaXRobot
 * Copyright @Nobi-Pro All rights reserved
"""
from async_pymongo import AsyncClient

from nobita.vars import DATABASE_NAME, DATABASE_URI

mongo = AsyncClient(DATABASE_URI)
dbname = mongo[DATABASE_NAME]

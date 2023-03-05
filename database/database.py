
import pymongo
import os
from config import DB_URI, DB_NAME


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']


async def present_user(user_id: int, bot_username: str = False):
    return bool(user_data.find_one({'_id': user_id, 'bot_username': bot_username}))


async def add_user(user_id: int, bot_username: str = False):
    user_data.insert_one({'_id': user_id, 'bot_username': bot_username})
    return


async def full_userbase():
    return user_data.find()


async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

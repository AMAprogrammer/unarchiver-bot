from pymongo import MongoClient
from local_dbconfig import host

client = MongoClient(host=host)

unarchive_db = client["unarchive"]

users = unarchive_db["users"]
admins = unarchive_db["admins"]
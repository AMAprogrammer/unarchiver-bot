from local_botconfig import api_id, api_hash, bot_token
from pyrogram import Client

bot = Client(
    name="Unarchiver",
    api_id=api_id,
    api_hash=api_hash,
    bot_token=bot_token
)
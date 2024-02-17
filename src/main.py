from botconfig import bot
from pyrogram import filters
from pyrogram.types import Message
from dbconfig import admins, users
from keyboards import main_keyboard
from tools import unarchive


@bot.on_message(filters=filters.private & filters.text)
async def handler(client, message:Message):
    text = message.text
    chat_id = message.chat.id
    
    user = users.find_one({"_id":chat_id})
    if not user:
        try:
            users.insert_one({
                "_id":chat_id,
                "step":"home"
            })
        except:
            await bot.send_message(chat_id=chat_id, text="error!\ntry again /start")
        else:
            await bot.send_message(chat_id=chat_id, text="Welcome to Unarchive Bot",reply_markup=main_keyboard)

    else:
        step = user["step"]
        
        
    if text == "/start":
        try:
            users.update_one({"_id":chat_id},{"$set":{"step":"home"}})
        except:
            await bot.send_message(chat_id=chat_id,text="error!\ntry again /start")
        else:
            await bot.send_message(chat_id=chat_id, text="Welcome to Unarchive Bot",reply_markup=main_keyboard)
        
    elif step == "home":
        
        if text == "Unarchive":
            try:
                users.update_one({"_id":chat_id},{"$set":{"step":"send_file"}})
            except:
                await bot.send_message(chat_id=chat_id, text="error!\n try again /start")
            else:
                await bot.send_message(chat_id=chat_id, text="send an archive file")
                
    elif step == "send_file":
        try:
            message.download()
        except:
            await bot.send_message(chat_id=chat_id,text="error!\ntry again /start")
        else:
            try:
                users.update_one({"_id":chat_id},{"$set":{"step":"send_password"}})
            except:
                await bot.send_message(chat_id=chat_id,text="error!\ntry again /start")
            else:
                await bot.send_message(chat_id=chat_id,text="send the password\n if the file is not protected send ``None``")
    
    elif step == "send_password":
        
        password = message.text
        
        result = unarchive(file_adress="", password="")  #TODO: edit and compelete this
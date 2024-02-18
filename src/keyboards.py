from pyrogram.types import ReplyKeyboardMarkup


main_keyboard = ReplyKeyboardMarkup(
    [
        ["Unarchive"]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)



none_password = ReplyKeyboardMarkup(
    [
        ["the file is not locked"]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
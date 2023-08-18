# import telebot

# bot = telebot.TeleBot("")


# print(bot.ban_chat_member("@suorcee", ))

import pyrogram
from pyrogram import filters


bot = pyrogram.Client("c", api_hash="b53d2d46ddff41ee2353256559b4c4c2", api_id=23164619, bot_token="6254468029:AAEuWgaIqZXBEG3vTiSS6D09NnU0LMpKmG0")
# bot.start()

@bot.on_message(filters=filters.command(['start']))
def sayHello(api, message):
    bot.send_message(message.chat.id, "Hello")


bot.run()


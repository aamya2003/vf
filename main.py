# import telebot

# bot = telebot.TeleBot("")


# print(bot.ban_chat_member("@suorcee", ))

import pyrogram
from pyrogram import filters


bot = pyrogram.Client("c", api_hash="b53d2d46ddff41ee2353256559b4c4c2", api_id=23164619, bot_token="6409008239:AAENDzlZ7dOo1oP_bY6lZZZqq5pQ0vexQ94")
# bot.start()

@bot.on_message(filters=filters.command(['start']))
def sayHello(api, message):
    bot.send_message(message.chat.id, "Hello")
from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return "<b> hello</b>"

def run():
  app.run(host='0.0.0.0', port=8080)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

bot.run()


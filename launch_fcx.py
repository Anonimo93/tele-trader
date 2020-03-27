
import os

from flask import Flask, request
import telebot
from core import fcx_markup
from telegram import ReplyKeyboardMarkup, KeyboardButton


TOKEN = "746406709:AAHGsGOKxHwPOhRMdUOM5JNKsVxI2cCTbyQ"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


keys = ReplyKeyboardMarkup(keyboard=fcx_markup, resize_keyboard=True)
text = "this is a test suit"


@bot.message_handler(commands=['start'])
def start(message):
    # bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    chat_id = 1053579181
    bot.send_message(chat_id, text=text, reply_markup=keys)






@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!getmessage", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://fcx-bot.herokuapp.com/' + TOKEN)
    return "!webhook", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

import telebot
import os
from threading import Thread
from dotenv import load_dotenv
from app import keep_alive


load_dotenv()

TELEGRAM_BOT_KEY = os.getenv('TELEGRAM_BOT_KEY')

bot = telebot.TeleBot(TELEGRAM_BOT_KEY)

print(bot)

@bot.message_handler(commands = ['hello'])
def greet(message):
    bot.send_message(message.chat.id, "Hello")

bot.polling()
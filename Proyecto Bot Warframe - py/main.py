import telebot
from dotenv import load_dotenv
import os

load_dotenv()

TelegramToken = os.getenv("TelegramToken")
bot = telebot.TeleBot(TelegramToken) 

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	

bot.polling()
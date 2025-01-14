import telebot
from dotenv import load_dotenv
import os
load_dotenv()


TelegramToken = os.getenv("TelegramToken") #Esta linea lo que hace es que trae el Token desde el dotenv
bot = telebot.TeleBot(TelegramToken) #Con esta linea conectamos el bot a Telegram

@bot.message_handler(content_types= ["text", "sticker"])
def send_welcome(message):
	bot.reply_to(message, "Welcome Operator! I am Ordis, your personal assistant. I can help you with the current rotations of different missions, here everything I am able to perform: \n /Relics to see the active fissures on the map. \n /Rotation to see the Night/Day cycle of the Earth. \n /VoidTrader To see the things that brings the Void Trader if it is available. \n /StatusWorlds To see the statuses of the 3 important open worlds.")
	

bot.polling() #Con esta inicializamos el bot
import telebot
from dotenv import load_dotenv
import os
load_dotenv()
from Eventos.fissure import Fissures
from Eventos.earthRotation import Rotation


TelegramToken = os.getenv("TelegramToken") #Esta linea lo que hace es que trae el Token desde el dotenv
bot = telebot.TeleBot(TelegramToken) #Con esta linea conectamos el bot a Telegram

#Lo que hace esta parte del script es que toma cualquier mensaje que no tenga "/", entonces manda el mensaje de inicio.
@bot.message_handler(func=lambda message: not message.text.startswith('/'), content_types=["text", "sticker"])
def send_welcome(message):
    bot.reply_to( message,
        "Welcome Operator! I am Ordis, your personal assistant. I can help you with the current rotations of different missions. Here is everything I can perform: \n"
        "/Relics - See the active fissures on the map.\n"
        "/Rotation - See the Night/Day cycle of the Earth.\n"
        "/VoidTrader - See the things the Void Trader brings, if available.\n"
        "/StatusWorlds - See the statuses of the three important open worlds."
    )
    
#Comando de Eventos 
@bot.message_handler(commands=["Relics", "Relic", "relics", "relic"])
def FissureVoid(message):
    FissuresInfo = Fissures() 
    bot.reply_to(message, FissuresInfo, "\n aaaaaaaa")

@bot.message_handler(commands=["Rotation", "rotation"])
def FissureVoid(message):
    RotationInfo = Rotation() 
    bot.reply_to(message, RotationInfo)

@bot.message_handler(func=lambda message: message.text.startswith('/'))
def unknown_command(message):
    bot.reply_to(message, "Sorry, Operator, I do not recognize that command. Please try one of the available commands.")

bot.polling() #Con esta inicializamos el bot
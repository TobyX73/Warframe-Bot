import telebot
from dotenv import load_dotenv
import os
load_dotenv()
from Eventos.fissure import FissuresInfo
from Eventos.earthRotation import RotationInfo
from Eventos.voidTrader import voidTraderInfo
from Eventos.openWorldStatus import openWorldInfo


TelegramToken = os.getenv("TelegramToken") #Esta linea lo que hace es que trae el Token desde el dotenv
bot = telebot.TeleBot(TelegramToken) #Con esta linea conectamos el bot a Telegram

#Lo que hace esta parte del script es que toma cualquier mensaje que no tenga "/", entonces manda el mensaje de inicio.
@bot.message_handler(func=lambda message: not message.text.startswith('/'), content_types=["text", "sticker"])
def SendWelcome(message):
    bot.reply_to( message,
        "Welcome Operator! I am Ordis, your personal assistant. I can help you with the current rotations of different missions. Here is everything I can perform: \n"
        "/Relics - See the active fissures on the map.\n"
        "/Rotation - See the Night/Day cycle of the Earth.\n"
        "/VoidTrader - See the things the Void Trader brings, if available.\n"
        "/StatusWorlds - See the statuses of the three important open worlds."
    )
    
#Comando de Eventos 
#Reliquias
@bot.message_handler(commands=["Relics", "Relic", "relics", "relic"])
def FissureVoid(message):
    VoidFissuresInfo = FissuresInfo() 
    bot.reply_to(message, VoidFissuresInfo)

#Rotación de Tierra
@bot.message_handler(commands=["Rotation", "rotation"])
def EarthRotation(message):
    EarthRotationInfo = RotationInfo() 
    bot.reply_to(message, EarthRotationInfo)

#Comerciante del Vacio
@bot.message_handler(commands=["VoidTrader", "voidtrader"])
def VoidTrader(message):
    TraderInfo = voidTraderInfo() 
    bot.reply_to(message, TraderInfo)

#Mundo abierto
@bot.message_handler(commands=["StatusWorlds", "statusworlds"])
def OpenWorld(message):
    WorldInfo = openWorldInfo() 
    bot.reply_to(message, WorldInfo)

#No reconocer comando
@bot.message_handler(func=lambda message: message.text.startswith('/'))
def UnknownCommand(message):
    bot.reply_to(message, "Sorry, Operator, I do not recognize that command. Please try one of the available commands.")


bot.polling() #Con esta inicializamos el bot
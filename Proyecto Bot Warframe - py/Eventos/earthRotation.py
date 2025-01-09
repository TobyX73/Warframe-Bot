import requests
import json

url = 'https://api.warframestat.us/pc/earthCycle/'
response = requests.get(url)
data = json.loads(response.text)

if isinstance (data, dict):
    if data.get ('isDay', False):
        print ("La rotacion de la tierra esta en Dia")
        print (f"Tiempo restante: {data.get('timeLeft')}")
    else:
        print ("La rotacion de la tierra esta en Noche")
        print (f"Tiempo restante: {data.get('timeLeft')}")
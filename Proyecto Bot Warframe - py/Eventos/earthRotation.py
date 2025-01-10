import requests
import json

url = 'https://api.warframestat.us/pc/earthCycle/'
response = requests.get(url)
data = json.loads(response.text)


#En este bloque de funcion lo unico que hago es checkear si el parametro 'isDay'
#es true o false para dar su respectivo mensaje con el tiempo que tardara en rotar al siguiente
if isinstance (data, dict):
    if data.get ('isDay', False):
        print ("La rotacion de la tierra esta en Dia")
    else:
        print ("La rotacion de la tierra esta en Noche")
    print (f"Tiempo restante: {data.get('timeLeft')}")
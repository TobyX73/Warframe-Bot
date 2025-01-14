import requests
import json

url = 'https://api.warframestat.us/pc/earthCycle/'
response = requests.get(url)
data = json.loads(response.text)


#En este bloque de funcion lo unico que hago es checkear si el parametro 'isDay'
#es true o false para dar su respectivo mensaje con el tiempo que tardara en rotar al siguiente
if isinstance(data, dict):
    if data.get('isDay', False):
        print("Earth's rotation is in Daytime")
    else:
        print("Earth's rotation is in Nighttime")
    print(f"Time remaining: {data.get('timeLeft')}")

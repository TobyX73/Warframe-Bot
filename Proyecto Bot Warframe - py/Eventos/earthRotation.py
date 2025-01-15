import requests
import json

url = 'https://api.warframestat.us/pc/earthCycle/'
response = requests.get(url)
data = json.loads(response.text)


#En este bloque de funcion lo unico que hago es checkear si el parametro 'isDay'
#es true o false para dar su respectivo mensaje con el tiempo que tardara en rotar al siguiente
def RotationInfo():
    if isinstance(data, dict):
        if data.get('isDay', False):
            return (f"Earth's rotation is in Daytime, time remaining: {data.get('timeLeft')}")
        else:
            return(f"Earth's rotation is in Nighttime, Time remaining: {data.get('timeLeft')}")
    else:
        return ("Could not connect to the API") 
    
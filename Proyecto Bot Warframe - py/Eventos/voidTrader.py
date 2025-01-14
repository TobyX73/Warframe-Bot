import requests
import json

url = 'https://api.warframestat.us/pc/voidTrader/'
response = requests.get(url)
data = json.loads(response.text)


#En este caso usamos isinstance para checkear primero que la data es un DICCIONARIO, no como en el caso de las reliquias que son una lista de objetos que tienen diccionarios apartes
#Checkeo si el comerciante esta activo y pasa todos sus datos, hasta llegar a un for donde despliega item por item y muestra sus precios
#En caso de que no este mostrara el tiempo en que tardara en llegar
if isinstance(data, dict):
    if data.get('active', False):
        print('The Void Trader is active')
        print(f"Location: {data.get('location', 'Unknown')}")
        print(f"Leaves in: {data.get('endString', 'Unknown')}")
        print("Items brought: ")
        print("-------------------------")
        for item in data.get('inventory', []):
            if isinstance(item, dict):
                print(f"Name: {item.get('item', 'Unknown')}")
                print(f"Price in Ducats: {item.get('ducats', 'Unknown')}")
                print(f"Price in Credits: {item.get('credits', 'Unknown')}")
                print("---------------------------")
    else:
        print(f"The Void Trader is not active, will arrive in: {data.get('startString', 'Unknown')}")
else: 
    print("Could not connect to the API")


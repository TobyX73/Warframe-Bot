import requests
import json

url = 'https://api.warframestat.us/pc/voidTrader/'
response = requests.get(url)
data = json.loads(response.text)


#En este caso usamos isinstance para checkear primero que la data es un DICCIONARIO, no como en el caso de las reliquias que son una lista de objetos que tienen diccionarios apartes
#Checkeo si el comerciante esta activo y pasa todos sus datos, hasta llegar a un for donde despliega item por item y muestra sus precios
#En caso de que no este mostrara el tiempo en que tardara en llegar
def voidTraderInfo():
    TraderInfo = []  # Array para almacenar la información
    if isinstance(data, dict):
        if data.get('active', False):
            ActiveTrader = (
                "The Void Trader is active\n"
                f"Location: {data.get('location', 'Unknown')}\n"
                f"Leaves in: {data.get('endString', 'Unknown')}\n"
                "Items brought:\n"
                "-------------------------"
            )
            TraderInfo.append(ActiveTrader)

            # Agregar información de los ítems
            for item in data.get('inventory', []):
                if isinstance(item, dict):
                    ItemsTrader = (
                        f"Name: {item.get('item', 'Unknown')}\n"
                        f"Price in Ducats: {item.get('ducats', 'Unknown')}\n"
                        f"Price in Credits: {item.get('credits', 'Unknown')}\n"
                        "---------------------------"
                    )
                    TraderInfo.append(ItemsTrader)
            return "\n".join(TraderInfo)  # Devolver toda la información como un string unificado
        else:
            return f"The Void Trader is not active, will arrive in: {data.get('startString', 'Unknown')}"
    else:
        return "Could not connect to the API"



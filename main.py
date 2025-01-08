import requests
import json

url = 'https://api.warframestat.us/pc/fissures'
response = requests.get(url)
data = json.loads(response.text)

# Iterar sobre los datos y extraer información relevante
if isinstance(data, list):
    for fissure in data:
        print(f"Tipo de reliquia: {fissure.get('tier', 'Desconocido')}")
        print(f"Nodo: {fissure.get('node', 'Desconocido')}")
        print(f"Tipo de misión: {fissure.get('missionType', 'Desconocido')}")
        print(f"Estado: {fissure.get('active', 'Desconocido')}")
        print("-------------------")
else:
    print("El formato de los datos ha cambiado o no se encontraron fisuras.")

#toby


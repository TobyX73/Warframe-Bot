import requests
import json

url = "https://api.warframestat.us/pc/fissures"
response = requests.get(url)
data = json.loads(response.text)

# Usé la funcion insinstance para comprobar si "data" es una lista, ya que es caso de que sea otra cosa va a tira error
#Luego entra a un ciclo for donde cada fisura dentro de esta lista "data" imprime los datos de las fisuras al momento con el .get
# Iterar sobre los datos y extraer información relevante
if isinstance(data, list):
    for fissure in data:
        print(f"Relic type: {fissure.get('tier', 'Unknown')}")
        print(f"Node: {fissure.get('node', 'Unknown')}")
        print(f"Mission type: {fissure.get('missionType', 'Unknown')}")
        print(f"Status: {fissure.get('active', 'Unknown')}")
        print(f"Required level: {fissure.get('enemyLevels', 'Not specified')}")
        isSteelPath = fissure.get('isHard', False)  
        print(f"Steel Path: {'Yes' if isSteelPath else 'No'}")
        print("-------------------")
else:
    print("The data format has changed or no fissures were found.")




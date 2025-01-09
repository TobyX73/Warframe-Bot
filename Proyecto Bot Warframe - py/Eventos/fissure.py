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
        print(f"Tipo de reliquia: {fissure.get("tier", "Desconocido")}")
        print(f"Nodo: {fissure.get("node", "Desconocido")}")
        print(f"Tipo de misión: {fissure.get("missionType", "Desconocido")}")
        print(f"Estado: {fissure.get("active", "Desconocido")}")
        print(f"Nivel requerido: {fissure.get("enemyLevels", "No especificado")}")
        isSteelPath = fissure.get("isHard", False)  
        print(f"Steel Path: {"Sí" if isSteelPath else "No"}")
        print("-------------------")
else:
    print("El formato de los datos ha cambiado o no se encontraron fisuras.")



import requests
import json

#En esta parte del codigo tuve que definir un diccionario de URLS ya que existen varios mundos abiertos, por lo tanto son 3 URLS de datos distintas
urls = {
    "Cetus (Earth)": "https://api.warframestat.us/pc/cetusCycle",
    "Orb Vallis (Venus)": "https://api.warframestat.us/pc/vallisCycle",
    "Cambion Drift (Deimos)": "https://api.warframestat.us/pc/cambionCycle"
}

#En este ciclo for, tenemos WORLD Y URL, lo que hace es que itera en cada URL y su clave es WORLD, el cual le pone el nombre al mundo abierto elegido
#Luego checkeamos de vuelta si el formato de data es un diccionario y describe a detalle cada uno de los mundos
#En este caso metemos el bloque de codigo de descripcion del mundo en el ciclo for, ya que itera por cada mundo y pone sus respectivos datos.
def openWorldInfo():
    worldInfo = []  # Lista para almacenar información de los mundos abiertos
    for world, url in urls.items():
        response = requests.get(url)
        data = json.loads(response.text)  # Parsear la respuesta en JSON
        if isinstance(data, dict):  # Verificar que la respuesta sea un diccionario
                eachWorldInfo = (
                    f"---- {world} ----- \n"
                    f"Current state: {data.get('state', 'Unknown')} \n"
                    f"Time remaining: {data.get('timeLeft', 'Unknown')} \n"
                    "--------------------"
                )
                worldInfo.append(eachWorldInfo)
    return "\n".join(worldInfo) if worldInfo else "Could not fetch data for any world."
 
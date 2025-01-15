import requests
import json

url = "https://api.warframestat.us/pc/fissures"
response = requests.get(url)
data = json.loads(response.text)


# Función que retorna toda la información de las fisuras
def Fissures():
    fissuresInfo = []  # Array para almacenar cada fisura
    if isinstance(data, list):
        for fissure in data:
            isSteelPath = fissure.get('isHard', False)
            fissure_info = (
                f"Relic type: {fissure.get('tier', 'Unknown')} \n" +
                f"Node: {fissure.get('node', 'Unknown')}  \n" +
                f"Mission type: {fissure.get('missionType', 'Unknown')} \n" +
                f"Status: {fissure.get('active', 'Unknown')} \n" +
                f"Steel Path: {'Yes' if isSteelPath else 'No'} \n" +
                "-------------------"
            )
            fissuresInfo.append(str(fissure_info))  # Agregar la información de cada fisura a la lista
        return "\n".join(fissuresInfo)  # Devuelve toda la lista unida de fisuras
    else:
        return "The data format has changed or no fissures were found."



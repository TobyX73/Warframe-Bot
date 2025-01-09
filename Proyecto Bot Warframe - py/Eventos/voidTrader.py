import requests
import json

url = 'https://api.warframestat.us/pc/voidTrader/'
response = requests.get(url)
data = json.loads(response.text)

if isinstance (data, dict):
  if data.get ('active', False):
      print ('El comerciante del Vacío está activo')
      print (f"Lugar: {data.get('location','Desconocido')}")
      print (f"Se va en: {data.get('endString','Desconocido')}")
      for item in ('inventory', []):
         print (f"Nombre: {item.get('item', 'Desconocido')}")
         print (f"Precio en Ducados: {item.get('ducats', 'Desconocido')}")
         print (f"Precio en Créditos: {item.get('credits', 'Desconocido')}")
         print ("---------------------------")
  else:
     print (f"El comerciante del Vacío no está activo, vendrá en: {data.get('startString', 'Desconocido')}")
else: 
   print ("No se pudo conectar a la API")
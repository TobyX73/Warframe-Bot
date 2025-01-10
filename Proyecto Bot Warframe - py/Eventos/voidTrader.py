import requests
import json

url = 'https://api.warframestat.us/pc/voidTrader/'
response = requests.get(url)
data = json.loads(response.text)


#En este caso usamos isinstance para checkear primero que la data es un DICCIONARIO, no como en el caso de las reliquias que son una lista de objetos que tienen diccionarios apartes
#Checkeo si el comerciante esta activo y pasa todos sus datos, hasta llegar a un for donde despliega item por item y muestra sus precios
#En caso de que no este mostrara el tiempo en que tardara en llegar
if isinstance (data, dict):
  if data.get ('active', False):
      print ('El comerciante del Vacío está activo')
      print (f"Lugar: {data.get('location','Desconocido')}")
      print (f"Se va en: {data.get('endString','Desconocido')}")
      print ("Items que trajo: ")
      print("-------------------------")
      for item in data.get('inventory', []):
         if isinstance(item, dict):
          print (f"Nombre: {item.get('item', 'Desconocido')}")
          print (f"Precio en Ducados: {item.get('ducats', 'Desconocido')}")
          print (f"Precio en Créditos: {item.get('credits', 'Desconocido')}")
          print ("---------------------------")
  else:
     print (f"El comerciante del Vacío no está activo, vendrá en: {data.get('startString', 'Desconocido')}")
else: 
   print ("No se pudo conectar a la API")


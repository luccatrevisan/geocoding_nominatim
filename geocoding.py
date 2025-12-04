"""
melhorias:
- deixar a busca mais específica.
    - a api permite uma busca mais detalhada do endereço com parâmetros diversos
- o que pode acontecer se for digitado um endereço errado?
    - faço um loop?
    - try/except?
"""
import urllib.request, urllib.parse, urllib.error
import json

address = input("Endereço: ")

api_url = "https://nominatim.openstreetmap.org/search?"
params = urllib.parse.urlencode( {"q" : address, "format" : "json"} )
url = api_url + params

data = urllib.request.urlopen(url)
info = data.read().decode()
jason = json.loads(info)

latitude = jason[0]["lat"]
longitude = jason[0]["lon"]

print(f"Latitude: {latitude}\nLongitude: {longitude}")

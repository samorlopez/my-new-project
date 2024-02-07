import urllib.request
import json

url = "http://api.openweathermap.org/data/2.5/weather?q=Seattle,US&appid=8372556c14f6a67a3322c1f451f1e3f7"
response = urllib.request.urlopen(url)
data = response.read()
parsed_data = json.loads(data)
print(parsed_data)
print(parsed_data.keys())
print(parsed_data["main"])
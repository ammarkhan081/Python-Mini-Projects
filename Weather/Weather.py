import requests
import json
city=input("Enter city:")
url=f'http://api.weatherapi.com/v1/current.json?key=e70917321e254b0c97573649241008&q={city}'
response=requests.get(url)
d=json.loads(response.text)
fd=json.dumps(d,indent=4)
print(fd)
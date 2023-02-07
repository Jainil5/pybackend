import requests
import json

response = requests.get("https://api.tomitokko.repl.co/")

print(response.status_code)

res = json.loads(response.text

)

import requests
import pprint

params = {
    "q": "http"
}

url = "https://api.github.com/search/repositories?q="

response = requests.get(url, params=params)

print(response.status_code)
pprint.pprint(response.json())

import requests

params = {
    "userId": 1
}

url = "https://jsonplaceholder.typicode.com/posts?userId="

response = requests.get(url, params=params)

print(response.status_code)
print(response.text)
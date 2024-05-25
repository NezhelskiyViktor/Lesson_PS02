import requests

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.post(url, data=data)

print(response.status_code)
print (f'ответ - {response.json()}')



import requests

url = 'http://192.168.0.215:8080/c'

headers = {
    'Content-type': 'application/json',
}

data6 = '{"text":"Six"}'

for i in range(1000):
    response = requests.post(url, headers=headers, data=data6)

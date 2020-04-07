import requests

url = 'http://192.168.0.215:8080/c'

headers = {
    'Content-type': 'application/json',
}

data1 = '{"text":"One"}'
data2 = '{"text":"Two"}'
data3 = '{"text":"Three"}'
data4 = '{"text":"Four"}'

for i in range(1):
    response = requests.post(url, headers=headers, data=data1)

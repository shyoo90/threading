#import os
#os.system('curl -X POST -H "Content-Type: application/json" -d "{\"name\": \"hello world\"}" http://192.168.0.215:8080/c')

import requests

url = 'http://192.168.0.215:8080/c'

headers = {
    'Content-type': 'application/json',
}

data1 = '{"text":"One"}'
data2 = '{"text":"Two"}'
data3 = '{"text":"Three"}'
data4 = '{"text":"Four"}'

for i in range(100):
    response = requests.post(url, headers=headers, data=data1)
    response = requests.post(url, headers=headers, data=data2)
    response = requests.post(url, headers=headers, data=data3)
    response = requests.post(url, headers=headers, data=data4)

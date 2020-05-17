import requests

url = "http://requestbin.net/r/10svs8v1"
json = {
    'mounth': 'May',
    'result': '1:0',
    'team': 'Manchester',
}

response = requests.post(url, json=json, data='Hi')
print(response.status_code)

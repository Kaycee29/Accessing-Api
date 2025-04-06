import requests
import json

url = 'http://api.football-data.org/v4/competitions/'

response = requests.get(url)

response_dict = response.json()

results = response_dict['competitions']

Competition_name = []

for result in results:
    Competition_name.append(test['name'])
print(Competition_name)
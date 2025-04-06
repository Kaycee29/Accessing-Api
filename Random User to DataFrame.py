import requests
import json
import os
import pandas as pd
import awswrangler as wr
from dotenv import load_dotenv

url = 'https://randomuser.me/api/?results=500'

response = requests.get(url)
response_dict = response.json()


Trials =  response_dict['results']
df = pd.DataFrame(Trials)
print(df)
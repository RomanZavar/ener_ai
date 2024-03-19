import os
import requests

from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

url = "http://api.giphy.com/v1/gifs/search"


params = {'api_key': os.getenv('API_KEY'),
          'q': 'programming',
          'limit': 5,
          'offset': 0,
          'rating': 'pg-13',
          'lang': 'ru',
          'bundle': 'massaging_non_clips', }


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
           'Accept': '*/*'}
response = requests.get(url=url, params=params, headers=headers)

j_data = response.json()

print()

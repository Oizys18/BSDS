import csv
from decouple import config
import requests
import json
import hashlib
from bs4 import BeautifulSoup


keywords = 'x=127.003942069544&y=37.5664750388987&categoru_group_code=PO3&query=경찰서&sort=distance'
URL = 'https://dapi.kakao.com/v2/local/search/keyword.json?&radius=1000&'
headers = {"Authorization": f"KakaoAK {config('KAKAOAK')}"}

url = URL + keywords
res = requests.get(url, headers=headers)
result = json.loads(res.text)

print(result)
print(result["meta"])
for item in result["documents"]:
    print(item['distance'])
    print(item['place_name'])
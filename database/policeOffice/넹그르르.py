import requests
from bs4 import BeautifulSoup
import json
from collections import OrderedDict
from decouple import config


res = requests.get('https://www.lost112.go.kr/prevent/lostCenterList.do')
soup = BeautifulSoup(res.content, 'html.parser')
tbody = soup.select_one('#tab1 > table > tbody')
for idx, tr in enumerate(tbody.select('tr')):
    officeName = tr.select_one(f'tr:nth-child({idx+1}) > td:nth-child(2)').text
    if officeName[-3:] in ['경찰서']:
        a = officeName[:-3]
        b = officeName[-3:]
        print(a, b)
    phoneNm = tr.select_one(f'tr:nth-child({idx+1}) > td:nth-child(3)').text





# url = 'https://dapi.kakao.com/v2/local/geo/coord2address.json?x=127.0671769&y=37.50903624&input_coord=WGS84&query=' + '서울강남경찰청'
# url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + '서울특별시 중구 을지로 234'
# headers = {"Authorization": f"KakaoAK {config('KakaoAK')}"}
# res = requests.get(url, headers=headers)
#
# result = json.loads(res.text)
#
# # match_first = result['documents'][0]
# # print(match_first)
# print(result['meta'])
# print(result['documents'])

import csv
from decouple import config
import requests
import json
import hashlib
from bs4 import BeautifulSoup


def make_center_and_address():
    center = []
    address = []
    with open('./seed/파출소 경찰소.csv', 'r') as f:
        items = csv.reader(f)

        for idx, item in enumerate(items):
            center.append({
                'id': idx,
                'category': item[4],
                'center_name': item[3],
                'police_office': item[2],
                'phone_number': item[5],
            })
            address.append(item[6])
        center.pop(0)
        address.pop(0)


    with open('user_center.csv', 'w', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for c in center:

            login_id = 'center' + str(c['id'])
            password = hashlib.sha256(login_id.encode()).hexdigest()

            w.writerow([c['id'], login_id, password, c['category'], c['police_office'], c['center_name'], c['phone_number']])

    headers = {"Authorization": f"KakaoAK {config('KakaoAK')}"}
    for i in [15, 59, 79, 90, 116, 186, 239]:
        print(center[i]['center_name'] + center[i]['category'])
        print(address[i])
        query = center[i]['center_name'] + center[i]['category']
        url = 'https://dapi.kakao.com/v2/local/search/keyword.json?query=' + query
        res = requests.get(url, headers=headers)
        result = json.loads(res.text)

        print(result['documents'][0]['place_name'])
        print(result['documents'][0]['road_address_name'])
        address[i] = result['documents'][0]['road_address_name']
        print()


    URL = 'https://dapi.kakao.com/v2/local/search/address.json?query='
    with open('user_address.csv', 'w', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for idx, addr in enumerate(address):

            url = URL + addr
            res = requests.get(url, headers=headers)
            result = json.loads(res.text)

            if result['meta']:
                data = result['documents'][0]['road_address']
                ad_id = idx + 1
                center_id = idx + 1
                address_name = data['address_name']
                region_1depth_name = data['region_1depth_name']
                region_2depth_name = data['region_2depth_name']
                region_3depth_name = data['region_3depth_name']
                road_name = data['road_name']
                x = data['x']
                y = data['y']
                zone_no = data['zone_no']

                w.writerow([ad_id, address_name,
                            region_1depth_name, region_2depth_name, region_3depth_name,
                            road_name, zone_no, x, y, center_id])

            else:
                print(idx)


def add_center_and_address():
    res = requests.get('https://www.lost112.go.kr/prevent/lostCenterList.do')
    soup = BeautifulSoup(res.content, 'html.parser')
    tbody = soup.select_one('#tab1 > table > tbody')
    phone_number_dict = {}
    for idx, tr in enumerate(tbody.select('tr')):
        officeName = tr.select_one(f'tr:nth-child({idx + 1}) > td:nth-child(2)').text
        if officeName[-3:] in ['경찰서']:
            phoneNm = tr.select_one(f'tr:nth-child({idx + 1}) > td:nth-child(3)').text
            phone_number_dict[officeName] = phoneNm

    center = []
    address = []
    idx = 240
    headers = {"Authorization": f"KakaoAK {config('KakaoAK')}"}
    with open('./seed/경찰관서위치_20200409.csv', 'r') as f:
        items = csv.reader(f)
        for item in items:
            if '경찰서' in item[2] and '서울' in item[2]:
                idx += 1

                center.append({
                    'id': idx,
                    'category': '경찰서',
                    'police_office': item[2][:-3],
                    'center_name': item[2][:-3],
                    'phone_number': phone_number_dict[item[2]],
                })

                url = f'https://dapi.kakao.com/v2/local/search/keyword.json?x={item[3]}&y={item[4]}&query={item[2]}'
                res = requests.get(url, headers=headers)
                result = json.loads(res.text)

                if result['meta']:
                    data = result['documents'][0]
                    address_name = data['road_address_name']

                    url2 = f'https://dapi.kakao.com/v2/local/search/address.json?query={address_name}'
                    res2 = requests.get(url2, headers=headers)
                    result2 = json.loads(res2.text)

                    if result2['meta']:
                        data2 = result2['documents'][0]['road_address']
                        ad_id = idx
                        center_id = idx
                        address_name = data2['address_name']
                        region_1depth_name = data2['region_1depth_name']
                        region_2depth_name = data2['region_2depth_name']
                        region_3depth_name = data2['region_3depth_name']
                        road_name = data2['road_name']
                        x = data2['x']
                        y = data2['y']
                        zone_no = data2['zone_no']

                        address.append([
                            ad_id,
                            address_name,
                            region_1depth_name,
                            region_2depth_name,
                            region_3depth_name,
                            road_name,
                            zone_no,
                            x,
                            y,
                            center_id,
                        ])
                    else:
                        print(idx, item[2])
                else:
                    print(item[2])

    with open('user_center.csv', 'a', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for c in center:
            login_id = 'center' + str(c['id'])
            password = hashlib.sha256(login_id.encode()).hexdigest()

            w.writerow(
                [c['id'], login_id, password, c['category'], c['police_office'], c['center_name'], c['phone_number']])

    with open('user_address.csv', 'a', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for add in address:
            w.writerow(add)


make_center_and_address()
add_center_and_address()

from bs4 import BeautifulSoup
from decouple import config
import json
from collections import OrderedDict
from urllib.parse import quote
from urllib.request import urlopen
import csv
import os


def save_as_csv(data):
    with open('image_path.csv', 'a', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for dt in data:
            atcId = dt['atcId']
            imgFilePath = dt['imgFilePath']
            hiPrdtNm = dt['hiPrdtNm']
            prdtNm = dt['prdtNm']
            w.writerow([atcId, imgFilePath, hiPrdtNm, prdtNm])

    # with open("img_path.txt", 'a') as f:
    #     for dt in data:
    #         img = f"{dt['atcId']},{dt['imgFilePath']},{dt['hiPrdtNm']},{dt['prdtNm']}\n"
    #         f.write(img)


def get_picture(items):
    # global name_db
    db = []
    for item in items:
        imgFilePath = item.select_one('fdFilePathImg').text
        if '_no_img' not in imgFilePath:
            prdtClNm = item.select_one('prdtClNm').text
            atcId = item.select_one('atcId').text
            temp = prdtClNm.split(' > ')
            hiPrdtNm, prdtNm = temp[0], temp[1]

            # if not name_db.get(hiPrdtNm):
            #     name_db[hiPrdtNm] = set()
            # name_db[hiPrdtNm].add(prdtNm)

            db.append({
                'atcId': atcId,
                'imgFilePath': imgFilePath,
                'hiPrdtNm': hiPrdtNm,
                'prdtNm': prdtNm
            })

    return db


ServiceKey = config('ServiceKey')
pageNo = 1
numOfRows = 50

# name_db = {}
real_db = []
for pageNo in range(1, 3):
    print()
    print('============ pageNo: ', pageNo, ' ============')
    params = f'ServiceKey={ServiceKey}&pageNo={pageNo}&numOfRows={numOfRows}'
    URL = f'http://apis.data.go.kr/1320000/LosPtfundInfoInqireService/getPtLosfundInfoAccTpNmCstdyPlace?' + params
    res = urlopen(URL)
    soup = BeautifulSoup(res, 'xml')
    if soup.select_one('header > resultCode').text == '00':
        db = get_picture(soup.select_one('body > items'))
        save_as_csv(db)
        real_db += db

with open('lost_images.json', 'w', encoding="utf-8") as f:
    json.dump(real_db, f, ensure_ascii=False, indent='\t')


# name_list = []
# for key, value in name_db.items():
#     name_list.append({
#         'hiPrdtNm': key,
#         'prdtNm': list(value)
#     })
#
# with open('prdtNm_key.json', 'w', encoding='utf-8') as f:
#     json.dump(name_list, f, ensure_ascii=False, indent='\t')

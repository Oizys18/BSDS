from bs4 import BeautifulSoup
from decouple import config
from urllib.request import urlopen
import csv


def save_as_csv(data):
    with open('image_path.csv', 'a', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for dt in data:
            atcId = dt['atcId']
            imgFilePath = dt['imgFilePath']
            hiPrdtNm = dt['hiPrdtNm']
            prdtNm = dt['prdtNm']
            color_eng = dt['color_eng']
            color_kor = dt['color_kor']
            w.writerow([atcId, imgFilePath, hiPrdtNm, prdtNm, color_eng, color_kor])


def get_picture(items):
    global color_map

    db = []
    for item in items:
        imgFilePath = item.select_one('fdFilePathImg').text
        if '_no_img' not in imgFilePath and 'noimg' not in imgFilePath:
            prdtClNm = item.select_one('prdtClNm').text
            atcId = item.select_one('atcId').text
            temp = prdtClNm.split(' > ')
            hiPrdtNm, prdtNm = temp[0], temp[1]
            fdSbjt = item.select_one('fdSbjt').text

            fdSbjt = fdSbjt.split('색)')[-2]
            fdSbjt = fdSbjt.split('(')
            color_eng, color_kor = fdSbjt[-2][:], fdSbjt[-1][:-1]

            if color_map.get(color_eng):
                if not color_map[color_eng] == color_kor:
                    print(color_eng, color_kor)
                    color_kor = color_map[color_eng]
            else:
                color_map[color_eng] = color_kor

            db.append({
                'atcId': atcId,
                'imgFilePath': imgFilePath,
                'hiPrdtNm': hiPrdtNm,
                'prdtNm': prdtNm,
                'color_eng': color_eng,
                'color_kor': color_kor,
            })

    return db


ServiceKey = config('ServiceKey')
pageNo = 1
numOfRows = 200

color_map = {}
for pageNo in range(1, 421):

    if not pageNo % 10:
        print('============ pageNo: ', pageNo, ' ============')

    params = f'ServiceKey={ServiceKey}&pageNo={pageNo}&numOfRows={numOfRows}'
    URL = f'http://apis.data.go.kr/1320000/LosPtfundInfoInqireService/getPtLosfundInfoAccTpNmCstdyPlace?' + params
    res = urlopen(URL)
    soup = BeautifulSoup(res, 'xml')
    if soup.select_one('header > resultCode').text == '00':
        db = get_picture(soup.select_one('body > items'))
        save_as_csv(db)
    else:
        print(pageNo)

colors = []
for key, value in color_map.items():
    colors.append((key, value))

with open('color_map.csv', 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for idx, (eng, kor) in enumerate(colors):
        w.writerow([idx + 1, eng, kor])

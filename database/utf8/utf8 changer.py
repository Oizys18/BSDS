import csv


temp = []
with open('경찰관서위치_20200409.csv', 'r') as f:
    items = csv.reader(f)
    for item in items:
        if '경찰서' in item[2] and '서울' in item[2]:
            print(item[2][:-3])
            temp.append({
                '구분': '경찰서',
                '관서명': item[2][:-3],
                '경찰서': item[2][:-3],
                'x좌표': item[3],
                'y좌표': item[4],
                '주소': item[5]
            })


with open('police_address.csv', 'w', newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for idx, dt in enumerate(temp):
        w.writerow([idx+1, dt['구분'], dt['관서명'], dt['경찰서'], dt['x좌표'], dt['y좌표'], dt['주소']])

import csv

color_name = {
    'red-ish': ['레드', '다크레드', '알리자린', '퓨시아'],
    'green-ish': ['시안', '다크시안', '씨그린', '에메랄드', '라임', '네온그린', '터키오이스',
                  '라임그린', '올리브', '샤르트뢰즈', '그린', '스트롱시안'],
    'blue-ish': ['로열블루', '코발트', '블루', '다크블루', '딥스카이블루'],
    'orange-ish': ['마젠타', '퓨시아', '피치오렌지', '오렌지', '다크오렌지'],
    'yellow-ish': ['엘로우'],
    'pink-ish': ['핑크', '다크핑크'],
    'purple-ish': ['블루바이올렛', '바이올렛', '다크바이올렛'],
    'brown-ish': ['브라운'],
    'grey-ish': ['실버', '그레이', '라이트 그레이'],
    'white-ish': ['화이트'],
    'black-ish': ['블랙'],
}

color_dict = {}


for key, value in color_name.items():
    print(key)
    for kor in value:
        # color_dict.append(kor)
        color_dict[kor] = key




def get_img_path():
    dataset = []
    for i in range(1, 9):

        with open(f'{i}.csv', 'r', encoding="utf-8") as f:
            items = csv.reader(f)
            for item in items:
                if 'no_img' not in item[1]:
                    if color_dict.get(item[-2]):
                        dataset.append([
                            item[0],
                            item[1],
                            item[2],
                            color_dict[item[4]]
                        ])
                    else:
                        print(item[-2])


    with open('real_img.csv', 'w', newline='', encoding='utf-8') as f:

        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for dt in dataset:
            w.writerow(dt)



def get_color_dict():
    get_color = set()
    for i in range(6, 9):

        with open(f'{i}.csv', 'r', encoding="utf-8") as f:
            items = csv.reader(f)
            for item in items:
                if len(item[-2]) > 8:
                    print(i)
                if item[-2] not in color_dict:
                    get_color.add((item[-2], item[-1]))


    get_color = list(get_color)
    with open('color.csv', 'w', newline='', encoding="utf-8") as f:
        w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for dt, dt2 in get_color:
            w.writerow([dt, dt2])

#
# get_color = {}
# for i in range(1, 9):
#
#     with open('color.csv', 'r', encoding="utf-8") as f:
#         items = csv.reader(f)
#         for item in items:
#             if len(item[-2]) > 8:
#                 print(i)
#             get_color.add((item[-2], item[-1]))


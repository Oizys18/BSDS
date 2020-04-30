from PIL import Image
import csv

with open('real_img2.csv', newline='', encoding='UTF8') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  spamreader = list(spamreader)
  for i in range(len(spamreader)):
    row = spamreader[i]
    print(i)
    if i % 5 == 0:
      print(f'{i}번째 입니다', )
    fileid = row[0].split(',')[0]
    im = Image.open(fileid)
    print(im.info())




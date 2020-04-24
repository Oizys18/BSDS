import csv 
import urllib.request
import os 
import time 

with open('real_img2.csv', newline='', encoding='UTF8') as csvfile:
  spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
  spamreader = list(spamreader)
  # len(spamreader)
  for i in range(len(spamreader)):
    time.sleep(0.5)
    row = spamreader[i]
    print(i)
    if i % 5 == 0:
      print(f'{i}번째 입니다', )
    fileid = row[0].split(',')[0]
    url = row[0].split(',')[1]
    category = row[0].split(',')[2]
    if not (os.path.isdir(category)):
      os.makedirs(os.path.join(category))
    response = urllib.request.urlopen(url) 
    if response.headers['Content-Type'] == 'image/jpg':
      urllib.request.urlretrieve(url, f'./train/{category}/{fileid}.jpg')


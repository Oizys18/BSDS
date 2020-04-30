from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv


path = 'chromedriver.exe'
driver = webdriver.Chrome(path)

driver.get('https://www.lost112.go.kr/find/findList.do')
time.sleep(2)


a = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/button[1]')
a.click()

b = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/div/div/div[1]/div[1]/button[2]')
b.click()
c = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/div/div/table/tbody/tr[1]/td[4]/a')
c.click()

d = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/button[2]')
d.click()
e = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/div/div/div[1]/div[1]/button[2]')
e.click()
e = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/div/div/div[1]/div[1]/button[2]')
e.click()
e = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/div/div/div[1]/div[1]/button[2]')
e.click()
f = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/div[1]/fieldset[2]/div/div/table/tbody/tr[3]/td[7]/a')
f.click()

serch_btn = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div/form/p/button')
serch_btn.send_keys(Keys.ENTER)

page_cnt = 0
get_data = []
get_img = []
while page_cnt < 23:
    page_cnt += 1

    if not page_cnt % 5:
        print(page_cnt)
        with open('../get_image_hd/lost_article_2020_1.csv', 'a', newline='', encoding="utf-8") as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for dt in get_data:
                w.writerow(dt)

        with open('../get_image_hd/image_color_path_2020_1.csv', 'a', newline='', encoding="utf-8") as f:
            w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for dt in get_img:
                w.writerow(dt)

        get_data = []
        get_img = []

    for i in range(1, 11):
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        tbody = soup.select_one('#contents > div.find_listBox > table > tbody')

        for idx, tr in enumerate(tbody.select('tr')):
            if tr.select_one('td > div > a > img'):
                name = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/div[3]/table/tbody/tr[{idx+1}]/td[2]/div/a')
                name.send_keys(Keys.CONTROL + '\n')

                detail_soup = BeautifulSoup(driver.page_source, 'html.parser')
                color_text = detail_soup.select_one('#contents > div.findDetail > div.find_info_txt').text

                if ')색)]을' in color_text:
                    wrap = detail_soup.select_one('#contents > div.findDetail > div.findDetail_wrap')

                    image_path = wrap.select_one('div.img_area > p.lost_img > img')['src']
                    image_path = f'https://www.lost112.go.kr{image_path}'

                    color_text = color_text.split(')색)]을')[0].split('(')
                    color_eng, color_kor = color_text[-2], color_text[-1]

                    wrap = detail_soup.select_one('#contents > div.findDetail > div.findDetail_wrap')

                    ul = wrap.select_one('div.find_info > ul')

                    lost_id = ul.select_one('li:nth-of-type(1) > p.find02').text
                    lost_date = ul.select_one('li:nth-of-type(2) > p.find02').text.split(' ')[0]
                    category = ul.select_one('li:nth-of-type(4) > p.find02').text.split(' > ')
                    high, low = category[0], category[1]
                    where = ul.select_one('li:nth-of-type(5) > p.find02').text

                    get_data.append([
                        lost_id, lost_date, where
                    ])

                    get_img.append([
                        lost_id, image_path, high, low, color_eng, color_kor
                    ])

                button = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[2]/div[3]/button')
                button.send_keys(Keys.ENTER)

        if i == 10:
            nth = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[4]/span[2]/a[1]')
        else:
            nth = driver.find_element_by_xpath(f'/html/body/div[1]/div[2]/div[2]/div[4]/a[{i + 1}]')

        nth.send_keys(Keys.ENTER)


with open('../get_image_hd/lost_article_2020_1.csv', 'a', newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for dt in get_data:
        w.writerow(dt)

with open('../get_image_hd/image_color_path_2020_1.csv', 'a', newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for dt in get_img:
        w.writerow(dt)


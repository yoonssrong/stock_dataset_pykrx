from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import requests
from datetime import datetime
import time
import pandas as pd
import re
import os

# 크롬 드라이버 옵션
options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

# 수집 대상 url
url = 'https://finance.daum.net/domestic/exchange/BOND-%2FKRCD%3DKQ'
driver = webdriver.Chrome(executable_path="./chromedriver.exe", chrome_options=options)
driver.get(url)

# 빈 데이터프레임 생성
output = pd.DataFrame(columns=['date', 'CD(91일)'])

for n in range(0, 130):
    time.sleep(1)

    html = driver.page_source
    html_bs = bs(html, 'html.parser')

    dates = html_bs.findAll('span', attrs={'class': 'time'})
    table = html_bs.findAll('span', attrs={'class': 'num'})
    table = [table[i * 3:(i + 1) * 3] for i in range((len(table) + 3 - 1) // 3)]

    # 테이블에서 날짜, CD금리 데이터 수집
    for i, dt in enumerate(dates):
        date = dt.text
        date = date.replace('.', '')
        CD91 = table[i][0].text
        df = pd.DataFrame([[date, CD91]], columns=['date', 'CD(91일)'])
        output = pd.concat([output, df])

    # 페이지 이동
    page_bar = driver.find_elements_by_css_selector("div.paging > *")
    try:
        if n < 10:
            page_bar[n + 1].click()
        elif n > 9:
            page_bar[n % 10 + 3].click()
    except:
        print("수집완료")
        break

driver.quit()

output.to_csv('./raw_data/CD(91일) 금리.csv', index=False, encoding='cp949')
print(output)
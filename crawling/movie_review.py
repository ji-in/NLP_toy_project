import random
random.uniform(0.2, 1.2)

import requests
import time
import random
from bs4 import BeautifulSoup

base_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page={}'

fp = open('review.tsv', 'w', encoding='utf-8', newline='\n')

for page in range(1, 101): # 1페이지부터 101페이지까지 보기
    url = base_url.format(page)
    res = requests.get(url)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, 'lxml')
        tds = soup.select('table.list_netizen > tbody > tr > td.title')
        for td in tds:
            comment = td.select_one('br').next_sibling.strip()
            fp.write(comment + '\n')
            print(comment)
        # 페이지를 바로 넘기면 크롤링이 안될 수도 있다.
        # 그리고 네이버측에서 크롤링을 막을 수 있기 때문에 delay를 걸어줘야 한다.
        interval = round(random.uniform(0.2, 1.2), 2)
        #random.uniform(0.2, 1.2) : 0.2에서 1.2 사이의 실수를 동일한 확률로 나오게 한다.
        # round(@, 2) : 소숫점 둘째자리까지 반올림하기
        time.sleep(interval)
        # interval초동안 프로세스를 중지하라

fp.close()
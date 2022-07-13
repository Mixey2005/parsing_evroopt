from random import randint
import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def collect_data(city_code='76'):
    cur_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M")
    ua = UserAgent()

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'user-Agent': 'ua.random'
    }


    cookies = {
        'tmr_reqNum' : f'{city_code}'
    }

    response = requests.get(url='https://evroopt.by/deals/',headers=headers,cookies=cookies)

    with open(f'index.html','w') as f:
        f.write(response.text)


def main():
    collect_data(city_code='76')

if __name__ == '__main__':
    main()
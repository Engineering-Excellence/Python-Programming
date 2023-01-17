import requests
from bs4 import BeautifulSoup


def crawling():
    # 종목 코드 리스트
    codes = [
        '005930',
        '000660',
        '035720'
    ]

    for code in codes:
        url = f'https://finance.naver.com/item/sise.naver?code={code}'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.select_one('div.wrap_company > h2 > a').text
        price = soup.select_one('#_nowVal').text
        price = int(price.replace(',', ''))
        bid_price = soup.select_one('span.tah.p11').text
        bid_price = int(bid_price.replace(',', ''))
        print(f'종목: {title}, 현재가: {price}, 매수호가: {bid_price}')


crawling()

import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt('뉴스 검색어를 입력하세요.')
lastPage = int(pyautogui.prompt('마지막 페이지를 입력하세요.'))
pageNum = 1

for i in range(1, lastPage * 10, 10):
    print(f'{pageNum:2d} 페이지입니다. ' + '=' * 150)
    response = requests.get(f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={keyword}&start={i}')
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit')
    print(links)  # 결과는 list
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    pageNum += 1

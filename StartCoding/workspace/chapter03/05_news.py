import requests
from bs4 import BeautifulSoup

response = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=삼정전자')
html = response.text

soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit')
print(links)  # 결과는 list
for link in links:
    title = link.text  # 태그 안에 text 요소를 가져온다
    url = link.attrs['href']  # href의 속성값을 가져온다
    print(title, url)

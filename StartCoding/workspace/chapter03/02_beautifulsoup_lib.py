import requests
from bs4 import BeautifulSoup

# NAVER에 get 방식으로 http 요청
response = requests.get('https://www.naver.com/')
print(response)

# NAVER에서 html을 응답
html = response.text

# html parser로 파싱
soup = BeautifulSoup(html, 'html.parser')

# 특정 id인 태그를 선택
word = soup.select_one('#NM_set_home_btn')
print(word.text)

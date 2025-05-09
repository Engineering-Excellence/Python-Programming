# 9.2.3 태그 속성 수집
from bs4 import BeautifulSoup, ResultSet
from re import compile
from os import sep
from typing import TextIO, Pattern

# (1) 로컬 파일 읽기
file: TextIO = open(f'..{sep}data{sep}html02.html', 'r', encoding='utf-8')
source: str = file.read()
file.close()

# (2) html 파싱
# html: BeautifulSoup = BeautifulSoup(markup=source, features='html.parser')
html: BeautifulSoup = BeautifulSoup(markup=source, features='lxml')

# (3) a 태그 찾기
links: ResultSet = html.find_all(name='a')
print('links size =', len(links))

# (4) a 태그에서 속성 찾기
for link in links:
    try:
        print(link.attrs['href'])
        print(link.attrs['target'])
    except KeyError as e:
        print('예외 발생:', e)

# (5) 정규표현식으로 속성 찾기
print('패턴 객체 이용 속성 찾기')
patt: Pattern[str] = compile(pattern='https?://')
links = html.find_all(href=patt)  # 패턴 찾기
print(links)

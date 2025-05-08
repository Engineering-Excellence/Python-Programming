# 9.2.2 로컬에서 자료 수집
from bs4 import BeautifulSoup, Tag, ResultSet
from os import sep
from typing import TextIO

# (1) 로컬 서버 파일 읽기
file: TextIO = open(f'..{sep}data{sep}html01.html', 'r', encoding='utf-8')
text: str = file.read()
file.close()

# (2) html 파싱
# html: BeautifulSoup = BeautifulSoup(markup=text, features='html.parser')
html: BeautifulSoup = BeautifulSoup(markup=text, features='lxml')

# (3) 태그 내용 가져오기

# (3-1) tag 이용
h1: Tag = html.html.body.h1  # 계층 접근
print('h1:', h1.string)

# (3-2) find('tag') 함수
h2: Tag = html.find(name='h2')
print('h2:', h2.string)

# (3-3) find_all('tag') 함수
lis: ResultSet[Tag] = html.find_all(name='li')
print('lis:', lis)

# (4) li 태그 내용
for li in lis:
    print(li.string)

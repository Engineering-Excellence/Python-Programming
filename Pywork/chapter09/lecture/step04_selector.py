# 9.3 선택자 자료 수집
from bs4 import BeautifulSoup, Tag, ResultSet
from os import path
from typing import TextIO

# (1) 로컬 파일 읽기
file: TextIO = open(path.join(path.dirname(__file__), '..', 'data', 'html03.html'), 'r', encoding='utf-8')
source: str = file.read()

# (2) html 파싱
html: BeautifulSoup = BeautifulSoup(markup=source, features='lxml')
# (3) 선택자 이용 태그 내용 가져오기

# (3-1) id 선택자: <table id='tab'>
print('>> table 선택자 <<')
table: Tag = html.select_one(selector='#tab')
print(table, end='\n\n')  # table 태그 전체 출력

# (3-2) id 선택자와 계층
print('>> 선택자 & 계층 <<')
ths: ResultSet[Tag] = html.select(selector='#tab > tr > th')
print(ths, end='\n\n')  # ResultSet(list[Tag])

# (3-3) class 선택자: <tr class='odd'>
print('>> class 선택자 <<')
trs: ResultSet[Tag] = html.select(selector='#tab > .odd')  # 홀수 행
print(trs, end='\n\n')

# (4) 태그[속성=값] 찾기
trs = html.select(selector='tr[class=odd]')

# (5) td 태그 내용
print('>> tr > td 출력 <<')
for tr in trs:  # 행
    tds: ResultSet[Tag] = tr.find_all(name='td')
    for td in tds:  # 열
        print(td.string)

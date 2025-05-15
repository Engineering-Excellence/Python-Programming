# [문제1] login.html 웹 문서를 대상으로 다음 조건에 맞게 내용을 추출하시오.

"""
<처리 조건>

1. <form> 태그의 하위 태그인 <input> 태그의 모든 내용 출력
2. 각 단계 처리
"""

from bs4 import BeautifulSoup, ResultSet, Tag
from os import path
from typing import TextIO

# 단계1. 파일 읽기
file: TextIO = open(path.join(path.dirname(__file__), '..', 'data', 'login.html'), 'r', encoding='utf-8')
source: str = file.read()

# 단계2. html 파싱
soup: BeautifulSoup = BeautifulSoup(source, 'lxml')

# 단계3. 태그 찾기
inps: ResultSet[Tag] = soup.select('form > input')

# 단계4. 태그 내용 출력
print('<input> 내용')
for inp in inps:
    try:
        print(inp.attrs['placeholder'])
    except KeyError:
        print(inp.attrs['value'])

# 9.4 news 자료 수집
from urllib3 import BaseHTTPResponse, request as req
from bs4 import BeautifulSoup, ResultSet, Tag
from pickle import dump, load  # object -> file(binary) -> load(object)
from os import path
from typing import BinaryIO

# news 제공 포털 사이트
url: str = 'https://news.naver.com'

# (1) url 요청
res: BaseHTTPResponse = req(method='GET', url=url)

# (2) source 디코딩
source: str = res.data.decode(encoding='utf-8')

# (3) html 파싱
html: BeautifulSoup = BeautifulSoup(markup=source, features='lxml')

# (4) tab[속성=값] 요소 추출
atags: ResultSet[Tag] = html.select(selector='a[class="cnf_news _cds_link _editn_link"]')
print('a tag 수:', len(atags), end='\n\n')

# (5) atag 태그 내용 수집
crawling_data: list[str] = []

cnt: int = 0
for atag in atags:
    cnt += 1
    atagStr = str(atag.string)  # string 변환
    crawling_data.append(atagStr.strip())

# 수집한 자료 확인
print('수집한 자료 확인:', cnt)
print(crawling_data, end='\n\n')

# (6) pickle save/load
path: str = path.join(path.dirname(__file__), "..", "data", "data.pickle")
file: BinaryIO = open(file=path, mode='wb')
dump(obj=crawling_data, file=file)
file.close()

file = open(file=path, mode='rb')
crawling_data = load(file)
file.close()

print('pickle load')
print(crawling_data)

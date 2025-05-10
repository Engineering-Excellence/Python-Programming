# 9.2 태그 자료 수집

# 9.2.1 원격 서버에서 자료 수집

# (1) request, BeautifulSoup 모듈 import
# from urllib import request as req
# from http.client import HTTPResponse
from urllib3 import BaseHTTPResponse, request as req  # 원격 서버 파일 요청
from bs4 import BeautifulSoup, Tag  # html 파싱

# 요청할 url
url: str = 'https://www.naver.com/index.html'

# (2) 원격 서버 파일 요청
# res: HTTPResponse = req.urlopen(url=url)
# data: bytes = res.read()
res: BaseHTTPResponse = req(method='GET', url=url)  # web 문서 요청
data: bytes = res.data  # text 형태로 읽음

# (3) source 디코딩
src: str = data.decode(encoding='utf-8')  # 디코딩
print(src)

# (4) html 파싱
# html: BeautifulSoup = BeautifulSoup(markup=src, features='html.parser')  # 내장 html 파싱
html: BeautifulSoup = BeautifulSoup(markup=src, features='lxml')  # 빠르고 강력한 파싱
print(html.prettify())

# (5) 태그 내용
a: Tag = html.find(name='a')
print('a tag:', a)
print('a tag 내용:', a.string)

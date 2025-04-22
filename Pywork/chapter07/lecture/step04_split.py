# 7.3 텍스트 처리

# 7.3.1 올바른 문장 선택

from re import split, match, compile
from typing import Pattern, AnyStr

# 텍스트 자료
multi_line: str = """https://www.naver.com
https://www.daum.net
www.hongkildong.com"""

# (1) 구분자를 이용하여 문자열 분리
web_site: list[str] = split(pattern='\n', string=multi_line, maxsplit=0, flags=0)
print(web_site, end='\n\n')

# (2) 패턴 객체 만들기: 반복 사용시 성능상 이점
pat: Pattern[AnyStr] = compile(pattern='https://', flags=0)
print(pat, end='\n\n')

# (3) 패턴 객체를 이용하여 정상 웹 주소 선택하기
sel_site: list[str] = [site for site in web_site if match(pat, site)]
print(sel_site)

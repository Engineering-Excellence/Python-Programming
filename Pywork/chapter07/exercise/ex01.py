# [문제1] 여러 줄의 문자열을 대상으로 <email 양식 처리조건>에 맞게 정규표현식을 적용하여 email 양식이 올바른 것만 출력되도록 하시오.

"""
<email 양식 처리조건>

1. 아이디: 첫자는 영문소문자, 단어길이 4자 이상
2. 호스트이름: 영문소문자 시작, 단어길이 3자 이상
3. 최상위 도메인: 영문소문자 3자리 이하
4. 정규표현식 기본 패턴: '메타문자@메타문자.메타문자'
"""

from re import match, compile, Pattern

emails: str = """hong@12.com
you2@naver.com
12kang@hanmail.net
kimjs@gmail.com"""

email_pat: Pattern[str] = compile('^[a-z]\\w{3,}@[a-z]\\w{2,}\.[a-z]{2,3}$')

for email in emails.split(sep='\n'):
    if match(email_pat, email):
        print(email)

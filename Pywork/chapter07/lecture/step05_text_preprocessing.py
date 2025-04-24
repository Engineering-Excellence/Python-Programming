# 7.3.2 자연어 전처리

from re import findall, sub, compile
from typing import Pattern

# 텍스트
texts: list[str] = [' 우리나라   대한민국, 우리나라%$ 만세', '궁금하면 500오백WON원', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

# 단계1: 소문자 변경
texts_re1: list[str] = [t.lower() for t in texts]
print('texts_re1:', texts_re1)

# 단계2: 숫자 제거
texts_re2: list[str] = [sub('\\d', '', text) for text in texts_re1]
print('texts_re2:', texts_re2)

# 단계3: 문장부호 제거
punct_pat: Pattern[str] = compile('[,.?!:;]')
texts_re3: list[str] = [sub(punct_pat, '', text) for text in texts_re2]
print('texts_re3:', texts_re3)

# 단계4: 특수문자 제거
spec_pat: Pattern[str] = compile('[@#$%^&*()]')
texts_re4: list[str] = [sub(spec_pat, '', text) for text in texts_re3]
print('texts_re4:', texts_re4)

# 단계5: 영문자 제거
# lower_pat: Pattern[str] = compile('[^a-z]')
# texts_re5: list[str] = [''.join(findall(lower_pat, text)) for text in texts_re4]
texts_re5: list[str] = [sub('[a-z]', '', text) for text in texts_re4]
print('texts_re5:', texts_re5)

# 단계6: 공백 제거
texts_re6: list[str] = [' '.join(text.split()) for text in texts_re5]  # 공백 기준 split -> join 결합
print('texts_re6:', texts_re6)

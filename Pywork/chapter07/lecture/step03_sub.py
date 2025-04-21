# 7.2.3 문자열 치환

from re import sub

st3: str = 'test^홍길동 abc 대한*민국 123$tbc'

# (1) 특수문자 제거
text1: str = sub(pattern='[\^*$]+', repl='', string=st3, count=0, flags=0)
print(text1)
print()

# (2) 숫자 제거
text2: str = sub('\\d', '', text1)
print(text2)

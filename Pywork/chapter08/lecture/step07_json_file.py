# 8.6.2 JSON 파일
from json import dumps, loads
from os import sep
from typing import TextIO

# (1) json 인코딩
user: dict = {'id': 1234, "name": '홍길동'}  # Python Dict
print(user)
print(type(user))
print(user['name'], end='\n\n')

jsonStr: str = dumps(obj=user, ensure_ascii=False)  # ASCII 인코딩 방식 적용 안 함
print(jsonStr)
print(type(jsonStr), end='\n\n')
# print(jsonStr['name'])  # TypeError

# (2) json 디코딩
pyObj: dict = loads(jsonStr)
print(pyObj)
print(type(pyObj))
print(pyObj['name'])
for key in pyObj:
    print(f'{key}: {pyObj[key]}')
print()

# (3) json 파일 읽기
file: TextIO = open(f'..{sep}data{sep}usagov_bitly.txt', 'r', encoding='utf-8')
lines: list[str] = file.readlines()  # 줄 단위 전체 읽기
file.close()

# (4) json 디코딩: file(json 문자열) -> Python dict 객체
rows: list[str] = [loads(row) for row in lines]
print('rows:', len(rows))

# (5) 10개 원소 출력
for row in rows[:10]:
    print(type(row), row)

# (6) dict -> DataFrame 변환
import pandas as pd

recode_df: pd.DataFrame = pd.DataFrame(rows)
recode_df.info()
print(recode_df.head())

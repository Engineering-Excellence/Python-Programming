# 8.6 특수 파일 처리

# 8.6.1 CSV, Excel 파일

# (1) pandas 패키지 import
import pandas as pd
from os import getcwd, sep

# 현재 작업디렉터리 확인
print(getcwd())

# (2) csv 파일 읽기
score: pd.DataFrame = pd.read_csv(f'..{sep}data{sep}score.csv')
score.info()  # 파일 정보
print(score.head())  # 컬럼명 포함 앞부분 5개 행
print()

# (3) 컬럼 추출
kor: pd.Series = score.kor  # 객체.컬럼명
eng: pd.Series = score['eng']  # 객체['컬럼명']
mat: pd.Series = score['mat']
dept: pd.Series = score['dept']

# (4) 과목별 최고 점수
print('max kor =', max(kor))
print('max eng =', max(eng))
print('max mat =', max(mat))

# (5) 과목별 최하 점수
print('min kor =', min(kor))
print('min eng =', min(eng))
print('min mat =', min(mat))

# (6) 과목별 평균 점수
from statistics import mean

print('kor mean =', round(mean(kor), 2))  # 느림
print('eng mean =', round(mean(eng), 2))
print('mat mean =', round(mean(mat), 2))

print('kor mean =', round(kor.mean(), 2))  # 빠름
print('eng mean =', round(eng.mean(), 2))
print('mat mean =', round(mat.mean(), 2))

# (7) dept 빈도수
dept_cnt: dict[int] = {}
for key in dept:
    dept_cnt[key] = dept_cnt.get(key, 0) + 1
print(dept_cnt)

print()

# (8) excel 파일 읽기
sam: pd.ExcelFile = pd.ExcelFile(f'..{sep}data{sep}sam_kospi.xlsx')

# (9) excel 파싱
kospi: pd.DataFrame = sam.parse('sam_kospi')
kospi.info()
print(type(kospi))

# (10) 컬럼 추출
high: pd.Series = kospi['High']
low: pd.Series = kospi['Low']

# (11) 평균 계산
print('high mean =', mean(high))
print('low mean =', mean(low))

print('high mean =', high.mean())
print('low mean =', low.mean())

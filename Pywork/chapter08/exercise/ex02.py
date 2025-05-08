# [문제2] emp.csv 파일을 읽어서 출력하시오.
import pandas as pd
from os import sep

emp: pd.DataFrame = pd.read_csv(f'..{sep}data{sep}emp.csv', encoding='utf-8')
emp.info()
sal: pd.Series = emp['sal']

print(f"\n관측치 길이: {sal.count()}")
print(f'전체 평균 급여: {sal.mean():.1f}')
print(f"최저 급여: {sal.min()}, 이름: {emp.loc[sal.idxmin(), 'ename']}")
print(f"최저 급여: {sal.max()}, 이름: {emp.loc[sal.idxmax(), 'ename']}")

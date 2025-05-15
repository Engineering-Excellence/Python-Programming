# [문제2] iris.csv 파일을 이용하여 다음과 같이 차트를 그리시오.

"""
<처리 조건>

1. irirs.csv 파일을 iris 변수명으로 가져온 후 파일 정보 보기
2. 1번 컬럼과 3번 컬럼을 대상으로 산점도 그래프 그리기
3. 1번 컬럼과 3번 컬럼을 대상으로 산점도 그래프 그린 후 5번 컬럼으로 색상 적용
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

# 1. iris 파일 정보
iris: pd.DataFrame = sns.load_dataset("iris")
iris.info()

# 2. sepal_length & petal_length 산점도 그래프
sepal_length: pd.Series = iris['sepal_length']
petal_length: pd.Series = iris['petal_length']
# plt.scatter(x=sepal_length, y=petal_length)

# 3. species 컬럼으로 색상 적용
# 꽃의 종별 범주 확인
print(iris['species'].unique())  # ['setosa' 'versicolor' 'virginica']

# 'setosa'=1, 'versicolor'=2, 'virginica'=3
species: list[int] = []
for v in iris['species']:
    match v:
        case 'setosa':
            species.append(1)
        case 'versicolor':
            species.append(2)
        case 'virginica':
            species.append(3)
        case _:
            raise ValueError

# 수치화된 변수로 color 적용
plt.scatter(x=sepal_length, y=petal_length, c=species)
plt.xlabel('sepal length')
plt.ylabel('petal length')
plt.title('Sepal Length vs. Petal Length scatter plotting')
plt.show()

# 산점도 그래프 그리기 (seaborn 활용)
sns.scatterplot(data=iris, x="sepal_length", y="petal_length", hue="species", palette="coolwarm")
plt.title('Sepal Length vs. Petal Length scatter plotting')
plt.show()

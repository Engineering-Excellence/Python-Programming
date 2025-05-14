# 9.6.2 기본 차트 그리기
from matplotlib import pyplot as plt, rcParams, RcParams  # 차트 생성
import random  # 차트 자료 생성

# 음수 부호 지원
rcParams['axes.unicode_minus']: RcParams = False

# 차트 자료 생성
print(random.randint(a=1, b=5))  # 1~5 난수 정수
print(random.random())  # 0~1 난수 실수
print(random.normalvariate(mu=0, sigma=1))  # 평균=0, 표준편차=1을 갖는 표준정규분포 난수

# (1) plot() 함수 도움말
help(plt.plot)

# (2) 기본 차트 그리기

# (2-1) 1개 data
data: range = range(10)
plt.plot(data)  # plot(y), x: index
plt.show()
plt.plot(data, 'r+')  # plot(y, 'r+')
plt.show()

# (2-2) 2개 data
data2: list[float] = [random.random() for _ in range(10)]  # 난수 실수
plt.plot(data, data2)  # line
plt.show()
plt.plot(data, data2, 'ro')  # point
plt.show()

# (3) 산점도 그리기

# (3-1) 단색 산점도
plt.scatter(x=data, y=data2, c='b', marker='o')
plt.show()

# (3-2) 여러 가지 색 산점도
cdata: list[int] = [random.randint(a=1, b=3) for _ in range(10)]
plt.scatter(x=data, y=data2, c=cdata, marker='o')
plt.show()

# (4) 히스토그램
data3: list[float] = [random.normalvariate(mu=0, sigma=1) for _ in range(1000)]
plt.hist(x=data3, bins=10)  # 정규분포
plt.show()

data4: list[float] = [random.uniform(a=1, b=100) for _ in range(1000)]
plt.hist(x=data4, bins=10)  # 균등분포
plt.show()

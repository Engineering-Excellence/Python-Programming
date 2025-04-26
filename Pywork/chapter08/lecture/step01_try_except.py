# 8.1 예외처리

# 8.1.1 간단한 예외처리
from io import TextIOWrapper
from os import sep

x: list = [10, 30, 25.2, 'num', 14, 51]

# (1) 예외 발생 코드
print('프로그램 시작')
for i in x:
    print(i)
    y = i ** 2  # 예외 발생
    print('y =', y)
print('프로그램 종료')

# (2) 예외 처리 코드
print('프로그램 시작')
for i in x:
    try:  # try 블록
        y = i ** 2
        print('i =', i, ', y =', y)
    except:  # exception 블록
        print('숫자 아님: %s' % i)
print('프로그램 종료')

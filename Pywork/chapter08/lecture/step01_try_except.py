# 8.1 예외처리

# 8.1.1 간단한 예외처리
from os import sep
from typing import TextIO

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

# 8.1.2 다중 예외처리

# 유형별 예외처리
print('\n유형별 예외처리')
try:
    div: float = 1000 / 2.53
    print('div = %5.2f' % div)  # 정상
    div = 1000 / 0  # 1차: 산술적 예외
    f: TextIO = open(file=f'{sep}test.txt')  # 2차: 파일 열기 예외
    num: int = int(input('숫자 입력: '))  # 3차: 기타 예외
    print('num =', num)

# 다중 예외처리 클래스
except ZeroDivisionError as e:  # 산술적 예외처리
    print('오류 정보:', e)
except FileNotFoundError as e:  # 파일 열기 예외처리
    print('오류 정보:', e)
except Exception as e:  # 기타 예외처리
    print('오류 정보:', e)
finally:
    print('finally 영역 - 항상 실행되는 영역')

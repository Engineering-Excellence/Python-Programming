# 8.2 텍스트 파일

# 8.2.1 텍스트 파일 입출력
from os import getcwd, sep
from io import TextIOWrapper
from typing import Optional

# (1) 현재 작업디렉터리
print('현재 경로:', getcwd())

ftest1: Optional[TextIOWrapper] = None
ftest2: Optional[TextIOWrapper] = None
ftest3: Optional[TextIOWrapper] = None

# (2) 예외처리
try:
    # (3) 파일 읽기
    ftest1 = open(file=f'..{sep}data{sep}ftest.txt', mode='r')
    print(ftest1.read())  # 파일 전체 읽기

    # (4) 파일 쓰기
    ftest2 = open(f'..{sep}data{sep}ftest2.txt', 'w')
    ftest2.write('my first text\n')  # 파일 쓰기

    # (5) 파일 쓰기 + 내용 추가
    ftest3 = open(f'..{sep}data{sep}ftest2.txt', 'a')
    ftest3.write('my second text\n')  # 파일 쓰기(추가)
except Exception as e:
    print('Error 발생:', e)
finally:
    ftest1.close()  # 파일 객체 닫기
    ftest2.close()
    ftest3.close()

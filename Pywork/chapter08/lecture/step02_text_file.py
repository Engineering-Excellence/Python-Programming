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

print()

# 8.2.2 텍스트 자료 읽기

# 파일 읽기 관련 함수
ftest: Optional[TextIOWrapper] = None
try:
    # (1) read(): 전체 텍스트 자료 읽기
    ftest = open(f'..{sep}data{sep}ftest.txt', 'r')
    full_text: str = ftest.read()
    print(full_text)
    print(type(full_text), end='\n\n')

    # (2) readlines(): 전체 텍스트 줄 단위 읽기
    ftest = open(f'..{sep}data{sep}ftest.txt', 'r')
    lines: list[str] = ftest.readlines()  # list 반환
    print(lines)
    print(type(lines))
    print('문단 수:', len(lines), end='\n\n')

    # (3) list -> 문장 추출
    docs: list[str] = []  # 문장 저장
    for line in lines:
        print(line.strip())  # text만 출력
        docs.append(line.strip())
    print('docs =', docs, end='\n\n')

    # (4) readline(): 한 줄 읽기
    ftest = open(f'..{sep}data{sep}ftest.txt', 'r')
    line: str = ftest.readline()  # 한 줄 읽기
    print('line =', line)
    print(type(line), end='\n\n')
except Exception as e:
    print('Error 발생:', e)
finally:
    # 파일 객체 닫기
    ftest.close()

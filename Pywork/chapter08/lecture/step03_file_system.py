# 8.3 파일 시스템

# 8.3.1 파일과 디렉터리 관련 함수
import os

# 현재 작업 디렉터리 경로 확인
print(os.getcwd())

# 작업 디렉터리 변경
os.chdir('..')
print(os.getcwd())

# 현재 작업 디렉터리 목록: list 반환
print(os.listdir('.'))

# 디렉터리 생성
os.mkdir('test')
print(os.listdir('.'))

# 디렉터리 이동
os.chdir('test')
print(os.getcwd())

# 여러 디렉터리 생성
os.makedirs(f'test2{os.sep}test3')
print(os.listdir('.'))

# 디렉터리 이동
os.chdir('test2')
print(os.listdir('.'))

# 디렉터리 삭제
os.rmdir('test3')
print(os.listdir('.'))

# 상위 디렉터리 2개 이동
os.chdir(f'..{os.sep}..')
print(os.getcwd())

# 여러 디렉터리 삭제
os.removedirs(f'test{os.sep}test2')

print()

# 8.3.2 경로 관련 함수

# lecture 디렉터리의 step01_try_except.py 파일 절대경로
print(os.path.abspath(f'lecture{os.sep}step01_try_except.py'))

# step01_try_except.py 파일의 디렉터리 이름
print(os.path.dirname(f'lecture{os.sep}step01_try_except.py'))

# Python 디렉터리 유무 확인
print(os.path.exists(f'C:{os.sep}Users{os.sep}user{os.sep}Documents{os.sep}Study{os.sep}Python'))

# 디렉터리와 파일 분리
print(os.path.split(f'C:{os.sep}CrashRepoterLog.txt'))
# 디렉터리와 파일 결합
print(os.path.join(f'C:{os.sep}', 'CrashRepoterLog.txt'))

# step01_try_except.py 파일 크기
print(os.path.getsize(f'lecture{os.sep}step01_try_except.py'))

print()

# 8.3.3 glob 모듈
from glob import glob

print(glob(pathname='*'))  # 현재 경로의 모든 목록 반환
print(glob(pathname=f'lecture{os.sep}*.py'))  # lecture 디렉터리에 포함된 *.py 파일 반환
print(glob(pathname=f'data{os.sep}ftest[0-9].txt', recursive=True)) # 하위 폴더까지 재귀 검색

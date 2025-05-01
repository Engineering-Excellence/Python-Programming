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

# 2.4 문자열(String)

# 문자열 유형
oneLine = 'this is one line string'
print(oneLine)

print('-' * 100)

multiLine = '''this is
multi line
string'''
print(multiLine)

print('-' * 100)

multiLine2 = 'this is\nmulti line\nstring too'
print(multiLine2)

print('=' * 100)

# 2.4.1 문자열 특징
# (1) 문자열 색인
string = 'PYTHON'
print(string[0])
print(string[5])
print(string[-1])
print(string[-6])

print('-' * 100)

# (2) 문자열 연산
print('python' + 'program')  # 결합 연산자
# print('python-' + 3.9 + '.exe')  # error
print('python-' + str(3.9) + '.exe')  # python-3.9.exe

print('=' * 100)  # 반복 연산자

# 2.4.2 슬라이싱(slicing)
# (1) 왼쪽 기준
print(oneLine)
print('문자열 길이:', len(oneLine))
print(oneLine[0:4])
print(oneLine[:4])
print(oneLine[:])  # 전체 원소
print(oneLine[::2])  # 2의 배수 index

print('-' * 100)

# (2) 오른쪽 기준
print(oneLine[0:-1:2])
print(oneLine[-6:-1])
print(oneLine[-6:])

print('-' * 100)

# (3) 부분 문자열 생성
subString = oneLine[-11:]
print(subString)

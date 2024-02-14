# 2.1 변수와 자료형

var1 = 'Hello, python!'
print(var1)
print(id(var1))  # 변수값이 아닌 주소가 할당되는 참조형 변수
print(type(var1))  # <class 'str'>

var1 = 100
print(var1)
print(id(var1))  # 동일한 변수에 다른 값을 할당하면 새로운 객체가 생성되어 id가 변경된다.
print(type(var1))  # <class 'int'>

var2 = 150.25
print(var2)
print(id(var2))
print(type(var2))  # <class 'float'>

var3 = True
print(var3)
print(id(var3))
print(type(var3))  # <class 'bool'>

print('=' * 320)

# 예약어 확인
import keyword  # 모듈 임포트: 코드 최상단에 import 하는 것이 원칙이지만, 학습 구분을 위해 여기에 코딩한다.

python_keyword = keyword.kwlist
print(python_keyword)

print(type(python_keyword))  # <class 'list'>
print(len(python_keyword))  # Python 3.9.13 버전 기준 예약어는 36개

print('=' * 320)

# 실수 → 정수
a = int(10.5)
b = int(20.42)
add = a + b
print('add =', add)

# 정수 → 실수
a = float(10)
b = float(20)
add2 = a + b
print('add2 =', add2)

# 논리값 → 정수
print(int(True))  # 1
print(int(False))  # 0

# 문자열 → 정수
st = '10'
print(int(st) ** 2)  # 제곱 연산

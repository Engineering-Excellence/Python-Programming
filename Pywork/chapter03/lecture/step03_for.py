# 3.3 반복문

# 3.3.4 for
# (1) 문자열 열거형객체 이용
string = "홍길동"
print(len(string))  # 문자 길이: 3
for s in string:  # 1문자 -> 변수 넘김: 3회
    print(s)

# (2) list 열거형객체 이용
lstset = [1, 2, 3, 4, 5]  # 5개 원소를 갖는 열거형객체

for e in lstset:
    print('원소:', e)

print()

# 3.3.5 for & range
# (1) range 객체 생성
num1 = range(10)  # range(start)
print('num1 =', num1)
num2 = range(1, 10)  # range(start, stop)
print('num2 =', num2)
num3 = range(1, 10, 2)  # range(start, stop, step)
print('num3 =', num3)

# (2) range 객체 활용
for n in num1:
    print(n, end=' ')
print()
for n in num2:
    print(n, end=' ')
print()
for n in num3:
    print(n, end=' ')
print()

print()

# 3.3.6 for & list
# (1) list에 자료 저장하기
import random
lst = []  # 빈 list 만들기
for i in range(10):  # 0~9
    r = random.randint(1, 10)  # 난수 발생
    lst.append(r)  # 난수 저장

print('lst =', lst)  # 난수 출력

# (2) list에 자료 참조하기
for i in range(10):
    print(lst[i] * 0.25)  # 난수 * 0.25

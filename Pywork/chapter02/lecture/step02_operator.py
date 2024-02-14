# 2.2 연산자(Operator)

# 2.2.1 산술 연산자
num1 = 100  # 피연산자1
num2 = 30  # 피연산자2
print('num1 =', num1)
print('num2 =', num2)

print('=' * 100)

add = num1 + num2  # 덧셈
print('add =', add)
sub = num1 - num2  # 뺄셈
print('sub =', sub)
mul = num1 * num2  # 곱셈
print('mul =', mul)
div = num1 / num2  # 나눗셈
print('div =', div)
div2 = num1 // num2  # 몫
print('div2 =', div2)
div3 = num1 % num2  # 나머지
print('div3 =', div3)
square = num1 ** 2  # 제곱
print('square =', square)

print('=' * 100)

# 2.2.2 관계 연산자
# (1) 동등 비교
bool_result = num1 == num2  # 두 변수의 값이 같은지 비교
print(bool_result)
bool_result = num1 != num2  # 두 변수의 값이 다른지 비교
print(bool_result)

# (2) 크기 비교
bool_result = num1 > num2  # num1 값이 큰지 비교
print(bool_result)
bool_result = num1 >= num2  # num1 값이 크거나 같은지 비교
print(bool_result)
bool_result = num1 < num2  # num2 값이 큰지 비교
print(bool_result)
bool_result = num1 <= num2  # num2 값이 크거나 같은지 비교
print(bool_result)

print('=' * 100)

# 2.2.3 논리 연산자
# 두 관계식이 같은지 판단
log_result = num1 >= 50 and num2 <= 10
print(log_result)

# 두 관계식 중 하나라도 같은지 판단
log_result = num1 >= 50 or num2 <= 10
print(log_result)

log_result = num1 >= 50  # 관계식 판단
print(log_result)

# 괄호 안의 관계식 판단 결과에 대한 부정
log_result = not (num1 >= 50)
print(log_result)

print('=' * 100)

# 2.2.4 대입 연산자
# (1) 변수에 값 할당(=)
i = tot = 10  # i = 10; tot = 10
i += 1  # i = i + 1
tot += i  # tot = tot + i
print('i = %d, tot = %d' % (i, tot))

# 같은 줄에 중복 출력
print('출력1', end=', ')  # end='구분자'
print('출력2')

# (2) 변수 교체
v1, v2 = 100, 200
v2, v1 = v1, v2
print('v1 = %d, v2 = %d' % (v1, v2))

# (3) 패킹(Packing) 할당
lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print('v1 = {}, v2 = {}'.format(v1, v2))

*v1, v2 = lst
print('v1 = {}, v2 = {}'.format(v1, v2))

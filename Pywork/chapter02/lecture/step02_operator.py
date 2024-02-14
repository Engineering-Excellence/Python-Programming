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

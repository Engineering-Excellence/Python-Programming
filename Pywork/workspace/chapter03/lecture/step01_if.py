# (1) 일반 조건문
result = 0
num = int(input('숫자를 입력하세요.: '))

if num >= 5:
    result = num * 2
else:
    result = num + 2
print('result =', result)

# (2) 3항 연산자
# 변수 = 참 if (조건문) else 거짓
result2 = num * 2 if num >= 5 else num + 2
print('result2 =', result2)

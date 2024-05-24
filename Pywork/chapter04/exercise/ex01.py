# [문제1] 다음 lst 변수를 대상으로 각 단계별로 list를 연산하시오.

lst = [10, 1, 5, 2]  # list 생성

# 단계1: lst 원소를 2배 생성하여 result 변수에 저장 및 출력하기
result = lst * 2
print(result)

# 단계2: lst의 첫 번째 원소에 2를 곱하여 result 변수에 추가 및 출력하기
result.append(lst[0] * 2)
print(result)

# 단계3: result의 홀수 번째 원소만 result2 변수에 추가 및 출력하기
result2 = result[1::2]
print(result2)

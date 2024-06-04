# [문제3] 팩토리얼(Factorial)을 계산하는 재귀함수를 작성하시오.

# 재귀함수 정의
def factorial(n: int) -> int:
    if n == 1:  # 종료 조건
        return 1
    else:
        return n * factorial(n=n - 1)


# 함수 호출
result_fact = factorial(n=5)
print('팩토리얼 결과:', result_fact)

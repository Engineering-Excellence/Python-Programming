# 5.5 특수함수

# 5.5.1 가변인수 함수
# (1) 튜플형 가변인수
def func1(name: str, *names: tuple):
    print(name)  # 실인수: 홍길동
    print(names)  # 실인수: ('이순신', '유관순')


func1('홍길동', '이순신', '유관순')

print()

# statistics 모듈 import
from statistics import mean, variance, stdev


# (2) 통계량 구하는 함수
def statis(func: str, *data: tuple) -> float:
    if func == 'avg':
        return mean(data)
    elif func == 'var':
        return variance(data)
    elif func == 'std':
        return stdev(data)
    else:
        raise TypeError


# statis 함수 호출
print('avg =', statis('avg', 1, 2, 3, 4, 5))
print('var =', statis('var', 1, 2, 3, 4, 5))
print('std =', statis('std', 1, 2, 3, 4, 5))
# print('err =', statis('err', 1, 2, 3, 4, 5))

print()


# (3) dict형 가변인수
def emp_func(name: str, age: int, **other: dict):
    print(name)
    print(age)
    print(other)


# emp_func 함수 호출
emp_func('홍길동', 35, addr='서울시', height=17)

# 5.5 특수함수

# 5.5.1 가변인수 함수
# (1) 튜플형 가변인수
def func1(name: str, *names: tuple) -> None:
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
def emp_func(name: str, age: int, **other: dict) -> None:
    print(name)
    print(age)
    print(other)


# emp_func 함수 호출
emp_func('홍길동', 35, addr='서울시', height=17)

print()


# 5.5.2 람다 함수
# (1) 일반 함수
def adder(x: int, y: int) -> int:
    return x + y


print('add =', adder(10, 20))

# (2) 람다 함수
print('add =', (lambda x, y: x + y)(10, 20))

print()

# 5.5.3 스코프(Scope)
# (1) 지역변수 예
x = 50  # 전역변수


def local_func(x: int) -> None:
    x += 50  # 지역변수 -> 종료 시점 소멸


local_func(x)
print('x =', x)


# (2) 전역변수 예
def global_func() -> None:
    global x  # 전역변수 x 사용
    x += 50  # x + 50 = 100


global_func()
print('x =', x)

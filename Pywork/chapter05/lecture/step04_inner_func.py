# 5.6 중첩함수

# 5.6.1 일급 함수와 함수 클로저
# (1) 일급 함수: 함수를 객체로 만들어서 사용하는 함수. 외부함수나 내부함수를 변수에 저장할 수 있는 특성을 가짐.
def a():  # outer
    print('a 함수')

    def b():  # inner
        print('b 함수')

    return b


c = a()  # 외부 함수 호출: a 함수
c()  # 내부 함수 호출: b 함수

print()

# (2) 함수 클로저
data = list(range(1, 101))


def outer_func(data: list) -> tuple:
    dataSet = data  # 값(1~100) 생성

    # inner
    def total():
        return sum(dataSet)

    def average(tot_val: int) -> float:
        return tot_val / len(dataSet)

    return total, average  # inner 반환


# 외부 함수 호출: data 생성
tot, avg = outer_func(data)

# 내부 함수 호출
tot_val = tot()
print('tot =', tot_val)
avg_val = avg(tot_val)
print('avg =', avg_val)

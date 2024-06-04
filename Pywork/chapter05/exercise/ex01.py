# [문제1] 다음 height 변수에 별(star)의 층수를 입력하면 각 층마다 별의 개수가 한 개씩 증가하여 출력되고, 마지막 줄에 별의 개수가 출력되도록 하시오.

# 함수 정의
def star_count(height: int) -> None:
    for i in range(1, height + 1):
        print('*' * i)


# 키보드 입력
h = int(input('height: '))
# star 개수 출력
star_count(height=h)
print(f'star 개수: {h * (h + 1) // 2}')

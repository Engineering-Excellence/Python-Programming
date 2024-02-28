# [문제2] while 반복문을 이용한 '숫자 맞추기 게임'

import random

print('>>숫자 맞추기 게임<<')
com = random.randint(1, 10)  # 1~10 사이 난수 정수 발생

while True:
    my = int(input('예상 숫자를 입력하세요.: '))  # 숫자 입력
    if my > com:
        print('더 작은 수를 입력하세요.')
    elif my < com:
        print('더 큰 수를 입력하세요.')
    else:
        print('~~ 성공 ~~')
        break

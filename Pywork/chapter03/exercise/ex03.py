# [문제3] for 반복문을 이용한 '수열 출력하기'

import sys

write = sys.stdout.write
acc = 0

write('수열 = ')
for i in range(1, 101):
    if i % 3 == 0 and i % 2 != 0:
        write(f'{str(i)} ')
        acc += i

write(f'\n누적합 = {acc}\n')

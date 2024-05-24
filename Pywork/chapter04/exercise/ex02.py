# [문제2] list 원소 추가 및 요소 검사하기
from random import randint

n = int(input("vector 수: "))
vector = [randint(0, 9) for _ in range(n)]
for i in vector:
    print(i)
print(f'vector 크기: {len(vector)}')

print('YES' if int(input()) in vector else 'NO')

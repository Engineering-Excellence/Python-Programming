# [문제4] position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수를 출력하시오.
from collections import Counter

position = ['과장', '부장', '대리', '사장', '대리', '과장']

# freq = {key: 0 for key in position}
# for p in position:
#     freq[p] += 1
# print(freq)

print(dict(Counter(position)))

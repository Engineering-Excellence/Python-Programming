# 비순서 자료구조
# 4.3.1 셋(set)

# 셋 객체 특징: 비순서, 중복 불가, 집합 연산
# (1) 중복 불가
s = {1, 3, 5, 3, 1}
print(len(s))
print(s)
print()

# (2) 요소 반복
for d in s:
    print(d, end=' ')
print()
print()

# (3) 집합 관련 함수
s2 = {3, 6}
print(s.union(s2))  # 합집합
print(s.difference(s2))  # 차집합
print(s.intersection(s2))  # 교집합
print()

# (4) 추가, 삭제 함수
s3 = {1, 3, 5}
print(s3)
s3.add(7)  # 원소 추가
print(s3)
s3.discard(3)  # 원소 삭제
print(s3)
print()

# 중복 제거: 중복 비허용의 특징을 이용하여 리스트의 중복 원소를 제거 가능
gender = ['남', '여', '남', '여']  # 중복 원소를 갖는 리스트
sgender = set(gender)  # list -> set: 중복 원소 제거
lgender = list(sgender)  # set -> list
print(lgender)
print(lgender[1])

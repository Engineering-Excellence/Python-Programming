# 4.3.2 딕트(dict)
# 딕트 객체 특징: 비순서, key(중복 불가):value(중복 가능)
# (1) dict 생성 방법 1
dic = dict(key1=100, key2=200, key3=300)
print(dic)

print()

# (2) dict 생성 방법 2
person = {'name': '홍길동', 'age': 35, 'address': '서울시'}
print(person)
print(person['name'])
print(type(dic), type(person))

print()

# (3) 원소 수정, 삭제, 추가
person['age'] = 45  # dict 원소 수정
print(person)
del person['address']  # dict 원소 삭제
print(person)
person['pay'] = 350  # dict 원소 추가
print(person)

print()

# 요소 검사와 반복
# (4) 요소 검사
print(person['age'])
print('age' in person)

print()

# (5) 요소 반복
for key in person.keys():  # key 넘김
    print(key)
print()
for value in person.values():  # value 넘김
    print(value)
print()
for item in person.items():  # (key, value) 넘김
    print(item)

print()

# 단어 출현 빈도수 구하기
# (1) 단어 데이터 셋
charset = ['abc', 'code', 'band', 'band', 'abc']
wc = {}  # 빈 셋

# (2) get() 함수 이용: key 이용 value 가져오기
for key in charset:
    wc[key] = wc.get(key, 0) + 1  # get(key, default) 이용
print(wc)

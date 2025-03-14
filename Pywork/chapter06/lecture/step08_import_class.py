# 6.4 내장 클래스

# 6.4.1 builtins 모듈 내장 클래스

# (1) 리스트 열거형 객체 이용
lst: list = [1, 3, 5]
for i, c in enumerate(lst):
    print('색인:', i, end=', ')
    print('내용:', c)

# (2) 튜플 열거형 객체 이용
dit: dict = {'name': '홍길동', 'job': '회사원', 'addr': '서울시'}
for i, k in enumerate(dit):
    print('순서:', i, end=', ')
    print('키:', k, end=', ')
    print('값:', dit[k])

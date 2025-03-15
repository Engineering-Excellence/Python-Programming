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

print()

# 6.4.2 import 모듈 내장 클래스

# (1) 모듈 내장 클래스 import
# import datetime  # 모듈 import
from datetime import date, time, datetime

# (2) date 클래스
help(date)  # date 클래스 도움말

today: date = date.today()  # date 객체 생성
print(today)  # date 객체 정보

# date 객체 멤버변수 호출
print(today.year)
print(today.month)
print(today.day)

# date 객체 메서드 호출
w: int = today.weekday()
week: dict = {0: '월', 1: '화', 2: '수', 3: '목', 4: '금', 5: '토', 6: '일'}
print(f'요일 정보: {week.get(w)}({w})')  # Monday==0, ..., Sunday==6

# (3) time 클래스
help(time)  # time 클래스 도움말

now: datetime = datetime.now()
currTime: time = time(hour=now.hour, minute=now.minute, second=now.second)  # time 객체 생성
print(currTime)  # time 객체 정보

# time 객체 멤버변수 호출
print(currTime.hour)
print(currTime.minute)
print(currTime.second)

# time 객체 메서드 호출
isoTime: str = currTime.isoformat()
print(isoTime)

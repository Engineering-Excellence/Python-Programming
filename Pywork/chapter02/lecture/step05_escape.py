# 2.4 문자열(String)

# 2.4.4 이스케이프 문자
# (1) escape 문자 적용
print('escape 문자 적용')
print('\n출력 이스케이프 문자')  # \n: 줄 바꿈 기능

print('-' * 100)

# (2) escape 문자 기능 차단
print('\\n출력 이스케이프 기능 차단1')
print(r'\n출력 이스케이프 기능 차단2')

print('-' * 100)

# (3) 경로 표현: C:\Python\test
print('path =', 'C:\Python\test')
print('path =', 'C:\\Python\\test')
print('path =', r'C:\Python\test')

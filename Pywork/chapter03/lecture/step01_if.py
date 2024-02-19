# 3.2 조건문

# 3.2.1 단일 조건문
var = 10  # if 블럭에서 사용될 변수
if var >= 5:  # 조건식
    print('var=', var)
    print('var는 5보다 크다.')
    print('조건이 참인 경우 실행')
print('항상 실행')

# 100~85: '우수', 84~70: '보통', 69 이하: '저조'
score = int(input('점수 입력: '))
if score >= 85 and score <= 100:
    print('우수')
else:
    if score >= 70:
        print('보통')
    else:
        print('저조')

# 3.2.2 중첩 조건문
score = int(input('점수 입력: '))
grade = ''  # 등급

if 85 <= score <= 100:
    grade = '우수'
elif score >= 70:
    grade = '보통'
else:
    grade = '저조'

print('당신의 점수는 %d이고, 등급은 %s' % (score, grade))

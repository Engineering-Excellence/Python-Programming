# [문제1] 조건문을 이용한 '짐의 무게 계산하기'

weight = int(input("짐의 무게(kg)는 얼마입니까? "))

if weight >= 10:
    print(f"수수료는 {(weight // 10) * 10000:,}원입니다.")
else:
    print("수수료는 없습니다.")

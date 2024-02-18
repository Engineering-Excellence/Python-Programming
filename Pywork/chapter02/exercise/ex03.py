# [문제3] 지방, 탄수화물, 단백질 칼로리의 합계를 계산하는 프로그램을 작성하시오.

# <조건1> 지방, 탄수화물, 단백질의 그램을 키보드로 입력받는다.
fat, carbohydrate, protein = input('지방, 탄수화물, 단백질의 그램을 순서대로 입력하세요.: ').split()

# <조건2> 총 칼로리 = 지방 * 9 + 단백질 * 4 + 탄수화물 * 4
print(f'총 칼로리: {int(fat) * 9 + int(carbohydrate) * 4 + int(protein) * 4} cal')

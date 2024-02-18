# [문제4] 3개의 단어를 키보드로 입력 받아서 각 단어의 첫 글자를 추출하여 단어의 약자를 출력하시오.

# <조건1> 각 단어 변수(word1, word2, word3) 저장
word1, word2, word3 = input('단어 3개를 입력하세요.: ').split()
print(f'첫번째 단어: {word1}\n두번째 단어: {word2}\n세번째 단어: {word3}')

# <조건2> 입력과 출력 구분선: 문자열 연산
print('=' * 30)

# <조건3> 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
abbr = word1[0] + word2[0] + word3[0]
print(f'약자: {abbr}')

# [문제4] 중첩 반복문을 이용한 '단어 카운트하기(word count)'

multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀처럼 매력적인 언어입니다."""

cnt = 0

for s in multiline.split():
    cnt += 1
    print(s)

print('단어 개수: %d개' % cnt)

# 9.5 단어 빈도 수
from pickle import load
from re import compile, sub, Pattern
from collections import Counter
from os import path
from typing import BinaryIO

# (1) pickle file load
file: BinaryIO = open(file=path.join(path.dirname(__file__), "..", "data", "data.pickle"), mode='rb')
news_data2: list[str] = load(file=file)

# (2) 텍스트 전처리
pattern: Pattern[str] = compile(r'[a-z\d,?.:\'\";!@#$%^&*()]')


def clean_text(text: str) -> str:
    """
    텍스트 전처리 함수

    :param text: 전처리할 문자열
    :return: 문장부호, 특수문자, 숫자, 영문, 공백이 정리된 문자열
    """
    return ' '.join(sub(pattern=pattern, repl='', string=text.lower()).split())


# 텍스트 전처리 함수 호출
clean_texts: list[str] = [clean_text(row) for row in news_data2]
print('>> 텍스트 전처리 결과 <<')
print(clean_texts, end='\n\n')

# (3) word count
word_counter: Counter[str] = Counter(' '.join(clean_texts).split())
print('>> 워드 카운트 <<')
print(dict(word_counter), end='\n\n')

# (4) 단어 전처리
# 불용 단어 제거
# del word_counter['[집중진단]']
word_counter.pop('[집중진단]', None)

# 2회 이상 출현 단어 & 2~3자 단어 선정
new_word_count: dict[str, int] = {word: count for word, count in word_counter.items() if
                                  count >= 2 and 2 <= len(word) <= 3}
print('>> 단어 전처리 <<')
print(dict(new_word_count), end='\n\n')

# (5) top word Counter
new_word_counter: Counter[str] = Counter(new_word_count)
top5_word: list[tuple[str, int]] = new_word_counter.most_common(5)
print('>> top 5 단어 <<')
print(top5_word, end='\n\n')

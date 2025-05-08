# [문제1] ftest.txt 파일을 읽어서 다음과 같이 줄 수와 단어 수를 카운트 하시오.

"""
<처리 조건>

1. 문장은 '\n'을 구분자로 한다.
2. 단어는 공백을 구분자로 한다.
"""
from os import sep
from typing import TextIO

file: TextIO = open(f'..{sep}data{sep}ftest.txt', 'r')

lines: list[str] = file.readlines()  # 줄 단위 전체 읽기
docs: list[str] = [line.rstrip() for line in lines]  # 문장 저장
words: list[str] = []  # 단어 저장

for doc in docs:
    words.extend(doc.split())

print('문장 내용')
print(docs)
print(f'문장 수: {len(docs)}', end='\n\n')
print('단어 내용')
print(words)
print(f'단어 수: {len(words)}')

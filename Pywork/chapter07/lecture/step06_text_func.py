# 7.3.3 전처리 함수

from re import sub
from timeit import timeit


# (1) 텍스트 전처리 함수
def clean_text(text: str) -> str:  # 문장 인수
    # 1~6단계
    texts_re: str = text.lower()  # 소문자 변경
    texts_re2: str = sub('\\d', '', texts_re)  # 숫자 제거
    texts_re3: str = sub('[,.?!:;]', '', texts_re2)  # 문장 부호 제거
    texts_re4: str = sub('[@#$%^&*()]', '', texts_re3)  # 특수문자 제거
    texts_re5: str = sub('[a-z]', '', texts_re4)  # 영문자 제거
    texts_re6: str = ' '.join(texts_re5.split())  # 공백 제거
    return texts_re6


def clean_text2(text: str) -> str:
    """
    텍스트 전처리 함수
    :param text: 전처리 할 문자열
    :type text: str
    :return: 전처리 된 문자열
    :rtype: str
    """
    return ' '.join(sub('[\\d,.?!:;@#$%^&*()a-z]', '', text.lower()).split())


if __name__ == '__main__':
    texts: list[str] = [' 우리나라   대한민국, 우리나라%$ 만세', '궁금하면 500오백WON원', '나는 대한민국 사람', '보험료 15000원에 평생 보장 마감 임박', '나는 홍길동']

    # (2) 함수 호출
    texts_result: list[str] = [clean_text(text) for text in texts]
    print(f'{texts_result}, 1,000,000회 실행시간: {timeit(lambda: clean_text(texts[0]), number=1000000)}초')
    texts_result = [clean_text2(text) for text in texts]
    print(f'{texts_result}, 1,000,000회 실행시간: {timeit(lambda: clean_text2(texts[0]), number=1000000)}초')

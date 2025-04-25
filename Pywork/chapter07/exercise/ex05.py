# [문제5] 다음 texts 변수의 텍스트를 전처리 하시오.

from re import sub


def clean_text(text: str) -> str:
    """
    텍스트 전처리 함수
    :param text: 전처리 할 문자열
    :type text: str
    :return: 전처리 된 문자열
    :rtype: str
    """
    return sub('[\\d\\s,.?!:;@#$%^&*()]', '', text.lower())


if __name__ == '__main__':
    texts: list[str] = ['AFAB54747,asabag?', 'abTTa  $$;a12:2424.', 'uysfsfA,A124&***$?']
    print([clean_text(t) for t in texts])

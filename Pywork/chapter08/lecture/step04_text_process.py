# 8.4 파일 자료 처리

# 8.4.1 텍스트 자료 수집
import os

# (1) 텍스트 디렉터리 경로 지정
print(os.getcwd())
txt_data: str = f'..{os.sep}txt_data{os.sep}'  # 상대경로 지정

# (2) 텍스트 디렉터리 목록 반환
sub_dir: list[str] = os.listdir(txt_data)  # txt_data 목록 반환
print(sub_dir)  # ['first', 'second']


# (3) 각 디렉터리의 텍스트 자료 수집 함수
def text_pro(sdirs: list[str]) -> tuple[list[str], list[str]]:
    """
    텍스트 자료 수집 함수

    :param sdirs: 텍스트 자료 수집 대상 디렉터리 리스트
    :type sdirs: list[str]
    :return: 수집된 텍스트 자료 리스트
    :rtype: tuple[list[str], list[str]]
    """
    first_txt: list[str] = []  # first 디렉터리 텍스트 저장
    second_txt: list[str] = []  # second 디렉터리 텍스트 저장

    # (3-1) 디렉터리 구성
    for sdir in sdirs:  # ['first', 'second']
        dirname: str = txt_data + sdir  # 디렉터리 구성
        file_list: list[str] = os.listdir(dirname)  # 파일 목록 반환

        # (3-2) 파일 구성
        for fname in file_list:
            file_path: str = dirname + os.sep + fname  # 파일 구성

            # (3-3) file 선택
            if os.path.isfile(file_path):
                try:
                    # (3-4) 텍스트 자료 수집
                    with open(file_path, 'r', encoding='utf-8') as file:
                        if sdir == 'first':
                            first_txt.append(file.read())
                        elif sdir == 'second':
                            second_txt.append(file.read())
                except Exception as e:
                    print('예외 발생:', e)
    return first_txt, second_txt  # 텍스트 자료 반환


# (4) 함수 호출
first_texts, second_texts = text_pro(sub_dir)

# (5) 수집한 텍스트 자료 확인
print('first_txt 길이 =', len(first_texts))
print('second_txt 길이 =', len(second_texts))

# (6) 텍스트 자료 결합
tot_texts: list[str] = first_texts + second_texts
print('tot_texts 길이 =', len(tot_texts))

# (7) 전체 텍스트 내용
print(type(tot_texts))
print(tot_texts)
for text in tot_texts:
    print(text, end='')

print()

# 8.4.2 pickle 저장
from pickle import dump, load  # file save

try:
    # (1) file save: write binary
    with open(file=f'..{os.sep}data{os.sep}tot_texts.pck', mode='wb') as pfile_w:
        dump(obj=tot_texts, file=pfile_w)

    # (2) file load: read binary
    with open(file=f'..{os.sep}data{os.sep}tot_texts.pck', mode='rb') as pfile_r:
        tot_texts_read: list[str] = load(file=pfile_r)
except Exception as e:
    print('예외 발생:', e)

print('tot_texts 길이 =', len(tot_texts_read))
print(type(tot_texts_read))
print(tot_texts_read)

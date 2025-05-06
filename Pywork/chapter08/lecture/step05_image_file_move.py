# 8.4.3 이미지 파일 이동
from glob import glob
import os

# (1) image 파일 경로
print(os.getcwd())
img_path: str = f'..{os.sep}images{os.sep}'  # 이미지 원본 디렉터리
img_path2: str = f'..{os.sep}images2{os.sep}'  # 이미지 이동 디렉터리

# (2) 디렉터리 존재 유무 확인
if os.path.exists(img_path):
    print(f'{img_path} 디렉터리가 존재함')

    # (3) image 파일 저장, 파일 이동 디렉터리 생성
    if not os.path.exists(img_path2):
        os.mkdir(img_path2)  # 디렉터리 생성
    images: list[str] = []  # jpg 파일 저장

    # (4) images 디렉터리에서 jpg 검색
    for pic_path in glob(img_path + '*.jpg') + glob("*.JPG"):  # jpg 검색

        # (5) 경로와 파일명 분리, 파일명 추가
        split_path: tuple[str, str] = os.path.split(pic_path)   # (디렉터리, 파일명)
        images.append(split_path[1])  # jpg 파일명 추가

        # (6) 이진파일 읽기
        with open(pic_path, 'rb') as rfile:
            output: bytes = rfile.read()

        # (7) 이진파일 쓰기 -> chapter08/jpg 폴더 이동
        with open(img_path2 + split_path[1], 'wb') as wfile:
            wfile.write(output)
    print('jpg file =', images)

else:
    print(f'{img_path} 디렉터리가 존재하지 않음')

# [문제2] BMI 테이블 대상으로 다음과 같은 조건으로 테이블을 검색하시오.

"""
<처리 조건>

1. 키(height)가 170~180 사이에 해당하는 레코드 조회
2. 키보드로 'thin', 'normal', 'fat' 중 하나를 입력하여 label에 속하는 레코드 출력하기(LIKE 명령어 사용)
"""

import pymysql
import os
from dotenv import load_dotenv

if load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'data', 'mysql.env')):
    print('\nenv load 성공')

config: dict[str, str | int | bool] = {
    'host': os.getenv(key='MYSQL_HOST'),
    'user': os.getenv(key='MYSQL_USER'),
    'password': os.getenv(key='MYSQL_PASSWORD'),
    'database': os.getenv(key='MYSQL_DATABASE'),
    'port': int(os.getenv(key='MYSQL_PORT')),
    'charset': os.getenv(key='MYSQL_CHARSET'),
    'use_unicode': bool(os.getenv(key='MYSQL_USE_UNICODE'))
}

conn = None
cursor = None

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # <조건1> 키 170~180 사이 검색
    sql: str = 'SELECT * FROM BMI WHERE HEIGHT BETWEEN 170 AND 180'
    cursor.execute(query=sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
    print('키 170~180 사이에 해당하는 레코드 수:', len(rows), end='\n\n')

    # <조건2> label 조회
    label: str = input('검색할 label 입력(thin/normal/fat): ')
    match label:
        case 'thin':
            sql = 'SELECT * FROM BMI WHERE IDX <= 1'
        case 'normal':
            sql = 'SELECT * FROM BMI WHERE IDX = 2'
        case 'fat':
            sql = 'SELECT * FROM BMI WHERE IDX >= 3'
        case _:
            print('잘못 입력하셨습니다.')
            exit(1)
    cursor.execute(query=sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
    print(f'{label} label 레코드 수: {len(rows)}')

except Exception as e:
    print('예외 발생:', e)
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

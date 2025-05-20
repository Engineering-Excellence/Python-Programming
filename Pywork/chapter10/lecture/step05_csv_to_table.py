# 10.5 File to DB

# 10.5.1 csv to table
"""
csv -> db table
    1차 실행: table 생성 -> 레코드 추가
    2차 실행: 레코드 검색
"""

import pandas as pd
import pymysql
import os
from dotenv import load_dotenv

data_dir: str = os.path.join(os.path.dirname(__file__), '..', 'data')

if load_dotenv(dotenv_path=os.path.join(data_dir, 'mysql.env')):
    print('env load 성공')

config: dict[str, str | int | bool] = {
    'host': os.getenv(key='MYSQL_HOST'),
    'user': os.getenv(key='MYSQL_USER'),
    'password': os.getenv(key='MYSQL_PASSWORD'),
    'database': os.getenv(key='MYSQL_DATABASE'),
    'port': int(os.getenv(key='MYSQL_PORT')),
    'charset': os.getenv(key='MYSQL_CHARSET'),
    'use_unicode': bool(os.getenv(key='MYSQL_USE_UNICODE'))
}

# (1) csv 파일 로드
bmi: pd.DataFrame = pd.read_csv(os.path.join(data_dir, 'bmi.csv'))
bmi.info()

# (2) 각 컬럼 추출
gender: pd.Series = bmi['Gender']
height: pd.Series = bmi['Height']
weight: pd.Series = bmi['Weight']
index: pd.Series = bmi['Index']

conn = None
cursor = None

try:
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # (3) table 생성
    sql = """CREATE TABLE IF NOT EXISTS BMI(
    GENDER VARCHAR(10) NOT NULL,
    HEIGHT INT NOT NULL,
    WEIGHT INT NOT NULL,
    IDX INT NOT NULL
    )"""
    cursor.execute(query=sql)

    # (4) 레코드 조회
    sql = 'SELECT * FROM BMI'
    cursor.execute(query=sql)
    rows: tuple[tuple[str, int, int, int]] = cursor.fetchall()
    if rows:  # (5) 레코드 존재할 경우: 레코드 출력
        for row in rows:
            print(f'{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}')
        print('전체 레코드 수:', len(rows))
    else:  # (6) 레코드 없을 경우: 레코드 추가
        print('100 레코드 추가')
        sql = 'INSERT INTO BMI VALUES (%s, %s, %s, %s)'
        for i in range(100):
            g = gender[i]
            h = height[i]
            w = weight[i]
            idx = index[i]
            cursor.execute(query=sql, args=(g, h, w, idx))
            conn.commit()

except Exception as e:
    print('db error:', e)
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

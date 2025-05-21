# 10.5.2 json to table

import json
import pandas as pd
import pymysql
import os
from dotenv import load_dotenv
from typing import TextIO

# (1) json 파일 로드
file: TextIO = open(file=os.path.join(os.path.dirname(__file__), '..', 'data', 'labels.json'), mode='r',
                    encoding='utf-8')

# (2) decoding: json 문자열 -> dict
lines: list[dict[str, str]] = json.load(fp=file)
file.close()
print(type(lines))
print(len(lines))
print(type(lines[0]))

# (3) DataFrame 생성
df: pd.DataFrame = pd.DataFrame(data=lines)
df.info()
print(df.head())

if load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'data', 'mysql.env')):
    print('\nenv load 성공', end='\n\n')

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

    # (4) table 생성
    sql: str = """CREATE TABLE IF NOT EXISTS LABELS(
    ID VARCHAR(30) PRIMARY KEY,
    URL VARCHAR(150) NOT NULL,
    LABELNAME VARCHAR(50) NOT NULL,
    COLOR CHAR(6) NOT NULL,
    DESCRIPTION VARCHAR(200)
    )"""
    cursor.execute(query=sql)

    # (5) 레코드 조회
    sql = 'SELECT * FROM LABELS'
    cursor.execute(query=sql)
    rows: tuple[tuple[str, str, str, str, str]] = cursor.fetchall()
    if rows:  # (6) 레코드 있는 경우
        print('LABELS 레코드 조회')
        for row in rows:
            print(row)
        print('\n전체 레코드 수:', len(rows))
    else:  # (7) 레코드 없는 경우
        print('30 레코드 추가')
        sql = 'INSERT INTO LABELS VALUES (%s, %s, %s, %s, %s)'
        for i in range(30):
            labelId: str = df.id[i]
            url: str = df.url[i]
            labelName: str = df.name[i]
            color: str = df.color[i]
            description: str = df.description[i]
            cursor.execute(query=sql, args=(labelId, url, labelName, color, description))
            conn.commit()

except Exception as e:
    print('db error:', e)
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

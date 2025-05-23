# 10.6 Table join

# 10.6.2 테이블 조인

import pymysql
import os
from dotenv import load_dotenv

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

    # (1) Table join
    pay: int = int(input('join 급여 입력: '))
    sql: str = """SELECT e.ENO, e.ENAME, e.PAY, d.DNAME, DADDR
    FROM EMP e INNER JOIN DEPT d
    ON e.DNAME = d.DNAME AND e.PAY >= %s"""

    # (2) 레코드 조회
    cursor.execute(query=sql, args=pay)
    data: tuple[tuple[int, str, int, str, str]] = cursor.fetchall()
    for row in data:
        print(row[0], row[1], row[2], row[3], row[4])
    print('검색된 레코드 수:', len(data))

except Exception as e:
    print('db error:', e)
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

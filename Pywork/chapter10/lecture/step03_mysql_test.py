# 10.4 MySQL 연동

# 10.4.1 환경변수와 DB 연동
import pymysql
import os
from dotenv import load_dotenv

# (1) db 연동 환경변수
if load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', 'data', 'mysql.env')):
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

conn = None
cursor = None

try:
    conn = pymysql.connect(**config)  # db 연동 객체
    cursor = conn.cursor()  # sql문 실행 객체

    # (2) 테이블 조회
    sql: str = 'SHOW TABLES'
    cursor.execute(query=sql)
    tables: tuple[tuple[str]] = cursor.fetchall()

    # (3) 전체 table 목록 출력
    print(tables)

    # (4) table 유무
    if tables:
        print('table 있음')
    else:
        print('table 없음')

except Exception as e:
    print('db 연동 error:', e)
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

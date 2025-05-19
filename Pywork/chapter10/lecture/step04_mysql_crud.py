# 10.4.2 MySQL CRUD

import pymysql
import os
from dotenv import load_dotenv

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
    conn = pymysql.connect(**config)
    cursor = conn.cursor()

    # (1) table 생성
    sql: str = """CREATE TABLE IF NOT EXISTS GOODS(
    CODE    INT AUTO_INCREMENT PRIMARY KEY,
    PRODUCT VARCHAR(30) UNIQUE NOT NULL,
    SU      INT            DEFAULT 0,
    DAN     DECIMAL(10, 2) DEFAULT 0.0
    )"""
    cursor.execute(query=sql)

    # (2) 레코드 추가
    code: int = int(input('상품코드 입력: ').strip())
    product: str = input('상품명 입력: ').strip()
    su: int = int(input('수량 입력: ').strip())
    dan: float = float(input('단가 입력: ').strip())

    sql = 'INSERT INTO GOODS VALUES (%s, %s, %s, %s)'
    cursor.execute(query=sql, args=(code, product, su, dan))
    conn.commit()  # db 반영

    # (5) 레코드 수정: code 이용 -> 상품명, 수량, 단가 수정
    code = int(input('수정할 코드 입력: ').strip())
    product = input('수정할 상품명 입력: ').strip()
    su = int(input('수정할 수량 입력: ').strip())
    dan = float(input('수정할 단가 입력: ').strip())

    sql = 'UPDATE GOODS SET PRODUCT = %s, SU = %s, DAN = %s WHERE CODE = %s'
    cursor.execute(query=sql, args=(product, su, dan, code))
    conn.commit()

    # (6) 레코드 삭제
    code = int(input('삭제할 코드 입력: ').strip())
    sql = 'DELETE FROM GOODS WHERE CODE = %s'
    cursor.execute(query=sql, args=code)
    conn.commit()

    # (3) 전체 목록 보기
    sql = 'SELECT * FROM GOODS'
    cursor.execute(query=sql)
    rows = cursor.fetchall()  # 전체 검색

    # 레코드 출력: 양식문자
    for row in rows:  # fetchone()
        print('%3d\t%-8s\t%3d\t%8.1f' % row)
    print('검색 레코드 수:', len(rows))

    # (4) 상품명 조회
    product = input('\n조회할 상품명 입력: ').strip()
    sql = 'SELECT * FROM GOODS WHERE PRODUCT LIKE %s'
    cursor.execute(query=sql, args='%' + product + '%')
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(row[0], row[1], row[2], row[3])
    else:
        print('해당 상품 없음')

except Exception as e:
    print('db error:', e)
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

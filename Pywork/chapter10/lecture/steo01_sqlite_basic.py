# 10 데이터베이스 자료처리

# 10.2 SQLite3

# 10.2.2 CRUD 만들기

import sqlite3
from os import path

print(sqlite3.version_info, end='\n\n')

conn: sqlite3.Connection = None
cursor: sqlite3.Cursor = None

try:
    # (1) db 연동 객체
    conn = sqlite3.connect(database=path.join(path.dirname(__file__), '..', 'data', 'sqlite_db'))  # db 생성 -> 연걸 object

    # (2) sql 실행 객체
    cursor = conn.cursor()

    # (3) table 생성
    sql: str = 'CREATE TABLE IF NOT EXISTS TEST_TABLE(USERNAME TEXT(10), PHONE TEXT(15), ADDR TEXT(50))'
    cursor.execute(sql)  # sql문 실행

    # (4) 레코드 추가
    sql = 'INSERT INTO TEST_TABLE VALUES (?, ?, ?)'  # Placeholder 방식: SQLite, PostgreSQL, JDBC - SQL Injection 방지
    cursor.execute(sql, ('홍길동', '010-1111-1111', '서울시'))
    cursor.execute(sql, ('이순신', '010-2222-2222', '부산시'))
    cursor.execute(sql, ('강감찬', '010-3333-3333', '낙성대'))
    conn.commit()  # db 반영

    # (5) 레코드 조회
    sql = 'SELECT * FROM TEST_TABLE'
    cursor.execute(sql)
    rows: list[tuple[str, str, str]] = cursor.fetchall()  # 조회 레코드 가져오기

    # (6) 레코드 출력
    for row in rows:
        print(row)
    print('\n이름\t\t전화번호\t\t\t주소')
    for row in rows:
        print(f'{row[0]}\t{row[1]}\t{row[2]}')

except Exception as e:
    print('db 연동 실패:', e)
    conn.rollback()  # 실행 취소

finally:
    if cursor:
        cursor.close()  # cursor 객체 닫기
    if conn:
        conn.close()  # conn 객체 닫기

import sqlite3
from os import path

conn: sqlite3.Connection = None
cursor: sqlite3.Cursor = None

try:
    conn = sqlite3.connect(database=path.join(path.dirname(__file__), '..', 'data', 'sqlite_db'))  # db 연동 객체
    cursor = conn.cursor()  # sql 실행 객체

    # (1) table 생성
    sql: str = """CREATE TABLE IF NOT EXISTS GOODS(
    CODE INTEGER PRIMARY KEY AUTOINCREMENT,
    PRODUCT TEXT(30) UNIQUE NOT NULL,
    SU INTEGER DEFAULT 0,
    DAN REAL DEFAULT 0.0
    )"""
    cursor.execute(sql)  # sql 실행

    # (2) 레코드 추가
    cursor.execute("INSERT INTO GOODS VALUES (1, '냉장고', 2, 8500000)")
    cursor.execute("INSERT INTO GOODS VALUES (2, '세탁기', 3,5500000)")
    cursor.execute("INSERT INTO GOODS(PRODUCT) VALUES('전자레인지')")
    cursor.execute("INSERT INTO GOODS(PRODUCT, DAN) VALUES('HDTV', 15000000)")
    conn.commit()  # db 반영

    # (5) 레코드 2차 추가
    code: int = int(input('상품코드 입력: ').strip())
    product: str = input('상품명 입력: ').strip()
    su: int = int(input('수량 입력: ').strip())
    dan: float = float(input('단가 입력: ').strip())
    sql = 'INSERT INTO GOODS VALUES (?, ?, ?, ?)'
    cursor.execute(sql, (code, product, su, dan))  # 레코드 추가
    conn.commit()

    # (6) 레코드 수정: code -> su, dan 수정
    code = int(input('수정 상품코드 입력: ').strip())
    su = int(input('수정 수량 입력: ').strip())
    dan = float(input('수정 단가 입력: ').strip())
    sql = 'UPDATE GOODS SET SU = ?, DAN = ? WHERE CODE = ?'
    cursor.execute(sql, (su, dan, code))  # 레코드 수정
    conn.commit()

    # (7) 레코드 삭제: code -> 삭제
    code = int(input('삭제 상품코드 입력: ').strip())
    sql = 'DELETE FROM GOODS WHERE CODE = ?'
    cursor.execute(sql, (code,))  # 레코드 삭제
    conn.commit()

    # (3) 레코드 조회
    sql = 'SELECT * FROM GOODS'
    cursor.execute(sql)
    rows: list[tuple[int, str, int, float]] = cursor.fetchall()  # 레코드 가져오기

    for row in rows:
        print(row[0], row[1], row[2], row[3])
    print('검색된 레코드 수:', len(rows))

    # (4) 상품명 조회
    product = input('\n상품명 입력: ').strip()
    sql = 'SELECT * FROM GOODS WHERE PRODUCT LIKE ?'
    cursor.execute(sql, ('%' + product + '%',))  # 조회
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print('검색된 레코드 없음')

except Exception as e:
    print('db error:', e)
    conn.rollback()
finally:
    if cursor:
        conn.close()
    if conn:
        conn.close()

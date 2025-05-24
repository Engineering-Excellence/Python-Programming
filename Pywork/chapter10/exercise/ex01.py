# [문제1] 다음과 같은 메뉴를 이용하여 goods 테이블을 관리하시오.

"""
<처리 조건>

1. [레코드 처리 메뉴]에서 메뉴 번호를 키보드로 입력받아서 레코드를 관리한다.
2. [레코드 처리 메뉴]는 다음과 같다.

[레코드 처리 메뉴]
1. 레코드 조회
2. 레코드 추가
3. 레코드 수정
4. 레코드 삭제
5. 프로그램 종료
    메뉴번호 입력:

< 각 메뉴 작업 절차>
1번 입력: 전체 레코드 조회 결과 출력
2번 입력: 키보드 입력(상품코드, 상품명, 수량, 단가) -> 레코드 추가
3번 입력: 키보드 입력(상품코드, 수량, 단가) -> 레코드 수정(수량, 단가 수정)
4번 입력: 키보드 입력(상품코드) -> 레코드 삭제
5번 입력: 프로그램 종료
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

    sql: str = """CREATE TABLE IF NOT EXISTS GOODS(
    CODE    INT AUTO_INCREMENT PRIMARY KEY,
    PRODUCT VARCHAR(30) UNIQUE NOT NULL,
    SU      INT            DEFAULT 0,
    DAN     INT            DEFAULT 0
    )"""
    cursor.execute(query=sql)

    while True:
        print('\n\t[레코드 처리 메뉴]')
        print('1. 레코드 조회')
        print('2. 레코드 추가')
        print('3. 레코드 수정')
        print('4. 레코드 삭제')
        print('5. 프로그램 종료')

        menu: str = input('\t메뉴번호 입력: ').strip()

        match menu:
            case '1':  # 1. 레코드 조회
                print('\n\t[레코드 조회]')
                sql = 'SELECT * FROM GOODS'
                cursor.execute(query=sql)
                rows = cursor.fetchall()
                for row in rows:
                    print(f'{row[0]:3d}\t{row[1]:8s}\t{row[2]:3d}개\t{row[3]:10,d}원')
                print(f'전체 레코드 수: {len(rows)}개')

            case '2':  # 2. 레코드 추가
                print('\n\t[레코드 추가]')
                code = int(input('상품코드 입력: ').strip())
                product = input('상품명 입력: ').strip()
                su = int(input('수량 입력: ').strip())
                dan = int(input('단가 입력: ').strip())
                sql = 'INSERT INTO GOODS VALUES (%s, %s, %s, %s)'
                cursor.execute(query=sql, args=(code, product, su, dan))
                conn.commit()
                print('레코드 추가 완료')

            case '3':  # 3. 레코드 수정
                print('\n\t[레코드 수정]')
                code = int(input('상품코드 입력: ').strip())
                sql = 'SELECT * FROM GOODS WHERE CODE = %s'
                cursor.execute(query=sql, args=code)
                rows = cursor.fetchall()
                for row in rows:
                    print(f'\n{row[0]:3d}\t{row[1]:8s}\t{row[2]:3d}개\t{row[3]:10,d}원')
                ans = input('주의! 정말로 수정하시겠습니까?(Y/N)').strip().upper()
                if ans == 'Y':
                    su = int(input('수량 입력: ').strip())
                    dan = int(input('단가 입력: ').strip())
                    sql = 'UPDATE GOODS SET SU = %s, DAN = %s WHERE CODE = %s'
                    cursor.execute(query=sql, args=(su, dan, code))
                    conn.commit()
                    print('레코드 수정 완료')
                else:
                    print('레코드 수정 취소')

            case '4':  # 4. 레코드 삭제
                print('\n\t[레코드 삭제]')
                code = int(input('상품코드 입력: ').strip())
                sql = 'SELECT * FROM GOODS WHERE CODE = %s'
                cursor.execute(query=sql, args=code)
                rows = cursor.fetchall()
                for row in rows:
                    print(f'\n{row[0]:3d}\t{row[1]:8s}\t{row[2]:3d}개\t{row[3]:10,d}원')
                ans = input('주의! 정말로 삭제하시겠습니까?(Y/N)').strip().upper()
                if ans == 'Y':
                    sql = 'DELETE FROM GOODS WHERE CODE = %s'
                    cursor.execute(query=sql, args=code)
                    conn.commit()
                    print(f'{rows[0][1]} 삭제 완료')
                else:
                    print('레코드 삭제 취소')

            case '5':  # 5. 프로그램 종료
                print('\n프로그램을 종료합니다.')
                break

            case _:  # 잘못 입력한 경우
                print('해당 메뉴는 없습니다.\n')

except Exception as e:
    print('예외 발생:', e)
    conn.rollback()
finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()

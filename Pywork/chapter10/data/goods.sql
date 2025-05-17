-- 10.3 MySQL(MariaDB) 설치

-- 10.3.2 DB, Table, User 만들기

-- (1) 데이터베이스 생성 및 사용자 데이터베이스 선택
CREATE DATABASE IF NOT EXISTS work;
SHOW DATABASES;
USE work;

-- (2) 테이블 만들기
CREATE TABLE IF NOT EXISTS GOODS
(
    CODE    INT AUTO_INCREMENT PRIMARY KEY,
    PRODUCT VARCHAR(30) UNIQUE NOT NULL,
    SU      INT            DEFAULT 0,
    DAN     DECIMAL(10, 2) DEFAULT 0.0
);
SHOW TABLES;

-- (3) 테이블에 레코드 추가
INSERT INTO GOODS
VALUES (1, '냉장고', 2, 850000);
INSERT INTO GOODS
VALUES (2, '세탁기', 3, 550000);
INSERT INTO GOODS
VALUES (3, '전자레인지', 2, 350000);
INSERT INTO GOODS
VALUES (4, 'HDTV', 3, 1500000);
COMMIT;

-- (4) 레코드 조회
SELECT *
FROM GOODS;

-- (5) 사용자 계정 만들기
CREATE USER IF NOT EXISTS 'admin'@'localhost' IDENTIFIED BY 'admin';

-- (6) 사용자 접속 권한 설정하기
GRANT ALL PRIVILEGES ON work.* TO 'admin'@'%';
GRANT ALL PRIVILEGES ON work.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;

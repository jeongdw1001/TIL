< 실습 >
```sql
USE employees;

USE mysql;
SELECT * FROM employees;

SELECT * FROM titles ;

SELECT * FROM employees.titles;

SELECT * FROM employees.titles;
SELECT * FROM titles;

SELECT first_name FROM employees;

SELECT first_name, last_name, gender FROM employees;

-- 한줄 주석 연습
SELECT first_name, last_name, gender -- 이름과 성별 열을 가져옴
FROM employees;

/* 블록 주석 연습
SELECT first_name, last_name, gender
FROM employees;
*/

```
```sql
-- <실습 1> --

SHOW DATABASES;

USE employees;

SHOW TABLE STATUS;

SHOW TABLES; 

DESCRIBE employees; -- 또는 DESC employees;

SELECT first_name, gender FROM employees;

```
```sql
-- </실습 1> --

SELECT first_name AS 이름 , gender 성별, hire_date '회사 입사일'
FROM employees;

-- <실습 2> --

DROP DATABASE IF EXISTS sqldb; -- 만약 sqldb가 존재하면 우선 삭제한다.
CREATE DATABASE sqldb;

USE sqldb;
CREATE TABLE usertbl -- 회원 테이블
( userID  	CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
  name    	VARCHAR(10) NOT NULL, -- 이름
  birthYear   INT NOT NULL,  -- 출생년도
  addr	  	CHAR(2) NOT NULL, -- 지역(경기,서울,경남 식으로 2글자만입력)
  mobile1	CHAR(3), -- 휴대폰의 국번(011, 016, 017, 018, 019, 010 등)
  mobile2	CHAR(8), -- 휴대폰의 나머지 전화번호(하이픈제외)
  height    	SMALLINT,  -- 키
  mDate    	DATE  -- 회원 가입일
);
CREATE TABLE buytbl -- 회원 구매 테이블(Buy Table의 약자)
(  num 		INT AUTO_INCREMENT NOT NULL PRIMARY KEY, -- 순번(PK)
   userID  	CHAR(8) NOT NULL, -- 아이디(FK)
   prodName 	CHAR(6) NOT NULL, --  물품명
   groupName 	CHAR(4)  , -- 분류
   price     	INT  NOT NULL, -- 단가
   amount    	SMALLINT  NOT NULL, -- 수량
   FOREIGN KEY (userID) REFERENCES usertbl(userID)
);

#DELETE FROM usertbl WHERE userID='LSG'; 잘못된 데이터를 입력해서 코드 생성

INSERT INTO usertbl VALUES('LSG', '이승기', 1987, '서울', '011', '1111111', 182, '2008-8-8');
INSERT INTO usertbl VALUES('KBS', '김범수', 1979, '경남', '011', '2222222', 173, '2012-4-4');
INSERT INTO usertbl VALUES('KKH', '김경호', 1971, '전남', '019', '3333333', 177, '2007-7-7');
INSERT INTO usertbl VALUES('JYP', '조용필', 1950, '경기', '011', '4444444', 166, '2009-4-4');
INSERT INTO usertbl VALUES('SSK', '성시경', 1979, '서울', NULL  , NULL      , 186, '2013-12-12');
INSERT INTO usertbl VALUES('LJB', '임재범', 1963, '서울', '016', '6666666', 182, '2009-9-9');
INSERT INTO usertbl VALUES('YJS', '윤종신', 1969, '경남', NULL  , NULL      , 170, '2005-5-5');
INSERT INTO usertbl VALUES('EJW', '은지원', 1972, '경북', '011', '8888888', 174, '2014-3-3');
INSERT INTO usertbl VALUES('JKW', '조관우', 1965, '경기', '018', '9999999', 172, '2010-10-10');
INSERT INTO usertbl VALUES('BBK', '바비킴', 1973, '서울', '010', '0000000', 176, '2013-5-5');
INSERT INTO buytbl VALUES(NULL, 'KBS', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'KBS', '노트북', '전자', 1000, 1);
INSERT INTO buytbl VALUES(NULL, 'JYP', '모니터', '전자', 200,  1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '모니터', '전자', 200,  5);
INSERT INTO buytbl VALUES(NULL, 'KBS', '청바지', '의류', 50,   3);
INSERT INTO buytbl VALUES(NULL, 'BBK', '메모리', '전자', 80,  10);
INSERT INTO buytbl VALUES(NULL, 'SSK', '책'    , '서적', 15,   5);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '청바지', '의류', 50,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);
INSERT INTO buytbl VALUES(NULL, 'EJW', '책'    , '서적', 15,   1);
INSERT INTO buytbl VALUES(NULL, 'BBK', '운동화', NULL   , 30,   2);

SELECT * FROM usertbl;
SELECT * FROM buytbl;
```

## - usertbl

userID|name|birthYear|addr|mobile1|mobile2|height|mDate
|---|---|---|---|---|---|---|---|
BBK	|바비킴	|1973	|서울	|010	|0000000	|176	|2013-05-05
EJW	|은지원	|1972	|경북	|011	|8888888	|174	|2014-03-03
JKW|	조관우|	1965	|경기	|018	|9999999	|172	|2010-10-10
JYP|	조용필|	1950	|경기	|011	|4444444	|166	|2009-04-04
KBS	|김범수	|1979	|경남	|011	|2222222	|173	|2012-04-04
KKH	|김경호|	1971	|전남	|019	|3333333|	177	|2007-07-07
LJB	|임재범	|1963	|서울	|016	|6666666	|182	|2009-09-09
LSG	|이승기	|1987	|서울	|011	|1111111	|182	|2008-08-08
SSK	|성시경	|1979	|서울	|null	|null	|186	|2013-12-12
YJS	|윤종신	|1969	|경남	|	null|	null|170	|2005-05-05
							
## - buytbl
num|userID|prodName|groupName|price|amount
|---|---|---|---|---|---|
1	|KBS|	운동화	|null	|30	|2
2	|KBS|	노트북	|전자	|1000|	1
3	|JYP|	모니터	|전자	|200|	1
4	|BBK|	모니터	|전자	|200|	5
5	|KBS|	청바지	|의류	|50	|3
6	|BBK|	메모리	|전자	|80	|10
7	|SSK|	책	|서적	|15|	5
8	|EJW|	책	|서적	|15	|2
9	|EJW|	청바지	|의류	|50	|1
10	|BBK|	운동화	|null	|30|	2
11	|EJW|	책	|서적|	15|	1
12	|BBK|	운동화|	null|	30|	2





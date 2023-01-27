1. 라이브러리 가져오기
2. 접속하기(DB)
3. 커서 가져오기(객체)
4. SQL 구문 만들기(CRUD)-Create,Read,Update,Delete / Select, Insert 등
5. SQL 구문 실행하기
6. DB에 complete하기
7. DB 연결 닫기



- 각 데이터베이스의 라이브러리 가져오기
	- python
	- DB 연결 라이브러리
		- pip install pymysql
		- import pymysql

- 접속하기(DB)
	- .connect(userID, PW, db 등)

- 커서 가져오기(객체 생성)
	- .cursor() : 모든 데이터가 들어오는 루트

- SQL 구문 만들기(CRUD)
	- select * from table; 등등 -->  명단 table 보여주면 데이터를 받아오는 과정이 필요
	- update, delete, insert --> true/false만 보여줌

- SQL 구문 실행하기
	- execute()

- DB에 complete하기
	- commit()

- DB 연결 닫기
	- close()
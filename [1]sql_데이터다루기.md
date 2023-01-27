## 1. pymysql 모듈 이해 및 실습


### 1.1 pymysql 라이브러리 소개 및 설치

- 일반적인 mysql 핸들링 코드 작성 순서

1. pymysql 모듈 import

2. pymysql.connect() 메소드를 사용해 mysql을 연결

    - 호스트명, 포트, 아이디, 암호, 접속할 db 등을 파라미터로 지정

3. mysql 접속이 성공하면, connection  객체로부터 cursor() 메서드를 호출하여 cursor() 객체를 가져옴

4. cursor 객체의 execute() 메서드를 사용해 sql 문장을 DB 서버에 전송

5. SQL 쿼리의 경우 Cursor 객체의 fetchall(), fetchone(), fetchmany() 등의 메서드를 사용하여 서버로부터 가져온 데이터를 코드에 활용

6. 삽입, 갱신, 삭제 등의 DML 문장을 실행하는 경우, INSERT/UPDATE/DELETE 후 connection 객체의 commit() 메서드를 사용하여 데이터를 확정

7. connection 객체의 close() 메서드를 사용하여 db 연결을 닫음



```python
!pip install pymysql
```

<pre>
Requirement already satisfied: pymysql in c:\users\user\appdata\roaming\python\python39\site-packages (1.0.2)
Note: you may need to restart the kernel to use updated packages.
</pre>

```python
# 라이브러리 가져오기
import pymysql
```


```python
# 접속하기(DB)
db = pymysql.connect(host='localhost',port=3306,user='root',passwd='ekdnsdbrk0224!?',charset='utf8')
```


```python
db
```

<pre>
<pymysql.connections.Connection at 0x2727a324040>
</pre>

```python
# 커서 object 가져오기(객체 생성)
cursor = db.cursor()
```


```python
# sql 실행하기
sql = "create database IF NOT EXISTS ecommerce"
cursor.execute(sql)
```

<pre>
1
</pre>

```python
sql = "show databases"
cursor.execute(sql)
result = cursor.fetchall()
result
```

<pre>
(('ecommerce',),
 ('employees',),
 ('information_schema',),
 ('my_emp',),
 ('my_emp01',),
 ('mysql',),
 ('performance_schema',),
 ('sakila',),
 ('students',),
 ('sys',),
 ('tabledb',),
 ('world',))
</pre>

```python
# db 변경
sql = 'use ecommerce'
cursor.execute(sql)
```

<pre>
0
</pre>

```python
# 현재 db 확인
sql = "select database()"
cursor.execute(sql)
result = cursor.fetchone()
result
```

<pre>
('ecommerce',)
</pre>

```python
cursor
```

<pre>
<pymysql.cursors.Cursor at 0x2727b63b490>
</pre>
- cursor는 control structure of database임 (연결된 객체)



```python
sql = """
CREATE TABLE product(
    PRODUCT_CODE varchar(20) not null,
    TITLE varchar(200) not null,
    ORI_PRICE int,
    DISCOUNT_PRICE int,
    DISCOUNT_PERCENT int,
    DELIVERY varchar(2),
    PRIMARY KEY(PRODUCT_CODE)
);
"""
```


```python
cursor.execute(sql)
```

<pre>
0
</pre>

```python
sql = 'show tables'
cursor.execute(sql)
result = cursor.fetchall()
result
```

<pre>
(('product',),)
</pre>

```python
# 연결종료
db.close()
```

### 1.2 패턴으로 익히는 pymysql



```python
# 1. 라이브러리 가져오기
import pymysql
# 2. 접속하기
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='ekdnsdbrk0224!?',db='ecommerce',charset='utf8')
db
```

<pre>
<pymysql.connections.Connection at 0x2727cbcd430>
</pre>

```python
# 커서 가져오기
cursor = db.cursor()
```


```python
# 4. sql 구문 만들기(CRUD SQL 구문 등)
sql = """
    CREATE TABLE product2 (
        PRODUCT_CODE varchar(20) not null,
        TITLE varchar(200) not null,
        ORI_PRICE int,
        DISCOUNT_PRICE int,
        DISCOUNT_PERCENT int,
        DELIVERY varchar(2),
        PRIMARY KEY(PRODUCT_CODE)
    );
"""
```


```python
# 5. SQL 구문 실행하기
cursor.execute(sql)
```

<pre>
0
</pre>

```python
# 6. db에 complete 하기
db.commit()
```


```python
# 7. db 연결 닫기
db.close()
```

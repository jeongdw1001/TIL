```sql


-- Q1.) 전체테이블 목록을 출력하자.
-- use my_emp
show tables;

-- Q2.) 사원의 이름, 봉급, 커미션을 출력해보자.
select ENAME, SAL, COMM
FROM EMP;

-- Q3.) 사원의 이름, 매니저를 출력해보자.
SELECT ENAME, MGR
FROM EMP;

-- Q4.) 사원의 이름, 연봉을 출력해보자.
SELECT ENAME, SAL*12 AS 연봉
FROM EMP;


-- Q5.) 사원의 이름과 급여를 출력하되 급여는 공급 + 커미션으로 계산한다. 
# NULL은 연산이 불가능
SELECT ENAME, SAL + COMM
FROM EMP;

-- NULL값을 0으로 변환하자 _ IFNULL, ORACLE에서는 NVL(컬럼, 대체값)
SELECT ENAME, SAL, SAL + ifnull(COMM, 0)
FROM EMP;

SELECT ENAME, SAL, SAL + ifnull(COMM, '값없음')
FROM EMP;

DESC EMP;

-- Q6.) 커미션이 책정되지 않은 사원은 커미션을 3000으로 지정한 후
-- 사원의 이름, 봉급, 커미션을 출력하자.

SELECT ENAME, IFNULL(COMM, 3000)
FROM EMP;

-- Q7.) 급여 = 봉급 + 커미션 - 세금 / 세금 = 봉급의 15%
-- 사원의 이름, 봉급, 커미션, 세금, 급여를 출력하자.

SELECT ENAME, SAL, COMM, SAL*0.15 AS 세금, (SAL+IFNULL(COMM, 0) - (SAL*0.15)) AS 급여 
FROM EMP; 
```
```sql
/*
비교연산 	> 	>= 	< 	<=	==	!=				<> : 확인해보기
SELECT			#3
FROM			#1
WHERE			#2 결과가 TRUE일때 출력

*/

-- Q1.) 사원의 봉급이 1000 이상인 사람의 이름,  봉급을 출력해보자.
SELECT ENAME, SAL
FROM EMP
WHERE SAL >= 1000 ;

-- Q2.) 부서번호가 10번인 사원의 이름과 부서 번호를 출력하자.
SELECT ENAME, DEPTNO
FROM EMP
WHERE DEPTNO = 10 ;

-- Q3.) 부서번호가 10번이고 월급이 1000 이상인 사원의 이름, 부서번호, 월급을 출력하자.
SELECT ENAME, DEPTNO, SAL
FROM EMP
WHERE DEPTNO = 10 AND SAL >= 1000;

-- Q4.) 부서번호가 10, 20번인 사원의 이름과 부서번호를 출력해보자.
SELECT ENAME, DEPTNO
FROM EMP
WHERE DEPTNO = 10 OR DEPTNO = 20;

-- Q5.) 사원의 입사년도가 80년 이후에 입사한 사원의 이름과 입사년도를 출력하자.
SELECT ENAME, HIREDATE
FROM EMP
WHERE HIREDATE >= '1980/01/01';

SELECT ENAME, HIREDATE
FROM EMP
WHERE HIREDATE >= '80/01/01';

SELECT ENAME, HIREDATE
FROM EMP
WHERE HIREDATE >= '80-01-01';

SELECT ENAME, HIREDATE
FROM EMP
WHERE HIREDATE >= '1980-01-01';
```
```sql
-- Q1) 사원테이블에서 사원의 이름이 A로 시작하는 사원의 이름을 출력하자.
SELECT ENAME
FROM EMP
WHERE ENAME LIKE 'A%';

-- Q2) 사원테이블에서 사원의 이름에 T가 2개 들어간 사원의 이름을 출력하자.
SELECT ENAME
FROM EMP
WHERE ENAME LIKE '%T%T';

-- Q3) 사원테이블에서 사원의 이름에 L이 2개 들어간 사원의 이름을 출력하자.
SELECT ENAME
FROM EMP
WHERE ENAME LIKE '%L%L';

-- Q4) 사원테이블에서 사원의 이름이 T로 끝나는 사원의 이름을 출력하자.
SELECT ENAME
FROM EMP
WHERE ENAME LIKE '%T';

-- Q5) 사원테이블에서 사원의 이름이 A로 시작하고 N으로끝나는 사원의 이름을 출력하자.
SELECT ENAME
FROM EMP
WHERE ENAME LIKE 'A%N';

-- Q6) 사원테이블에서 사원의 이름에 두번째가 M인 사원의 이름을 출력하자.
SELECT ENAME
FROM EMP
WHERE ENAME LIKE '_M%';
```
```sql
/*
	SELECT  칼럼1, 칼럼2, 칼럼3
    FROM 테이블
    ORDER BY 칼럼1;
    
    SELECT  칼럼1, 칼럼2, 칼럼3
    FROM 테이블
    ORDER BY 1;
    ASC / DESC를 칼럼명 뒤에 오름차순, 내림차순
    
*/
-- Q1) 사원테이블에서 사원의 이름을 오름차순으로 출력해보자.
	SELECT  ENAME
    FROM EMP
    ORDER BY ENAME ASC;
    
    SELECT  ENAME
    FROM EMP
    ORDER BY 1 ASC;

-- Q2) 사원테이블에서 사원의 이름을 내림차순으로 출력해보자.
	SELECT  ENAME
    FROM EMP
    ORDER BY 1 DESC;

-- Q3) 사원테이블에서 사원의 이름을 오름차순으로 구현하고 봉급을 내림차순으로 출력해보자.
	SELECT  ENAME, SAL
    FROM EMP
    ORDER BY 1, SAL DESC;
    
    SELECT  ENAME, SAL
    FROM EMP
    ORDER BY ENAME, 2 DESC;
```
```sql    
/*
	집계함수(칼럼명) : null 처리 안됨
    sum, avg, var, mean, count ...
*/    

-- Q1) 봉급을 집계함수를 통해서 출력해보자.
select sum(sal), avg(sal), var(sal), mean(sal), count(sal)
from emp;

-- Q2) count함수 사용
select count(ename), count(*), count(comm), count(ifnull(comm,0))
from emp;

select sum(comm), count(ifnull(comm,0))
from emp;

select avg(comm), count(ifnull(comm,0))
from emp;

select max(comm), count(ifnull(comm,0))
from emp;

select min(comm), count(ifnull(comm,0))
from emp;

-- Q3) 사원테이블에서 부서번호가 10번인 사원의 평균 월급을 구해보자
select avg(sal) 
from emp
where deptno=10;

-- Q4) 사원테이블에서 부서번호가 10번과 20번인 사원의 평균 월급을 구해보자
select avg(sal) 
from emp
where deptno in(10,20);		#data or data...

select avg(sal) 
from emp
where deptno=10 or deptno=20;

-- Q5) 사원테이블에서 직업이 salesman인 사원의 평균 월급을 구해보자
select avg(sal) 
from emp
where job = 'SALESMAN';  # -> 데이터가 대문자로 이루어져있으므로 대문자로 적어야함.
```
```sql  
/*
group by
1. group by문 다음에는 데이터를 구분 짓기 위한 표현식으로  ************************완전중요*************************
해당 테이블의 컬럼 명이나 변수 값 등이 올 수 있으며 
그룹 함수를 사용한 형태는 올 수 없다. <group by avg(sal) 안됨

2. select-list에는 group by문에 명시된 표현식(단, *는 안됨)과 
그 외 그룹함수를 사용한 표현식만이 올 수 있다.  **************************완전중요*************************

3. 출력된 결과를 정렬하기 위해 order by문을 사용하면 된다.
단, order by문 다음에는 select-list에서 명시된 칼럼 또는
표현식과 칼럼의 별칭(alias), 컬럼 번호 등만 사용
*/

-- Q1) 부서별 평균 월급을 구해라.
SELECT ENAME, AVG(SAL)
FROM EMP
GROUP BY DEPTNO;

SELECT DEPTNO
FROM EMP
GROUP BY DEPTNO;

SELECT DEPTNO AS NO, AVG(SAL)
FROM EMP
GROUP BY DEPTNO
ORDER BY NO;

SELECT DEPTNO AS NO, AVG(SAL) AS 평균월급
FROM EMP
GROUP BY DEPTNO
ORDER BY 평균월급 DESC;

-- Q2) 직업별 평균 월급을 구하자.
SELECT JOB, AVG(SAL)
FROM EMP
GROUP BY JOB;

-- Q3) 부서별 평균월급을 구하되, 10번 부서의 평균 월급을 구하자.
SELECT DEPTNO, AVG(SAL)
FROM EMP
WHERE DEPTNO = 10
group by DEPTNO;

-- Q4) 직업별 월급의 합을 구하라.
SELECT JOB, SUM(SAL)
FROM EMP
GROUP BY JOB;

-- Q5) 직업이 SALESMAN인 사원의 월급의 합을 구하라.
SELECT JOB, SUM(SAL)
FROM EMP
WHERE JOB = 'SALESMAN'
GROUP BY JOB;

-- Q6) 사원테이블에서 사원의 최대월급을 출력하라.
SELECT MAX(SAL)
FROM EMP;


-- Q7) 각 부서별로 최대월급을 출력하라.
SELECT DEPTNO, MAX(SAL)
FROM EMP
GROUP BY DEPTNO;
```
```sql  
/* 
	IS [NOT] NULL
    
*/

-- Q1) 사원테이블에서 커미션이 책정되어 있는 사원의 이름과 커미션을 출력해라.
SELECT ENAME, COMM
FROM EMP
WHERE COMM IS NOT NULL;

-- Q2) 사원테이블에서 커미션이 책정되어 있지 않은 사원의 이름과 커미션을 출력해라.
SELECT ENAME, COMM
FROM EMP
WHERE COMM IS NULL;
```
````sql  
/*HAVING 사용하기(많으면 3문제 출제)
- GROUP함수로 집계된 데이터에 조건을 줄 때 사용
- 연산자는 GROUP BY 연산에 의해서 나누어진 데이터들을 다시 걸러주기 위해서 사용한다.
제2의 WHERE조건문이라고 할 수 있으며 조건문에서 그룹함수가 사용 가능
- HAVING문 다음에는 SELECT-LIST에서 사용한 컬럼곽 그룸함수를 사용한 컬럼에 대해서만 조건을 줄 수 있다.

[내부 수행(호출) 순서]
SELECT --------------------5
FROM --------------------1
WHERE --------------------2
GROUP BY --------------------3
HAVING --------------------4
ORDER BY --------------------6

[실행순서]    -> 1년 2회정도 출제
SELECT --------------------6
FROM --------------------1
WHERE --------------------2
GROUP BY --------------------3
HAVING --------------------4
ORDER BY --------------------5

*/

-- Q1) 직업별 총월급을 구하고, 총월급이 5000 이상인 것만 출력하라.
SELECT JOB, SUM(SAL)
FROM EMP
GROUP BY JOB
HAVING SUM(SAL) >= 5000;

-- Q1) 부서별 총월급을 구하고, 총월급이 10000 이상인 것만 출력하라.
SELECT DEPTNO, SUM(SAL)
FROM EMP
GROUP BY DEPTNO
HAVING SUM(SAL) >= 10000;
 
/*
WITH ROLLUP = 그룹총합, 부분소계 : ROLLUP 연산자는 GROUP BY문과 함께 사용되며
GROUP BY문에서 명시한 컬럼 순서대로 추가적인 요약정보를 단계적으로 만들어준다.
*/

-- Q1) 부서별 총합 뿐만 아니라 전체 총합 및 세부 내역을 보고 싶을 때
SELECT DEPTNO, ENAME, SUM(SAL)
FROM EMP
GROUP BY DEPTNO, ENAME WITH ROLLUP;

-- Q2) ROLLUP을 이용해 직위별 사원의 이름과 월급을 출력하라.
SELECT JOB, ENAME, SUM(SAL)
FROM EMP
GROUP BY JOB, ENAME WITH ROLLUP;

SELECT JOB, ENAME, SUM(SAL)
FROM EMP
GROUP BY JOB, ENAME WITH ROLLUP
ORDER BY 1;
 
/*
CUBE = 소계, 총계 : GROUP BY 문과 함께 사용되며 GROUP BY 문에서 명시한
전체 컬럼에 대하여 추가적인 요약 정보를 단계적으로 만들어준다.

GROUPING : GROUPING 함수는 그룹 기준에서 고려하지 않은 부분 총계인 경우에 1을 리턴하고,
그렇지 않은 경우 0을 리턴한다.

*/

SELECT ENAME, COMM, SUM(COMM) AS SUM, GROUPING(ENAME), GROUPING(COMM)
FROM EMP
GROUP BY ENAME, COMM WITH ROLLUP;


/* ROW_NUMBER
SELECT ROW_NUMBER() [OVER PARTITION BY, ORDER BY]
열 A값의 내림차순으로 일련 번호 리턴 : SELECT ROW_NUMBER() OVER (ORDER BY A DESC);

컬럼 X 값으로 그룹핑 분할하고, 그 중에서 컬럼 A의 값의 내림차순으로 일련번호를 리턴
SELECT ROW_NUMBER() OVER (PARTITION BY X ORDER BY A DESC);

SELECT RANK() OVER (PARTITION BY , ORDER BY )	1,2,2,2,5,6,6,8등

SELECT DENSE_RANK() OVER (PARTITION BY, ORDER BY ) 	1,2,2,2,3,4,4,5등

*/

SELECT ROW_NUMBER() OVER (ORDER BY ENAME) ,  ENAME
FROM EMP;

SELECT ROW_NUMBER() OVER (PARTITION BY JOB ORDER BY ENAME) ,  ENAME
FROM EMP;

SELECT RANK() OVER (ORDER BY DAY(HIREDATE)) AS RANK_NO,
	   DENSE_RANK() OVER (ORDER BY DAY(HIREDATE)) AS DENSE_NO, EMPNO, ENAME, HIREDATE
FROM EMP;

SELECT RANK() OVER (ORDER BY YEAR(HIREDATE)) AS RANK_NO,
	   DENSE_RANK() OVER (ORDER BY YEAR(HIREDATE)) AS DENSE_NO, EMPNO, ENAME, HIREDATE
FROM EMP;

SELECT RANK() OVER (ORDER BY MONTH(HIREDATE)) AS RANK_NO,
	   DENSE_RANK() OVER (ORDER BY MONTH(HIREDATE)) AS DENSE_NO, EMPNO, ENAME, HIREDATE
FROM EMP;

SELECT RANK() OVER (ORDER BY DATE(HIREDATE)) AS RANK_NO,
	   DENSE_RANK() OVER (ORDER BY DATE(HIREDATE)) AS DENSE_NO, EMPNO, ENAME, HIREDATE
FROM EMP;

SELECT RANK() OVER (ORDER BY WEEKDAY(HIREDATE)) AS RANK_NO,
	   DENSE_RANK() OVER (ORDER BY WEEKDAY(HIREDATE)) AS DENSE_NO, EMPNO, ENAME, HIREDATE
FROM EMP;

SELECT WEEKDAY('23-01-04'); # 0 ~ 6
/*	
	(DATETIME OR DATE)
	YEAR() : 1000 ~ 9999  4자리 표시
    MONTH() : 1 ~ 12
    DAY()	  : 1 ~ 31
    DAYOFMONTH() = DAY()
	HOUR() / MINUTE() / SECOND()
    DATE_ADD(INTERVAL), DATE_SUB()
    
*/

DESC EMP;
-- Q1) 변수를 통해서 날짜함수를 활용해보자.
SET @date = now();
SELECT @date, year(@date), month(@date), day(@date);
select hour(@DATE), MINUTE(@DATE) , second(@DATE);

-- Q2) 변수를 통해서 날짜함수를 활용해보자. _제어문 IF, WHILE, LOOP, REPEAT문, CASE~WHEN~THEN 문 (CASE~END문)

SET @date = now();
SELECT @DATE,
	CASE WEEKDAY(@DATE)
		WHEN 0 THEN '월요일'
        WHEN 1 THEN '화요일'
        WHEN 2 THEN '수요일'
        WHEN 3 THEN '목요일'
        WHEN 4 THEN '금요일'
        WHEN 5 THEN '토요일'
        WHEN 6 THEN '일요일'
	END AS 요일;

-- 함수만들기, 프로시저만들기, 트리거 = 활용

/*========== 중복데이터에서 단일값 출력 , BETWEEN ~ AND 연산자 =============*/
SELECT distinct JOB
FROM EMP;

-- 사원의 봉급이 1000에서 2000 사이의 사원의 이름과 봉급을 출력해보자.
SELECT ENAME, SAL
FROM EMP
WHERE SAL BETWEEN 1000 AND 2000;

SELECT ENAME, SAL
FROM EMP
WHERE SAL NOT BETWEEN 1000 AND 2000;

SELECT ENAME, SAL
FROM EMP
WHERE SAL BETWEEN 6000 AND 7000;


/*
	데이터 형변환:
    [BINARY, CHAR, DATE, DATETIME, DECIMAL, JSON, NCHAR,
    
/*
SELECT cast(now() as signed); --형식변환

/*
	select
    from
    where
    group by
    having
    order by
    limit ;
    
*/

SELECT *
FROM EMP
ORDER BY EMPNO DESC
LIMIT 5;	#처음부터 5개

SELECT *
FROM EMP
ORDER BY EMPNO DESC
LIMIT 5 OFFSET 10;  #11~15번째 RECORD까지 검색

SELECT *
FROM EMP
ORDER BY EMPNO DESC
LIMIT 1 OFFSET 14; #14번부터 1개

SELECT *
FROM EMP
ORDER BY EMPNO DESC
LIMIT 10; #처음부터 10개





```
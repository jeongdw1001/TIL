# 조인문제
```sql
use emp;

-- 1.  사원들의    이름, 부서번호, 부서이름을    출력하라.
select ename, emp.deptno, dname
FROM emp , dept
WHERE EMP.DEPTNO = DEPT.DEPTNO;

/*
select ename, deptno, dname
FROM my_emp INNER JOIN MY_DEPT USING(DEPTNO); 
*/

-- 2. DALLAS에서    근무하는   사원의    이름, 직위, 부서번호, 부서이름을 
-- 출력하라.
select ename, job, deptno, dname
FROM EMP JOIN dept USING(DEPTNO)
WHERE LOC = 'dallas' ; 

-- 3.  이름에    'A'가    들어가는   사원들의    이름과    부서이름을    출력하라.
select ename, dname
FROM EMP JOIN dept USING(DEPTNO)
WHERE ename like "%A%" ; 

-- 4.  사원이름과    그    사원이   속한   부서의    부서명, 그리고    월급을 
-- 출력하는데    월급이   3000이상인    사원을    출력하라.
select ename, dname, sal
FROM EMP JOIN dept USING(DEPTNO)
WHERE sal >= 3000; 

-- 5.  직위가    'SALESMAN'인   사원들의    직위와    그    사원이름, 그리고 
-- 그    사원이    속한    부서   이름을    출력하라.
select JOB, ename, dname
FROM EMP JOIN dept USING(DEPTNO)
WHERE JOB like 'SALESMAN' ; 

-- 6.  커미션이    책정된    사원들의    사원번호, 이름, 연봉, 연봉+커미션, 
-- 급여등급을    출력하되, 각각의    컬럼명을    '사원번호', '사원이름', 
-- '연봉','실급여', '급여등급'으로    하여    출력하라.

select empno as 사원번호, 
		ename as 사원이름, 
        sal*12 as 연봉, 
		(sal+comm) as 실급여 ,
        grade as 급여등급
FROM emp JOIN dept USING(DEPTNO)
		 join salgrade on (SAL BETWEEN LOSAL AND HISAL)
where comm is not null;

-- 7.  부서번호가 10번인 사원들의 부서번호, 부서이름, 사원이름, -- 월급, 급여등급을 출력하라.
select deptno as 부서번호, 
		dname as 부서이름, 
        ename as 사원이름, 
        sal as 월급, 
		grade as 급여등급
FROM emp JOIN dept USING(DEPTNO)
		 join salgrade on (SAL BETWEEN LOSAL AND HISAL)
where deptno = 10;

-- 8.  부서번호가   10번, 20번인    사원들의    부서번호, 부서이름, 
-- 사원이름, 월급, 급여등급을    출력하라. 그리고    그    출력된 
-- 결과물을    부서번호가    낮은    순으로, 월급이    높은   순으로
-- 정렬하라.
select deptno as 부서번호, 
		dname as 부서이름, 
        ename as 사원이름, 
        sal as 월급, 
		grade as 급여등급
FROM emp JOIN dept USING(DEPTNO)
		 join salgrade on (SAL BETWEEN LOSAL AND HISAL)
where deptno = 10 or deptno = 20
order by deptno asc, sal desc;

-- 9.  사원번호와 사원이름, 그리고 그 사원을 관리하는 관리자의 
-- 사원번호와 사원이름을 출력하되 각각의 컬럼명을 '사원번호', 
-- '사원이름', '관리자번호', '관리자이름'으로 하여 출력하라.
select 사원.empno as 사원번호,
		사원.ename as 사원이름,
        관리자.empno as 관리자번호,
        관리자.ename as 관리자이름
from emp 사원 left outer join emp 관리자 on 사원.mgr = 관리자.empno;

-- 10. 자신의 관리자보다 먼저 입사한 모든 사원의 이름 및  입사일을해당 
-- 관리자의 이름 및 입사일과 함께 표시하고 열 이름을 각각 출력하라-
select 사원.ename as EMPLOYEE,
		사원.HIREDATE AS EMPHIREDATE,
        관리자.ENAME AS MANAGER,
        관리자.HIREDATE AS MGRHIREDATE
FROM EMP 사원 LEFT OUTER JOIN EMP 관리자 on 사원.mgr = 관리자.empno
WHERE 사원.HIREDATE < 관리자.HIREDATE;


-- 11.해당 부서 모든 사원에 대한 부서 이름, 위치, 사원수 및 평균 급여를 표시하는 정의를
-- 열 이름을 각각 DNAME,   LOC,   NUMBER   OF   PEOPLE,SALARY로  작성한다.
SELECT DNAME, LOC, 
		COUNT(ENAME) AS 'NUMBER OF PEOPLE', 
        AVG(SAL) AS SALARY
FROM DEPT LEFT OUTER JOIN EMP USING(DEPTNO)
GROUP BY DEPTNO
ORDER BY AVG(SAL) DESC;
```
```python
import pandas as pd
import numpy as np
```
```python
emp = pd.read_csv('..\data\emp.csv')
emp
```
---
```sql
q1) select job, max(sal) from emp group by job;
- reset_index() 키워드는 series(컬럼)로 출력하는게 아니라
DataFrame(테이블)으로 출력하는 키워드
```
```python
result = emp.groupby('job')['sal'].max().reset_index()
#print(type(result))
print(result)
```
```python
result = emp.groupby('deptno')['sal'].max().reset_index()
#print(type(result))
print(result)
```
---
```sql
q2) select deptno, sum(sal)
    from emp
    where deptno != 20
    group by deptno
```
```python
result = emp.groupby('deptno')['sal'].sum().reset_index()
print (result[['deptno','sal']][result['deptno'] != 20 ] )
```
```python
result = emp.groupby('deptno')['sal'].sum().reset_index()
print (result[['deptno','sal']] )
```
---
```sql
q3) 부서번호, 부서별 평균월급을 구해보자.
select deptno, avg(sal)
from emp
group by deptno;
```
```python
result = emp.groupby('deptno')['sal'].mean().reset_index()
print(result)
#print(dir(result))
#print(help(result.astype))
#df.astype('int32').dtypes
```
---
```python
q4) 위에서 평균 월급을 출력할 때 정수 부분만 출력해보자.
```
```python
result = emp.groupby('deptno')['sal'].mean().reset_index().astype(int)
print(result)
```
---
```sql
q5) 부서위치, 부서별 월급의 합을 구해보자.

select d.loc, sum(e.sal)
from emp e, dept d
where e.deptno = d.deptno
group by d.loc;

select loc, sum(sal)
from emp, join dept using(deptno) 
#from emp join dept on(emp.deptno = dept.deptno)
group by loc;
```
```python
emp = pd.read_csv('..\data\emp.csv')
dept = pd.read_csv('..\data\dept.csv')
# 여기까지 from emp, join dept 

result = pd.merge (emp, dept,on='deptno' )
# using(deptno)

result02 = result.groupby('loc')['sal'].sum().reset_index()
#group by loc; select loc, sum(sal)
print(result02)
```
```python
DataFrame.merge(right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

pandas.merge( emp_left, dept_right, how='inner', on='deptno')

how ='inner' : emp 와 dept 데이터 프레임에 공통적으로 존재하는 교집합일 경우에만 추출하겠다.
        
how ='outer' : 열의 데이터가 양쪽 데이터 프레임에 공통적으로    존재하는 교집합이 아니어도 추출하겠다.
                           
how ='left'  :   왼쪽 데이터 프레임의 키열에 속하는 데이터값을 기준으로 병합하겠다.
        
how = 'right' :  오른쪽 데이터 프레임의 키열에 속하는 데이터 값을 기준으로 병합하겠다.

```
---
```sql
q6) select loc, sum(sal)
    from emp outer right join dept using(deptno)
    group by loc;
```
```python
result = pd.merge( emp, dept, how='inner', on='deptno')
result02 = result.groupby('loc')['sal'].sum().reset_index()
print(result02)
```
---
```python
q7) csv모듈을 이용해서 emp.csv를 읽어오자.
```
```python
import csv
```
```python
print(dir(csv))
```
```python
emp_res = csv.reader('..\data\emp.csv')
#print(type(emp_res))
#print(dir(emp_res))

for m_list in emp_res:
    print(m_list)
```
```python
file = open('..\data\emp02.csv')
emp_res = csv.reader(file)
for m_list in emp_res:
    print(m_list)
```
---
```python
q7) emp_res 객체를 통해서 이름과 봉급을 구하자. 단 봉급은 월급 * 11.2로 구하자.
```
```python
file = open('..\data\emp02.csv')
emp_res = csv.reader(file)
for m_list in emp_res:
    r = float(m_list[5]) * 11.2
    print(m_list[1],round(r))
```
---
```python
Q8) emp_res에서 직업이 'SALESMAN'인 사원의 이름과 직업을 출력해보자.
```
```python
file = open('..\data\emp02.csv')
emp_res = csv.reader(file)
for m_list in emp_res:
    if m_list[2]=='SALESMAN':
        print(m_list[1],m_list[2])
```
---
```python
Q9)emp.csv를 결측치 확인하자. **************************중요***********************
결측치 NaN = Not a Number
```
```python
emp = pd.read_csv('..\data\emp.csv')
print(emp[['ename','comm']])
```
```python
# 커미션의 결측치를 확인 해보자.
print(emp[['ename','comm']][emp['comm'].isnull()])
```
```python
# 커미션의 결측치가 아닌 사원을 확인 해보자.
print(emp[['ename','comm']][~emp['comm'].isnull()])
```
```python
#emp.csv의 결측치를 다시 확인
print(emp.isnull())  #Nan 확인 True
```
```python
#emp.csv의 결측치의 개수를 확인해보자.
print(emp.isnull().sum())
```
---
```python
Q10) 파생데이터 생성 = 파생변수 생성 = 기존의 데이터를 가지고 가공해서 만든 새로운 데이터의 컬럼
```
```python
#emp에 있는 sal을 sal02라는 컬럼을 생성해서 추가하자.
emp = pd.read_csv('..\data\emp.csv')
emp['sal02']=emp['sal']
emp
```
---
```python
Q11) 이름과 부서 위치를 출력해보자.
```
```python
emp = pd.read_csv('..\data\emp.csv')
dept = pd.read_csv('..\data\dept.csv')
result = pd.merge (emp, dept, how='inner', on='deptno')
print(result[['ename','loc']])
```
```python
emp['loc']=result['loc']
emp
```
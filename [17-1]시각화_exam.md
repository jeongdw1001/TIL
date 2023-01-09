## exam01) emp.csv를 로드한 후 이름과 봉급을 깃점으로 선 그래프를 그린다.
## exam02) 직업별로 봉급을 그룹화 한 결과를 원그래프를 그려서 수치를 범례표시 한다.
## exam03) 부서별 결과를 막대그래프로 표시한다. 단, 봉급의 합을 이용한다.
## exam04) 직업별 부서별 두개의 봉급의 최대값으로 곡선을 그려낸다.



---
```python
#exam01) emp.csv를 로드한 후 이름과 봉급을 깃점으로 선 그래프를 그린다.

import matplotlib.pyplot as plt 
import pandas as pd
emp = pd.read_csv('..\data\emp.csv')
array_x = emp['ename']
array_y = emp['sal']
result1 = plt.plot(array_x,array_y) 

plt.xticks(rotation=70)
plt.show() 
```
```python
# exam02) 직업별로 봉급을 그룹화 한 결과를 원그래프를 그려서 수치를 범례표시 한다.

import matplotlib.pyplot as plt 
import pandas as pd

emp = pd.read_csv('..\data\emp.csv')
result2 = emp.groupby('job')['sal'].sum()
plt.title('groupby_job')

result2.plot.pie(autopct='%1.2f%%') 
plt.tight_layout()
plt.show() 

```
```python
# exam03) 부서별 결과를 막대그래프로 표시한다. 단, 봉급의 합을 이용한다.

import matplotlib.pyplot as plt 
import pandas as pd

emp = pd.read_csv('..\data\emp.csv')
result3 = emp.groupby('deptno')['sal'].sum()

result3.plot.bar() 
plt.show() 
```
```python
# exam04) 직업별 부서별 두개의 봉급의 최대값으로 곡선을 그려낸다.

x1 = emp.groupby('job')['sal'].max()
x2 = emp.groupby('deptno')['sal'].max()

plt.plot(x1,linestyle='--', color='orange', marker='o', label='job')
plt.plot(x2,linestyle=':', color='green', marker='o', label='deptno')

plt.legend()

plt.xlabel('x1')
plt.xlabel('x2')
plt.grid()

plt.xticks(rotation=70)
plt.show()
```

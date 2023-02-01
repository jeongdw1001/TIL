```python
# 설정변경코드
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity="all"
```


```python
# 모듈 import
import numpy as np
import pandas as pd
```


```python
s = pd.Series(range(10))
s[3] = np.nan
s
```




    0    0.0
    1    1.0
    2    2.0
    3    NaN
    4    4.0
    5    5.0
    6    6.0
    7    7.0
    8    8.0
    9    9.0
    dtype: float64




```python
s.count() # nan은 제외하고 count
```




    9




```python
np.random.randint(5) # 정수 0~4 사이에서 난수 발생
np.random.randint(5, size=4) # 난수 4개를 생성
```




    2






    array([2, 2, 4, 1])




```python
# 난수 발생 시 항상 고정된 값을 발생시킬 수도 있음
np.random.seed(3)
np.random.randint(5, size=4)
```




    array([2, 0, 1, 3])




```python
# 위 셀에서 고정시켰지만 한 번 사용했으므로 seed는 리셋됨
np.random.randint(5, size=4)
```




    array([3, 2, 0, 1])




```python
# 시드값이 매번 다르게 전달되도록 코드를 작성
import time
np.random.seed(int(time.time()))
np.random.randint(5, size=4)
```




    array([1, 4, 0, 1])




```python
np.random.randint(5, size=(4,4))
```




    array([[1, 2, 1, 3],
           [1, 4, 0, 1],
           [3, 4, 2, 2],
           [0, 2, 2, 0]])




```python
np.random.seed(3) # 시드값이 고정되어서 동일한 값의 난수가 발생
df1 = pd.DataFrame(np.random.randint(5,size=(4,4)))
df1.iloc[2,3] = np.nan # 2행 3열의 value는 NaN으로 변경 : 3열 데이터는 실수형으로 변환됨
df1
# 컬럼(피처)은 동일한 타입의 데이터로만 구성할 수 있다.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 각 열에 대한 원소의 개수 반환
# 3열은 3개라면 결측치가 있음 예상 가능
df1.count()
```




    0    4
    1    4
    2    4
    3    3
    dtype: int64



### count 함수 사용 예제


```python
import seaborn as sns
titanic = pd.read_csv('C:/ds_work/data/test.csv')
del titanic['Unnamed: 0']
titanic.head(10)
titanic.tail(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>NaN</td>
      <td>0</td>
      <td>0</td>
      <td>8.4583</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>6</th>
      <td>0</td>
      <td>1</td>
      <td>male</td>
      <td>54.0</td>
      <td>0</td>
      <td>0</td>
      <td>51.8625</td>
      <td>S</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>E</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>7</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>2.0</td>
      <td>3</td>
      <td>1</td>
      <td>21.0750</td>
      <td>S</td>
      <td>Third</td>
      <td>child</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>27.0</td>
      <td>0</td>
      <td>2</td>
      <td>11.1333</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1</td>
      <td>2</td>
      <td>female</td>
      <td>14.0</td>
      <td>1</td>
      <td>0</td>
      <td>30.0708</td>
      <td>C</td>
      <td>Second</td>
      <td>child</td>
      <td>False</td>
      <td>NaN</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>889</th>
      <td>1</td>
      <td>1</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.00</td>
      <td>C</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>890</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.75</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic.to_csv('C:/ds_work/data/test.csv')
```


```python
titanic.count()
```




    survived       891
    pclass         891
    sex            891
    age            714
    sibsp          891
    parch          891
    fare           891
    embarked       889
    class          891
    who            891
    adult_male     891
    deck           203
    embark_town    889
    alive          891
    alone          891
    dtype: int64



### 카테고리 값 세기



```python
np.random.seed(1)
s2 = pd.Series(np.random.randint(6, size=100))
s2.head(10)
s2.tail()
len(s2)
```




    0    5
    1    3
    2    4
    3    0
    4    1
    5    3
    6    5
    7    0
    8    0
    9    1
    dtype: int32






    95    4
    96    5
    97    2
    98    4
    99    3
    dtype: int32






    100




```python
s2.value_counts()
s2.value_counts(normalize=True)
```




    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64






    1    0.22
    0    0.18
    4    0.17
    5    0.16
    3    0.14
    2    0.13
    dtype: float64



### 범주형 데이터에 value_counts() 함수 적용


```python
# titanic 데이터 alive 열 : 생존여부가 yes/no로 표시되어 있음
titanic['alive'].dtype # 해당 열의 data type을 반환
titanic['alive'].value_counts()
titanic['alive'].value_counts(normalize=True)
```




    dtype('O')






    no     549
    yes    342
    Name: alive, dtype: int64






    no     0.616162
    yes    0.383838
    Name: alive, dtype: float64




```python
titanic['alive'].value_counts(normalize=True)*100
```




    no     61.616162
    yes    38.383838
    Name: alive, dtype: float64




```python
titanic['sex'].dtype # 'O' ; object
titanic['sex'].value_counts
titanic['sex'].value_counts(normalize=True)*100
```




    dtype('O')






    <bound method IndexOpsMixin.value_counts of 0        male
    1      female
    2      female
    3      female
    4        male
            ...  
    886      male
    887    female
    888    female
    889      male
    890      male
    Name: sex, Length: 891, dtype: object>






    male      64.758698
    female    35.241302
    Name: sex, dtype: float64



### 데이터프레임에 value_counts() 함수 사용


```python
titanic[['sex','alive']].head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>sex</th>
      <th>alive</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>male</td>
      <td>no</td>
    </tr>
    <tr>
      <th>1</th>
      <td>female</td>
      <td>yes</td>
    </tr>
  </tbody>
</table>
</div>




```python
titanic[['sex','alive']].value_counts()
```




    sex     alive
    male    no       468
    female  yes      233
    male    yes      109
    female  no        81
    dtype: int64




```python
type(titanic[['sex','alive']].value_counts()) # 시리즈
```




    pandas.core.series.Series




```python
pd.DataFrame(titanic[['sex','alive']].value_counts())
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>0</th>
    </tr>
    <tr>
      <th>sex</th>
      <th>alive</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>male</th>
      <th>no</th>
      <td>468</td>
    </tr>
    <tr>
      <th>female</th>
      <th>yes</th>
      <td>233</td>
    </tr>
    <tr>
      <th>male</th>
      <th>yes</th>
      <td>109</td>
    </tr>
    <tr>
      <th>female</th>
      <th>no</th>
      <td>81</td>
    </tr>
  </tbody>
</table>
</div>



### 정렬함수 : 데이터 정렬 시 사용


```python
s2
```




    0     5
    1     3
    2     4
    3     0
    4     1
         ..
    95    4
    96    5
    97    2
    98    4
    99    3
    Length: 100, dtype: int32




```python
s2.value_counts()
```




    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64




```python
s2.value_counts().sort_index()
```




    0    18
    1    22
    2    13
    3    14
    4    17
    5    16
    dtype: int64




```python
s2.value_counts().sort_index(ascending=False)
```




    5    16
    4    17
    3    14
    2    13
    1    22
    0    18
    dtype: int64




```python
s2.value_counts().sort_values()
```




    2    13
    3    14
    5    16
    4    17
    0    18
    1    22
    dtype: int64




```python
s2.value_counts().sort_values(ascending=False)
```




    1    22
    0    18
    4    17
    5    16
    3    14
    2    13
    dtype: int64



### 데이터 프레임 정렬


```python
df1
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df1.sort_values() # TypeError:'by'
```


```python
df1.sort_values(by=0) 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.sort_values(by=0,ascending=False) 
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.sort_values(by=[0,2],ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>2</td>
      <td>0</td>
      <td>4</td>
      <td>4.0</td>
    </tr>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df = pd.DataFrame({'num_legs' : [2,4,4,6],
                  'num_wings' : [2,0,0,0]},
                  index=['falcon','dog','cat','ant'])
df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df.sort_index()
df.sort_index(ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>num_legs</th>
      <th>num_wings</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>falcon</th>
      <td>2</td>
      <td>2</td>
    </tr>
    <tr>
      <th>dog</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>cat</th>
      <td>4</td>
      <td>0</td>
    </tr>
    <tr>
      <th>ant</th>
      <td>6</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



### 행/열 합계


```python
np.random.seed(1)
df2=pd.DataFrame(np.random.randint(10, size=(4,8)))
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.sum(axis=1)
```




    0    35
    1    34
    2    41
    3    42
    dtype: int64




```python
df2.sum(axis=0)
```




    0    24
    1    33
    2    25
    3    24
    4    15
    5    10
    6     5
    7    16
    dtype: int64




```python
df2.sum()
```




    0    24
    1    33
    2    25
    3    24
    4    15
    5    10
    6     5
    7    16
    dtype: int64




```python
df2['total']=df2[[0,1,2,3,4,5,6,7]].sum(axis=1)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5</td>
      <td>8</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
      <td>35</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6</td>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
      <td>34</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
      <td>41</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
      <td>42</td>
    </tr>
  </tbody>
</table>
</div>



### df의 기본 함수
- mean(axis=0/1)
- min(axis=0/1)
- max(axis=0/1)


```python
df2.mean(axis=0)
df2.mean(axis=1)
```




    0         6.00
    1         8.25
    2         6.25
    3         6.00
    4         3.75
    5         2.50
    6         1.25
    7         4.00
    total    38.00
    dtype: float64






    0    7.777778
    1    7.555556
    2    9.111111
    3    9.333333
    dtype: float64




```python
df2.min(axis=0)
df2.min(axis=1)
```




    0         4
    1         7
    2         2
    3         4
    4         0
    5         0
    6         0
    7         1
    total    34
    dtype: int64






    0    0
    1    2
    2    0
    3    0
    dtype: int64




```python

```




    0    0
    1    2
    2    0
    3    0
    dtype: int64




```python
df2.max(axis=0)
df2.max(axis=1)
```




    0         9
    1         9
    2         9
    3         9
    4         9
    5         7
    6         4
    7         7
    total    42
    dtype: int64






    0    35
    1    34
    2    41
    3    42
    dtype: int64




```python
df2.loc()
```




    0    35
    1    34
    2    41
    3    42
    dtype: int64




```python
# 각 열의 최대값을 구해서 max_data라는 행을 추가
# 새로운 행 추가(loc 인덱서 사용)
# df.loc['추가되는 행 이름'] = data
# (주의!) 동일한 코드를 반복 실행하면 max_data까지에서 최대값을 구하므로 의미가 달라질 수 있음
df2.loc['max_data']=df2.max(axis=0)
df2.loc['max_data']=df2[[0,1,2,3,4,5,6,7]].max(axis=0)
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



### 행/열 삭제 : drop() 사용 예제
- df.drop('행이름',0) : 행 삭제
- df.drop('열이름',1) : 열 삭제

- 원본 반영 : inplace=True


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
      <th>total</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
      <td>34.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
      <td>41.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>42.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# df2.drop('total',1,inplace=True)
df2.drop('max_data',0)
df2
```

    C:\Users\user\AppData\Local\Temp\ipykernel_25032\3766238089.py:2: FutureWarning: In a future version of pandas all arguments of DataFrame.drop except for the argument 'labels' will be keyword-only.
      df2.drop('max_data',0)
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>



### NaN 값 처리 함수
- df.dropna(axis=0/1)
    - NaN 값이 있는 열 또는 행을 삭제
    - 원본 반영되지 않음
- df.fillna(0)
    - NaN 값을 정해진 숫자로 채움
    - 원본 반영되지 않음 


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.0</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 결측치값 적용
# NaN값 생성 : np.NaN 속성
df2.iloc[0,0] = np.NaN
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# NaN이 포함된 행을 삭제
df2.dropna(axis=0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>0</th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>6.0</td>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.0</td>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# NaN이 포함된 열을 삭제
df2.dropna(axis=1)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# NaN이 포함된 열을 삭제
df2.dropna(axis=1, inplace=True)
# 원본 데이터 삭제
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.iloc[0,0] = np.nan
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.fillna(0) # NaN 값을 0으로 대체
df2.fillna(1) # NaN 값을 1로 대체
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.fillna(1, inplace=True)
```


```python
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
### 데이터프레임의 형변환
- df.astype(자료형)
- 전체 데이터에 대해서 형변환을 진행
```


```python
df2.iloc[0,0] = np.nan
df2
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.fillna(0).astype(int) # NaN 값을 0으로 채우면서 df의 데이터를 정수형으로 형변환
df2.fillna(0).astype(float) # NaN 값을 1로 채우면서 df의 데이터를 실수형으로 형변환
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>9</td>
      <td>5</td>
      <td>0</td>
      <td>0</td>
      <td>1</td>
      <td>7</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>2</td>
      <td>4</td>
      <td>5</td>
      <td>2</td>
      <td>4</td>
      <td>2</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>7</td>
      <td>9</td>
      <td>1</td>
      <td>7</td>
      <td>0</td>
      <td>6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>7</td>
      <td>6</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>1</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>9</td>
      <td>7</td>
      <td>4</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
df2.fillna(0)[1].astype(int) # 1열만 추출
```




    0           0
    1           9
    2           7
    3           9
    max_data    9
    Name: 1, dtype: int32




```python
test_df = df2.fillna(0).astype(float)
test_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0.0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7.0</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9.0</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 1열만 정수형으로 변경
test_df[1] = test_df[1].astype(int)
test_df
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1</th>
      <th>2</th>
      <th>3</th>
      <th>4</th>
      <th>5</th>
      <th>6</th>
      <th>7</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>9.0</td>
      <td>5.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>7.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>5.0</td>
      <td>2.0</td>
      <td>4.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>7</td>
      <td>7.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>7.0</td>
      <td>0.0</td>
      <td>6.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>7.0</td>
      <td>6.0</td>
      <td>9.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
    </tr>
    <tr>
      <th>max_data</th>
      <td>9</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>9.0</td>
      <td>7.0</td>
      <td>4.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>



### 열 또는 행에 동일한 연산 반복 적용할 때 : apply() 함수

- apply() 함수는 DataFrame의 행이나 열에 복잡한 연산을 vectorizing 할 수 있게 해주는 함수로 매우 많이 활용되는 함수임
- 동일한 연산 (함수화 되어있어야 함)을 모든 열에 혹은 모든 행에 반복 적용하고자 할 때 사용
- apply (반복적용할 함수, axis = 0/1)
    - 0 : 열마다 반복
    - 1 : 행마다 반복
    - 생략시 기본값 : 0


```python
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# np.sum() 함수는 전달된 첫번째 인수 데이터들의 합산 결과를 반환하는 함수
np.sum([1,2,3])
```




    6




```python
#df3의 각 열에 대해서 np.sum() 함수를 반복 적용
np.sum(df3['a'])
np.sum(df3['b'])
np.sum(df3['c'])
```




    15






    15






    16




```python
for i in ['a','b','c']:
    print(np.sum(df3[i]))
df3.apply(np.sum,0) # df3의 각 열에 대해서 np.sum() 적용한 결과를 반환
```

    15
    15
    16
    




    a    15
    b    15
    c    16
    dtype: int64




```python
# seaborn 패키지의 titanic 데이터셋을 load 하시오
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.head()
titanic.tail()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>22.0</td>
      <td>1</td>
      <td>0</td>
      <td>7.2500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>38.0</td>
      <td>1</td>
      <td>0</td>
      <td>71.2833</td>
      <td>C</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>3</td>
      <td>female</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.9250</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>35.0</td>
      <td>1</td>
      <td>0</td>
      <td>53.1000</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>C</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>False</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>35.0</td>
      <td>0</td>
      <td>0</td>
      <td>8.0500</td>
      <td>S</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>survived</th>
      <th>pclass</th>
      <th>sex</th>
      <th>age</th>
      <th>sibsp</th>
      <th>parch</th>
      <th>fare</th>
      <th>embarked</th>
      <th>class</th>
      <th>who</th>
      <th>adult_male</th>
      <th>deck</th>
      <th>embark_town</th>
      <th>alive</th>
      <th>alone</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>886</th>
      <td>0</td>
      <td>2</td>
      <td>male</td>
      <td>27.0</td>
      <td>0</td>
      <td>0</td>
      <td>13.00</td>
      <td>S</td>
      <td>Second</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>True</td>
    </tr>
    <tr>
      <th>887</th>
      <td>1</td>
      <td>1</td>
      <td>female</td>
      <td>19.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.00</td>
      <td>S</td>
      <td>First</td>
      <td>woman</td>
      <td>False</td>
      <td>B</td>
      <td>Southampton</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>888</th>
      <td>0</td>
      <td>3</td>
      <td>female</td>
      <td>NaN</td>
      <td>1</td>
      <td>2</td>
      <td>23.45</td>
      <td>S</td>
      <td>Third</td>
      <td>woman</td>
      <td>False</td>
      <td>NaN</td>
      <td>Southampton</td>
      <td>no</td>
      <td>False</td>
    </tr>
    <tr>
      <th>889</th>
      <td>1</td>
      <td>1</td>
      <td>male</td>
      <td>26.0</td>
      <td>0</td>
      <td>0</td>
      <td>30.00</td>
      <td>C</td>
      <td>First</td>
      <td>man</td>
      <td>True</td>
      <td>C</td>
      <td>Cherbourg</td>
      <td>yes</td>
      <td>True</td>
    </tr>
    <tr>
      <th>890</th>
      <td>0</td>
      <td>3</td>
      <td>male</td>
      <td>32.0</td>
      <td>0</td>
      <td>0</td>
      <td>7.75</td>
      <td>Q</td>
      <td>Third</td>
      <td>man</td>
      <td>True</td>
      <td>NaN</td>
      <td>Queenstown</td>
      <td>no</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>




```python
# titanic df의 alive, sex, class 열에 대해서 value_counts() 함수를 적용하여 결과를 확인하시오. 
# apply() 함수 사용할 것
titanic[['alive','sex','class']].apply(pd.value_counts,0)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>alive</th>
      <th>sex</th>
      <th>class</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>First</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>216.0</td>
    </tr>
    <tr>
      <th>Second</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>184.0</td>
    </tr>
    <tr>
      <th>Third</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>491.0</td>
    </tr>
    <tr>
      <th>female</th>
      <td>NaN</td>
      <td>314.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>male</th>
      <td>NaN</td>
      <td>577.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>no</th>
      <td>549.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>yes</th>
      <td>342.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



- 데이터프레임의 기본 집계함수 (sum, min, max, mean 등)들은 행/열 단위 벡터화 연산을 수행함
    - apply() 함수를 사용할 필요가 없음
- 일반적으로 apply() 함수 사용은 복잡한 연산을 해결하기 위한 lambda 함수나 사용자 정의 함수를 각 열 또는 행에 일괄 적용시키기 위해 사용

### 사용자 정의 함수를 apply()에 사용하는 예제
- 사용자 정의 함수 생성 : 사용자로부터 시리즈를 전달받아 (매개변수) 해당 시리즈의 최대값과 최소값 차이를 구해 반환하는 함수
- diff를 정의


```python
def diff(x):
    return x.max() - x.min()
```


```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
diff(df3['a'])
diff(df3['b'])
diff(df3['c'])
```




    3






    4






    4




```python
# apply 함수 적용
df3.apply(diff,0)
```




    a    3
    b    4
    c    4
    dtype: int64




```python
pd.Series(3)
pd.Series(3).max()
```




    0    3
    dtype: int64






    3



### 1회성함수 lambda 함수를 apply()에 사용하는 예제


```python
(lambda x : x.max()-x.min())(df3['a'])
```




    3




```python
df3.apply(lambda x : x.max()-x.min(),0)
```




    a    3
    b    4
    c    4
    dtype: int64



### df3 각 열에 대해 최대값과 최소값의 차이를 구하시오.
- apply 함수 제외


```python
df3.max(axis=0)-df3.min(axis=0)
```




    a    3
    b    4
    c    4
    dtype: int64




```python
np.square([1,2,3])
df3
df3.apply(np.square,0)
df3.apply(np.square,1)
```




    array([1, 4, 9], dtype=int32)






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>9</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>16</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
      <td>25</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>4</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9</td>
      <td>9</td>
      <td>25</td>
    </tr>
    <tr>
      <th>2</th>
      <td>16</td>
      <td>1</td>
      <td>4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>9</td>
      <td>16</td>
      <td>16</td>
    </tr>
    <tr>
      <th>4</th>
      <td>16</td>
      <td>25</td>
      <td>16</td>
    </tr>
  </tbody>
</table>
</div>



### 데이터 값을 카테고리 값으로 변환
- 값의 크기를 기준으로하여 카테고리 값으로 변환하고 싶을 때
    - cut(data, bins, labels)
        - data : 구간 나눌 실제 값
        - bins : 구간 경계 값
        - labels : 카테고리 값
    - qcut(data, 구간수, labels)


```python
# 구간을 나눌 실제 값 : 관측 데이터
ages = [0,0,5,4,6,4,5,2,10,21,23,37,15,38,31,61,20,41,31,100]
```


```python
# data : 구간 나눌 실제 값
data = ages
# 구간 경계 값
bins = [0,4,18,25,35,60,100]
# labels : 카테고리 값
# 순서는 구간 bins와 동일해야 함
labels = ['영유아','미성년자','청년','중년','장년','노년']
```


```python
len(data)
cats = pd.cut(data,bins,labels=labels)
cats
```




    20






    [NaN, NaN, '미성년자', '영유아', '미성년자', ..., '노년', '청년', '장년', '중년', '노년']
    Length: 20
    Categories (6, object): ['영유아' < '미성년자' < '청년' < '중년' < '장년' < '노년']




```python
type(cats)
```




    pandas.core.arrays.categorical.Categorical




```python
cat_list = list(cats)
cat_list
```




    [nan,
     nan,
     '미성년자',
     '영유아',
     '미성년자',
     '영유아',
     '미성년자',
     '영유아',
     '미성년자',
     '청년',
     '청년',
     '장년',
     '미성년자',
     '장년',
     '중년',
     '노년',
     '청년',
     '장년',
     '중년',
     '노년']




```python
test = pd.DataFrame({'나이':ages,'연령대':cat_list})
test
test['연령대'].value_counts()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>나이</th>
      <th>연령대</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>5</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>4</th>
      <td>6</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>5</th>
      <td>4</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>6</th>
      <td>5</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>7</th>
      <td>2</td>
      <td>영유아</td>
    </tr>
    <tr>
      <th>8</th>
      <td>10</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>9</th>
      <td>21</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>10</th>
      <td>23</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>11</th>
      <td>37</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>12</th>
      <td>15</td>
      <td>미성년자</td>
    </tr>
    <tr>
      <th>13</th>
      <td>38</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>14</th>
      <td>31</td>
      <td>중년</td>
    </tr>
    <tr>
      <th>15</th>
      <td>61</td>
      <td>노년</td>
    </tr>
    <tr>
      <th>16</th>
      <td>20</td>
      <td>청년</td>
    </tr>
    <tr>
      <th>17</th>
      <td>41</td>
      <td>장년</td>
    </tr>
    <tr>
      <th>18</th>
      <td>31</td>
      <td>중년</td>
    </tr>
    <tr>
      <th>19</th>
      <td>100</td>
      <td>노년</td>
    </tr>
  </tbody>
</table>
</div>






    미성년자    5
    영유아     3
    청년      3
    장년      3
    중년      2
    노년      2
    Name: 연령대, dtype: int64



### Categorical 클래스 객체
- 카테고리명 속성 : Categorical.categories
    - 카테고리명 저장
- 코드 속성 : Categorical.codes
    - 인코딩한 카테고리 값을 정수로 갖는다.


```python
type(cats)
```




    pandas.core.arrays.categorical.Categorical




```python
cats.categories
```




    Index(['영유아', '미성년자', '청년', '중년', '장년', '노년'], dtype='object')




```python
cats.codes
```




    array([-1, -1,  1,  0,  1,  0,  1,  0,  1,  2,  2,  4,  1,  4,  3,  5,  2,
            4,  3,  5], dtype=int8)



### 구간 경계선을 지정하지 않고 데이터 개수가 같도록 지정한 수의 구간으로 분할하기 : qcut()
- 형식 : pd.qcut(data, 구간수, labels=[d1,d2,,,])
- 예) 1000개의 데이터를 4구간으로 나누려고 한다면 qcut 명령어를 사용
- 한 구간 마다 250개씩 나누게 된다.
- 예외, 같은 숫자인 경우에는 같은 구간으로 처리


```python
np.random.seed(2)
data = np.random.randint(20,size=20)
data

qcat = pd.qcut(data,4,labels=['Q1','Q2','Q3','Q4'])
qcat
```




    array([ 8, 15, 13,  8, 11, 18, 11,  8,  7,  2, 17, 11, 15,  5,  7,  3,  6,
            4, 10, 11])






    ['Q2', 'Q4', 'Q4', 'Q2', 'Q3', ..., 'Q1', 'Q1', 'Q1', 'Q3', 'Q3']
    Length: 20
    Categories (4, object): ['Q1' < 'Q2' < 'Q3' < 'Q4']




```python
np.sort(data)
```




    array([ 2,  3,  4,  5,  6,  7,  7,  8,  8,  8, 10, 11, 11, 11, 11, 13, 15,
           15, 17, 18])




```python
pd.value_counts(qcat)
```




    Q1    5
    Q2    5
    Q3    5
    Q4    5
    dtype: int64




```python
df0 = pd.DataFrame(data, columns=['관측수'])
# df0
df0['범주']=qcat
df0
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>관측수</th>
      <th>범주</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>8</td>
      <td>Q2</td>
    </tr>
    <tr>
      <th>1</th>
      <td>15</td>
      <td>Q4</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13</td>
      <td>Q4</td>
    </tr>
    <tr>
      <th>3</th>
      <td>8</td>
      <td>Q2</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11</td>
      <td>Q3</td>
    </tr>
    <tr>
      <th>5</th>
      <td>18</td>
      <td>Q4</td>
    </tr>
    <tr>
      <th>6</th>
      <td>11</td>
      <td>Q3</td>
    </tr>
    <tr>
      <th>7</th>
      <td>8</td>
      <td>Q2</td>
    </tr>
    <tr>
      <th>8</th>
      <td>7</td>
      <td>Q2</td>
    </tr>
    <tr>
      <th>9</th>
      <td>2</td>
      <td>Q1</td>
    </tr>
    <tr>
      <th>10</th>
      <td>17</td>
      <td>Q4</td>
    </tr>
    <tr>
      <th>11</th>
      <td>11</td>
      <td>Q3</td>
    </tr>
    <tr>
      <th>12</th>
      <td>15</td>
      <td>Q4</td>
    </tr>
    <tr>
      <th>13</th>
      <td>5</td>
      <td>Q1</td>
    </tr>
    <tr>
      <th>14</th>
      <td>7</td>
      <td>Q2</td>
    </tr>
    <tr>
      <th>15</th>
      <td>3</td>
      <td>Q1</td>
    </tr>
    <tr>
      <th>16</th>
      <td>6</td>
      <td>Q1</td>
    </tr>
    <tr>
      <th>17</th>
      <td>4</td>
      <td>Q1</td>
    </tr>
    <tr>
      <th>18</th>
      <td>10</td>
      <td>Q3</td>
    </tr>
    <tr>
      <th>19</th>
      <td>11</td>
      <td>Q3</td>
    </tr>
  </tbody>
</table>
</div>



### 인덱스 설정 함수
데이터 프레임 인덱스 설정을 위해 set_index(),reset_index()
- set_index() : 기존 행 인덱스를 제거하고 데이터 열 중 하나를 인덱스로 설정해주는 함수
- reset_index() : 기존 행 인덱스를 제거하고 기본 인덱스로 변경
- 기본 인덱스 : 0부터 1씩 증가하는 정수 인덱스
    - 따로 설정하지 않으면 기존 인덱스는 데이터열로 추가됨


```python
df3 = pd.DataFrame({
    'a':[1,3,4,3,4],
    'b':[2,3,1,4,5],
    'c':[1,5,2,4,4]
})
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.set_index('a')
df3
df3.set_index('a',inplace=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3
df3.loc[3]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.reset_index()
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>a</th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1</td>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4</td>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>






<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
    <tr>
      <th>a</th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
# 인덱스 값이 관측값이 아니거나 불필요한 경우는 df의 열데이터로 추가되지 않게 해야함
# drop=True : 기존 인덱스 삭제
df3.reset_index(drop=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.reset_index(inplace=True,drop=True)
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### index 이름 변경
- rename(index={현재 index : 바꿀 index})사용, 행인덱스
- rename(column={현재 index : 바꿀 index})사용, 열인덱스


```python
df3.rename(index={0:'1반',1:'2반'})
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>b</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1반</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2반</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df3.rename(columns={'b':'학생'},inplace=True)
```


```python
df3
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>학생</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4</td>
      <td>4</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5</td>
      <td>4</td>
    </tr>
  </tbody>
</table>
</div>



### 리스트 내포 연산
리스트 내포 for문의 일반 문법
- [표현식(연산식) for 항목 in 반복가능객체 if 조건문]
- if 조건문은 생략 가능
- 반복가능객체 : 리스트, 튜플, 딕셔너리, range() 등


```python
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*2)
result
```




    [2, 4, 6, 8]




```python
result=[num*2 for num in a]
result
```




    [2, 4, 6, 8]




```python
# 반복문 이용
test = []
for i in range(1,5):
    test.append('id_'+str(i))
test
```




    ['id_1', 'id_2', 'id_3', 'id_4']




```python
test=['id_'+str(i) for i in range(1,5)]
test
```




    ['id_1', 'id_2', 'id_3', 'id_4']



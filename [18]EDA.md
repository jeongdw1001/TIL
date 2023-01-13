
```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
%matplotlib inline  
```
```python
movie_df = pd.read_csv('..\data\movies_train.csv')
movie_df
```
```python
# Q1) 헤드값 확인_ 데이터 미리 확인하기
movie_df.head()
```
```python
movie_df.tail()
```
```python
#Q2) shape
movie_df.shape
```
```python
#Q3) 기술 통계 확인하자.
movie_df.describe()
```
```python
#Q4) 특정프레임의 특징 열 통계함수 적용하자.
print(movie_df['box_off_num'].mean())
print(movie_df['box_off_num'].min())
print(movie_df['box_off_num'].max())
```
```python
#Q5) 장르별 고유값 개수
movie_df['genre'].value_counts()
```
```python
#Q6) 특징열 추출
print(movie_df['title'])
print(type(movie_df['title']))
```
```python
#Q7 제목, 감독, 시청수 추출
movie_df[['title','director','box_off_num']]

movie_df.loc[1]

movie_df.iloc[1]
```
```python
#Q8) 행 인덱스를 지정하는 메소드 df.set_index(컬럼이름)
#help(movie_df.set_index) title로 행인덱스를 지정해서 리턴 받아보자.
movie_df02 = movie_df.set_index('title')
movie_df02
```
```python
movie_df02.loc['내부자들'] # [[인덱스이름 1,인덱스이름 2]]
```
```python
movie_df02.iloc[1] # [[인덱스 위치 1, 인덱스 위치 2]]
```
```python
#q9) 여러행을 추출해보자. 1,3,5,7 movie_df의 객체 행 추출
movie_df.loc[[1,3,5,7]]

```
```python
#q10) 여러행을 추출해 보자. _loc[]       
# iloc[[인덱스 이름 1 : 인덱스 이름 2]]     #loc[[인덱스 위치 1 : 인덱스 위치 2]] 
movie_df.loc[1:5]
```
```python
#q11) 요소를 추출해 보자. _loc[]       
# loc[행인덱스 이름,열이름]     #iloc[행인덱스 위치, 열인덱스 위치]
movie_df.loc[1,'title']
```
```python
#q11) 요소를 추출해 보자. _iloc[]       
movie_df.iloc[1,0]
```
```python
#q12) 여러개의 요소를 추출해 보자. _iloc[]       
movie_df.iloc[[1,3,5],[0,6]]
```
```python
#q13)  df[조건식] 장르가 공포인 데이터만 추출해보자.
movie_df[movie_df['genre'] == '공포']

```
```python
#q14)  df[조건식]      장르가 공포인 데이터의 원하는 컬럼을 추출해보자.
movie_df[movie_df['genre'] == '공포'][['title','time','director']]

```
```python
#q16)  df[조건식]      장르가 공포인 데이터의 원하는 컬럼을 추출해보자.
#단, 방영시간이 90분 이하인 데이터만 추출하자.
movie_df[(movie_df['genre'] == '공포') & (movie_df['time'] <= 90)][['title','time','director']]

```
```python
#q17) 관객수(box_off_num)가 가장 많은 영화 정보를 알고싶다.
movie_df[movie_df['box_off_num'] == movie_df['box_off_num'].max()]
```
```python
#q18) 관객수(box_off_num)가 가장 많은 영화 중에서 top3를 알고싶다.
# 1. 특정열을 기준으로 데이터를 정렬해야함
# 2. 기준에 맞는 top3 구하기
# df.sort_values(*, axis=0, ascending=True, )

movie_df.sort = movie_df.sort_values(by='box_off_num',ascending=False)
movie_df.sort[0:3]
```
```python
#q19) 분할, 그룹핑 하기
movie_df_group = movie_df.groupby('screening_rat')
print('분할 개수 :',movie_df_group.ngroups)
```
```python
#print(help(movie_df_group.groups))    'get_group', 'groups'
print(movie_df_group.groups.keys())
#print(dir(movie_df_group.groups))
#print(dir(movie_df_group))

```
```python
#q20) 전체 관람가인 영화의 정보를 추출해보자.
movie_df_group.get_group('전체 관람가')
```
```python
# q21) screening_rat 별 관객수를 구해보자.
movie_df_group['box_off_num'].count()

```
```python
# screening_rat 별 가장 많은 관객수를 구해보자.
movie_df_group['box_off_num'].max()

```
```python
movie_df_group['title'].count()
```
```python
https://pandas.pydata.org/pandas-docs/stable/user_guide/groupby.html
Aggregation
Applying multiple functions at once
Named aggregation
Applying different functions to DataFrame columns
Cython-optimized aggregation functions
Aggregations with User-Defined Functions
***********************도움말 보고 공부하기(필수)************************
```
```python
# q22) DataFrame.agg(func=None, axis=0)을 이용해서 집계함수를 적용해보자.
#가장 오랜시간, 가장 많은 관객수를 추출해보자.
# 분할한 그룹 객체에 대하여 집계 함수를 적용
type(movie_df_group)
movie_df_group.agg({'time':max, 'box_off_num':max})
```
```python
movie_df_group.agg({'time':[max,min], 'box_off_num':[max,min]})
```
```python
#q23) 데이터 프레임의 특정열을 기준으로 사용자 함수를 만들어 보자. df.agg(사용자 정의함수명)
# 영화시간이 가장 긴시간과 짧은 시간의 차이는?
def my_diff(x):
    diff = x.max() - x.min()
    return diff
movie_df_group['time'].agg(my_diff)
```
```python
#pandas.to_datetime(arg, errors='raise', )
# .to_datetime(df['칼럼명']

movie_df['n_date'] = pd.to_datetime(movie_df['release_time'])
```
```python
movie_df.info()  #n_date  600 non-null
```
```python
#q25) 년, 월, 일로 파생변수를 만들어 컬럼 추가를 해보자.
movie_df['year'] = movie_df['n_date'].dt.year
movie_df['month'] = movie_df['n_date'].dt.month
movie_df['day'] = movie_df['n_date'].dt.day

movie_df
```
```python
#q26) 년도별 최대 관객수를 구해보자.
movie_df.groupby('year')['box_off_num'].max()
```
```python
#q27) 누락데이터 처리 Nan 
# 누락데이터 확인 -> 누락데이터 제거 -> 누락데이터 치환
res = pd.read_csv('../data/titanic.csv')
res.head()
```
```python
import seaborn as sns
titanic = sns.load_dataset('titanic')
titanic.head()
```
```python
titanic.info()
```
```python
titanic['deck'].value_counts(dropna=False)
```
```python
titanic.isnull() #결측치 확인
```
```python
#누락 데이터 개수  isnull().sum()
titanic.isnull().sum()
```
```python
# 누락 데이터 행, 열 삭제 dropna(axis, thresh = 누락데이터 개수) -> 데이터 과적합
# 대상 -> 시뮬레이션 99.8% 정확도(테스트) -> 서비스 배포 -> 65%
titanic = titanic.dropna(axis = 1, thresh = 500)
titanic.head()
```
```python
titanic.isnull().sum()    #누락데이터 deck 삭제
```
```python
# 결측(누락)데이터 치환 df.fillna(대체값 , inplace=True) _ 최대값, 최소값, 평균값 등등 
age_mean = titanic['age'].mean()
age_mean

```
```python
titanic['age'].fillna(age_mean, inplace=True)
```
```python
titanic.isnull().sum() 
```
```python
#결측(누락)데이터 : 최빈값으로 구해서 치환
titanic['embarked']
```
```python
titanic['embarked'].value_counts(dropna=False)
```
```python
titanic['embarked'].value_counts(dropna=False).idxmax()  #결측(누락)데이터 : 최빈값=idxmax()으로 구해서 치환
```
```python
e_idxmax = titanic['embarked'].value_counts(dropna=False).idxmax() 
titanic['embarked'].fillna(e_idxmax, inplace=True)
```
```python
et_idxmax = titanic['embarked'].value_counts(dropna=False).idxmax() 
titanic['embarked'].fillna(et_idxmax, inplace=True)
```
```python
titanic.isnull().sum()
<<<<<<< HEAD
```

=======
```
>>>>>>> c71c4abcbd0cc0800e4e04d52414fb6644a93bf8

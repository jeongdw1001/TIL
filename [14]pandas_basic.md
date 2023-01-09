1) 시리즈 및 데이터 프레임

2) 시리즈 ( Series) 만들기

3) 데이터 프레임 ( DataFrame) 만들기

4) CSV 파일에서 데이터 프레임 만들기

5) 데이터 참조 및 데이터 조건 검색

6) 열 추가 및 삭제 ,행 추가 및 삭제

7) 데이터 정렬,  통계량

8) 데이터 연결, 결합

9) 데이터 그룹화

10) 결손값, 시계열 데이터 처리

*도움말 링크 : https://pandas.pydata.org/


import pandas as pd
import numpy as np

2) 시리즈 ( Series) 만들기

s1 = pd.Series([0,1,2])
print(s1)

s2 = pd.Series(np.random.rand(3))
print(s2, end='\n')

s3 = pd.Series({0:'나',1:'너',2:'우리'})
print(s3, end='\n')

s4 = pd.Series({'e':'1','b':'2','d':'3'})  #key : value 
# 정렬 안됨, 대입 순서대로
print(s4, end='\n')
# dtype : object --> 연산이 불가능(=분석이 불가능)
print(s4.info())  #시리즈 정보를 확인

print(dir(s4))

print(help(s4))
# Series(pandas.core.base.IndexOpsMixin, pandas.core.generic.NDFrame)
 |  Series(data=None, index=None, dtype: 'Dtype | None' = None, name=None, copy: 'bool' = False, fastpath: 'bool' = False)
 
 

3) 데이터 프레임 ( DataFrame) 만들기

d1 = pd.DataFrame([[0,1,2],
                  [3,4,5],
                  [6,7,8],
                  [9,10,11]],
                  index = [10,11,12,13],
                  columns = ['c1','c2','c3']
                 )

print(d1,end='\n\n')
d1.info()

d2 = pd.DataFrame(np.random.rand(12).reshape(4,3),
                  columns = ['c1','c2','c3'])
print(d2, end='\n\n')

d3 = pd.DataFrame({'Initial':['B','F','W'],
                  'Name':['나','너','우리']},
                  columns = ['Name','Initial','Initial','Initial']
                 )
print(d3, end='\n\n')
#d1.info()

# 독립변수 X1~Xn (features)
#종속변수 y (class labels) =정답 라벨

#iris.csv 설치된 경로 
#C:\Anaconda3\pkgs\scikit-learn-1.0.2-py39hf11a4ad_1\Lib\site-packages\sklearn\datasets\data

#!pip install scikit-learn
from sklearn.datasets import load_iris
data = load_iris()
type(data)
print(data) #2차원 [가 2개


#4) csv 파일에서 데이터 프레임 만들기
iris_d = pd.read_csv('..\data\iris.csv')
iris_d
iris_d.info()

#RangeIndex :150 entries, 0 to 149
print(iris_d.index)
print(len(iris_d))

import sklearn

from sklearn.datasets import load_iris

data = load_iris()
print(data)
#type(data) # bunch = dict타입의 대용량 형식


4) CSV 파일에서 데이터 프레임 만들기

iris_d =pd.read_csv('../data/iris.csv')
iris_d
iris_d.info() # 정보, 목록 전체, 상위, 하위 몇개씩 확인

iris_d.head(10) #5줄 기본

iris_d.tail(10)

#RangeIndex :150 entries, 0 to 149
print(iris_d.index)
print(len)

5) 데이터 참조 및 데이터 조건 검색, 단일 컬럼 추출, 다중 컬럼 추출, 인덱싱, 슬라이싱 = iloc[], loc[정수, 컬럼명]

iris_d[:5] #5행 추출

iris_d[-5:] #5행 끝에서부터 추출

iris_s =pd.read_csv('C:\Anaconda3\pkgs\scikit-learn-1.0.2-py39hf11a4ad_1\Lib\site-packages\sklearn\datasets\data\iris.csv')
iris_s
#iris_s.info() # 정보, 목록 전체, 상위, 하위 몇개씩 확인

iris_d['class'].head(10) #데이터프레임['열이름'] Series객체로 리턴
r= iris_d['class']
type(r)

#데이터프레임['열이름','열이름의 목록'] 하나 이상의 Series객체로 리턴
iris_d[['sepallength','sepalwidth']].head(10)
r=iris_d[['sepallength','sepalwidth']]
print(type(r))

iris_d.iloc[1]

iris_d

iris_d.iloc[0]

iris_d.iloc[1,1]

iris_d.iloc[0:5,0:2]
#iris_d.iloc[:5,:2]

iris_d.iloc[2]  #loc랑 비교

iris_d.loc[2, 'sepalwidth']

iris_d.loc[1:5, ['sepalwidth','petallength']]

#sepallength  sepalwidth  petallength  petalwidth  class

6) 데이터 조건 검색 : and, or -> not, &, |, ~를 사용한다.

#sepallength 7.0보다 크고 sepalwidth 3.0작은 데이터를 추출해보자.
iris_d[(iris_d['sepallength'] > 7.0) & (iris_d['sepalwidth'] < 3.0)]

6-1)열 추가 및 삭제, 행 추가 및 삭제 -> 시계열 계산

7) 데이터 정렬, 통계량

iris_d['mycolumn'] = np.random.rand(len(iris_d.index))
iris_d.head()

#del iris_d['mycolumn']
iris_d.head()

# 데이터 프레임에 컬럼을 추가해서 다시 리턴하는 메소드 assign(컬럼명 = 값)
# drop()을 이용하면 원하는 컬럼을 삭제할 수 있다.

my_res = iris_d.assign(mycolumn=np.random.rand(len(iris_d.index)))
my_res.head()
#iris_d.head()


#print(help(my_res.drop))
my_res.drop('mycolumn', axis=1)

###### 행추가, 삭제 .append() ignore_index
help(my_res.append)

row = pd.DataFrame([[1,1,1,1,'Iris-setosa']], columns = iris_d.columns)
row  #새로 리턴을 해줌

m_iris = iris_d.append(row,ignore_index=True) # True : 새로운 번호, False : 0번 부터
m_iris[-2:]

m_iris=m_iris.drop(150, axis=0)
m_iris

m_iris[-2:]

m_iris.tail()

7) 데이터 정렬,  통계량
sort_index() : 데이터 프레임의 인덱스를 기반으로 정렬
sort_values() : 임의의 열의 값에 의한 소트
inplace = False 소트에 의해 새로운 데이터 프레임을 작성

sorted_iris = iris_d.sort_values(['sepallength','sepalwidth','petallength','petalwidth'])
sorted_iris.head(10)

# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html

#True:오름차순
sorted_iris_T = iris_d.sort_values(['sepallength','sepalwidth','petallength','petalwidth'],ascending=True)
sorted_iris_T.head(10)  

#False:내림차순
sorted_iris_F = iris_d.sort_values(['sepallength','sepalwidth','petallength','petalwidth'],ascending=False)
sorted_iris_F.head(10) 

iris_d.sort_index(ascending=False)

iris_d.describe() #평균, 표준편차, 최대값, 최소값, 집계
# 표준편차랑 분산
# 표준편차 : 분산의 정도, 산포도 수치형식, 분산값에 루트를 씌운 값
# 데이터가 평균과 얼마나 차이가 있는지 확인
# 확률분포 -> 인구증가, 중복데이터ㅕㅓ  

8) 데이터 연결 : concat, 결합 : merge
# 행과 행을 연결        

# 열과 열을 연결 
concat_res = pd.concat([iris_d.loc[:,["sepallength"]], \
                        iris_d.loc[:,["class"]]], axis=1)
concat_res

# 행과 행을 연결 
concat_res = pd.concat([iris_d[:5],iris_d[-5:]])
concat_res

9) 데이터 그룹화 _groupby()

iris_d.groupby('class').head()

iris_d.groupby('class')[['sepallength','sepalwidth']].mean()

10) 결손값, 시계열 데이터 처리


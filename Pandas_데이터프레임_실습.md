# 데이터프레임
- 2차원 행렬 데이터에 인덱스를 붙인 것
- 행과 열로 만들어지는 2차원 배열 구조
- R의 데이터 프레임에서 유래
- 데이터프레임의 각 열은 시리즈로 구성되어 있음
- DataFrame() 함수를 사용해서 생성

- pd.read_csv('파일명')
- DataFrame.to_csv('파일명)

# 데이터프레임 생성

## 리스트로 데이터 프레임 만들기

- DataFrame([[list1],[list2]]) : 리스트 안에 리스트 형태로 인수를 전달(2차원 리스트 형태로 전달)
- 각 list는 한 행으로 구성됨
- 행의 원소 개수가 다르면 None 값으로 저장
- index 인수 값이 없으면 기본 인덱스(위치 인덱스 : 0부터 시작)가 생성됨


```python
import pandas as pd
import numpy as np
```


```python
df = pd.DataFrame([['a','b','c'],['a','a','g'],['a','a']])
df
```

### 딕셔너리로 데이터프레임 생성
- dict의 key => column name


```python
df1 = pd.DataFrame(
{
    'A':[90,80,70],
    'B':[85,98,75],
    'C':[88,99,77],
    'D':[87,89,86]
},index = [1,2,3]
)
df1
```


```python
data = {
    '2015':[9904312,3448737,2890451,2466052],
    '2010':[9631482,3393191,2632035,2000002],
    '2005':[9732546,3512547,2517680,2456016],
    '2000':[9853972,3655437,2466338,2473990],
    '지역':['수도권','경상권','수도권','경상권'],
    '2010-2015 증가율':[0.0283,0.0163,0.0982,0.0141]
}
df3 = pd.DataFrame(data)
df3
```

### 위에서 생성된 데이터 프레임은 열의 순서가 보장되지 않고, 각 행의 의미 전달이 어렵다.
- index 파라미터와 columns 파라미터를 사용해서 df의 의미 전달이 쉬워진다.


```python
columns = ['지역','2000','2005','2010','2015','2010-2015 증가율']
index = ['서울','부산','인천','대구']
df3 = pd.DataFrame(data, index=index, columns=columns)
df3
```

### 시리즈로 데이터 프레임 생성
- 각 Series의 인덱스 => columnname


```python
a = pd.Series([100,200,300],['a','b','d'])
b = pd.Series([101,201,301],['a','b','k'])
c = pd.Series([110,210,310],['a','b','c'])
```


```python
pd.DataFrame([a,b,c],index=[100,101,102])
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
      <th>d</th>
      <th>k</th>
      <th>c</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>100</th>
      <td>100.0</td>
      <td>200.0</td>
      <td>300.0</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>101</th>
      <td>101.0</td>
      <td>201.0</td>
      <td>NaN</td>
      <td>301.0</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>102</th>
      <td>110.0</td>
      <td>210.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>310.0</td>
    </tr>
  </tbody>
</table>
</div>



### csv 데이터로부터 DataFrame 생성
- 데이터 분석을 위해, dataframe을 생성하는 가장 일반적인 방법
- 데이터 소스로부터 추출된 csv(comma separated values) 파일로부터 생성
- pandas.read_csv 함수 사용


```python
train_data = pd.read_csv('C:/ds_work/data/train.csv')
train_data.head()
```

### read_csv 함수 파라미터
- sep : 각 데이터 값을 구별하기 위한 구분자(seperator) 설정
- header : header를 무시할 경우, None 설정
- index_col : index로 사용할 column 설정
- usecols : 실제로 dataframe에 로딩할 columns만 설정


```python
train_data = pd.read_csv('C:/ds_work/data/train.csv', 
                        index_col = 'PassengerId',
                        usecols = ['PassengerId','Survived','Name','Sex','Age'])
```


```python
# df.columns 속성 : df의 컬럼명을 저장하고 있는 속성
train_data.columns
```




    Index(['Survived', 'Name', 'Sex', 'Age'], dtype='object')




```python
train_data.head()
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
      <th>Survived</th>
      <th>Name</th>
      <th>Sex</th>
      <th>Age</th>
    </tr>
    <tr>
      <th>PassengerId</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>1</th>
      <td>0</td>
      <td>Braund, Mr. Owen Harris</td>
      <td>male</td>
      <td>22.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1</td>
      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>
      <td>female</td>
      <td>38.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1</td>
      <td>Heikkinen, Miss. Laina</td>
      <td>female</td>
      <td>26.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1</td>
      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>
      <td>female</td>
      <td>35.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>0</td>
      <td>Allen, Mr. William Henry</td>
      <td>male</td>
      <td>35.0</td>
    </tr>
  </tbody>
</table>
</div>



### 인덱스와 컬럼의 이해
1. 인덱스(index)
    - index 속성
    - 각 아이템을 특정할 수 있는 고유의 값을 저장
    - 복잡한 데이터의 경우, 멀티 인덱스로 표현 가능
  
  
2. 컬럼(column)
    - columns 속성
    - 각각의 특성(feature)을 나타냄
    - 복잡한 데이터의 경우, 멀티 컬럼으로 표현 가능


```python
df3
```


```python
print(df3.columns)
type(df3.columns)
```


```python
print(type(df3.index))
df3.index
```

### 행/열 인덱스 이름 설정
- index.name
- columns.name


```python
df3.index.name = '도시'
df3.columns.name = '특성'
```


```python
df3
```


```python
print(type(df3.values))
df3.values
```


```python
print(type(df3.values[0]))
df3.values[0]
```

### dataFrame 데이터 파악하기
    - shape 속성 (row, column)
    - describe 함수 : 숫자형 데이터의 통계치 계산
    - info 함수 : 데이터 타입, 각 아이템의 개수 등 출력


```python
train_data.head()
```


```python
print(len(train_data)) # df의 행 수
print(train_data.size) # df의 값의 개수
train_data.shape # df의 행과 열 수
```


```python
train_data.info()
```


```python
train_data.describe()  # 수치형 데이터에 대해서만 기본 통계량을 반환
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
      <th>Survived</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>891.000000</td>
      <td>714.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>0.383838</td>
      <td>29.699118</td>
    </tr>
    <tr>
      <th>std</th>
      <td>0.486592</td>
      <td>14.526497</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.420000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>0.000000</td>
      <td>20.125000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>0.000000</td>
      <td>28.000000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>1.000000</td>
      <td>38.000000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>1.000000</td>
      <td>80.000000</td>
    </tr>
  </tbody>
</table>
</div>



### 데이터 프레임 전치
- 전치 : 행과 열을 바꾸는 기능
- df.T
- 원본 df는 변경되지 않음


```python
df3
```


```python
df3.T 
```


```python
df3['지역'].values
```


```python
df3.T['서울'].values
```


```python
df3.T['서울']['2000']
```

### 데이터 프레임 내용 변경
- 열추가, 열삭제, 내용 갱신


### 해당 열이 있으면 내용 갱신, 열이 없으면 추가
- 열추가 : df[열이름(key)]=values


```python
df3
```


```python
df3.columns
```


```python
df3['2010-2015 증가율'] = df3['2010-2015 증가율']*100
```


```python
df3['2010-2015 증가율']
```


```python
# 열 추가
df3['비고'] = ['특별시','광역시','특례시','특례시']
```


```python
df3
```


```python
del df3['비고']
```


```python
# 가공열 추가
df3['2005-2015 증가율'] = ((df3['2015']-df3['2005'])/df3['2005']*100).round(2)
df3
```


```python
#del df3['2005-2015 증가율']
```


```python
df3
```

### DF의 행추가
- pd의 인덱서 사용
- concate() 사용 : 추가하고자 하는 data를 df로 새로 생성 후 결합


```python
# loc 인덱서 사용 : df.loc[새로추가될행이름]=[데이터1,,,,,,,,,데이터n]
df3.loc['광주']=['호남권',2470000,2456000,2453000,2460000,1.00]
# 변경도 가능
```


```python
df3
```

### 데이터 프레임 인덱싱
1. 열인덱싱
2. 인덱서를 사용하지 않는 행 인덱싱
    - []기호를 이용해서 인덱싱 할 때 주의점 : []기호는 열 위주 인덱싱이 원칙

### 1. 열인덱싱
- 열 라벨(컬럼명)을 키 값으로 생각하고 인덱싱한다.

    - 인덱스로 라벨값을 하나 넣으면 시리즈 객체가 반환
    - 라벨의 배열이나 리스트를 넣으면 부분적  df가 반환


```python
df3
```

### 한 개의 열 추출


```python
print(df3['지역'])
type(df3['지역'])
```


```python
# 1개의 열 추출시, 연산자 사용 가능(시리즈로 반환)
print(df3.지역)
type(df3.지역)
```


```python
# 인덱스 값으로 컬럼명의 리스트를 사용하면 dataframe으로 반환
df3[['지역']]
```


```python
type(df3[['지역']])
```


```python
df3[['2010','2015']]
```

### 판다스 데이터 프레임에 열이름(컬럼명)이 문자열일 경우
- 수치 인덱스를 사용할 수 없음
- 위치 인덱싱 기능을 사용할 수 없음 : keyerror 발생


```python
try:
    df3[0]
except Exception as e:
    print(type(e))
```


```python
df3.columns
```


```python
# 예제 df5 생성해보기
df5 = pd.DataFrame(np.arange(12).reshape(3,4))
df5
```


```python
df5[[1,2]]
```


```python
np.arange(12)
np.arange(12).reshape(3,4) # 배열의 차원을 변경
```

### 행 단위 인덱싱
- 행 단위 인덱싱을 하고자 하면 인덱서라는 특수 기능을 사용하지 않는 경우 슬라이싱을 해야함
- 인덱스 값이 문자(라벨)면 문자 슬라이싱도 가능
    - 위치값 슬라이싱도 가능


```python
df3
```


```python
# 첫번째 행 추출
df3[:'서울']
```


```python
df3['인천':'인천']
```


```python
df3[:1]
#df3[0:1]
```


```python
df3[1:3] # 시작값 : 끝값+1 ===> 끝값+1=3이므로 끝값은 2
```


```python
df3['부산':'인천']
```

### 개별요소 접근 [열][행]


```python
df3['2015'] # 시리즈 반환
```


```python
df3['2015']['부산']
```


```python
df3[['2015']]
# dataframe으로 반환
```
df3[['2015']]['부산']
# KeyError 발생
# df3[['2015']] : dataframe으로 반환하기 때문

```python
df3[['2015']]['부산':'부산']
```


```python
df3[['2015','2010']]
```


```python
df3[['2015','2010']]['부산':'부산']
         # 열            #행
```


```python
df3
```


```python
# 열 인덱싱에 슬라이싱 사용 불가
# df3[['2000':'2010']]
# SyntaxError
```

### 행 삭제
- drop() 함수 사용
- drop(index=[삭제할 행 인덱스])
- 원본 반영 x
- 삭제와 동시에 원본 반영하려면
  drop(index=[삭제할 행 인덱스],inplace=True)


```python
df3.drop(index=['광주'])
```


```python
df3
```


```python
df3.drop(index=['광주'],inplace=True)
```


```python
df3
```

### drop() 이용 열 삭제
- drop(columns=[삭제할 열])


```python
df3.drop(columns=['2010-2015 증가율','2010'])
```


```python
#df3.drop(columns=['2010-2015 증가율','2010'])
```

### drop()함수 columns/index 미 표기시
- drop([삭제할 행 또는 열], axis=0/1)
- axis : 0(행),1(열)


```python
df3.drop(['대구'],axis=0)
```


```python
df3.drop(['2000'],axis=1)
```

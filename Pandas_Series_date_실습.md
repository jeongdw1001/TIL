### Series
- pandas의 기본 객체 중 하나
- numpy의 ndarray를 기반으로 인덱싱을 기능을 추가하여 1차원 배열을 나타냄
- index를 지정하지 않을 시, 기본적으로 ndarray와 같이 0-based 인덱스 생성, 지정할 경우 명시적으로 지정된 index를 사용
- 같은 타입의 0개 이상의 데이터를 가질 수 있음


```python
import pandas as pd
import numpy as np
```

### Series 생성하기
- data로만 생성하기
- index는 기본적으로 0부터 자동적으로 생성


```python
# pd.Series(집합적 자료형)
# pd.Series(리스트)
s = pd.Series([1,2,3])
s
# 위 코드는 시리즈 생성 시 인덱스를 명시하지 않았음. 0 base 인덱스 생성
```




    0    1
    1    2
    2    3
    dtype: int64




```python
# pd.Series(튜플)
s = pd.Series((1.0,2.0,3.0))
s
```




    0    1.0
    1    2.0
    2    3.0
    dtype: float64



### pd.Series()
- 시리즈 생성 시 반드시 집합적 자료형을 이용해야 함


```python
s2 = pd.Series(['a','b','c'])
s2
```




    0    a
    1    b
    2    c
    dtype: object




```python
# 리스트 내에 서로 다른 type의 data가 있으면 형변환이 일어남 - 문자열로 변환됨
s_1 = pd.Series(['a',1,3.0])
s_1
```




    0      a
    1      1
    2    3.0
    dtype: object



- 범위를 시리즈의 value 생성하는데 사용하기
- range/np.arange 함수 사용


```python
s=pd.Series(range(10,14))
s
```




    0    10
    1    11
    2    12
    3    13
    dtype: int64




```python
range(10,14)
```




    range(10, 14)




```python
np.arange(200)
```




    array([  0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,
            13,  14,  15,  16,  17,  18,  19,  20,  21,  22,  23,  24,  25,
            26,  27,  28,  29,  30,  31,  32,  33,  34,  35,  36,  37,  38,
            39,  40,  41,  42,  43,  44,  45,  46,  47,  48,  49,  50,  51,
            52,  53,  54,  55,  56,  57,  58,  59,  60,  61,  62,  63,  64,
            65,  66,  67,  68,  69,  70,  71,  72,  73,  74,  75,  76,  77,
            78,  79,  80,  81,  82,  83,  84,  85,  86,  87,  88,  89,  90,
            91,  92,  93,  94,  95,  96,  97,  98,  99, 100, 101, 102, 103,
           104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116,
           117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
           130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142,
           143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155,
           156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168,
           169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181,
           182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194,
           195, 196, 197, 198, 199])




```python
s3=pd.Series(np.arange(200))
s3
```




    0        0
    1        1
    2        2
    3        3
    4        4
          ... 
    195    195
    196    196
    197    197
    198    198
    199    199
    Length: 200, dtype: int32




```python
# 내가 만든 예시
s4=pd.Series(['a',2,np.arange(200)])
s4
```




    0                                                    a
    1                                                    2
    2    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,...
    dtype: object



- 결측값을 포함해서 시리즈 만들기
    - 결측값 NaN : numpy라는 모듈에서 생성할 수 있음
    - 결측값 생성 위해서는 numpy 모듈 import
    - 판다스가 처리하는 자료구조인 시리즈와 데이터프레임에서 결측치가 있는 경우는 datatype이 float로 변환


```python
# NaN은 np.nan 속성을 이용해서 생성
s=pd.Series([1,2,3,np.nan,6,8])
s
```




    0    1.0
    1    2.0
    2    3.0
    3    NaN
    4    6.0
    5    8.0
    dtype: float64



- 인덱스 명시해서 시리즈 만들기
    - 숫자 인덱스 지정
    - s = pd.Series([값1, 값2, 값3],index=[1,2,3])


```python
s=pd.Series([10,20,30],index=[1,2,3])
s
```




    1    10
    2    20
    3    30
    dtype: int64



- 문자 인덱스 지정


```python
s=pd.Series([95,100,88],index=['홍길동','이몽룡','성춘향'])
s
```




    홍길동     95
    이몽룡    100
    성춘향     88
    dtype: int64



- 인덱스 활용 : 시리즈의 index
    - 시리즈의 index는 index 속성으로 접근


```python
s0=pd.Series([10,20,30],index=[1,2,3])
s0
```




    1    10
    2    20
    3    30
    dtype: int64




```python
s0.index
```




    Int64Index([1, 2, 3], dtype='int64')




```python
s00 = pd.Series([1,2,3])
s00.index
```




    RangeIndex(start=0, stop=3, step=1)




```python
s = pd.Series([9904312,3448737,289045,2466052],index=['서울','부산','인천','대구'])
s.index
```




    Index(['서울', '부산', '인천', '대구'], dtype='object')




```python
s.index.name = '광역시'
s
```




    광역시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    dtype: int64




```python
s.index
```




    Index(['서울', '부산', '인천', '대구'], dtype='object', name='광역시')




```python
s.values
# 시리즈 값의 전체 형태는 array(numpy의 자료구조) 형태
```




    array([9904312, 3448737,  289045, 2466052], dtype=int64)



- 시리즈.name 속성
    - 시리즈 데이터에 이름을 붙일 수 있다.
    - name 속성은 값의 의미 전달에 사용


```python
s.name = '인구'
s
```




    광역시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64



### 인덱싱 : 데이터에서 특정한 데이터를 골라내는 것
- 시리즈의 인덱싱 종류
    1. 정수형 위치 인덱스
    2. 인덱스 이름 또는 인덱스 라벨
        - 인덱스 별도 지정하지 않으면 0부터 시작하는 정수형 인덱스가 지정됨

- 원소접근
    - 정수형 인덱스 : 숫자 s[0]
    - 문자형 인덱스 : 문자 s['인천']


```python
print(s.index) 
s['인천'] # 문자형 인덱스로 접근
# s[2] # 위치 인덱스 사용 가능
```

    Index(['서울', '부산', '인천', '대구'], dtype='object', name='광역시')
    




    289045




```python
# 정수형 인덱스인 경우
s03 = pd.Series([1,2,3],index=[4,5,6])
s03
# 명시적 인덱스 (정수 인덱스) 사용

```




    4    1
    5    2
    6    3
    dtype: int64




```python
s03[4]
```




    1




```python
s03[5]
```




    2




```python
s03[6]
```




    3




```python
# s03[0]
# 위치인덱스 접근 - KeyError
```


```python
# 문자형 인덱스(부산 데이터 추출 해보기)
s['부산']
```




    3448737




```python
# 두 개 이상의 인덱싱 코드를 나열하면 
# 튜플형태로 반환
s[3], s['대구']
```




    (2466052, 2466052)




```python
# 노트북 팁
# 데이터에 두 번 접근
s03
s # 마지막 연산에 대해서만 접근 결과를 보여줌
```




    광역시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64



### 리스트 이용 인덱싱
- 자료의 순서를 바꾸거나 특정자료 여러개를 선택할 수 있다.
- 인덱스값 여러개를 이용해 접근시 []안에 넣는다.


```python
print(s)
# s[0,3,1]
# KeyError: 'key of type tuple not found and not a MultiIndex'
s[0],s[3],s[1]
# 시리즈명[[인덱스리스트]] - 시리즈 형태로 반환
s[[0,3,1]]
# 인덱스 리스트 내의 해당 인덱스의 item을 추출 후 시리즈 형태로 반환
```

    광역시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64
    




    광역시
    서울    9904312
    대구    2466052
    부산    3448737
    Name: 인구, dtype: int64



### 시리즈 슬라이싱
- 정수형 위치 인덱스를 사용한 슬라이싱
    - 시리즈[start:stop+1]
- 문자(라벨)인덱스 이용 슬라이싱
    - 시리즈['시작라벨':'끝라벨'] : 표시된 라벨 범위 모두 추출


```python
s[0:2]
```




    광역시
    서울    9904312
    부산    3448737
    Name: 인구, dtype: int64




```python
print(s)
```

    광역시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64
    


```python
s[[1,2]]
```




    광역시
    부산    3448737
    인천     289045
    Name: 인구, dtype: int64




```python
s[['부산','인천']] 
```




    광역시
    부산    3448737
    인천     289045
    Name: 인구, dtype: int64




```python
s[1:3]
# 시리즈 슬라이싱을 사용하면 시리즈로 반환
```




    광역시
    부산    3448737
    인천     289045
    Name: 인구, dtype: int64




```python
# 정수형 인덱스를 명시했을 경우
s_01 = pd.Series([100,200,300,400],index=[1,2,3,4])
print(s_01)
s_01[[2,3,4]]
```

    1    100
    2    200
    3    300
    4    400
    dtype: int64
    




    2    200
    3    300
    4    400
    dtype: int64




```python
# 슬라이싱 사용
s_01[2:4]
```




    3    300
    4    400
    dtype: int64



### 시리즈의 인덱스를 명시할 때는 가급적이면 문자형으로 명시하는 것이 좋다.

### 문자 인덱스
- [.]연산자를 이용하여 접근 가능


```python
# 인덱스를 문자값으로 지정한 시리즈
s0 = pd.Series(range(3),index=['a','b','c'])
s0
```




    a    0
    b    1
    c    2
    dtype: int64




```python
s0['a']
#s0.a
```




    0




```python
print(s)
s['서울']
```

    광역시
    서울    9904312
    부산    3448737
    인천     289045
    대구    2466052
    Name: 인구, dtype: int64
    




    9904312




```python
s.부산
```




    3448737



### 인덱스 통한 데이터 업데이트


```python
s['서울'] = 10000000
s['서울']
```




    10000000




```python
s
```




    광역시
    서울    10000000
    부산     3448737
    인천      289045
    대구     2466052
    Name: 인구, dtype: int64



### 인덱스 재사용하기


```python
print(s.index)
```

    Index(['서울', '부산', '인천', '대구'], dtype='object', name='광역시')
    


```python
s1 = pd.Series(np.arange(4),s.index)
s1
```




    광역시
    서울    0
    부산    1
    인천    2
    대구    3
    dtype: int32



### 시리즈 연산


```python
s
```




    광역시
    서울    10000000
    부산     3448737
    인천      289045
    대구     2466052
    Name: 인구, dtype: int64



### 벡터화 연산
- 집합적 자료형의 원소 각각을 독립적으로 계산을 진행하는 방법
    - 단, 연산은 시리즈의 값에만 적용되며 인덱스 값은 변경 불가


```python
pd.Series([1,2,3]) + 4
```




    0    5
    1    6
    2    7
    dtype: int64




```python
s / 1000000 # 원본에는 영향 없음
```




    광역시
    서울    10.000000
    부산     3.448737
    인천     0.289045
    대구     2.466052
    Name: 인구, dtype: float64




```python
# s 시리즈 값 중 2500000 보다ㅣ 크고 5000000보다 작은 원소를 추출
s[(s>250e4) & (s<500e4)]
# s 시리즈 각 원소값 각각에 대해서 조건식을 확인해서 결과가 True인 원소를 반환
```




    광역시
    부산    3448737
    Name: 인구, dtype: int64



### Boolean Selection


```python
s0 = pd.Series(np.arange(10),np.arange(10)+1)
s0
```




    1     0
    2     1
    3     2
    4     3
    5     4
    6     5
    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
s0 > 5
```




    1     False
    2     False
    3     False
    4     False
    5     False
    6     False
    7      True
    8      True
    9      True
    10     True
    dtype: bool




```python
s0[s0 > 5]
```




    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
# 짝수 값만 추출
s0[s0%2 == 0]
```




    1    0
    3    2
    5    4
    7    6
    9    8
    dtype: int32




```python
s0.index > 5
```




    array([False, False, False, False, False,  True,  True,  True,  True,
            True])




```python
s0[s0.index > 5]
```




    6     5
    7     6
    8     7
    9     8
    10    9
    dtype: int32




```python
s0[(s0 > 5) & (s0 < 8)]
```




    7    6
    8    7
    dtype: int32




```python
(s0 >= 7).sum() # 조건의 결과가 True인 원소들의 총 개수
```




    3




```python
(s0[s0 >= 7]).sum() # 조건의 결과가 True인 원소들의 합
```




    24



### 두 시리즈 간의 연산


```python
num_s1 = pd.Series([1,2,3,4],index=['a','b','c','d'])
num_s1
```




    a    1
    b    2
    c    3
    d    4
    dtype: int64




```python
num_s2 = pd.Series([5,6,7,8],index=['b','c','d','a'])
num_s2
```




    b    5
    c    6
    d    7
    a    8
    dtype: int64




```python
num_s1 + num_s2 # 같은 인덱스를 찾아 연산을 진행
```




    a     9
    b     7
    c     9
    d    11
    dtype: int64




```python
num_s3 = pd.Series([5,6,7,8],index=['e','b','f','g'])
num_s4 = pd.Series([1,2,3,4],index=['a','b','c','d'])
```


```python
num_s3 + num_s4 
# 동일한 인덱스는 연산을 진행하고 나머지 인덱스는 연산처리 불가능 NaN값으로 처리
```




    a    NaN
    b    8.0
    c    NaN
    d    NaN
    e    NaN
    f    NaN
    g    NaN
    dtype: float64




```python
num_s3.values - num_s4.values
```




    array([4, 4, 4, 4], dtype=int64)



### 딕셔너리와 시리즈의 관계
- 시리즈 객체는 라벨(문자)에 의해 인덱싱이 가능
- 라벨을 key로 가지는 딕셔너리형
- 딕셔너리에서 제공하는 대부분의 연산자 사용 가능
    - in 연산자 : T/F
    - for 루프를 통해 각 원소의 key 와 value 에 접근 가능

### in 연산자 / for 반복문 사용


```python
s
```




    광역시
    서울    10000000
    부산     3448737
    인천      289045
    대구     2466052
    Name: 인구, dtype: int64




```python
'서울' in s
```




    True




```python
'대전' in s
```




    False




```python
'대전' not in s
```




    True




```python
# 딕셔너리의 items() 함수 시리즈에 사용 가능
s.items()
```




    <zip at 0x1d6f43be4c0>




```python
list(s.items())
```




    [('서울', 10000000), ('부산', 3448737), ('인천', 289045), ('대구', 2466052)]




```python
# 시리즈 각 원소 출력
for k,v in s.items():
    print('%s=%d' % (k,v))
```

    서울=10000000
    부산=3448737
    인천=289045
    대구=2466052
    

### 딕셔너리로 시리즈 만들기
- Series({key:value,key1:value2,,,,})
- 인덱스 : key
- 값 : value


```python
scores = {'홍길동':96, '이몽룡':100, '성춘향':88}
s = pd.Series(scores)
s
```




    홍길동     96
    이몽룡    100
    성춘향     88
    dtype: int64




```python
city = {'서울':9631482, '부산':3393191, '인천':2632035, '대전':1490158}
s = pd.Series(city)
s
```




    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64



- 딕셔너리의 원소는 순서를 갖지 않는다.
    - 딕셔너리로 생성된 시리즈의 원소도 순서가 보장되지 않는다.
    - 만약 순서를 보장하고 싶으면 인덱스를 리스트로 지정해야한다.


```python
city = {'서울':9631482, '부산':3393191, '인천':2632035, '대전':1490158}
s = pd.Series(city, index=city.keys())
s
```




    서울    9631482
    부산    3393191
    인천    2632035
    대전    1490158
    dtype: int64




```python
s = pd.Series(city, index=['부산','인천','서울','대전'])
s
```




    부산    3393191
    인천    2632035
    서울    9631482
    대전    1490158
    dtype: int64



### 시리즈 데이터의 갱신, 추가, 삭제
- 인덱싱을 이용하면 딕셔너리처럼 갱신, 추가 가능


```python
s['부산'] = 1630000
s
```




    부산    1630000
    인천    2632035
    서울    9631482
    대전    1490158
    dtype: int64




```python
#del s['서울']
```


```python
s
```




    부산    1630000
    인천    2632035
    대전    1490158
    dtype: int64




```python
s['대구']=111111
s
```




    부산    1630000
    인천    2632035
    대전    1490158
    대구     111111
    dtype: int64



### Series 함수

### size, shape, unique, count, value_counts 함수
    
    - size(속성) : 개수 반환
    - shape(속성) : 튜플 형태로 shape 반환
    - unique : 유일한 값만 ndarray로 반환 
    - count : NaN을 제외한 개수를 반환
    - mean : NaN을 제외한 평균
    - value_counts : NaN을 제외하고 각 값들의 빈도를 반환


```python
s1 = pd.Series([1,1,2,1,2,2,2,1,1,3,3,4,5,5,7,np.NaN])
s1
```




    0     1.0
    1     1.0
    2     2.0
    3     1.0
    4     2.0
    5     2.0
    6     2.0
    7     1.0
    8     1.0
    9     3.0
    10    3.0
    11    4.0
    12    5.0
    13    5.0
    14    7.0
    15    NaN
    dtype: float64




```python
len(s1)
```




    16




```python
s1.size
```




    16




```python
s1.shape 
```




    (16,)




```python
s1.unique()
```




    array([ 1.,  2.,  3.,  4.,  5.,  7., nan])




```python
s1.count()
# nan을 제외한 원소의 개수
```




    15




```python
a = np.array([2,2,2,2,np.NaN])
print(a.mean())
# mean() : 평균값
# array에 대해 mean()을 적용하면 nan이 포함된 계산을 진행

b = pd.Series(a) # 배열을 시리즈로 변경
print(b)
b.mean() # nan 제외하고 평균값 계산
```

    nan
    0    2.0
    1    2.0
    2    2.0
    3    2.0
    4    NaN
    dtype: float64
    




    2.0




```python
s1.mean()
# s1은 series이므로 nan 제외하고 계산
```




    2.6666666666666665




```python
s1.value_counts()
# 각 원소들에 대해 동일값의 원소끼리 그룹핑하여 개수를 세서 반환하는 함수
# 빈도수(히스토그램에서 사용)
```




    1.0    5
    2.0    4
    3.0    2
    5.0    2
    4.0    1
    7.0    1
    dtype: int64




```python
s1.isnull().sum()  
```




    1



### 날짜 자동 생성 : data_range


```python
# 날짜 인덱스를 이용해 시리즈 만들기
index_date = ['2018-10-07','2018-10-08','2018-10-09','2018-10-10']
s4 = pd.Series([200,196,np.NaN,500],index = index_date)
s4
```




    2018-10-07    200.0
    2018-10-08    196.0
    2018-10-09      NaN
    2018-10-10    500.0
    dtype: float64




```python
type(s4.index[0])
```




    str



- 판다스 패키지의 date_range 함수 (날짜생성)
    - pd.date_range(start=None, end=None, periods=Npne,freq='D')
    - start : 시작날짜 / end : 끝날짜 / periods : 날짜 생성기간 / freq : 날짜 생성 주기
    - start는 필수 옵션
    - end나 periods는 둘 중 하나가 있어야 함
    - freq는 기본 day로 설정


```python
pd.date_range(start='2023-01-30', end='2023-02-21')
# datetimeindex 반환
# dtype = 'datetime64[ns]'
```




    DatetimeIndex(['2023-01-30', '2023-01-31', '2023-02-01', '2023-02-02',
                   '2023-02-03', '2023-02-04', '2023-02-05', '2023-02-06',
                   '2023-02-07', '2023-02-08', '2023-02-09', '2023-02-10',
                   '2023-02-11', '2023-02-12', '2023-02-13', '2023-02-14',
                   '2023-02-15', '2023-02-16', '2023-02-17', '2023-02-18',
                   '2023-02-19', '2023-02-20', '2023-02-21'],
                  dtype='datetime64[ns]', freq='D')




```python
pd.date_range(start='2023-01-30', end='2023-02-21', freq='D')
# freq='D' : 기본 값
```




    DatetimeIndex(['2023-01-30', '2023-01-31', '2023-02-01', '2023-02-02',
                   '2023-02-03', '2023-02-04', '2023-02-05', '2023-02-06',
                   '2023-02-07', '2023-02-08', '2023-02-09', '2023-02-10',
                   '2023-02-11', '2023-02-12', '2023-02-13', '2023-02-14',
                   '2023-02-15', '2023-02-16', '2023-02-17', '2023-02-18',
                   '2023-02-19', '2023-02-20', '2023-02-21'],
                  dtype='datetime64[ns]', freq='D')




```python
pd.date_range(start='2023-01-30', end='2023-02-21', freq='3D')
# 3일씩 증가
```




    DatetimeIndex(['2023-01-30', '2023-02-02', '2023-02-05', '2023-02-08',
                   '2023-02-11', '2023-02-14', '2023-02-17', '2023-02-20'],
                  dtype='datetime64[ns]', freq='3D')




```python
pd.date_range(start='2023-01-30', end='2023-02-21', freq='W')
# 1주일씩 증가
# freq='W-SUN' : 1주 시작일 일요일을 표시
# 2023-01-30 : 월요일
```




    DatetimeIndex(['2023-02-05', '2023-02-12', '2023-02-19'], dtype='datetime64[ns]', freq='W-SUN')




```python
pd.date_range(start='2023-01-30', periods=4, freq='W')
# 1주일씩 증가
# 2023-01-30 이후 일요일 날짜 4개 생성
```




    DatetimeIndex(['2023-02-05', '2023-02-12', '2023-02-19', '2023-02-26'], dtype='datetime64[ns]', freq='W-SUN')




```python
pd.date_range(start='2023-01-30', periods=4, freq='M')
# 2023-01-30 이후 매달 마지막 날짜 4개 생성
```




    DatetimeIndex(['2023-01-31', '2023-02-28', '2023-03-31', '2023-04-30'], dtype='datetime64[ns]', freq='M')




```python
pd.date_range(start='2023-01-30', periods=4, freq='MS')
# 2023-01-30 이후 매달 1일 4개 생성
```




    DatetimeIndex(['2023-02-01', '2023-03-01', '2023-04-01', '2023-05-01'], dtype='datetime64[ns]', freq='MS')




```python
pd.date_range(start='2023-01-30', periods=4, freq='2BMS')
# (Buisness)업무일 기준 2개월 간격 매달 1일 4개 생성
```




    DatetimeIndex(['2023-02-01', '2023-04-03', '2023-06-01', '2023-08-01'], dtype='datetime64[ns]', freq='2BMS')




```python
pd.date_range(start='2023-01-30', periods=12, freq='2BM')
# (Buisness)업무일 기준 2개월 간격 마지막 날 주기
```




    DatetimeIndex(['2023-01-31', '2023-03-31', '2023-05-31', '2023-07-31',
                   '2023-09-29', '2023-11-30', '2024-01-31', '2024-03-29',
                   '2024-05-31', '2024-07-31', '2024-09-30', '2024-11-29'],
                  dtype='datetime64[ns]', freq='2BM')




```python
pd.date_range(start='2023-01-30', periods=4, freq='QS')
# 분기 시작일 기준
```




    DatetimeIndex(['2023-04-01', '2023-07-01', '2023-10-01', '2024-01-01'], dtype='datetime64[ns]', freq='QS-JAN')




```python
pd.date_range(start='2023-01-30', periods=4, freq='AS')
# 2023-01-30 이후 연도 시작일 4개 생성
```




    DatetimeIndex(['2024-01-01', '2025-01-01', '2026-01-01', '2027-01-01'], dtype='datetime64[ns]', freq='AS-JAN')



### pandas 패키지의 data_range 함수(시간생성)


```python
pd.date_range(start='2023-01-30 08:00', periods=10, freq='H')
```




    DatetimeIndex(['2023-01-30 08:00:00', '2023-01-30 09:00:00',
                   '2023-01-30 10:00:00', '2023-01-30 11:00:00',
                   '2023-01-30 12:00:00', '2023-01-30 13:00:00',
                   '2023-01-30 14:00:00', '2023-01-30 15:00:00',
                   '2023-01-30 16:00:00', '2023-01-30 17:00:00'],
                  dtype='datetime64[ns]', freq='H')




```python
pd.date_range(start='2023-01-30 08:00', periods=10, freq='BH')
# 업무시간 기준 9 to 5로 설정
```




    DatetimeIndex(['2023-01-30 09:00:00', '2023-01-30 10:00:00',
                   '2023-01-30 11:00:00', '2023-01-30 12:00:00',
                   '2023-01-30 13:00:00', '2023-01-30 14:00:00',
                   '2023-01-30 15:00:00', '2023-01-30 16:00:00',
                   '2023-01-31 09:00:00', '2023-01-31 10:00:00'],
                  dtype='datetime64[ns]', freq='BH')




```python
pd.date_range(start='2023-01-30 08:00', periods=10, freq='30min')
```




    DatetimeIndex(['2023-01-30 08:00:00', '2023-01-30 08:30:00',
                   '2023-01-30 09:00:00', '2023-01-30 09:30:00',
                   '2023-01-30 10:00:00', '2023-01-30 10:30:00',
                   '2023-01-30 11:00:00', '2023-01-30 11:30:00',
                   '2023-01-30 12:00:00', '2023-01-30 12:30:00'],
                  dtype='datetime64[ns]', freq='30T')




```python
pd.date_range(start='2023-01-30 08:00', periods=10, freq='10s')
```




    DatetimeIndex(['2023-01-30 08:00:00', '2023-01-30 08:00:10',
                   '2023-01-30 08:00:20', '2023-01-30 08:00:30',
                   '2023-01-30 08:00:40', '2023-01-30 08:00:50',
                   '2023-01-30 08:01:00', '2023-01-30 08:01:10',
                   '2023-01-30 08:01:20', '2023-01-30 08:01:30'],
                  dtype='datetime64[ns]', freq='10S')



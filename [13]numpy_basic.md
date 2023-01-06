## 파이썬 리스트 
: 가변형, 시퀀스 ( str, list, tuple) = [+,*,중첩,슬라이싱, 인덱싱], []
- 단점 : 동작 속도가 느리다. 콤마 요소 분리, 구별

### numpy : 수식 라이브러리, 수치연산, 배열객체
- 동작 속도가 빠르다. / 연속적인 메모리 / 한가지 타입만 처리가능

[도움말 array 링크](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html)


1) np.array 로 객체생성
2) np.arrage 로 객체생성

## ndarray(shape[, dtype, buffer, offset, ...])


```numpy
import numpy as np
a = np.array([0,1,2,3,4,5])
print(a)
print(type(a))
print(a.dtype) #a 객체가 가진 데이터 타입
```

```numpy
#결과
[0 1 2 3 4 5]
<class 'numpy.ndarray'>
int32
```

```numpy
print(dir(np.sctypeDict))
np.sctypeDict.keys()  #numpy에서 사용되는 데이터 타입
```

```numpy
#결과
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
dict_keys(['?', 0, 'byte', 'b', 1, 'ubyte', 'B', 2, 'short', 'h', 3, 'ushort', 'H', 4, 'i', 5, 'uint', 'I', 6, 'intp', 'p', 9, 'uintp', 'P', 10, 'long', 'l', 7, 'L', 8, 'longlong', 'q', 'ulonglong', 'Q', 'half', 'e', 23, 'f', 11, 'double', 'd', 12, 'longdouble', 'g', 13, 'cfloat', 'F', 14, 'cdouble', 'D', 15, 'clongdouble', 'G', 16, 'O', 17, 'S', 18, 'unicode', 'U', 19, 'void', 'V', 20, 'M', 21, 'm', 22, 'bool8', 'b1', 'int64', 'i8', 'uint64', 'u8', 'float16', 'f2', 'float32', 'f4', 'float64', 'f8', 'complex64', 'c8', 'complex128', 'c16', 'object0', 'bytes0', 'str0', 'void0', 'datetime64', 'M8', 'timedelta64', 'm8', 'Bytes0', 'Datetime64', 'Str0', 'Uint64', 'int32', 'i4', 'uint32', 'u4', 'int16', 'i2', 'uint16', 'u2', 'int8', 'i1', 'uint8', 'u1', 'complex_', 'int0', 'uint0', 'single', 'csingle', 'singlecomplex', 'float_', 'intc', 'uintc', 'int_', 'longfloat', 'clongfloat', 'longcomplex', 'bool_', 'bytes_', 'string_', 'str_', 'unicode_', 'object_', 'int', 'float', 'complex', 'bool', 'object', 'str', 'bytes', 'a'])
```

```numpy

a = np.array([0.0,1.0,2.0,3.0,4.0,5.0])  # = ndarray
```
```numpy
#결과
[0. 1. 2. 3. 4. 5.]
<class 'numpy.ndarray'>
float64
```

```numpy
print(a)
print(type(a))
print(a.dtype) #a 객체가 가진 데이터 타입    
#0,1 = bit * 8 = 1byte = 주소가 생성 = -128 ~127
```

```numpy
- 주소 생성 -> 메모리 할당 -> 값 대입
- 불리언 bool(1) . byte(1)
- 정수형 short(2)  -> int32(4) -> int64(8) -> long(8) ~ 16
- 실수형 float(4) -> 'float32', 'f4' -> float(8) -> double(8)
- 문자와 문자열 -> str
- 하나의 데이터 타입만 가져와서 저장해야함
- ex) 'int32' = 정수형 32bit, 'i4' = 정수형 4byte
- float64 = f8(=8*8) = 실수형 64bit = 실수형 8byte
```
```numpy
a = np.arange(10) #0~9   # ,를 구분하지 않는다.
print(a)
print(type(a))
a = [1,2,3,4,5]
a

```
```numpy
#결과
[0 1 2 3 4 5 6 7 8 9]
<class 'numpy.ndarray'>
```

### 3) ndarray(shape[, dtype, buffer, offset, ...]) / shape   

3-1) : 차원 (Rank, Dimension)을 []로 갯수를 늘린다.    
[[[a]]] = 3차원 [[b]] = 2차원

아벨(수학자) 4차원이상 -> 컴

대상 -> 특징추출(x_독립변수, y_종속변수) -> 도메인 -> 설명(통계_R/python) -> 예측(ML) -> ML + AI = DL (CNN을 기점으로 이미지 영상 프로세싱)

3-2) : 차원의 종류

1차원 : shape(x,)   
2차원 : shape(x,y), 행렬(matrix)   
3차원 : shape(x,y,z), (행,열,면) -> (면,행,렬)   
...n차원 : (x,y,z,,,,,,,,,,)   

```numpy
# 1차원 : shape(x,)
a= np.arange(12)
print(a)
print(a.shape) #1열 12행
t = a.shape
print(type(t))
print(a.shape[0])
```

```numpy
#결과
[ 0  1  2  3  4  5  6  7  8  9 10 11]
(12,)
<class 'tuple'>
12
```

```numpy
# 2차원 배열의 shape: 행(row, 수직(이미지연산), axis = 0)과 열(column, 수평(이미지연산),axis = 1)
m = np.array([[0,1,2],
              [0,1,2]])
​
print(m)
print(m.shape)   #2열 3행
print(m.shape[0],m.shape[1])
```

```numpy
#결과
[[0 1 2]
 [0 1 2]]
(2, 3)
2 3
```

```numpy
# 3차원 배열의 shape : (면,행,렬)
m = np.array([[ [0,1,2],
               [3,4,5]],
             [[0,1,2],
              [3,4,5] ]])
print(m)
print(m.shape)
print(m.shape[0],m.shape[1],m.shape[2])
```

```numpy
#결과
[[[0 1 2]
  [3 4 5]]

 [[0 1 2]
  [3 4 5]]]
(2, 2, 3)
2 2 3
```

## 4) 배열과 슬라이싱 _reshape()

```numpy
# 2차원 배열 인덱싱 슬라이싱
a = np.arange(12).reshape(3,4)  #[0,1,2,3,4,5,6,7,8,9,10,11]를 3행 4열로 만들기
print(a)
print(a.shape)
```

```numpy
#결과
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
(3, 4)
```

```numpy
#a가 가진 값을 리턴해보자 = 인덱싱
print(a[0][0])
print(a[0,0])
print(a[2][1])
print(a[2][3], a[2,3])
```
```numpy
#결과
0
0
9
11 11
```

```numpy
#a가 가진 값 슬라이싱
# [0 1 2 3]
print(a[0])
print(a[0, :])  # [행, 열]
​
print(a[:, :-1]) #마지막 열을 제외하겠다.
print(a[:, 1:]) #첫번째 열을 제외하겠다.
​
print('슬라이싱으로 전체 출력 형식을 만들자. ')
print(a[:, :])
print(a[0:, 0:])
```

```numpy
#결과
[0 1 2 3]
[0 1 2 3]
[[ 0  1  2]
 [ 4  5  6]
 [ 8  9 10]]
[[ 1  2  3]
 [ 5  6  7]
 [ 9 10 11]]
슬라이싱으로 전체 출력 형식을 만들자. 
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
```

```numpy
# 0행의 모든 데이터를 20으로 변경 후 전체 출력해보자.
​
a[0] = 20
print(a[:,:])
print(a[::2,::2]) # [start: end-1 :stop]
#슬라이싱 요소 전체의 값을 변경해보자.
print(a[:,:])
print(a[::2,::3])
a[::2,::3] = 0
print(a[:,:])
​
a[:,:] = -1
print(a[:,:])
​
#3차원 배열 인덱싱 슬라이싱
a = np.arange(12).reshape(2,2,3)
print(a,a.shape)
#인덱싱
print(a[0][0][0])
print(a[0,0,0])
​
#5
print(a[0,1,2])
#3
print(a[0,1,0])
​
#슬라이싱
print(a[:,:,:])
print('----------------')
print(a[:,1:,:1])
#case 1: 3차원
# 6 7
print('----------------')
print(a[1:,:-1,:2])
print('----------------')
print(a[-1:,1:,1:])
print('----------------')
print(a[1:,-1:,:2])
print(a[:1,1:,1:])
​
# 4 5
print('----------------')
print(a[-1:,1:,1:])
​
​
#case 2 : 1차원
print('----------------')
print(a[1,0:,:2])
print(a[0,1,1:])
​
#case 3 : 3차원
print('----------------')
print(a[1:,:1,:2])
print(a[:1,1:,1:])
​
#case 4 : 2차원
print('----------------')
print(a[1,:-1,:-1])
print(a[0,1:,1:])
5) 불린인덱싱 : 조건식을 이용한 인덱싱, 조건 검색 필터를 사용한 추출값 (중요 !!!)
a= np.array([1,2,3,4,5,6])
print(a)
print(a>2)
#배열의 객체 a에서 2보다 큰 값을 배열로 리턴
print(a[a>2]) # 이미지 -> 빨간사과(대체-보정작업) -> 이상값(노이즈) 추출해서 변경하고 싶다.
bool_index = np.array([True, True,  True,  True,  True,  True])
print(bool_index)
print(a[bool_index])
# 배열 a에서 3이 아닌 요소를 추출
# 2보다 크고 6보다 작은 요소를 추출 and
# 짝수만 추출
# 평균(mean)보다 작은값을 추출해보자.
​
#bool_index = np.array([True, True,  False,  True,  True,  True])
#print(a[bool_index])
print(a[a!=3])
​
print(a[(a>2) & (a<6)])
​
print(a[a % 2 == 0])
​
print(a[a < a.mean()], a.mean())
# flatten() : 다차원 배열을 1차원으로 만든다.
a = np.arange(12).reshape(3,4)
print(a,a.shape)
​
f = a.flatten()
print(f,f.shape)
# 데이터 순서를 거꾸로 변경
print(a[::-1])
print('-'*20)
print(a[:,::-1])
print('-'*20)
print(a[::-1,::-1])
# transpose() : 전치 행렬, 행과 열을 서로 맞바꾸는 함수
t = a.transpose()
print(t,t.shape)  # (3,4)   -> (4,3)  , (x,y)   -> (y,x)  
print(a.T)       # transpose()함수와 동일한 결과
#print(dir(a.T))
a.flat = 0  #임시로 변경 후 값을 0으로 대입받고 차원을 다시 리턴한다.
print(a)
a.flat = 255  
print(a)
6) numpy의 속성 (Attribute) : 멤버변수, 메서드

shape,dtype,ndim,flat,T,size,nbytes

d = np.arange(12).reshape(3,4)
print(d,d.shape)
print(d.dtype)  # int32 or int64
print(d.ndim)   # 2차원  ==> print(len(d.shape)) 와 동일
print(d.T)      # transpose()함수와 동일한 결과, 전치행렬
print(d.size)   # 12개 , 요소의 갯수
print(d.nbytes) # 48 bytes : 32bit(4 byte) * 12 
d.flat = 1
print(d)
​
a = np.arange(12).reshape(3,4)
print(a,a.shape)
​
print(a.max(),np.max(a))  # 최댓값
print(a.min(),np.min(a))  # 최소값
print(a.sum()) #합
print(a.mean()) #평균
​
print(a.std()) #표준편차
print(a.var()) #분산
print(np.median(a)) #중위수 : 
​
#사분위수
print('25%:', np.percentile(a,25))
print('50%:', np.percentile(a,50))
print('75%:', np.percentile(a,75))


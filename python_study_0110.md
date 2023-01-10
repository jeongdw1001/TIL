>## 1. 파이썬 언어 특징     

   - 대화식 인터프리터 언어
   - 동적 자료형을 지원
   - 플랫폼에 독립적인 언어
   - 개발 기간 단축에 초점을 맞춘 언어
   - 간단하고 쉬운 문법(들여쓰기, 재사용 가능한 코드)
   - 고수준의 자료형 제공 (리스트 list, 사전 dict, 문자열 string, 튜플 tuple, 셋 set)
   - 자동으로 관리되는 메모리(메모리 자동 할당, 사용 후 자동 해제)
   - 팀 단위 작업에 유용한 언어(모듈 단위의 코드)
   - 쉬운 유지 보수
   - 수많은 라이브러리 제공
   - 짧아지는 코드
     - 일급 함수 
       - 함수 객체를 변수에 저장할 수 있음
       - 함수에서 반환 값으로 사용
       - 함수에 인수로 전달할 수 있는 함수
   - 높은 확장성
   - 확장 및 내장
  
  ### 1) 파이썬 사용 적합 분야
   - gui, 웹 프로그램(Django), 네트워크 프로그램, DB, 텍스트 처리, 수치 연산(numpy, matlab), 병렬 연산
  
  ### 2) 파이썬 인터프리터 종류
   - Cpython, Jython, IronPython, pypy 등
  

  >## 2. 파이썬 패키지
  - 모듈, 패키지, 프로젝트의 관계 
    - 파이썬은 디렉토리에 __init__.py 파일이 존재하면 이를 패키지라 여긴다.
    - 패키지로부터 모듈을 사용하기 위한 파이썬 키워드 from / import
    -> from [package name] import [module name]
    - 외부에서 패키지를 참조하는 시점에 해당 패키지의 __init__.py 파일이 실행된다

>## 3. Python 프로그램 구조
### 1) 변수
- 유니 코드 문자나 밑줄로 시작해야 한다.
- 이름에 공백 불가
- 아스키 코드의 특수 문자는 사용 불가
- 예약어 불가
- 파이썬 전체 예약어 알아내기 코드
  ```python
  import keyword
  keyword.kwlist  
  len(keyword.kwlist)  #35개
  ```
  ```python
  # 파이썬 전체 예약어
  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
  ```
  ### 2) 포맷팅
  | type   | 설명   |  
  | ------ | ------ | 
  | %s     | 문자열 |
  | %c     | 문자 1개 | 
  | %d     | 정수 | 
  | %f     | 부동 소수 | 

```python
>>> import pprint
>>> numbers = [[1,2,3],[4,5],[6,7,8,9]]
>>> print(numbers)
[[1, 2, 3], [4, 5], [6, 7, 8, 9]]

>>> print(*numbers)
[1, 2, 3] [4, 5] [6, 7, 8, 9]

>>> print(*numbers, sep = '\n')
[1, 2, 3]
[4, 5]
[6, 7, 8, 9]

>>> pprint.pprint(numbers)
[[1, 2, 3], [4, 5], [6, 7, 8, 9]]

>>> pprint.pprint(numbers, width = 20)
[[1, 2, 3],
 [4, 5],
 [6, 7, 8, 9]]

>>> pprint.pprint(numbers, width = 20, indent = 4)
[   [1, 2, 3],
    [4, 5],
    [6, 7, 8, 9]]
```


### 3) 데이터 저장 방법에 따른 자료형 분류
| 자료형   | 설명   |  예시   |
| ---   | ---   |  ---   |
| direct 형   | 직접 데이터를 표현하는 자료형, 숫자형이 속함   |  int, float, complex   |
| sequence 형 | 다른 데이터를 포함하는 자료형, 순서가 있는 집합 자료형   |  list, str, tuple, bytes, range   |
| mapping 형   | 다른 데이터를 포함하는 자료형   |  dict   |
| set 형   | 순서가 없고, 중복된 항복도 없다.   |  set   |


### 4) 변경 가능성에 따른 자료형 분류
| 자료형 | 설명   |  예시   |
| ---   | ---   |  ---   |
| 변경 가능형(Mutable)  | 데이터의 값을 변경할 수 있다.   |  list, dict, set, array   |
| 변경 불가능형(Immutable) | 데이터의 값을 변경할 수 없다.   |  int, str, float, complex, tuple   |

>## 4. Python bool/bytes/숫자형
### 1) bool
- bool는 참이나 거짓을 나타내는 True와 False 두 상수를 갖는다.
- bool 값은 정수로 간주되어 True는 1, False는 0으로 간주한다.
- 식에서 bool 값을 알고 싶으면 bool()를 사용하며, bool 식은 주로 if문이나 while문에서 사용한다.

### 2) bytes
- bytes는 0 ~ 255 사이 코드의 열이다. 
- bytes 상수 선언은 b로 시작한다.
- 문자열은 유니코드를 기본으로 한다
- bytes는 1byte로 표현되는 문자만 가능
- bytes를 문자열로 변환하려면 decode() 사용
- 문자열을 bytes로 변경하려면 encode() 사용
- 기본값으로 UTF-8을 사용
- 직접 인코딩을 지정할 수 있다.
- 변경이 가능한 bytes를 원하면 bytearray 자료형을 사용한다.

### 3) 숫자형
- 정수형 상수는 10진수와 2진수, 8진수, 16진수 상수
- 10진 정수를 2/8/16진수로 변환 
```python
>>> bin( 23 ) # 10진수를 2진수로 변환 
>>> oct( 23 ) # 10진수를 8진수로 변환
>>> hex( 23 ) # 10진수를 16진수로 변환
```
```python
#결과
'0b10111'
'0o27'
'0x17'
```

- 실수형인 경우는 정수로 오차 없이 표현할 수 있는 값인지를 is_integer()를 사용하여 확인할 수 있다.
- 실수를 정수로 변환하는 또 다른 방법은 반올림(Round), 올림(Ceil), 내림(Floor)를 사용하는 것이다.
- 파이썬 기본 산술 연산자: +(덧셈), -(뺄셈), *(곱셈), /(나눗셈), //(몫), **(지수), %(나머지)

## * 논리 연산자
| 논리 연산자 
(우선순위순) | 설명  |
| ---   | ---   | 
| not x  | x가 거짓이면 True, 아니면 False  |
| x and y  | x가 거짓이면 x, 아니면 y   |
| x or y   | x가 참이면 x, 아니면 y   |

## * 내장 수치 연산 함수
| 함수 | 설명  |
| ---   | ---   | 
| abs(x) | x의 절대값  |
| int(x) | x를 정수형으로 변환 |
| float(x) | x를 실수형으로 변환 |
| complex(x) | 실수부 re와 허수부 im을 가지는 복소수를 구함 |
| pow(x,y) | x의 y승을 구함 |
| max( iterable ), min( iterable ) | 최대값과 최소값을 구함 |
| sum(iterable) | 합을 계산 |
| divmod( x, y ) | ( x // y, x % y ) 쌍을 구함|

> ## 5. Python 문자열
- 인덱싱(indexing)은 순서가 있는 데이터에서 index로 하나의 객체를 참조하는 것이며, index는 정수이며 0부터 시작한다. 
  - [ k ] 형식, k번 위치의 값 하나를 취한다.
- 슬라이싱(Slicing)은 시퀀스 자료형의 일정 영역에서 새로운 객체를 반환하며, 결과의 자료형은 원래의 자료형과 같다.
  - [ 시작오프셋 : 끝오프셋 ]
  - [ s : t : p ] 형식
  - s부터 t사이 구간의 값을 p 간격으로 취한다.
- 오프셋은 생략할 수 있으며, 시작 오프셋을 생략하면 0, 끝 오프셋을 생략하면 마지막 값으로 처리한다.

### 1) 문자열 연산
- 문자열은 그 자체 값을 변경할 수 없는 변경 불가능 자료형이다.
```python
# format()를 사용한 서식 지정_하나씩 지정하는것 권장
>>> int_val = 23; float_val = 2.34567
>>> print( format( int_val, '3d' ), 'any value', format( float_val, '.2f' ) )

23 any value 2.35
```

```python
>>> s = 'i like programming. i like swimming'

>>> s.upper()   # 대문자로 변환
'I LIKE PROGRAMMING. I LIKE SWIMMING'

>>> s.lower()   # 소문자로 변환
'i like programming. i like swimming'

>>> 'i like programming.'.swapcase()
'I LIKE PROGRAMMING.'

>>> s.capitalize()  # 첫 문자를 대문자로 변환
'I like programming. i like swimming'

>>> s.title()
'I Like Programming. I Like Swimming'

>>> s.count('like') # 부분 문자 발생 횟수
2

>>> s.find('like')  # 검색
2

>>> s.find('like',3)
22

>>> s.find('my')
-1

>>> s.rfind('like') # 역순 검색
22

>>> s.index('like')
2

>>> s.index('my')   # find()와 동일, 없을 경우 예외 발생
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

>>> s.rindex('like')
22

>>> s.startswith('i like')  # ‘i like’로 시작하는 문자열인가?
True

>>> s.split() # 공백으로 분리
['i', 'like', 'programming.', 'i', 'like', 'swimming']
```
### 2) Python 리스트
```python
# 리스트의 일부 값 변경
>>> a = [ 'spam', 'eggs', 100, 1234 ]
>>> a[2] = a[2] + 23;
>>> a
['spam', 'eggs', 123, 1234]

# 리스트의 일부 값 치환
>>> a[ 0:2 ] = [ 1, 12 ];
>>> a
[1, 12, 123, 1234]
```


- 리스트 메서드
  
|메서드|설명|
|---|---|
|append|데이터를 리스트 끝에 추가(스택의 push) 한다.|
|insert|데이터를 지정한 위치에 삽입한다.|
|index|요소를 검색한다.
|count|요소의 개수를 알아낸다.
|sort|리스트를 정렬한다.
|reverse|리스트의 순서를 바꾼다.
|remove|리스트의 지정한 값 하나를 삭제한다.
|pop|리스트의 지정한 값 하나를 읽어 내고 삭제(스택의 Pop) 한다.
|extend|리스트를 추가한다.


- 순차적인 정수 리스트를 만들 때 range() 함수 사용

```python
# 리스트 내장 형식
[ <식> for <타깃1> in <객체1>
       …
       for <타깃n> in <객체n> 
       ( if <조건식> ) ]
```
### 3) Python 튜플
- 튜플(tuple)은 임의의 객체들이 순서를 가지는 모음으로 리스트와 유사한 면이 많다. 
- 차이점은 변경 불가능한 자료형이라는 것이다.
- 튜플은 시퀀스 자료형이므로 시퀀스 자료형의 특성을 모두 가진다.











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

```python
>>> t = ( 1, 2, 3 )
>>> t
(1, 2, 3)

>>> t * 2                       # 반복하기
(1, 2, 3, 1, 2, 3)

>>> t + ( 'apple', 'banana' )   # 연결하기
(1, 2, 3, 'apple', 'banana')
>>> print( t[ 0 ], t[ 1:3 ] )   # 인덱싱과 슬라이싱
1 (2, 3)
>>> len(t)                      # 길이 정보
3
>>> 1 in t                      # 멤버 검사
True
>>> t[0] = 100                  #error
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```
```python
# 튜플은 검색에 관련된 메서드 두 개를 제공
>>> t.count( 2 )        # 2가 몇 개 있는가? 
>>> t.index( 2 )    # 첫 번째 2의 위치는?
>>> t.index( 2, 1 ) # 1 위치부터 검색
```
 
- 패킹과 언패킹
  - 한 데이터에 여러 개의 데이터를 넣는 것을 패킹(Packing)이라 한다.
  - 패킹과 반대로 한 데이터에서 데이터를 각각 꺼내 오는 것을 언패킹(Unpacking)이라 한다.

- 리스트와의 차이점
  - 리스트와의 공통점은 임의의 객체를 저장할 수 있다는 것과 시퀀스 자료형이라는 것이다.
  -  리스트와의 차이점은 변경 불가능한 시퀀스 자료형이고, 함수의 가변 인수를 지원한다.
  -  변경해야 할 데이터들은 리스트에, 변경하지 말아야 할 데이터는 튜플에 저장한다.
  -  리스트와 튜플은 list()와 tuple() 내장 함수를 사용하여 상호 변환할 수 있다.

- 튜플의 특별한 활용
1. 함수에 있어서 하나 이상의 값을 반환할 때 활용
```python
>>> def calc( a, b ):
# return앞은 반드시 tab으로 띄기
return a + b, a * b
>>> x, y = calc( 5, 4 ); print( x, y )
```
2. 튜플에 있는 값들을 함수의 인수로 사용할 때 활용
```python
>>> args = ( 4, 5 ) 
>>> calc( *args )
```
3. 파이썬 2 형식의 서식 문자열에 데이터를 공급할 때 활용
```python
>>> “%d %f %s” % ( 12, 3.456, ‘hello’ )
```

### 4) Python 집합
- 집합(Set)은 여러 값을 순서 없이 그리고 중복 없이 모아 놓은 자료형이다.
- 파이썬에서는 set과 frozenset 두 가지 집합 자료형을 제공한다.
- set은 변경 가능한 집합이고 frozenset은 변경 불가능한 집합이다.
- 원소 추가 : 
  - set 객체에 원소를 추가하는 메서드는 add()와 update()가 있다.
- add() 메서드는 한 원소를 추가하고, update() 메서드는 주어진 객체에 대한 합집합 연산을 한다.
- copy() 메서드를 사용하면 set 객체를 통째로 복사할 수 있다.
- 원소 제거 : 
  - set 객체에서 원소를 제거하는 메서드는 clear()와 discard(), pop(), remove()등이 있다.
- 집합 연산 : 
  - union(합집합), intersection(교집합), difference(차집합), symmetric_difference(대칭 차집합) 연산이 있다.
- 집합 내장 : 
  - {}를 이용하면 리스트 내장과 같이 for 문을 통해서 집합을 직접 만들 수 있다.
```python
>>> { v * v for v in [ 1, 2, 3, 4 ] }    # 연산 결과가 set 객체로 모인다. 
>>> { v for v in ‘python’ if v not in ‘aeiou’ }
```
### 5) Python 사전
- 사전(Dictionary)은 특정 키를 주면 이와 관련된 값을 돌려주는 내용 기반으로 검색하는 자료형이다.
- 사전은 임의 객체의 집합적 자료형인데, 데이터의 저장 순서가 없다. 
- 집합적이라는 의미에서 리스트와 튜플과 동일하다.
- 하지만, 데이터의 순서를 정할 수 없는 
매핑형이다.
- 시퀀스 자료형은 데이터의 순서를 정할 수 있어서 정수 오프셋에 의한 인덱싱이 가능하지만, 매핑형에서는 키(Key)를 이용한 값(Value)에 접근한다.
- 사전은 변경 가능한 자료형으로 값을 저장할 때도 키를 사용한다. 키가 사전에 등록되어 있지 않으면 새로운 항목으로 만들어지며, 키가 이미 사전에 등록되어 있으면 이 키에 해당하는 값이 변경된다.
- 값은 임의의 객체가 될 수 있지만, 키는 해시 기능이라 변경 불가능한 자료형이어 
야 한다.

- 객체의 심볼 테이블
  - 이름 공간(심볼이 저장되는 공간)을 가지는 모든 객체는 심볼 테이블을 갖는다.
    - 모듈과 함수, 클래스, 클래스 인스턴스, 함수 
  - 어떤 객체의 심볼 테이블은 ‘__dict__’ 속성을 확인해 보면 된다.


```python
# 모듈 내에서 자신의 모듈을 참조하는 방법
>>> import sys
>>> dir(sys)
['__breakpointhook__', '__displayhook__', '__doc__', '__excepthook__', '__interactivehook__', '__loader__', '__name__', '__package__', '__spec__', '__stderr__', '__stdin__', '__stdout__', '__unraisablehook__', '_base_executable', '_clear_type_cache', '_current_exceptions', '_current_frames', '_deactivate_opcache', '_debugmallocstats', '_enablelegacywindowsfsencoding', '_framework', '_getframe', '_git', '_home', '_xoptions', 'addaudithook', 'api_version', 'argv', 'audit', 'base_exec_prefix', 'base_prefix', 'breakpointhook', 'builtin_module_names', 'byteorder', 'call_tracing', 'copyright', 'displayhook', 'dllhandle', 'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', 'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_origin_tracking_depth', 'get_int_max_str_digits', 'getallocatedblocks', 'getdefaultencoding', 'getfilesystemencodeerrors', 'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', 'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', 'int_info', 'intern', 'is_finalizing', 'last_traceback', 'last_type', 'last_value', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'orig_argv', 'path', 'path_hooks', 'path_importer_cache', 'platform', 'platlibdir', 'prefix', 'ps1', 'ps2', 'pycache_prefix', 'set_asyncgen_hooks', 'set_coroutine_origin_tracking_depth', 'set_int_max_str_digits', 'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdlib_module_names', 'stdout', 'thread_info', 'unraisablehook', 'version', 'version_info', 'warnoptions', 'winver']

>>> dir(sys.modules)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

>>> current_module = sys.modules[__name__]
>>> a = 10

>>> getattr(current_module, 'a')
10

>>> current_module.__dict__['a']
10
```


```python
>>> int('64',16)    # 16진수 64를 10진수로 변환
100
>>> int('144',8)    # 8진수 144를 10진수로 변환
100
>>> int('101111',2) # 2진수 101111을 10진수로 변환
47
>>> hex(100)        # 10진수 100을 16진수 문자열로 변환 

'0x64'
>>> oct(100)        # 10진수 100을 8진수 문자열로 변환 
'0o144'
>>> bin(100)        # 10진수 100을 2진수 문자열로 변환
'0b1100100'
```

- decode : 바이트에서 변환
- encode : 바이트로 변환




*pvm
1. 실행 영역을 동적으로 할당한다.
2. 파이썬 모듈을 컴파일한다.
3. 프로세스가 끝나면 동적할당영역에 모든 선언된 객체 등 메모리를 차지하는 리소스들을 소거함
4. 플랫폼에 독립적이다.
5. 동적공간 20%

- DDL (Data Definition Language)
  - 객체의 생성, 변경, 삭제 명령어
  - create, alter, drop

- DML (Data Manipulation Language)
  - 레코드 제어 명령어 
  - select, insert, update, delete
  
- DCL (Data Control Language)
  - 객체 권한 부여 
  - commit, rollback, grant, revoke 

### => DDL은 데이터와 그 구조를 정의한다는 점이 있습니다. DML는 데이터의 검색, 수정, 삭제 등을 처리합니다. DCL은 데이터 베이스의 사용자 권한을 제어한다는 점에서 차이가 있습니다.


># 파이썬 모듈
## 1) 모듈
- 파이썬 모듈은 파이썬 프로그램 파일이나 C, Fortran 확장 파일로 프로 
그램과 데이터를 정의하고 있으며 client(어떤 모듈을 호출하는 측)가 모듈에 정의된 함수나 변수의 이름을 사용하도록 허용하는 것이다.
- 모듈 파일은 어떠한 코드로도 작성할 수 있다. 함수를 정의할 수 있고, 클래스를 정의할 수 있고 변수도 정의할 수 있다. 이렇게 정의된 내용은 다른 모듈에 의해서 호출되고 사용된다.
- 코드들을 한 단위로 묶어 사용할 수 있게 하는 하나의 단위
- 서로 연관된 작업을 하는 코드들의 모임
- 관리 가능하고 개념적으로 독립된 형태의 작은 단위로 작성 함으로써 코드 독립성을 유지하고 재사용성을 높일 수 있다.

## 2) 패키지
- 패키지(Package)는 모듈을 모아 놓은 단위
- 관련된 여러 개의 모듈 
을 계층적인 몇 개의 디렉터리로 분류해서 저장하고 계층화
- 각 디렉터리에는 __init__.py 파일이 반드시 있어야 한다.
- 이 파일이 없으면 해당 폴더 
는 파이썬 패키지로 간주하지 않는다.
- __init__.py 파일은 패키지를 초기화하는 어떠한 파이썬 코드도 포함할 수 있다.

># 파이썬 클래스
## 1) 클래스 인스턴스
- 클래스 인스턴스(Class Instance)는 클래스의 실제 객체
- 인스턴스 객체도 독 
자적인 이름 공간을 갖는다.
- 클래스는 하나 이상의 인스턴스 객체를 생성하는 자 
료형과 같다.
- 클래스는 상속(Inheritance)이 가능
- 상속받은 클래스(Subclass, 하위클래스) 
는 상속해 준 클래스(Superclass, 상위클래스)의 모든 속성을 자동으로 물려받는 
다.


## 2) 용어
- 클래스(Class) : class문으로 정의하며, 멤버와 메서드를 가지는 객체
- 클래스 객체(Class Object) : 클래스와 같은 의미로 사용
  - 클래스는 특정 대상을 
가리키지 않고 일반적으로 언급하기 위해서 사용하는 반면에, 클래스 객체는 어떤 클래스를 구체적으로 지정하기 위해 사용하기도 한다.
- 클래스 인스턴스(Class Instance) : 클래스를 호출하여 생성된 객체
- 멤버(Member) : 클래스 혹은 클래스 인스턴스 공간에 정의된 변수
- 메서드(Method) : 클래스 공간에 정의된 함수
- 속성(Attribute) : 멤버와 메서드 전체
- 다형성(Polymorphism) : 상속 관계 내의 다른 클래스의 인스턴스들이 같은 메서드 호출 
에 대해 각각 다르게 반응하도록 하는 기능이다.
- 다중 상속(Multiple Inheritance) : 두 개 이상의 상위 클래스로부터 상속받는 것




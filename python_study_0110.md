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




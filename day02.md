1) 4차산업혁명
   - Iot(사물인터넷)
   - Cloud(클라우드)
   - BigData(빅데이터)
   - Mobile(모바일)
   - AI
   - Brockchain(블록체인)
   - CloudComputing(클라우드컴퓨팅)
   - DataValue(데이터가치)


## 빅데이터 단계

### 1. 기획*** : 
- what? 무엇을 할지? 주제 선정 어려움
- how? 문서작업, 설계작업
말로 쓰고 -> 순서도 작성 -> 코딩
- 외부에 있는지, 내부에 있는지 등등 각 단계별 목적이나 목표를 미리 구상해야 함
(운영, 보정 등)
- insight?

### 2. 수집

### 3. 저장(Database)
-   RDBMS 가장 많이 사용 (관계형, 중복을 없애기 위함) 테이블을 먼저 만들고 데이터베이스를 넣어야 함 (중요한 데이터를 저장, 개런티 X, 안정성X , 유지보수 내가 해야 함)
o   Oracle (돈 주고 사야함)
o   MSSQL
o   SYBASE
o   DB2 (금융 쪽 생각한다면 공부해 볼 것)
o   SQLite
o   마리아DB
o   Etc.
-   NoSQL (날아가도 크게 문제없는 데이터, 안정성 떨어짐, 개런티 X, 오픈소스, 유지보수 해줌)
o   MongoDB (많이씀)
o   HBASE(하둡에서 쓰고 있는 데이터베이스)
   클라우드DB(
o   Lct4
o   ReSt
o   JSON
o   etc
만든 이유: 저장 & 검색
-   단순 저장이 아니기에 검색을 위해 잘 저장해야 함

Json은 {key:value}로 저장함
SQL (Structured Query Language)
-   데이터 처리 (RDBMS)
-   DDL: create, drop alter
-   DML: Select(검색) update(수정), delete(삭제), insert(삽입)
-   DCL: Control Language (권한을 주고 뺏고), grant, revoke, deny


### 4. 처리 - 빅데이터
- 전처리 (이미지, sns, ... 비정형 data > 수치화)
  - null값 처리 (Nan, '' 등) ***
  - 제거/ 대체/ 새로운 값 대체 (알고리즘 대체값)
  - tuple은 내용 수정이 불가
  - 스케일링
  - 0과1로 만들어 놓는 방법


### 5. 분석
- 통계 : 집단의 특징 확인 모여있는가/분산되어있는가
  - 중심화 경향치가 높은가, 낮은가 = 공통점
    - 평균, 중앙값, 최빈값
  - 산포도 = 차이점
    - 분산, 표준편차
  - 분포 :: Normal 분포, Student 분포, t-분포, f-분포, 표준화
  - 확인 :: 산술 연산(논리 연산)을 통한 확률 계산
  - 확률 변수를 통한 확인


### 6. 시각화
- 알고리즘이 다양한 것 중에 제일 좋은 코드 선정 후 모델링
- 데이터를 보고 다양한 생각을 해본 후에 본격 시각화를 위한 과정이 필요
- 그래프, 관점

### 7. 활용
- 보정 -> 유지보수
- DevOPS

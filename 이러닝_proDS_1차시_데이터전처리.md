## ProDS DS등급 필기2_1차시_데이터 전처리 : 데이터 생성, 데이터 정제

### 데이터 정제

- 이상값의 탐지
	- 표준화 점수(Z-score) : z1, z2, z3,,,, 
		- 언제나 평균값이 0이고, 표준편차가 1이 된다
		- 표준화 점수의 절대값이 2,3보다 큰 경우를 이상값으로 진단

- 이상값 처리 방법
	- 이상값 제외(trimming)
		- 처리는 간단하지만, 정보 손실이 발생하고 추정량 왜곡이 생길 수 있음.
	- 이상값 대체(winsorization)
		- 이상값을 정상값 중 최대 또는 최소 등으로 대체하는 방식
		- 분포 : 꼬리가 긴 형태에서 짧은 형태로 보완 가능
	- 변수 변환
		- 자료값 전체에 로그 변환, 제곱근 변환 등을 적용
		- 언제든 복구 가능

- 연속형 자료의 범주화
	- 변수구간화(binning)
		- 연속형 변수를 구간을 이용하여 범주화 하는 과정
	- 변수구간화의 효과
		- 이상치 문제를 완화
		- 결측치 처리 방법이 될 수 있음
		- 변수 간 관계가 단순화되어 분석시 과적합을 방지할 수 있고, 결과 해석이 용이해짐

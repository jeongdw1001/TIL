## 003_1 Get Method 실습

### 1. get 방식 데이터 통신(1)



```python
import urllib.request
from urllib.parse import urlparse
```


```python
# 기본요청1(encar)
url = "http://www.encar.com/"

mem = urllib.request.urlopen(url)
```


```python
# 여러 정보
print('type : {}'.format(type(mem)))
print('geturl : {}'.format(mem.geturl()))
print('status : {}'.format(mem.status))
print('headers : {}'.format(mem.getheaders()))
print('getcode : {}'.format(mem.getcode()))
print('read : {}'.format(mem.read(1).decode('utf-8')))
print('parse : {}'.format(urlparse('http://www.encar.co.kr?test=test')))
```

<pre>
type : <class 'http.client.HTTPResponse'>
geturl : http://www.encar.com/index.do
status : 200
headers : [('X-Encar-Web', 'P3'), ('Date', 'Wed, 18 Jan 2023 04:27:56 GMT'), ('Set-Cookie', 'WMONID=-5OUN9wiVFD; Expires=Thu, 18-Jan-2024 13:27:56 GMT; Path=/'), ('Content-Type', 'text/html; charset=EUC-KR'), ('Connection', 'close'), ('Content-Language', 'ko-KR'), ('Set-Cookie', 'JSESSIONID=Z8DatKO4kamL9Fa5cONgQ8a3JTM9d10B3kTjOgfCK5JmZajHb4bt1jnqM1MIfuVD.mono-was3-prod_servlet_encarWeb7;Path=/'), ('P3P', "CP='CAO PSA CONi OTR OUR DEM ONL'"), ('X-UA-Compatible', 'IE=Edge'), ('X-Encar-WAS', 'W7'), ('Transfer-Encoding', 'chunked')]
getcode : 200
read : 

parse : ParseResult(scheme='http', netloc='www.encar.co.kr', path='', params='', query='test=test', fragment='')
</pre>

```python
# 기본요청2(ipify)
API = "https://api.ipify.org"
API
```

<pre>
'https://api.ipify.org'
</pre>

```python
# get 방식 parameter
values = {
    'format':'json'
}
```


```python
print('before param : {}'.format(values))
params = urllib.parse.urlencode(values) #{'format': 'json'}을 파싱
print('after param : {}'.format(params)) #format=json로 변환
```

<pre>
before param : {'format': 'json'}
after param : format=json
</pre>

```python
# 요청 URL 생성
url = API + "?" + params
print("요청 url = {}".format(url))
```

<pre>
요청 url = https://api.ipify.org?format=json
</pre>

```python
# 수신 데이터 읽기
data = urllib.request.urlopen(url).read()
```


```python
# 수신 데이터 디코딩
text = data.decode("utf-8")
print('response : {}'.format(text))
```

<pre>
response : {"ip":"211.178.245.5"}
</pre>
## 003_2 Get Method RSS_실습

### 2. get 방식 데이터 통신(2) _RSS



```python
import urllib.request
import urllib.parse
```


```python
# 행정안전부 : https://www.mois.go.kr
# 행정안전부 RSS API URL
API = "http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp"
```


```python
params = []
```


```python
for num in [1001, 1012, 1013, 1014]:
    params.append(dict(ctxCd=num))
```


```python
# 연속해서 4회 요청
for c in params:
    # 파라미터 출력
    # print(c)
    # URL 인코딩
    param = urllib.parse.urlencode(c)
    # URL 완성
    url = API + "?" + param
    # URL 출력
    print("url=", url)
    # 요청
    res_data = urllib.request.urlopen(url).read()
    # 수신 후 디코딩
    contents = res_data.decode("utf-8")
    #print(contents)
```

<pre>
url= http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1001
url= http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1012
url= http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1013
url= http://www.mois.go.kr/gpms/view/jsp/rss/rss.jsp?ctxCd=1014
</pre>
## 003_3 Request URL_실습

### 다음 주식 정보 가져오기



```python
!pip install fake-useragent
```

<pre>
Requirement already satisfied: fake-useragent in c:\anaconda3\lib\site-packages (1.1.1)
Requirement already satisfied: importlib-resources>=5.0 in c:\anaconda3\lib\site-packages (from fake-useragent) (5.10.2)
Requirement already satisfied: zipp>=3.1.0 in c:\anaconda3\lib\site-packages (from importlib-resources>=5.0->fake-useragent) (3.7.0)
</pre>

```python
import json
import urllib.request as req
from fake_useragent import UserAgent
```


```python
# Fake Header 정보(가상으로 User-Agent 생성)
ua = UserAgent()
```


```python
# 헤더 선언
headers = { 
    'User-Agent': ua.ie,
    'referer':'https://finance.daum.net/'
}
```


```python
# 다음 주식 요청 URL
url = "https://finance.daum.net/api/search/ranks?limit=10"
```


```python
# 요청
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')
```


```python
# 응답 데이터 확인(Json Data)
#print('res',res)
```


```python
# 응답 데이터 str -> json 변환 및 data 값 저장
rank_json = json.loads(res)['data']
```


```python
# 중간 확인
print('중간 확인 : ', rank_json, '\n')
```

<pre>
중간 확인 :  [{'rank': 1, 'rankChange': 0, 'symbolCode': 'A005930', 'code': 'KR7005930003', 'name': '삼성전자', 'tradePrice': 60100, 'change': 'FALL', 'changePrice': 900, 'changeRate': 0.0147540984, 'chartSlideImage': None, 'isNew': False}, {'rank': 2, 'rankChange': 0, 'symbolCode': 'A035720', 'code': 'KR7035720002', 'name': '카카오', 'tradePrice': 61900, 'change': 'RISE', 'changePrice': 100, 'changeRate': 0.001618123, 'chartSlideImage': None, 'isNew': False}, {'rank': 3, 'rankChange': 2, 'symbolCode': 'A090710', 'code': 'KR7090710005', 'name': '휴림로봇', 'tradePrice': 2710, 'change': 'RISE', 'changePrice': 25, 'changeRate': 0.009310987, 'chartSlideImage': None, 'isNew': False}, {'rank': 4, 'rankChange': -1, 'symbolCode': 'A277810', 'code': 'KR7277810008', 'name': '레인보우로보틱스', 'tradePrice': 64300, 'change': 'RISE', 'changePrice': 1100, 'changeRate': 0.0174050633, 'chartSlideImage': None, 'isNew': False}, {'rank': 5, 'rankChange': -1, 'symbolCode': 'A108860', 'code': 'KR7108860008', 'name': '셀바스AI', 'tradePrice': 11250, 'change': 'RISE', 'changePrice': 2430, 'changeRate': 0.2755102041, 'chartSlideImage': None, 'isNew': False}, {'rank': 6, 'rankChange': 0, 'symbolCode': 'A096300', 'code': 'KR7096300009', 'name': '베트남개발1', 'tradePrice': 231, 'change': 'RISE', 'changePrice': 22, 'changeRate': 0.1052631579, 'chartSlideImage': None, 'isNew': True}, {'rank': 7, 'rankChange': 0, 'symbolCode': 'A323410', 'code': 'KR7323410001', 'name': '카카오뱅크', 'tradePrice': 27750, 'change': 'FALL', 'changePrice': 700, 'changeRate': 0.0246045694, 'chartSlideImage': None, 'isNew': False}, {'rank': 8, 'rankChange': 1, 'symbolCode': 'A001440', 'code': 'KR7001440007', 'name': '대한전선', 'tradePrice': 1550, 'change': 'FALL', 'changePrice': 20, 'changeRate': 0.0127388535, 'chartSlideImage': None, 'isNew': False}, {'rank': 9, 'rankChange': 0, 'symbolCode': 'A066570', 'code': 'KR7066570003', 'name': 'LG전자', 'tradePrice': 94900, 'change': 'RISE', 'changePrice': 200, 'changeRate': 0.0021119324, 'chartSlideImage': None, 'isNew': True}, {'rank': 10, 'rankChange': 0, 'symbolCode': 'A034020', 'code': 'KR7034020008', 'name': '두산에너빌리티', 'tradePrice': 15950, 'change': 'FALL', 'changePrice': 350, 'changeRate': 0.0214723926, 'chartSlideImage': None, 'isNew': False}] 

</pre>

```python
for elm in rank_json:
    # print(type(elm)) #Type 확인
    print('순위 : {}, 금액 : {}, 회사명 : {}'.format(elm['rank'], elm['tradePrice'], elm['name']))
```

<pre>
순위 : 1, 금액 : 60100, 회사명 : 삼성전자
순위 : 2, 금액 : 61900, 회사명 : 카카오
순위 : 3, 금액 : 2710, 회사명 : 휴림로봇
순위 : 4, 금액 : 64300, 회사명 : 레인보우로보틱스
순위 : 5, 금액 : 11250, 회사명 : 셀바스AI
순위 : 6, 금액 : 231, 회사명 : 베트남개발1
순위 : 7, 금액 : 27750, 회사명 : 카카오뱅크
순위 : 8, 금액 : 1550, 회사명 : 대한전선
순위 : 9, 금액 : 94900, 회사명 : LG전자
순위 : 10, 금액 : 15950, 회사명 : 두산에너빌리티
</pre>
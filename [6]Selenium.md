
```python
# 패키지 호출
!pip install selenium
```

<pre>
Requirement already satisfied: selenium in c:\anaconda3\lib\site-packages (4.7.2)
Requirement already satisfied: trio~=0.17 in c:\anaconda3\lib\site-packages (from selenium) (0.22.0)
Requirement already satisfied: trio-websocket~=0.9 in c:\anaconda3\lib\site-packages (from selenium) (0.9.2)
Requirement already satisfied: certifi>=2021.10.8 in c:\anaconda3\lib\site-packages (from selenium) (2021.10.8)
Requirement already satisfied: urllib3[socks]~=1.26 in c:\anaconda3\lib\site-packages (from selenium) (1.26.9)
Requirement already satisfied: outcome in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (1.2.0)
Requirement already satisfied: attrs>=19.2.0 in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (21.4.0)
Requirement already satisfied: cffi>=1.14 in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (1.15.0)
Requirement already satisfied: exceptiongroup>=1.0.0rc9 in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (1.1.0)
Requirement already satisfied: idna in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (3.3)
Requirement already satisfied: sortedcontainers in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (2.4.0)
Requirement already satisfied: async-generator>=1.9 in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (1.10)
Requirement already satisfied: sniffio in c:\anaconda3\lib\site-packages (from trio~=0.17->selenium) (1.2.0)
Requirement already satisfied: pycparser in c:\anaconda3\lib\site-packages (from cffi>=1.14->trio~=0.17->selenium) (2.21)
Requirement already satisfied: wsproto>=0.14 in c:\anaconda3\lib\site-packages (from trio-websocket~=0.9->selenium) (1.2.0)
Requirement already satisfied: PySocks!=1.5.7,<2.0,>=1.5.6 in c:\anaconda3\lib\site-packages (from urllib3[socks]~=1.26->selenium) (1.7.1)
Requirement already satisfied: h11<1,>=0.9.0 in c:\anaconda3\lib\site-packages (from wsproto>=0.14->trio-websocket~=0.9->selenium) (0.14.0)
</pre>

```python
from selenium import webdriver
```

### 브라우저 열기 : 방법 1) 

- 직접 드라이버의 경로를 지정하여 실행



```python
driver = webdriver.Chrome("C:\Myexam\chromedriver/chromedriver.exe")
```

<pre>
C:\Users\user\AppData\Local\Temp\ipykernel_19108\1014152672.py:1: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome("C:\Myexam\chromedriver/chromedriver.exe")
</pre>
### 브라우저 열기 : 방법 2) 

- 환경 변수 설정이 되어 있는 상태에서 실행

- 드라이버 파일이 같은 디렉토리에 있는 경우에 실행



```python
#driver = webdriver.Chrome()
```

## 2. Selenium의 기본 사용법

1. 셀레니움이란?

2. 웹 드라이버 객체 만들기 및 페이지 이동

3. 윈도우 사이즈 조절

4. 브라우져 스크롤 이동

5. Alert 다루기

6. 입력창에 문자열 입력하기

7. 버튼 클릭하기

8. 텍스트 데이터 가져오기

9. 속성 데이터 가져오기

10. 윈도우 및 브라우져 종료하기


### 2-1. 셀레니움이란?

- 셀레니움은 브라우져를 자동화하는 툴로 테스팅을 목적으로 웹 어플리케이션을 자동화 하는 목적으로 만들어졌지만, 테스팅에 국한돼서 사용 되지는 않음. 

- 웹 기반의 작업들을 자동화하여 업무 효율성을 높일 수 있으며 다양한 언어와 다양한 브라우져를 지원


### 2-2. 웹 드라이버 객체 만들기 및 페이지 이동

- driver의 get 함수를 이용하여 크롬 브라우저에서 페이지를 이동할 수 있습니다.

- 아래의 코드는 naver 웹 페이지로 이동합니다.

- url은 http를 꼭 포함해야 합니다.



```python
driver.get("https://www.naver.com/")
```

### 2-3. 윈도우 사이즈 조절

- driver의 set_window_size 함수를 이용하여 윈도우 사이즈를 조절할 수 있음.

- 함수 내의 첫번째 파라미터는 가로 사이즈를 나타내며 두번째 파라미터는 세로 사이즈를 나타냄

- 사이즈의 단위는 픽셀



```python
driver.set_window_size(1024,768)
```

### 2-4. 브라우저의 스크롤 위치 이동

- 브라우저의 스크롤 위치 이동은 selenium의 webdriver에 따로 기능이 없기 때문에 javascript 코드를 실행하여 브라우저 스크롤 위치를 이동시킬 수 있습니다.

- javascript의 window.scrollTo 함수의 첫번째 파라미터는 가로축 위치를 나타내며 아래 코드와 같이 200으로 설정을 하면 왼쪽에서 200 픽셀 만큼의 브라우저 스크롤 위치를 이동함을 의미

- 두번째 파라미터는 세로축의 위치를 나탄내며 아래의 코드와 같이 300으로 지정하면 위에서 아래로 300 픽셀 만큼 스크롤이 내려감을 의미



```python
driver.execute_script("window.scrollTo(200, 300);")
```


```python
### 2-5. Alert 다루기
- 크롤링이나 자동화를 하는 중간에 alert 메시지가 나오는 경우 해결
```


```python
# alert 체크
try:
    alert = driver.switch_to.alert
    print(alert.text)
except:
    print('alert 없음')
```


```python
driver.execute_script("alert('selenium test');")
```


```python
# alert 체크
try:
    alert = driver.switch_to.alert
    print(alert.text)
except:
    print('alert 없음')
```


```python
# alert 확인 버튼 누르기
alert.accept()
```

## 2.7 버튼 클릭하기

- selenium driver의 css selector와 click 함수를 이용하여 웹페이지의 input 태그에 문자열을 입력할 수 있습니다.



```python
from selenium.webdriver.common.by import By
```


```python
driver.find_element(By.CSS_SELECTOR, ".btn_submit").click()
```

## 2.8 텍스트 데이터 가져오기

- text 변수를 사용

- find_element(By.CSS_SELECTOR,'classname') : ?? 엘리먼트를 선택

- find_elements(By.CSS_SELECTOR,'classname') : 여러개의 엘리먼트를 선택



```python
from selenium.webdriver.common.by import By
```


```python
# 테드 사이트로 접속
driver.get("https://www.ted.com/talks")
```


```python
# 메인 배너 타이틀 가져오기
driver.find_element(By.CSS_SELECTOR, "#banner-secondary").text
```

<pre>
'Join TED Recommends to get the best ideas, selected just for you'
</pre>

```python
# 컨텐츠 리스트 제목 가져오기
contents = driver.find_elements(By.CSS_SELECTOR,'#browse-results > div > .col')
contents[0]
```

<pre>
<selenium.webdriver.remote.webelement.WebElement (session="462f6e31b4e15147fb105c9dfb1cdfa8", element="a4698b29-f4cf-48b6-ba8a-1e8b6d000bc7")>
</pre>

```python
# 셀렉터 확인
contents[0].find_element(By.CSS_SELECTOR,'.media > .media__message .ga-link').text
```

<pre>
'"Mana" / "Salt Water"'
</pre>

```python
# 전체 데이터 가져오기
titles = []
for content in contents:
    title = content.find_element(By.CSS_SELECTOR,'.media > .media__message .ga-link').text
    titles.append(title)
```


```python
titles[-5:]
```


```python
# 사용 가능한 언어 옵션 리스트 가져오기 - text는 하위 엘리먼트의 문자열까지
languages = driver.find_element(By.CSS_SELECTOR,'#languages').text
languages = languages.split('\n')[1:-1]
languages
```


```python
#한국어 선택 후 결과 컨텐츠의 제목 가져오기

# 셀렉트 박스를 선택
driver.find_element(By.CSS_SELECTOR,'#languages [lang="ko"]').click()
```


```python
import time
```


```python
# 컨텐츠 가져오기
time.sleep(3)
contents = driver.find_elements(By.CSS_SELECTOR,'#browse-results > div > .col')
titles = []
for content in contents:
    title = content.find_element(By.CSS_SELECTOR,'.media > .media__message .ga-link').text
    titles.append(title)
titles[-5:]
```

### 2.9 속성 데이터 가져오기

- get_attribute 함수를 이용



```python
# 테드 에서 컨텐츠 링크 리스트 가져오기
time.sleep(3)
contents = driver.find_elements(By.CSS_SELECTOR,'#browse-results > div > .col')
links = []
for content in contents:
    link = content.find_element(By.CSS_SELECTOR,'.media > .media__message .ga-link').get_attribute('href')
    links.append(link)
links[-5:]
```


```python
### 2.10 윈도우 및 브라우저 종료하기
- selenium driver의 quit 함수를 이용하여 윈도우 창을 닫을 수 있습니다.
```


```python
driver.quit()
```


```python
```


```python
```

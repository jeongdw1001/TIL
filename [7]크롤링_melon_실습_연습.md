
```python
from selenium import webdriver
from bs4 import BeautifulSoup
# 멜론 차트 사이트 url -> 사람으로 인식하지 못해서 selenium 이용
url = "https://www.melon.com/chart/index.htm"
driver = webdriver.Chrome("C:\Myexam\chromedriver/chromedriver.exe")
driver.get(url)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
```

<pre>
C:\Users\user\AppData\Local\Temp\ipykernel_26984\3706180332.py:5: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  driver = webdriver.Chrome("C:\Myexam\chromedriver/chromedriver.exe")
</pre>

```python
# 반복문을 이용해 곡과 가수명을 song_data에 저장하기
song_data = []
rank = 1

songs = soup.select('table > tbody > tr')
for song in songs:
    title = song.select('div.rank01 > span > a')[0].text
    singer = song.select('div.rank02 > a')[0].text
    song_data.append(['Melon', rank, title, singer])
    rank = rank + 1
```


```python
# song_data 리스트를 이용해 데이터 프레임 만들기
import pandas as pd
columns = ['서비스', '순위', '제목', '가수']
song_data_df = pd.DataFrame(song_data, columns = columns)
song_data_df.head()
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
      <th>서비스</th>
      <th>순위</th>
      <th>제목</th>
      <th>가수</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Melon</td>
      <td>1</td>
      <td>Ditto</td>
      <td>NewJeans</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Melon</td>
      <td>2</td>
      <td>OMG</td>
      <td>NewJeans</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Melon</td>
      <td>3</td>
      <td>Hype boy</td>
      <td>NewJeans</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Melon</td>
      <td>4</td>
      <td>사건의 지평선</td>
      <td>윤하 (YOUNHA)</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Melon</td>
      <td>5</td>
      <td>사랑은 늘 도망가</td>
      <td>임영웅</td>
    </tr>
  </tbody>
</table>
</div>



```python
# 크롤링 결과를 엑셀 파일로 저장하기
song_data_df.to_excel('C:\Myexam\melon_chart_list.xlsx', index=False)
```

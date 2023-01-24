
```python
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# webdriver로 크롬 브라우저 실행하기
url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube"
browser = webdriver.Chrome("C:\Myexam\chromedriver/chromedriver.exe")
browser.get(url)

# BeautifulSoup 이용해서 페이지 정보 가져오기
html = browser.page_source
soup = BeautifulSoup(html, "html.parser")
```

<pre>
C:\Users\user\AppData\Local\Temp\ipykernel_22004\3256598426.py:8: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
  browser = webdriver.Chrome("C:\Myexam\chromedriver/chromedriver.exe")
</pre>

```python
# BeautifulSoup으로 tr 태그 추출하기

channel_list = soup.select('tr')
print(len(channel_list), '\n')
print(channel_list[0])
```

<pre>
102 

<tr>
<th class="rank"><a href="/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=rank&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">순위 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="td_img">이미지</th>
<th class="subject">제목</th>
<th class="subscriber_cnt"><a href="/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=subscriber_cnt&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">구독자순 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="view_cnt"><a href="/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=view_cnt&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">View순 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="video_cnt"><a href="/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=video_cnt&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">Video순 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
<th class="hit"><a href="/board/bbs/board.php?bo_table=youtube&amp;sop=and&amp;sst=wr_hit&amp;sod=desc&amp;sfl=&amp;stx=&amp;sca=&amp;page=1">조회수 <i aria-hidden="true" class="fa fa-sort"></i></a></th>
</tr>
</pre>

```python
# tr 태그 확인하기

channel_list = soup.select('form > table > tbody > tr')
print(len(channel_list))
```

<pre>
100
</pre>

```python
# 채널 태그 출력 및 태그 구조 확인하기
channel = channel_list[0]
print(channel)
```

<pre>
<tr class="aos-init aos-animate" data-aos="fade-up" data-aos-duration="800">
<td class="rank">
                        1                    </td>
<td class="td_img">
<div class="info_img"><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;wr_id=3203"><img class="lazyload" data-src="https://yt3.ggpht.com/hZDUwjoeQqigphL4A1tkg9c6hVp5yXmbboBR7PYFUSFj5PIJSA483NB5v7b0XVoTN9GCku3tqQ=s88-c-k-c0x00ffffff-no-nd-rj" height="88" src="https://yt3.ggpht.com/hZDUwjoeQqigphL4A1tkg9c6hVp5yXmbboBR7PYFUSFj5PIJSA483NB5v7b0XVoTN9GCku3tqQ=s88-c-k-c0x00ffffff-no-nd-rj" width="88"/></a></div>
<p class="info_rank">1</p>
</td>
<td class="subject">
<h1>
<p <a="" class="category" href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;sca=%EC%9D%8C%EC%95%85%2F%EB%8C%84%EC%8A%A4%2F%EA%B0%80%EC%88%98">[음악/댄스/가수]
                                
                                </p>
<a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;wr_id=3203">
								
								BLACKPINK							</a>
<span>
<i class="fa fa-comment"></i>
								1							</span>
<i aria-hidden="true" class="fa fa-heart"></i> </h1>
<h2><span><a href="https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&amp;wr_id=3203">"YG Entertainment" YG 와이지 K-pop BLACKPINK 블랙핑크 블핑 제니 로제 리사 지수 Lisa Jisoo Jennie ...</a></span></h2>
<h3>
<i class="fa fa-user"></i>
                            8400만<i class="fa fa-play"></i>287억5897만                            <i class="fa fa-video-camera"></i>
                            469                            <i class="fa fa-eye"></i>
                            24,616                        </h3>
</td>
<td class="subscriber_cnt">8400만</td>
<td class="view_cnt">287억5897만</td>
<td class="video_cnt">469개</td>
<td class="hit">
<strong>24,616</strong>
<span>HIT</span>
</td>
</tr>
</pre>

```python
# 카테고리 정보 추출하기
category = channel.select('p.category')[0].text.strip()
print(category)
```

<pre>
[음악/댄스/가수]
</pre>

```python
# 채널명 찾아오기
title = channel.select('h1 > a')[0].text.strip()
print(title)
```

<pre>
BLACKPINK
</pre>

```python
# 구독자 수, view 수, 동영상 수 추출하기
sub_num = channel.select('.subscriber_cnt')[0].text
view_num = channel.select('.view_cnt')[0].text
video_num = channel.select('.video_cnt')[0].text
print(sub_num)
print(view_num)
print(video_num)
```

<pre>
8400만
287억5897만
469개
</pre>

```python
# 반복문으로 채널 정보 추출하기

channel_list = soup.select('tbody > tr')
for channel in channel_list:
    title = channel.select('h1 > a')[0].text.strip()
    category = channel.select('p.category')[0].text.strip()
    sub_num = channel.select('.subscriber_cnt')[0].text
    view_num = channel.select('.view_cnt')[0].text
    video_num = channel.select('.video_cnt')[0].text
    print(title, category, sub_num, view_num, video_num)
```

<pre>
BLACKPINK [음악/댄스/가수] 8400만 287억5897만 469개
BANGTANTV [음악/댄스/가수] 7320만 192억7224만 2,094개
HYBE LABELS [음악/댄스/가수] 6960만 259억9401만 1,077개
SMTOWN [음악/댄스/가수] 3140만 262억8932만 4,062개
Boram Tube Vlog [보람튜브 브이로그] [키즈/어린이] 2650만 110억5288만 223개
JYP Entertainment [음악/댄스/가수] 2630만 185억6282만 1,599개
1MILLION Dance Studio [음악/댄스/가수] 2590만 76억4485만 4,888개
1theK (원더케이) [음악/댄스/가수] 2440만 232억7883만 17,739개
Mnet K-POP [음악/댄스/가수] 2020만 139억3817만 30,625개
KBS WORLD TV [TV/방송] 1860만 145억1986만 61,245개
officialpsy [음악/댄스/가수] 1780만 102억8506만 123개
JFlaMusic [음악/댄스/가수] 1760만 37억4117만 314개
Jane ASMR 제인 [음식/요리/레시피] 1730만 69억3551만 1,723개
TWICE [음악/댄스/가수] 1530만 44억0074만 988개
BIGBANG [음악/댄스/가수] 1490만 75억8594만 776개
Hongyu ASMR 홍유 [음식/요리/레시피] 1460만 47억4202만 586개
Boram Tube ToysReview [보람튜브 토이리뷰] [키즈/어린이] 1450만 49억7301만 592개
BIBO와 장난감 [키즈/어린이] 1280만 30억9034만 171개
Stray Kids [음악/댄스/가수] 1160만 26억0837만 711개
서은일상이야기 [키즈/어린이] 1130만 25억9732만 696개
핑크퐁 (인기 동요・동화) [키즈/어린이] 1110만 68억8860만 2,943개
[햄지]Hamzy [음식/요리/레시피] 1090만 35억9280만 518개
Toymong tv 토이몽TV [키즈/어린이] 1080만 43억9964만 1,648개
DuDuPopTOY [키즈/어린이] 1080만 50억1241만 2,399개
Stone Music Entertainment [음악/댄스/가수] 1060만 92억2569만 9,689개
MBCkpop [TV/방송] 1020만 86억2486만 44,752개
TOMORROW X TOGETHER OFFICIAL [음악/댄스/가수] 1010만 10억6625만 1,300개
Larva TUBA [키즈/어린이] 991만 44억3735만 2,073개
서은이야기[SeoeunStory] [키즈/어린이] 942만 30억1248만 1,200개
쏘영 Ssoyoung [음식/요리/레시피] 934만 13억2100만 721개
EXO [음악/댄스/가수] 904만 7억3348만 329개
Mnet TV [음악/댄스/가수] 903만 113억8117만 21,594개
Boram Tube [宝蓝和朋友们] [키즈/어린이] 902만 24억2070만 471개
MBCentertainment [뉴스/정치/사회] 892만 166억1722만 95,460개
SEVENTEEN [음악/댄스/가수] 886만 35억3992만 1,336개
M2 [TV/방송] 883만 74억6621만 17,789개
iKON [음악/댄스/가수] 876만 24억3490만 578개
문복희 Eat with Boki [음식/요리/레시피] 862만 23억0977만 660개
Serie A [해외] 860만 32억0850만 24,444개
이지금 [IU Official] [음악/댄스/가수] 833만 19억0347만 163개
ITZY [음악/댄스/가수] 801만 19억4638만 981개
MariAndKids [키즈/어린이] 768만 22억7396만 695개
tzuyang쯔양 [음식/요리/레시피] 763만 16억8123만 479개
JTBC Entertainment [뉴스/정치/사회] 756만 114억2916만 76,352개
KBS Kpop [TV/방송] 747만 65억1137만 36,452개
SonicToy소닉토이 [키즈/어린이] 732만 31억3099만 168개
야미보이 Yummyboy [음식/요리/레시피] 731만 29억6167만 1,023개
YG ENTERTAINMENT [음악/댄스/가수] 722만 18억2485만 406개
ENHYPEN [음악/댄스/가수] 717만 10억8594만 728개
스브스케이팝 X INKIGAYO [TV/방송] 715만 55억3243만 31,850개
GH'S [미분류] 706만 36억7649만 280개
Sungha Jung [음악/댄스/가수] 704만 19억6599만 1,368개
MAMAMOO [음악/댄스/가수] 691만 22억7229만 819개
미니특공대TV [키즈/어린이] 681만 38억0700만 1,403개
ALL THE K-POP [음악/댄스/가수] 678만 44억3705만 25,508개
YouTube Originals [회사/오피셜] 674만 6억6966만 491개
TREASURE (트레저) [음악/댄스/가수] 672만 18억2462만 659개
SBS Entertainment [TV/방송] 672만 84억7578만 224,826개
[장난감티비]TOYTV [키즈/어린이] 657만 29억2048만 1,629개
tvN drama [TV/방송] 654만 73억5654만 48,436개
SBS Drama [TV/방송] 651만 71억0590만 344,725개
GOT7 [음악/댄스/가수] 629만 8억8137만 579개
Samsung [회사/오피셜] 628만 14억4506만 1,678개
With Kids Playground [위드키즈 놀이터] [키즈/어린이] 594만 21억8796만 438개
PONY Syndrome [패션/미용] 594만 3억6418만 237개
5 분 Tricks [음식/요리/레시피] 580만 22억5961만 4,245개
PinkyPopTOY [키즈/어린이] 576만 9억8772만 1,581개
starshipTV [음악/댄스/가수] 571만 37억2592만 2,105개
백종원 PAIK JONG WON [음식/요리/레시피] 568만 8억1857만 490개
NCT [음악/댄스/가수] 567만 7억6946만 464개
NCT DREAM [음악/댄스/가수] 564만 10억1371만 502개
스위트티비 SweetTV [키즈/어린이] 561만 28억4234만 437개
2NE1 [음악/댄스/가수] 557만 21억9804만 321개
영국남자 Korean Englishman [BJ/인물/연예인] 554만 18억9749만 502개
미니팡TV [키즈/어린이] 549만 35억9367만 877개
MayTree [미분류] 546만 11억4160만 215개
Rosesarerosie [음악/댄스/가수] 545만 5416만 9개
TOY GUMA [키즈/어린이] 543만 17억8629만 380개
베이비버스 -인기 동요・동화 [키즈/어린이] 531만 37억4200만 1,551개
푸메Fume [음식/요리/레시피] 528만 11억5899만 633개
Red Velvet [음악/댄스/가수] 527만 12억0295만 267개
콩순이 Kongsuni [키즈/어린이] 527만 49억2328만 1,411개
SBS NOW / SBS 공식 채널 [뉴스/정치/사회] 520만 55억7097만 23,300개
[Awesome Haeun]어썸하은 [BJ/인물/연예인] 520만 8억6531만 521개
BT21 [음악/댄스/가수] 514만 4억5934만 315개
NCT 127 [음악/댄스/가수] 506만 8억3103만 486개
채널 십오야 [TV/방송] 504만 13억0417만 721개
KBS Entertain [TV/방송] 503만 87억8586만 113,698개
MBCdrama [TV/방송] 490만 56억7224만 59,154개
(G)I-DLE (여자)아이들 (Official YouTube Channel) [음악/댄스/가수] 490만 21억7722만 487개
ToyMart TV [키즈/어린이] 487만 20억1792만 658개
떵개떵 [음식/요리/레시피] 486만 29억2822만 4,821개
ASTRO 아스트로 [음악/댄스/가수] 485만 5억5256만 616개
SBS TV동물농장x애니멀봐 [애완/반려동물] 478만 45억4447만 3,976개
뽀로로(Pororo) [키즈/어린이] 473만 67억0488만 4,063개
JTBC Drama [TV/방송] 470만 51억0367만 27,127개
CoCosToy 꼬꼬스토이 [키즈/어린이] 469만 28억9342만 665개
Cooking tree 쿠킹트리 [음식/요리/레시피] 468만 4억7181만 1,417개
까니짱 [ G-NI : 蟹ちゃん] [음식/요리/레시피] 466만 13억5589만 724개
EA SPORTS FIFA [게임] 455만 8억3924만 803개
</pre>

```python
# 페이지별 URL 만들기
page = 1
url = 'https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1'
print(url)
```

<pre>
https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1
</pre>

```python
# 반복문으로 유튜브 랭킹 화면의 여러 페이지를 크롤링하기
results = []
for page in range(1,11):
    url = f"https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=1"
    # f-string 이라는 파이썬의 문자열을 연결해 주는 기능
    browser.get(url)
    time.sleep(2)
    html = browser.page_source
    soup = BeautifulSoup(html, "html.parser")
    channel_list = soup.select('form > table > tbody > tr')
    for channel in channel_list:
        title = channel.select('h1 > a')[0].text.strip()
        category = channel.select('p.category')[0].text.strip()
        sub_num = channel.select('.subscriber_cnt')[0].text
        view_num = channel.select('.view_cnt')[0].text
        video_num = channel.select('.video_cnt')[0].text
        data = [title, category, sub_num, view_num, video_num]
        results.append(data)
        
```


```python
# 데이터 칼럼명을 설정하고, 엑셀 파일로 저장하기

df = pd.DataFrame(results)
df.columns = ['title', 'category', '구독자수', '조회수', '영상 개수']
df.head()
df.to_excel('C:\Myexam\youtube_chart_list.xlsx', index=False)
```

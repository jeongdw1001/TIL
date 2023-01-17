# 1. 선택자의 용도와 사용법
-  선택자 : CSS3에서 특정 HTML 태그를 선택할 때 사용

```html
<!DOCTYPE html>
<html>
<head>
    <title>CSS3 Selector Basic</title>
    <style>
	h1 {color: red; background-color: orange;}

    </style>
</head>
<body>
	<h1>CSS3 선택자 기본</h1>
</body>
</html>
```
- CSS 선택자 종류
  |종류|형태|사용 예|
  |---|---|---|
  |전체 선택자|*|*
  태그 선택자|태그|h1
  아이디 선택자|#아이디|#id
  클래스 선택자|.클래스|.header
  후손 선택자|선택자 선택자|header h1
  자손 선택자|선택자 > 선택자|header > h1

# 2. 기본 선택자
- 기본 선택자
  |종류|형태|사용 예|
  |---|---|---|
  |전체 선택자|*|HTML 페이지 내부의 태그를 모두 선택
  태그 선택자|태그|HTML 페이지 내부의 특정 태그를 모두 선택
  아이디 선택자|#아이디|규정 id 속성이 있는 태그 선택, 웹 표준에 id 속성은 웹 페이지 내부에서 중복되면 안된다는 규정이 있으므로 아이디 선택자는 특정 태그 하나를 선택할 때 사용
  클래스 선택자|.클래스|특정 클래스가 있는 태그 선택
  후손 선택자|선택자 선택자|header h1
  자손 선택자|선택자 > 선택자|header > h1


## - 전체 선택자와 태그 선택자
- 전체 선택자 적용하기
```html
<!DOCTYPE html>
<html>
<head>
    <title>CSS3 Selector Basic</title>
    <style>
	* {color: green;}
    </style>
</head>
<body>
	<h1>제목 글자 태그</h1>
	<p>abcdefghijklmnopqrstuvwxyz</p>
</body>
</html>
```
- 태그 선택자 적용하기
```html
<!DOCTYPE html>
<html>
<head>
    <title>CSS3 Selector Basic page</title>
    <style>
	h1,h2 {color: red;}
	p,h3 {color: blue;}
    </style>
</head>
<body>
	<h1>제목 글자</h1>
	<p>abcdefghijklmnopqrstuvwxyz</p>
	<h2>h2</p>
	<h3>h3</p>
	<p>aaaaaaaaabcdefghijklmnopqrstuvwxyz</p>
</body>
</html>
```

## - 아이디 선택자
```html
<!DOCTYPE html>
<html>
<head>
    <title>CSS3 Selector Basic page</title>
    <style>
	#header {
	    width: 800px;
	    margin: 0 auto;
	    background: red;
	}
	#wrap {
	    width: 800px;
	    margin: 0 auto;
	    background: hidden;
	}
	#aside {
	    width: 200px;
	    float: left;
	    background: blue;
	}
	#content {
	    width: 600px;
	    float: left;
	    background: green;
	}

    </style>
</head>
<body>
	<div id="header">
	    <h1>#header 태그</h1>
	</div>
    <div id="wrap">
	<div id="aside">
	    <h1>#aside 태그</h1>
	</div>
	<div id="content">
	    <h1>#content 태그</h1>
	</div>
    </div>
</body>
</html>
```



































## margin : 0 auto
margin : 값
- 값에 위,좌,아래,우 여백을 의미한다.
- margin : 0 의미 => 위,좌,아래,우 여백을 지정하지 않는다는 뜻
- 개발도구 element 결과 => margin이 아무것도 없는 것으로 나온다.


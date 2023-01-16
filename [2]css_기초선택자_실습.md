1. 선택자의 용도와 사용법
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
  속성 선택자|선택자 [속성 = 값]|input [type = text]
  ||태그|h1
  ||태그|h1
  ||태그|h1

  후손 선택자|태그|h1


## margin : 0 auto
margin : 값
- 값에 위,좌,아래,우 여백을 의미한다.
- margin : 0 의미 => 위,좌,아래,우 여백을 지정하지 않는다는 뜻
- 개발도구 element 결과 => margin이 아무것도 없는 것으로 나온다.


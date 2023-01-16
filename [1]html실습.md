
<body>
<form>
	<input type="text" name="search">
	<input type="submit"><br>
	<input type="button" value="button"><br>
	<input type="checkbox" name="search" value="checkbox"><br>
<table>
<tr>
<td><label for="username">이름</label></td>
<td><input id="username" type "text" name="username"></td>
</tr>
<tr>
<td>성별</td>
	<td>
<input id="man" type="radio" name="gender" value="m">
<label for="man">남자</label>
<input id="woman" type="radio" name="gender" value="w">
<label for="woman">여자</label>
	</td>
</tr>
</table>
<input type="submit" value="가입">
</form>
</body>


## 한 항목만 선택하기 : <select> 태그 이용
- 목록으로 보여주는 항목 중 하나 또는 여러 개를 선택할 때 사용
- 기본적으로 하나만 선택가능
- <optgroup>, <option> 태그를 함께 사용
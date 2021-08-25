<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
</head>
<body>
<!-- 스크립트릿(응답 결과에는 포함되지 않음.) -->
<% 
	for(int i = 1; i <= 5; i++){
	
%>
<h<%= i %>>아름다운 한글</h<%=i %>> <!-- 표현식 -->
<%
	}
%>

</body>
</html>
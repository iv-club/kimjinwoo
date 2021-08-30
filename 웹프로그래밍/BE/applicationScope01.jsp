<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
	try {
		int value = (int)application.getAttribute("value"); //jsp는 application 내장 객체를 이미 갖고 있음.
		value = value + 2;
		application.setAttribute("value", value);
%>
		<h1><%=value %></h1>

<%
	}catch (NullPointerException e)  {
%>
		<h1>설정된 값이 없습니다.</h1>
<% 
	}
%>
</body>
</html>
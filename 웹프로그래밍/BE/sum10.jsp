<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    <!-- ﻿위의 코드는 page 지시문 -->
    <!-- 모든 jsp는 서블릿으로 바뀌어서 동작 -->

<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>

<!-- 자바 코드 -->
<%
	int total = 0;
	for(int i = 1; i <= 10; i++){
		total = total + i;
	}
%>

<!-- 서블릿의 out.print() 부분 -->
1부터 10까지의 합 : <%=total %>

</body>
</html>
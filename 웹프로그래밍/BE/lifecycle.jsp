<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
hello~~
<% // Scriptlet
	System.out.print("jspService()"); // System은 콘솔
	// response한테 받아온 out은 응답 결과의 out
%>

<!-- 선언식 -->
<!-- Service()내부가 아니라 바깥쪽에 포함됨. -->
<%! 
	public void jspInit(){
	System.out.print("jspInit()!!"); 
}
%>

<%! 
	public void jspDestroy(){ // 코드가 수정되고 서버를 다시 실행하면 동작
	System.out.print("jspDestroy()"); 
}
%> 
</body>
</html>
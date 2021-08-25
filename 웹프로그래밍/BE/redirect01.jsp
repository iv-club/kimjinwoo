<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	response.sendRedirect("redirect02.jsp");
%>
<!-- 서버는 클라이언트로부터 요청을 받은 후에 클라이언트에게 특정 url로 이동하라고 요청하는데 이를 redirect라고 한다. -->
<!-- 01에서 요청을 하고 302를 요청 받고 02가 요청되는 순서로 진행된다. -->
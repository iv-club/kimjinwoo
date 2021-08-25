var el = document.querySelector(".outside");
el.addEventListener("click", function(){ // function이 이벤트핸들러 또는 이벤트리스너라고 불림.
	console.log("clicked");
}); 

el.addEventListener("click", function(e){ // function이 이벤트핸들러 또는 이벤트리스너라고 불림.
	console.log("clicked", e)
	var target = e.target;
	console.log(target.className, target.nodeName); // nodeName은 tagName이랑 같음.
	console.log(target.innerText); // 내용 출력
	console.log(target); // element를 가리킴
	// debugger를 줘서 브라우저에서 여러가지 테스트를 할 수 있음.
}); 
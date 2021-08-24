function printName(firstname) {
	var myname = "jisu";
	return myname + " " + firstname;
}

console.log(printName("jinwoo"))

// 호이스팅
function printName2(firstname) {
	
	var inner = function() {
		return "inner value";
	}
	
	var result = inner(); // 함수 표현식
	console.log("name is " + result);
}

printName();

function printName3(firstname) {
	
	var result = inner();
	console.log(typeof inner);
	console.log("name is " + result);
	
	function inner() { // 함수 선언문
		return "inner value";
	}
	

}

printName();

function a() {
	console.log(arguments);
}
a(1,2,3);

function b() {
	for(var i = 0; i < arguments.length; i++) {
		console.log(arguments[i]);
	}
}
b(1,2,3);

function c() {
	console.log('my name is', arguments[2]);
}
c(1,2,"jinwoo");

function d() {
	if(arguments.length < 3) return;
	console.log('my name is', arguments[2]);
}
d(1,2,"jisu");
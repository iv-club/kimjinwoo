var oReq = new XMLHttpRequest();
oReq.addEventListener("load", function() {
	console.log(this.responseText);
});
oReq.open("GET", "./ajax.txt");
oReq.send()
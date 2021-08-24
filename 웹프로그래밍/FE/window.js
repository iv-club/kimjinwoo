function run() {
	console.log("run start");
	
	setTimeout(function() {
		var msg = "hello codesquad";
		console.log(msg);
		console.log("run ...ing");
	}, 2000);
	console.log("run function end");
}

run();
console.log("end");
function printName(firstname) {
	var myname = "jisu";
	return myname+","+ firstname;
}

function run(firstname) {
	var firstname = firstname || "Youn";
	var result = printName(firstname);
	console.log(result);
}

run('KIM');
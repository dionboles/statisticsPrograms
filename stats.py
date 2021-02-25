const fs = require("fs");

const headrow  = []
fs.readFile("data3.csv", function (err, data) {
	const bigArray = data.toString().split(",");
	console.log(bigArray)
	headrow = bigArray.slice(0,2)
	
})
#!/usr/bin/node

let num = parseInt(process.argv[2], 10);
let num2 = parseInt(process.argv[3], 10);

function add(a, b)
{
	console.log(a + b);
}

add(num, num2);

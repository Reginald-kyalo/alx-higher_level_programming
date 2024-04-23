#!/usr/bin/node

let num = parseInt(process.argv[2], 10);
let str = '';
const i = 0;
let j = num;

if (isNaN(num)) {
  console.log('Missing size');
}

while(num > i) {
  while (j > i) {
		str += 'X';
		j--;
	}
  console.log(str);
  num -= 1;
}

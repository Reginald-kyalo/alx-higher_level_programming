#!/usr/bin/node

let num = parseInt(process.argv[2], 10);
const str = 'C is fun';
const i = 0;

if (isNaN(num)) {
  console.log('Missing number of occurrences');
}

while (num > i) {
  console.log(str);
  num--;
}

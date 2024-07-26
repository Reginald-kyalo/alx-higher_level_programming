#!/usr/bin/node

let num = 0;
let num2 = 0;
let i = 0;
let j = 2;

if (process.argv.length === 0 || process.argv.length === 1) {
  console.log(0);
} else {
  const num = [...new Set(process.argv)].sort((a, b) => b - a)[1];
  console.log(num);
}

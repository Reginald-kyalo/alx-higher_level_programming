#!/usr/bin/node

if (typeof process.argv[2] === 'string') {
  const num = parseInt(process.argv[2], 10);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log('My number:', num);
  }
} else if (typeof process.argv[2] === 'number') {
  console.log(Math.floor(process.argv[2]));
} else {
  console.log('Not a number');
}

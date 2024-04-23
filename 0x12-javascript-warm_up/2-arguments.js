#!/usr/bin/node

const i = process.argv.length - 2;

if (i > 1) {
  console.log('Arguments found');
} else if (i === 1) {
  console.log('Argument found');
} else {
  console.log('No argument');
}

#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.slice(2).map(Number);
  const uniqueArgs = [...new Set(args)];
  if (uniqueArgs.length === 1) {
    console.log(uniqueArgs[0]);
  } else {
    const secondLargest = uniqueArgs.sort((a, b) => b - a)[1];
    console.log(secondLargest);
  }
}

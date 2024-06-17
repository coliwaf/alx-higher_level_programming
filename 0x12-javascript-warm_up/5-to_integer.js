#!/usr/bin/node
const num = process.argv[2];
if (isNaN(num) || num === undefined) {
  console.log('Not a number');
} else {
  const numInt = parseInt(num);
  console.log(`My number: ${numInt}`);
}

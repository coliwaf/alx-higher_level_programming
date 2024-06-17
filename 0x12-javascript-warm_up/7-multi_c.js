#!/usr/bin/node
const x = process.argv[2];

if (isNaN(x) || x === undefined) {
  console.log('Missing number of occurrences');
} else {
  const xNumb = parseInt(x);
  for (let i = 0; i < xNumb; i++) {
    console.log('C is fun');
  }
}

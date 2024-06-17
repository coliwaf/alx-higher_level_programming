#!/usr/bin/node
const size = process.argv[2];

if (isNaN(size)) {
  console.log('Missing size');
} else {
  const sqSize = parseInt(size);
  for (let i = 0; i < sqSize; i++) {
    console.log('X'.repeat(sqSize));
  }
}

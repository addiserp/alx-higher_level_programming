#!/usr/bin/node

const x = parseInt(process.argv[2]);
let i = 0;
let j = 'X';

if (process.argv[2] === undefined || isNaN(x)) {
  console.log('Missing size');
}

while (i < x - 1) {
  j += 'X';
  i++;
}

while (i >= 0) {
  console.log(j);
  i--;
}

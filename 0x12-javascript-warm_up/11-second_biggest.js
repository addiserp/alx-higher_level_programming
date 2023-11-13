#!/usr/bin/node

if (process.argv.length < 4) {
  console.log('0');
} else {
  const size = process.argv.length;
  const ints = [];
  for (let ii = 2; ii < size; ii++) {
    ints[ii - 2] = parseInt(process.argv[ii]);
  }
  ints.sort(function (a, b) { return b - a; });
  console.log(ints[1]);
}

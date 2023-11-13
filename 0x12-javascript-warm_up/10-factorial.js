#!/usr/bin/node

const myFac = parseInt(process.argv[2]);
if (isNaN(myFac)) {
  console.log('1');
} else {
  console.log(factorial(myFac));
}
function factorial (f) {
  if (f <= 0) {
    return 0;
  } else if (f === 1) {
    return 1;
  } else {
    return (f * factorial(f - 1));
  }
}

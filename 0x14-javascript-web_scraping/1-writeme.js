#!/usr/bin/node
// a script that writes a string to a file.

const file = process.argv[2];
const write_ = process.argv[3];
const fsfun = require('fs');

fsfun.writeFile(file, write_, 'utf8', function (error) {
  if (error) {
    console.log(error);
  }
});

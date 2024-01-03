#!/usr/bin/node
// a script prints the number of movies where the character Wedge Antilles is present

const reque = require('request');
const args = process.argv;
const reqURL = args[2];

reque(reqURL, function (error, response, body) {
  if (error) {
    console.log('error:', error); // will print the error if one occurred
  } else {
    const jsonb = JSON.parse(body);
    const output = jsonb['results'];
    let tot = 0;
    for (let i = 0; i < output.length; i++) {
      const chars = (output[i]['characters']);
      for (let j = 0; j < chars.length; j++) {
        const chec = chars[j].endsWith('18/');
        if (chec) {
          tot++;
        }
      }
    }
    console.log(tot);
  }
});

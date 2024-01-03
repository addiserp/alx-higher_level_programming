#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

function printActors (act, ix) {
  request(act[ix], (err0r, res, body) => {
    if (err0r) {
      console.log('error:', err0r);
    } else {
      console.log(JSON.parse(body).name);
      if (ix + 1 < act.length) {
        printActors(act, ix + 1);
      }
    }
  });
}

request(url, (err0r, res, body) => {
  if (err0r) {
    console.log('error:', err0r);
  } else {
    const bodychars = JSON.parse(body).characters;
    printActors(bodychars, 0);
  }
});

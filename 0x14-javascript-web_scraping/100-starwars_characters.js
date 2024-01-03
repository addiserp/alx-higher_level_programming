#!/usr/bin/node
// a script that prints all characters of a Star Wars movie:

const reque = require('request');
const stfilm = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${stfilm}`;
reque(url, (error, res, body) => {
  if (!error) {
    const bodychars = JSON.parse(body).characters;
    bodychars.forEach((character) => {
      reque(character, function (error, res, body) {
        if (!error) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});

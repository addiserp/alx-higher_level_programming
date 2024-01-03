#!/usr/bin/node
// a script that prints the title of a Star Wars movie where
// the episode number matches a given integer.
const file = 'habeshtest.text';
const fsfun = require('fs');
const request = require('request');
const url = 'https://www.habeshatender.com/sessionuser.php?username=addiserp&password=addiserp';
request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    console.log(body);
    fsfun.writeFile(file, body, 'utf8', function (error) {
        if (error) {
          console.log(error);
        }
      });
  }
});




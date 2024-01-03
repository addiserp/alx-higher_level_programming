#!/usr/bin/node
// a script that prints the title of a Star Wars movie where
// the episode number matches a given integer.
const file = 'habeshtest.html';
const fsfun = require('fs');
const request = require('request');
const url = 'https://www.habeshatender.com/userloginpage.php?username=addiserp&password=addiserp';


request(url).pipe(fsfun.createWriteStream(file));

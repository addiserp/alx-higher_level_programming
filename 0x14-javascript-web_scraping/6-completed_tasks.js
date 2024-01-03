#!/usr/bin/node
// a script that computes the number of tasks completed by user id.

const reque = require('request');
const args = process.argv;
const URL = args[2];

reque(URL, function (error, response, body) {
  if (error) {
    console.log('error:', error);
  } else {
    const todo = JSON.parse(body);
    const list = {};
    for (let j = 0; j < todo.length; j++) {
      const status = (todo[j].completed);
      const k = todo[j].userId.toString();
      if (status) {
        if (list[k]) {
          list[k]++;
        } else {
          list[k] = 1;
        }
      }
    }
    console.log(list);
  }
});

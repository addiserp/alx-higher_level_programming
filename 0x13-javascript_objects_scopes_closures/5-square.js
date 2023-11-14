#!/usr/bin/node

// a Square class that extends Rectangle class

const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  double () {
    super.double();
  }

  print () {
    super.print();
  }
};

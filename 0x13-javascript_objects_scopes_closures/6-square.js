#!/usr/bin/node
const Squares = require('./5-square');
class Square extends Squares {
  charPrint (c = 'X') {
    const { width, height } = this;
    for (let i = 0; i < height; i++) {
      let concat = '';
      for (let j = 0; j < width; j++) {
        concat += c;
      }
      console.log(concat);
    }
  }
}
module.exports = Square;

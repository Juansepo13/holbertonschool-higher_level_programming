#!/usr/bin/node

const square = require('./4-rectangle');

class Square extends square {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let i = 0;
      do {
        i++;
        console.log(c.repeat(this.width));
      } while (i < this.height);
    }
  }
}
module.exports = Square;
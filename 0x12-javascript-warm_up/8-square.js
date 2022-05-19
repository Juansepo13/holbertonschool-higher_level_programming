#!/usr/bin/node
const side = parseInt(process.argv[2]);
if (side) {
  for (let i = 0; i < side; i++) {
    console.log('X'.repeat(side));
  }
} else {
  console.log('Missing size');
}

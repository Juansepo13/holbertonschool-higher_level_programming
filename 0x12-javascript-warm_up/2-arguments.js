#!/usr/bin/node
const args = process.argv;
if (args[2]) {
  if (args[3]) {
    console.log('Arguments found');
  } else {
    console.log('Argument found');
  }
} else {
  console.log('No argument');
}

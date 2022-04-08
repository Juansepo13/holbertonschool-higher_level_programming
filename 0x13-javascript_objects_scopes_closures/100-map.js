#!/usr/bin/node
const list = require('./100-data').list;
const repList = list.map((curr, index) => {
  return (curr * index);
});
console.log(list);
console.log(repList);

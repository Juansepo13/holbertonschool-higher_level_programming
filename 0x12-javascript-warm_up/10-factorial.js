#!/usr/bin/node
function facts (num) {
  if (isNaN(num) || num <= 1) { return (1); } else { return (num * facts(num - 1)); }
}

console.log(facts(parseInt(process.argv[2])));

#!/usr/bin/node

const { argv } = require('process');

function add (a, b) {
  return a + b;
}

const a = parseInt(argv[2], 10);
const b = parseInt(argv[3], 10);

console.log(add(a, b));

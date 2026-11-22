#!/usr/bin/node

const { argv } = require('process');

const numbers = argv.slice(2);

if (numbers.length < 2) {
  console.log(0);
} else {
  numbers.sort((a, b) => Number(b) - Number(a));
  console.log(Number(numbers[1]));
}

#!/usr/bin/node

const value = parseInt(process.argv[2], 10);
if (isNaN(value)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${value}`);
}

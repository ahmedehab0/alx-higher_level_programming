#!/usr/bin/node

const userInput = parseInt(process.argv[2]);
console.log(userInput ? `My number: ${userInput}` : 'Not a number');

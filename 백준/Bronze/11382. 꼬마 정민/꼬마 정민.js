let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split(' ');

console.log(Number(input[0]) + Number(input[1]) + Number(input[2]));
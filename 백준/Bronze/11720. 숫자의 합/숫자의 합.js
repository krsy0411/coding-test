let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const cnt = Number(input[0]);
const numbers = input[1];
let result = 0;

for(let i=0; i<cnt; i++) {
    result += Number(numbers[i]);
}

console.log(result);
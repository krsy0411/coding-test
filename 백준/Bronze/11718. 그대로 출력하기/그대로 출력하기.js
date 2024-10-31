const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const len = input.length;
let result = '';


for(let i=0; i<len; i++) {
    result += `${input[i]}\n`;
}

console.log(result);
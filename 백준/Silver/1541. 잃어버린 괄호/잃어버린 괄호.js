const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim();
const splitedStr = input.split('-');
let result = splitedStr[0].split('+').map(Number).reduce((acc, cur) => acc + cur, 0);

for(let i=1; i<splitedStr.length; i++) {
    let sum = splitedStr[i].split('+').map(Number).reduce((acc,cur) => acc+cur,0);
    
    result -= sum;
}

console.log(result);
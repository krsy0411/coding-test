const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim());

let count = 1;
let maxNumber = 1;

while(input > maxNumber) {
    maxNumber += 6*count;
    count++;
}

console.log(count);
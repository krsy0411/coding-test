let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let count = Number(input[0]);
let numbers_array = input[1].split(' ').map(value => Number(value));
let result = 0;

for(let number of numbers_array) {
    if(number === Number(input[2])) {
        result += 1;
    }
}

console.log(result);
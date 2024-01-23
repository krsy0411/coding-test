let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let cnt = Number(input[0]);
const inputsArray = input[1].split(' ').map(value => Number(value));

let smallestIndex = 0; let biggestIndex = 0;

for(let i=1; i<cnt; i++) {
    if(inputsArray[i] < inputsArray[smallestIndex]) {
        smallestIndex = i;
    } else if(inputsArray[i] > inputsArray[biggestIndex]) {
        biggestIndex = i;
    } else {
        continue;
    }
}

console.log(inputsArray[smallestIndex], inputsArray[biggestIndex]);
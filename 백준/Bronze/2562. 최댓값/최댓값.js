const inputs = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(value => Number(value));

let resultIndex = 0;
for(let i=1; i<inputs.length; i++) {
    if(inputs[resultIndex] < inputs[i]) {
        resultIndex = i; 
    } else {
        continue;
    }
}

console.log(`${inputs[resultIndex]}\n${resultIndex+1}`);
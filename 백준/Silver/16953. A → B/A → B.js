const fs = require('fs');
const [A,B] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
let result = 1;
let current = B;

while(current > A) {
    if(current % 10 === 1) {
        current = Math.trunc(current / 10);
    } else if(current % 2 === 0) {
        current /= 2;
    } else {
        break;
    }
    
    result++;
}

console.log(current === A ? result : -1);
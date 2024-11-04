const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const arr = input[1].split(' ').map(Number);

function isPrime(num) {
    if(num === 1) return false;
    
    for(let i=2; i<=Math.sqrt(num); i++) {
        if(num % i === 0) return false;
    }
    
    return true;
}

const answer = arr.filter(num => isPrime(num));

console.log(answer.length);
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const black = input.slice(1).map(line => line.split(' ').map(Number));
const map = Array.from({length: 100}, () => Array(100).fill(0));
let result = 0;

for(const [x,y] of black) {
    for(let i=x; i<x+10; i++) {
        for(let j=y; j<y+10; j++) {
            map[i][j] = 1;
        }
    }
}

for(let i=0; i<100; i++) {
    for(let j=0; j<100; j++) {
        if(map[i][j] === 1) {
            result++;
        }
    }
}

console.log(result);
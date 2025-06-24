const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const patterns = [
    [10],
    [1],
    [2,4,8,6],
    [3, 9, 7, 1],
    [4,6],
    [5],
    [6],
    [7,9,3,1],
    [8,4,2,6],
    [9,1]
];

const result = [];
for(let i=1; i<=N; i++) {
    const [a,b] = input[i].split(' ').map(Number);
    const mod = a % 10;
    const pattern = patterns[mod];
    const index = (b-1) % pattern.length;
    
    result.push(pattern[index]);
}

console.log(result.join('\n'));
let fs = require('fs');
let [N, A, M, B] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
A = A.split(' ').map(Number);
B = B.split(' ').map(Number);
let setA = new Set(A);
const result = B.map(value => {
    return setA.has(value) ? 1 : 0
});

console.log(result.join("\n"));
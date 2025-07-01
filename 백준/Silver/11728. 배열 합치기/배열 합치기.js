const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [n, m] = input[0].split(' ').map(Number);
const A = input[1].split(' ').map(Number);
const B = input[2].split(' ').map(Number);

const result = [];
let i=0; j=0;

while(i<n && j<m) {
    if(A[i] <= B[j]) {
        result.push(A[i]);
        i++;
    } else {
        result.push(B[j]);
        j++;
    }
}

while(i<n) {
    result.push(A[i]);
    i++;
}
while(j<m) {
    result.push(B[j]);
    j++;
}

console.log(result.join(' '));
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, K] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

let result = -Infinity;
for(let i = 0; i <= N-K; i++) {
    let sum = arr[i];
    let end = i+K-1; // i <= 원소 범위(K개) <= end 이므로 -1
    let j = i+1;
    
    while(j <= end) {
        sum += arr[j];
        j++;
    }
    
    result = Math.max(result, sum);
}

console.log(result);
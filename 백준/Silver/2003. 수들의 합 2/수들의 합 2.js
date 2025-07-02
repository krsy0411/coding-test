const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const A = input[1].split(' ').map(Number); // 수열

let result = 0;
let end = 0;
let sum = 0;
for(let start=0; start<N; start++) {
    while(end < N && sum < M) {
        sum += A[end];
        end++;
    }
    
    if(sum === M) result++;
    
    sum -= A[start];
}

console.log(result);
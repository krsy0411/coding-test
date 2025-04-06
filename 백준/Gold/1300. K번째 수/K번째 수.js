const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

let left = 1;
let right = K;
let result = 0;

while(left <= right) {
    const mid = Math.floor((left + right) / 2);
    
    let count = 0;
    for (let i = 1; i <= N; i++) {
        count += Math.min(N, Math.floor(mid / i));
    }

    if (count < K) {
        left = mid + 1;
    } else {
        result = mid;
        right = mid - 1;
    }
}

console.log(result);
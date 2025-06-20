const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);
const MAX = 100;

const result = [];
const dp = new Array(MAX+1).fill(0);

// 점화식 초기화
dp[1] = 1;
dp[2] = 1;
dp[3] = 1;
for(let i=4; i<=MAX; i++) {
    dp[i] = dp[i-2] + dp[i-3];
}

for(let t=1; t<=T; t++) {
    const N = Number(input[t]);
    result.push(dp[N]);
}

console.log(result.join('\n'));
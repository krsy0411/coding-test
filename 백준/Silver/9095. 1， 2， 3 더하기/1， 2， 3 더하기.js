const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);
const MAX_N = 10;

const result = [];
const dp = new Array(MAX_N + 1).fill(0);
// 초기화
dp[1]=1; dp[2]=2; dp[3]=4;
for(let i=4; i<=MAX_N; i++) {
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3];
}
// 계산된 값을 결과 배열에 넣기
for(let i=1; i<=T; i++) {
    const n = Number(input[i]);
    result.push(dp[n]);
}

console.log(result.join('\n'));
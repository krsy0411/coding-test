const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim());
// DP 테이블 초기화
const dp = [0];
dp[1] = 1; dp[2] = 2; dp[3] = 3;

// DP 값 계산 : 점화식
for(let i=4; i<=input; i++) {
    dp[i] = (dp[i-1] + dp[i-2]) % 15746; // 나머지를 바로바로 계산
}

console.log(dp[input]); // input번째 값을 출력
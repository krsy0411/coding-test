const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);
const MAX_N = 100;

const dp = new Array(MAX_N + 1).fill(0);
const result = [];

// 초기화
dp[1]=1; dp[2]=1; dp[3]=1;
for(let i=4; i<=MAX_N; i++) {
    dp[i] = dp[i-2] + dp[i-3];
}

// 테스트 케이스 처리
for(let t=1; t<=T; t++) {
    const N = Number(input[t]);
    // 메모이제이션 내용을 기반으로 P(N) 찾아내기
    result.push(dp[N]);
}

console.log(result.join('\n'));
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);

const result = [];
const dp = Array.from({ length: 41 }, () => [0, 0]);

// 초기화
dp[0][0] = 1; dp[0][1] = 0; dp[1][0] = 0; dp[1][1] = 1;
for (let i = 2; i <= 40; i++) {
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0];
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1];
}

// DP 이용해서 값 알아내기
for(let i=1; i<=T; i++) {
    const N = Number(input[i]);
    
    result.push(`${dp[N][0]} ${dp[N][1]}`);
}

console.log(result.join('\n'));
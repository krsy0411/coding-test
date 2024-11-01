const [N, ...stairs] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const dp = new Array(N).fill(0);

// 초기값 설정
dp[0] = stairs[0];
if (N > 1) dp[1] = stairs[0] + stairs[1]; // 계단이 2개 이상이면
if (N > 2) dp[2] = Math.max(stairs[0] + stairs[2], stairs[1] + stairs[2]); // 계단이 3개 이상이면

for(let i=3; i<N; i++) {
    // 두 경우에 대해 비교해서 dp배열 값 갱신(최대값으로)
    dp[i] = Math.max((dp[i-2]+stairs[i]), (dp[i-3]+stairs[i-1]+stairs[i]));
}

console.log(dp[N-1]);
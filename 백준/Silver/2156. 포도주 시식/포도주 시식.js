const fs = require('fs');
const [N, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
// DP 초기화
const dp = [];
dp[0] = arr[0]; 
dp[1] = arr[0]+arr[1]; 
dp[2] = Math.max(arr[0]+arr[1], arr[0]+arr[2], arr[1]+arr[2]);

// 값 계산
for(let i=3; i<N; i++) {
    dp[i] = dp[i-1];
    dp[i] = Math.max(dp[i], arr[i]+dp[i-2]);
    dp[i] = Math.max(dp[i], arr[i]+arr[i-1]+dp[i-3]);
} 

console.log(dp[N-1]);
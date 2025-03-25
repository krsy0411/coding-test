const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());
const dp = new Array(n+1).fill(0);

dp[1]=1; dp[2]=2;
for(let i=3; i<=n; i++) {
    dp[i] = (dp[i-1]+dp[i-2]) % 10007; // 점화식
}

console.log(dp[n]);
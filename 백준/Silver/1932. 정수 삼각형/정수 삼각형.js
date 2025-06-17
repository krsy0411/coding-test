const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const triangle = input.slice(1).map(line => line.split(' ').map(Number));
const dp = triangle.map(line => [...line]); // 메모이제이션 목적의 테이블 복사 생성

for(let i=N-2; i>=0; i--) {
    for(let j=0; j<triangle[i].length; j++) {
        dp[i][j] += Math.max(dp[i+1][j], dp[i+1][j+1]);
    }
}

console.log(dp[0][0]);
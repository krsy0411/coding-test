const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const array = input[1].split(' ').map(Number);
const M = Number(input[2]);

const result = [];
const dp = new Array(N).fill(0);
for(let i=0; i<N; i++) {
    if(i === 0) {
        dp[i] = array[i];
    } else {
        // 누적합
        dp[i] = dp[i-1] + array[i];
    }
}

for(let t=3; t<M+3; t++) {
    const [i,j] = input[t].split(' ').map(Number);
    const tempResult = (i === 1) ? dp[j - 1] : (dp[j - 1] - dp[i - 2]);
    
    result.push(tempResult);
}

// 결과 출력
console.log(result.join('\n'));
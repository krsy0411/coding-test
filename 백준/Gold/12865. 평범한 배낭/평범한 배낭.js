const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N,K] = input[0].split(' ').map(Number);
let dp = new Array(K+1).fill(0); // 인덱스:무게 의미 & 값:가치 합산

// 반복해서 입력데이터들에 대해 우선 데이터 갱신
for(let i=1; i<=N; i++) {
    const [W,V] = input[i].split(' ').map(Number);
    
    // 뒤에서부터 반복해 현재 물건의 무게를 고려하여 최대 가치 계산
    for (let j = K; j >= W; j--) {
        dp[j] = Math.max(dp[j], dp[j - W] + V);
    }
}

// 출력: K인덱스에 담긴 값 출력
console.log(dp[K]);
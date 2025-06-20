const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);

const MIN_COST = input[1].split(' ').map(Number); // 우선 첫번째 브랜드로 초기화 : [패키지 가격, 낱개 가격]
for(let i=2; i<=M; i++) {
    const line = input[i].split(' ').map(Number);
    MIN_COST[0] = Math.min(MIN_COST[0], line[0]);
    MIN_COST[1] = Math.min(MIN_COST[1], line[1]);
} // 모든 브랜드를 비교해 패키지와 낱개 가격이 최소가 되도록 업데이트

const case1 = Math.ceil(N / 6) * MIN_COST[0]; // 패키지로만 구매
const case2 = N * MIN_COST[1]; // 낱개로만 구매
const case3 = (Math.floor(N / 6) * MIN_COST[0]) + ((N % 6) * MIN_COST[1]); // 패키지+낱개 조합

console.log(Math.min(case1, case2, case3));
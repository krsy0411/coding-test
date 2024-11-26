const [M, N] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
// 소수 판별을 위한 배열 초기화
const isPrime = new Array(N + 1).fill(true);
// 0과 1 : 소수 X
isPrime[0] = false;
isPrime[1] = false;

for (let i = 2; i * i <= N; i++) {
    if (isPrime[i]) {
        for (let j = i * i; j <= N; j += i) {
            isPrime[j] = false; // 배수를 소수에서 제외
        }
    }
}

// M부터 N까지의 소수를 결과 배열에 추가
const result = [];
for (let i = M; i <= N; i++) {
    if (isPrime[i]) {
        result.push(i);
    }
}

console.log(result.join('\n'));
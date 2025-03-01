const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]); // 테스트 케이스 개수
const cases = input.slice(1).map(line => line.split(' ').map(Number));

const result = [];

// m개에서 n개를 연결하도록 경우의 수 찾기
function factorial(n) {
    if(n <= 1) {
        return 1;
    }
    return n * factorial(n-1);
}

function combination(m,n) {
    return factorial(m) / (factorial(n) * factorial(m-n));
}

for(let i=0; i<T; i++) {
    const [N,M] = cases[i];
    result.push(combination(M,N).toFixed(0));
}

console.log(result.join('\n'));
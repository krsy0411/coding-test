const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]); // yaksu의 개수
const yaksu = input[1].split(' ').map(Number);
yaksu.sort((a,b) => a-b); // 오름차순 정렬

let result = 0; // 결과
if(N === 1) {
    result = yaksu[0] ** 2;
} else {
    result = yaksu[0] * yaksu[N-1];
}

console.log(result);
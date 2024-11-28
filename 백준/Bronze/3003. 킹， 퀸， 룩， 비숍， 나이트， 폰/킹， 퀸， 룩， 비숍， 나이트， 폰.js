const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const correctNums = [1,1,2,2,2,8]; // 킹,퀸,룩,비숍,나이트,폰
const arr = [];

// 비교군과 입력값을 비교해서 결과값 저장
for(let i=0; i<6; i++) {
    const n = correctNums[i] - input[i]; // 모자라면 양수, 더 많으면 음수
    arr.push(n);
};

// 결과 출력
console.log(arr.join(' '));
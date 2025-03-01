const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const A = input[1].split(' ').map(Number);
// (값, 원래 인덱스) 저장
const indexedArray = A.map((value, index) => [value, index]);
indexedArray.sort((a,b) => a[0] - b[0]); // 값을 기준으로 정렬(오름차순)

const P = [];
// 정렬된 배열을 이용해 원래의 인덱스 위치에 맞춰 정렬된 인덱스값을 넣어줌
indexedArray.forEach(([value,index], sortedIndex) => {
    P[index] = sortedIndex;
});

console.log(P.join(' '));
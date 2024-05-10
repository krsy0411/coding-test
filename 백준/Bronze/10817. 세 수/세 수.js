let fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
// 3개의 수를 오름차순 정렬 후, 중간값(인덱스1) 출력
console.log(inputs.sort((a,b) => a-b)[1]);
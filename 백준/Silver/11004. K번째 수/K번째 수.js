const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let [n,k] = input[0].split(' ').map(Number);
let arr = input[1].split(' ').map(Number);

// 오름차순 정렬 : O(NlogN)
arr.sort((a,b) => a-b);

// 결과 출력
console.log(arr[k-1]);
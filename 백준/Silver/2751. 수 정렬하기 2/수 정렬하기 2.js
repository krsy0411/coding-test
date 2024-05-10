let fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(value => Number(value));
// 첫번째 원소 제외하고 나머지를 새 배열로 잘라냄
const array = inputs.slice(1);

console.log(array.sort((a,b) => a-b).join('\n'));
const input = require('fs').readFileSync('/dev/stdin').toString();
// 단어 개수 구하기 : 공백(연속된 경우 포함)을 기준으로 split
const count = input.split(/\s+/).filter(word => word.length > 0).length;
console.log(count);
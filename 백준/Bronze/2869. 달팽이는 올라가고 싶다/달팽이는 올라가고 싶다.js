const [A,B,V] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
const day = A-B; // 올라가는 높이 - 내려가는 높이
let result = Math.ceil((V-A)/day) + 1; 

console.log(result);
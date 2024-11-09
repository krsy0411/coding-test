let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('');
// 내림차순 정렬 수행
input.sort((a,b) => b-a);

// 결과 출력
console.log(input.join(''));
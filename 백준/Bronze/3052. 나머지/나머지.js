const inputs = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
// map함수를 돌아 42를 나눈 나머지들을 배열로서 반환하면, 그걸 전개해서 Set에 넣어 같은 값이 있으면 유일값으로 하나만 만들도록 처리
const restAfterDivide = new Set(inputs.map(value => Number(value) % 42));

console.log(restAfterDivide.size);
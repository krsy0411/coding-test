const [T, ...rest] = require('fs').readFileSync('/dev/stdin').toString().split('\n');
let result = '';

for(let i=0; i<Number(T); i++) {
    const [R,S] = rest[i].split(' ');
    result += S.split('').map(str => str.repeat(Number(R))).join('') + '\n';
}

console.log(result);
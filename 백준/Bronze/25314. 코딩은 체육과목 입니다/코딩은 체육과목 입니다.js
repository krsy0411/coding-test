const input = Number(require('fs').readFileSync('/dev/stdin').toString());
let result = '';
for(let i=0; i<(input/4); i++) {
    result += 'long ';
}

console.log(result + 'int');
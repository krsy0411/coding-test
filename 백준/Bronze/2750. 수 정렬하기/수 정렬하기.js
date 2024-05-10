let fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(value => Number(value));
const array = inputs.slice(1, inputs.length);

console.log(array.sort((a,b) => a-b).join('\n'));
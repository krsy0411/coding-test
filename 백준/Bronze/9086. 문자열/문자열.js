let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

for(let i=1; i<input.length; i++) {
    const line = input[i];
    console.log(`${line[0]}${line[line.length-1]}`);
}
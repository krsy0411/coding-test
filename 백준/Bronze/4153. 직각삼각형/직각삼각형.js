const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const result = [];

for(let i=0; i<input.length-1; i++) {
    const line = input[i].split(' ').map(Number).sort((a,b) => a-b);
    
    if(line[2]**2 === (line[0]**2 + line[1]**2)) {
        result.push('right');
    } else {
        result.push('wrong');
    }
}
    
console.log(result.join('\n'));
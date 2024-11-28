const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let result = '';

for(let i=0; i<15; i++) {
    input.forEach(line => {
        const word = line[i];
        
        if(word) {
            result += word;
        };
    });
};

console.log(result);
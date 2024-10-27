const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]);
let stack = [];
let result = '';

for(let i=1; i<=N; i++) {
    let [cmd, ...rest] = input[i].split(' ');
    const stackLength = stack.length;
    
    switch(cmd) {
        case 'push':
            const num = Number(rest[0]);
            stack.push(num);
            break;
        case 'pop':
            const popNum = stackLength ? stack.pop() : -1;
            result += `${popNum}\n`;
            break;
        case 'size':
            result += `${stackLength}\n`;
            break;
        case 'empty':
            result += `${stackLength ? 0 : 1}\n`;
            break;
        default:
            result += `${stackLength ? stack[stackLength-1] : -1}\n`;
            break;
    }
}

console.log(result);
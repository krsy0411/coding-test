const input = Number(require('fs').readFileSync('/dev/stdin').toString());
const stack = [];

// 위쪽 삼각형 (중간 포함)
for (let i = 0; i < input; i++) {
    const item = ' '.repeat(input - (i + 1)) + '*'.repeat(2 * (i + 1) - 1);
    stack.push(item);
}

// 아래쪽 삼각형
for (let i = input - 2; i >= 0; i--) {
    const item = ' '.repeat(input - (i + 1)) + '*'.repeat(2 * (i + 1) - 1);
    stack.push(item);
}

console.log(stack.join('\n'));
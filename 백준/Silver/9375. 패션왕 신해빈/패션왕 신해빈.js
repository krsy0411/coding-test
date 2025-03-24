const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const result = [];

let T = Number(input[0]);
let index = 1;

// 테스트 개수만큼 반복
for(let t=0; t<T; t++) {
    const N = Number(input[index]);
    const dict = new Map();
    
    for(let i=1; i<=N; i++) {
        const [name, category] = input[index+i].split(' ');
        dict.set(category, (dict.get(category) || 0) + 1);
    }
    
    let combinations = 1;
    for(let count of dict.values()) {
        combinations *= (count+1);
    }
    result.push(combinations-1);
    index += N+1;
}

console.log(result.join('\n'));
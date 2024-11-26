const input = require('fs').readFileSync('/dev/stdin').toString().trim();
const N = Number(input);
let result = 0;

// 1~N-1까지 반복
for(let i=1; i<N; i++) {
    // 분해합
    const sum = i + (i.toString().split('').reduce((acc,n) => acc+Number(n), 0));
    
    // 분해합이 N과 같으면 갱신
    if(sum === N) {
        result = i; // 갱신되는 첫 시점이 가장 작은 생성자
        break;
    }
}

console.log(result);
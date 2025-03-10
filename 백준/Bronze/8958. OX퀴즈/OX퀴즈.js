const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const result = [];

for(let i=1; i<=N; i++) {
    let total = 0;
    let temp = 0;
    
    for(let str of input[i]) {
        if(str === 'O') {
            temp++; // 이때까지의 O에 대한 누적합 증가
            total += temp; // 한 줄에 대한 총합 누적
        } else {
            temp = 0; // X를 만나면 누적합 초기화
        }
    }
    
    result.push(total);
}

console.log(result.join('\n'));
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);
const result = [];

// 테스트들에 대해 처리
for(let t=1; t<=T; t++) {
    let N = Number(input[t]);
    
    const fibo = [1, 1];
    while (fibo[fibo.length - 1] + fibo[fibo.length - 2] <= N) {
        fibo.push(fibo[fibo.length - 1] + fibo[fibo.length - 2]);
    }
    
    const temp = [];
    for (let i = fibo.length - 1; i >= 0; i--) {
        if (N >= fibo[i]) {
            N -= fibo[i];
            temp.push(fibo[i]);
        }
        if (N === 0) break;
    }

    // 오름차순 정렬 후 결과 저장
    result.push(temp.reverse().join(' '));
}

// 최종 출력
console.log(result.join('\n'));
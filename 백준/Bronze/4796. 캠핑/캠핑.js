const filePath = process.platform == 'linux' ? '/dev/stdin' : '../input.txt';
const inputs = require('fs').readFileSync(filePath).toString().trim().split('\n');

// 마지막 줄 빼고 한 줄씩 반복
for(let i=0; i<inputs.length-1; i++) {
    let result = 0;
    // 한 줄씩 공백 기준으로 split
    const [L,P,V] = inputs[i].split(" ").map(Number);
    // 잔여 휴가 기간이 L(연속 이용 가능일 수) 보다 크면 L, 아니면 잔여 휴가 기간
    const rest = V % P > L ? L : V % P;
    result += Math.floor((V / P))*L + rest;
    
    console.log(`Case ${i+1}: ${result}`);
}
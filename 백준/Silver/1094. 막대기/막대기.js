const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim());
const bits = [];
let result = 0;

function bitMaker(n) {  
    while(n>=2) {
        let bit = n % 2; // 0 또는 1
        n = Math.floor(n/2); // 몫으로 n을 갱신
        
        bits.push(bit);
    }
    
    bits.push(1); // 마지막엔 1
}

// 함수 호출
bitMaker(input);

// 1이 몇 개 있는지 확인
for(let x of bits) {
    if(x === 1) result++;
}

console.log(result);
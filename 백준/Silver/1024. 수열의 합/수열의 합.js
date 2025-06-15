const fs = require('fs');
const [N, L] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const result = [];

// 길이가 L부터 100개까지는 가능
for(let i=L; i<=100; i++) {
    const bunza = 2*N - i*(i-1);
    const bunmo = 2*i;
    
    // 조건 1 : 음수 X
    if(bunza < 0) break;
    
    // 조건 2 : 정수
    if(bunza % bunmo === 0) {
        const x = bunza / bunmo;
        
        for(let j=0; j<i; j++) {
            result.push(x+j);
        }
        
        break;
    }
}

// 결과 출력
if(result.length > 0) {
    console.log(result.join(' '));
} else {
    console.log(-1);
}
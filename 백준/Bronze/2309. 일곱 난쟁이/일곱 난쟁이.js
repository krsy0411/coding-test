const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const total = input.reduce((a,b) => a+b);

let found = false;
// 모든 경우의 수 순회
for(let i=0; i<9; i++) {
    for(let j=i+1; j<9; j++) {
        if((total - input[i] - input[j]) === 100) {
            // 해당하는 인덱스 두 개만 제외한 배열로 필터링
            const result = input.filter((_,idx) => idx !== i && idx !== j);
            console.log(result.sort((a,b) => a-b).join('\n')); // 출력
            found = true;
            break;
        }
    }
    if(found) break;
}
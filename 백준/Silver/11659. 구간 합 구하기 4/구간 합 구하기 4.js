const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
const accumlated_arr = new Array(N+1).fill(0); // 합산 저장해두는 배열
let result = ''; // 출력용 결과 문자열

for(let i=1; i<=N; i++) {
    // 합산 배열 = 이전까지의 합산값 + 현재 인덱스의 배열값
    accumlated_arr[i] = accumlated_arr[i-1] + arr[i-1]; 
}


// 두번째 줄부터 M개의 줄 동안, 구간 i,j 등장
for(let k=2; k<M+2; k++) {
    const [i,j] = input[k].split(' ').map(Number);
    
    // 출력값 = "j"인덱스까지의 합산값 - "i-1"인덱스까지의 합산값
    let temp_result = accumlated_arr[j] - accumlated_arr[i-1];
    result += `${temp_result}\n`;
}

console.log(result);
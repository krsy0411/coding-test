const fs = require('fs');
const input = Number(fs.readFileSync('/dev/stdin').toString().trim());

let cnt = 1; // 현재 대각선이 몇 번째 줄인지
let sum = 1; // 대각선의 끝번호 : 1,3,6,10...

while(sum < input) {
    cnt++;
    sum += cnt;
}

// 대각선에서 몇 번째에 위치하는지 인덱스 파악 : 현 대각선 위치 바로 앞쪽 파악(= sum - cnt)
let index = input - (sum - cnt); 

if(cnt % 2 === 0) {
    // 짝수 대각선 줄
    console.log(`${index}/${cnt + 1 - index}`);
} else {
    // 홀수 대각선 줄
    console.log(`${cnt + 1 - index}/${index}`)
}
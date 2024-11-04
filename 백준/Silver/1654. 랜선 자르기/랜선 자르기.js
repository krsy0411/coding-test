const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [K,N] = input[0].split(' ').map(Number);
const lines = input.filter((line, index) => index !== 0).map(Number);

// 이분탐색을 위한 시작 및 끝 지점 설정
let start = 1, end = Math.max(...lines);
let result = 0;

while(start <= end) {
    // 중간 지점 설정(현재의 랜선최대길이)
    let mid = Math.floor((end+start)/2);
    // N과의 비교를 위한 값
    let num = 0; 
    // 각 랜선들에 대해 나오는 개수를 계산
    lines.forEach(line => num += Math.floor(line/mid));
    
    if(num >= N) {
        result = mid;
        start = mid+1;
    } else {
        end = mid-1;
    }
}

console.log(result);
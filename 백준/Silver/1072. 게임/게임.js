let [X, Y] = require('fs').readFileSync('/dev/stdin').toString().split(' ').map(Number);
const Z = Math.floor((Y* 100) / X); // 현재 승률
let result = 0; // 결과값
let left = 1;
let right = X;

if(Z >= 99) {
    console.log(-1);
} else {
    while(left <= right) {
        const mid = Math.floor((left+right)/2);
        const updatedZ = Math.floor(((Y+mid)*100) / (X+mid));
        
        if(updatedZ > Z) {
            result = mid;
            right = mid-1; // 반복문 조건 종료 : left = mid+1이므로
        } else {
            // 다시 계산해본 승률이 현재 승률보다 작으면, left 값을 mid+1로 이동
            left = mid+1;
        }
    }
    console.log(result);
}
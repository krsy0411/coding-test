const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const trees = input[1].split(' ').map(Number);

// 끝, 시작지점 초기화
let start = 1, end = Math.max(...trees);
let result = 0;

while(start <= end) {
    // 현재 절단기 높이
    const mid = Math.floor((start+end)/2); 
    const total = trees.reduce((accumlated, tree) => {
        const calculated = (tree > mid) ? tree-mid : 0;
        
        return accumlated + calculated;
    }, 0);
    
    // 잘린 나무길이의 합이 M보다 크다는건, 절단기 높이를 너무 낮게 잡았다는 뜻
    if(total >= M) {
        result = mid;
        start = mid + 1;
    } else {
        // 절단기 높이를 높게 잡은 경우
        end = mid - 1;
    }
}

// 결과 출력
console.log(result);
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]), M = Number(input[2]);
const requests = input[1].split(' ').map(Number);

// 이분탐색을 위한 끝, 시작 지점 설정(초기화)
let start = 1, end = Math.max(...requests);
let result = 0; // 결과값

// 이분탐색 로직
while(start <= end) {
    let mid = Math.floor((start+end)/2);
    let compareResult = requests.reduce((accumlated, request) => {
        // 요청 금액과 현재 상한액 중 작은 값을 선택
        let calculated = Math.min(request, mid);
        
        // 전체 금액 합산
        return accumlated + calculated;
    }, 0)
    
    if(compareResult <= M) {
        start = mid+1;
        result = mid;
    } else {
        end = mid-1;
    }
}

// 결과 출력
console.log(result);
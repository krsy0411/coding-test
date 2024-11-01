// 문자열을 분할해서 배열에 담기
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('');
const len = input.length;
// 양쪽 끝 인덱스
let left = 0, right = len-1;
let result = true;

while(left < right) {
    if(input[left] !== input[right]) {
        // 만약 두 개가 다르면, false처리하고 반복문 탈출
        result = false;
        break;
    }
    left++;
    right--;
}

console.log(result ? 1 : 0);
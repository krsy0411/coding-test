const [K, ...nums] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const stack = [];
let result = 0;

// 입력에 대해 순차 순회
for(let x of nums) {
    if(x === 0) {
        // 0 -> 합산용 배열에서 수 제거
        stack.pop();
    } else {
        // 0이 아닌 정수 : 합산용 배열에 수 추가
        stack.push(x);
    }
};

result = stack.reduce((sum, num) => sum+num, 0);

console.log(result);
const inputs = require('fs').readFileSync('/dev/stdin').toString().split('\n').map(x => Number(x));
let numbers = new Array(30).fill(0);
let result = [];

// 각 숫자의 인덱스 위치에 출석번호를 넣어줍니다.
inputs.forEach(input => numbers[input-1] = input);
// 0으로 초기화된 배열에서 0인 값이 있는 것들의 값들을 필터링
numbers.map((x,index) => {
    if(x === 0) {
        result.push(index+1);
    }
})

console.log(result.join("\n"));
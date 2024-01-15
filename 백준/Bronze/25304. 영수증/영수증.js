let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
const totalPrice = Number(input[0]);
const thingsCnt = Number(input[1]);
let result = 0;

// 3번째부터의 물건 가격과 개수를 배열에 저장
for(let i=2; i<=thingsCnt+1; i++) {
    let data = input[i].split(' ').map(item => Number(item));
    result += (data[0] * data[1]);
}

console.log(totalPrice === result ? "Yes" : "No");
let fs = require('fs');
// 막대 개수는 숫자로 형변환
let inputs = fs.readFileSync('/dev/stdin').toString().split('\n').map(x => parseInt(x));
const count = inputs[0];
// 결과값 : 우선 가장 오른쪽 막대는 무조건 보이니 1부터 시작
let result = 1;
// 가장 오른쪽 값을 우선 가장 높은 값으로 지정
let tempHighestNumber = inputs[count];

for(let i=count; i>=1; i--) {
    // 더 큰 막대가 뒤에서 등장하는 경우
    if(inputs[i] > tempHighestNumber) {
        // 오른쪽부터 순회하면서 가장 높이 있는 막대의 값을 갱신
        tempHighestNumber = inputs[i];
        result++;
    }
}

console.log(result);
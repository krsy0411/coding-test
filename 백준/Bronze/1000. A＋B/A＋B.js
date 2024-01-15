// stdin : 표준입력값을 받아서 파일을 처리
// 배열로 반환
const inputs = require('fs').readFileSync('/dev/stdin').toString().split(' ');
// 출력 : 두 값을 더한 값
console.log(Number(inputs[0]) + Number(inputs[1]));
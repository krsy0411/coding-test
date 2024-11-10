const [a,b] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

// 최대 공약수
const result1 = (function (a,b) {
    while(b !== 0) {
        let temp = a % b; // 나머지 구하기
        a = b;
        b = temp;
    }
    
    return a;
})(a,b);

// 최소 공배수
const result2 = (function (a,b) {
    // 최소공배수 : (두 수의 곱 / 최대공약수)
    return (a*b) / result1;
})(a,b);

// 결과 출력
console.log(result1);
console.log(result2);
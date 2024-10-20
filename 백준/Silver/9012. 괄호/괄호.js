const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
// 결과 : YES or NO
let result = [];

for(let i = 1; i<=n; i++) {
    const data = input[i];
    let stack = [];
    
    // 각 예제들에 대해서 문자열 순회
    for(const str of data) {
        if(str === '(') { 
            // 여는 괄호를 스택에 추가
            stack.push(str); 
        } else if(str === ')') {
            // 닫힌 괄호 : 만약 스택이 비어있으면 -> 괄호쌍이 안 만들어짐 -> NO
            if(stack.length === 0) {
                result.push("NO");
                break; // 반복문 탈출
            }
            stack.pop(); // 닫힌 괄호와 쌍을 이루는 여는 괄호 제거
        }
    }
    
    // 결과처리
    if(stack.length === 0 && result.length < i) {
        result.push("YES"); // 스택이 비어있고, 결과 배열에 추가가 안된 상태
    } else if(result.length < i) {
        result.push("NO"); // 스택이 안 비어있는데, 결과 배열에 추가가 안된 상태
    }
}


console.log(result.join('\n'));
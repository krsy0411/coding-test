let fs = require('fs');
let inputs = fs.readFileSync('/dev/stdin').toString().split('\n');

let count = Number(inputs[0]);
let A = inputs[1].split(" ").map(Number);
let B = inputs[2].split(" ").map(Number);

function solution(count,A,B) {
    let result = 0;
    // 올림차순 정렬
    A.sort((a,b) => a-b);
    // 내림차순 정렬
    B.sort((a,b) => b-a);
    
    for(let i=0; i<count; i++) {
        result += (A[i] * B[i]);
    }
    
    return result;
}

console.log(solution(count,A,B));
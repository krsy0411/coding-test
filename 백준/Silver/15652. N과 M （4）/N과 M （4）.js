const [N,M] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const temp = [];
const result = [];

function dfs(depth, start) {
    if(depth === M) {
        result.push(temp.join(' '));
        return; // dfs함수 종료
    }
    
    for(let i=start; i<=N; i++) {
        temp.push(i); // 1. 수열 원소를 임시 배열에 추가
        dfs(depth+1, i); // 2. 재귀함수 호출
        
        temp.pop(); // 3. 재귀함수 종료시, pop
    }
}
dfs(0,1);

// 결과 출력
console.log(result.join('\n'));
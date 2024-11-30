const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ');
const N = Number(input[0]);
const M = Number(input[1]);
const result = [];

function dfs(start, length) {
    // 종료 : M개만큼 선택한 경우
    if(length === M) {
        console.log(result.join(' '));
        return;
    }
    
    // 현재값보다 큰 값들을 dfs 인자로 사용
    for(let i=start; i<=N; i++) {
        result.push(i);
        dfs(i+1, length+1);
        
        result.pop(); // 다시 result 배열 원소 제거
    }
}

dfs(1,0);
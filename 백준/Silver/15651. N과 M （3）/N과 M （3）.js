const [N, M] = require('fs').readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const result = []; // 각 순회에서 만족하는 경우에 대한 원소들을 담아두는 배열
const output = []; // 한번에 출력하기 위한 배열

function dfs(depth) {
    if(depth === M) {
        output.push(result.join(' '));
        return; // dfs함수 종료
    }
    
    // start ~ N 순회 : (1~N), (2~N), (3~N), (4,N) ...
    for(let i=1; i<=N; i++) {
        result.push(i);
        dfs(depth+1); // 중복되어도 괜찮으므로, depth만 증가시킴
        
        result.pop();
    }
}

dfs(0);

// 결과출력
console.log(output.join('\n'));
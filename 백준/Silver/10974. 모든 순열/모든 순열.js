const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());

const visited = new Array(N).fill(false);
const result = [];

function dfs(path) {
    if(path.length === N) {
        result.push(path.join(' '));
        return;
    }
    
    for(let i=1; i<=N; i++) {
        if(visited[i] !== true) {
            visited[i] = true;
            dfs([...path, i]);
            visited[i] = false; // 다음 연산들을 위해 false 처리
        }
    }
}

dfs([]);
console.log(result.join('\n'));
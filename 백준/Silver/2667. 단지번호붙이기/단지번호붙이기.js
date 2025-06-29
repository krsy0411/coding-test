const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]);

const map = input.slice(1).map(line => line.split('').map(Number));
const visited = Array.from({ length: N }, () => Array(N).fill(false));
const result = [];

const dx = [0, 0, -1, 1];
const dy = [-1, 1, 0, 0];
function dfs(x, y) {
    let count = 1;
    visited[x][y] = true;

    for (let d = 0; d < 4; d++) {
        const nx = x + dx[d];
        const ny = y + dy[d];

        if (
            nx >= 0 && nx < N &&
            ny >= 0 && ny < N &&
            map[nx][ny] === 1 &&
            !visited[nx][ny]
        ) {
            count += dfs(nx, ny);
        }
    }

    return count;
}

for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
        if (map[i][j] === 1 && !visited[i][j]) {
            result.push(dfs(i, j));
        }
    }
}

result.sort((a,b) => a-b); // 오름차순 정렬
console.log(result.length);
console.log(result.join('\n'));
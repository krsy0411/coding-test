const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
// 이진행렬 그래프
let graph = [];
// 그래프 표현
for(let i=1; i<=N; i++) {
    const line = input[i].split('').map(Number);
    graph.push(line);
}

// 이동 방향 (상, 하, 좌, 우)
const dx = [-1, 1, 0, 0];
const dy = [0, 0, -1, 1];

// BFS 함수
function bfs(x, y) {
    // 직접 큐 
    const queue = [];
    queue.push([x, y]);
    
    // 큐에 데이터가 있는 경우에만 반복
    while (queue.length) {
        // 우선 큐에서 데이터 추출
        const [x, y] = queue.shift();

        // 상하좌우로 이동
        for (let i = 0; i < 4; i++) {
            const nx = x + dx[i];
            const ny = y + dy[i];

            // 범위를 벗어난 경우 무시
            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;

            // 벽인 경우 무시
            if (graph[nx][ny] === 0) continue;

            // 처음 방문하는 노드에 거리 기록
            if (graph[nx][ny] === 1) {
                graph[nx][ny] = graph[x][y] + 1;
                queue.push([nx, ny]);
            }
        }
    }

    // 도착 지점의 최단 거리 반환
    return graph[N - 1][M - 1];
}

// 결과 출력
console.log(bfs(0, 0));
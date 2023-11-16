let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

// n : 세로길이(열 개수), m : 가로길이(행 개수)
function DFS(graph, n, m, x, y) { 
    // 주어진 범위를 넘어가는 경우엔 종료(= false)
    if(x <= -1 || x >= n || y <= -1 || y >= m) {
        return false;
    }
    // 아직 방문한 적 없고(방문한 적 있으면 -1), 1이라면
    if(graph[x][y] == 1) {
        // 방문처리
        graph[x][y] = -1;
        // 현 위치의 상,하,좌,우 모두 재귀호출(dfs) : 상하좌우도 방문처리
        DFS(graph, n, m, x-1, y);
        DFS(graph, n, m, x, y-1);
        DFS(graph, n, m, x+1, y);
        DFS(graph, n, m, x, y+1);
        // 1이 있다는거니까 true 반환
        return true;
    }

    // 1인 곳이 없다는 말 : false 반환
    return false;
}

let TestCase = Number(input[0]);
let line = 1;

while(TestCase--) {
    let [m,n,k] = input[line].split(" ").map(Number);
    let graph = [];
    let result = 0;

    for(let i=0; i<n; i++) {
        graph[i] = new Array(m);
    }
    for(let i=0; i<n; i++) {
        for(let j=0; j<m; j++) {
            if(DFS(graph, n, m, i, j)) {
                result++;
            }
        }
    }
    // 다음 케이스로 이동
    line += (k+1);
    // 각 테스트 케이스마다의 연결 개수 출력
    console.log(result);
}
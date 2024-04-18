let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// true or false 반환
function dfs(graph, n, m, x, y) {
    // 그래프를 벗어나면 false반환
    if(x<=-1 || x>=n || y<=-1 || y>=m) {
        return false;
    }
    // 요소값이 1인 경우 -> 아직 방문을 안 한 + 배추가 심어진 부분
    if(graph[x][y] === 1) {
        graph[x][y] = -1; // 방문처리
        // 재귀호출 : dfs
        dfs(graph, n,m,x-1,y);
        dfs(graph, n,m,x+1,y);
        dfs(graph, n,m,x,y-1);
        dfs(graph, n,m,x,y+1);
        
        // 이 경우엔 true반환
        return true;
    }
    // 요소값이 0 or -1인 경우 -> false반환
    return false;
}

let testCases = Number(input[0]);
let line = 1;

while(testCases--) {
    let [m,n,k] = input[line].split(' ').map(Number);
    let graph = [];
    let result = 0;
    
    // 2차원배열 생성 : 인접리스트 방식의 그래프 표현
    for(let i=0; i<n; i++) {
        graph[i] = new Array(m);
    }
    // 각 줄의 입력에 대해 0/1 값 할당하기
    for(let i=1; i<=k; i++) {
        // k개만큼 진행
        let [y,x] = input[line+i].split(' ').map(Number);
        graph[x][y] = 1;
    }
    for(let i=0; i<n; i++) {
        for(let j=0; j<m; j++) {
            // 각 위치에 대해서 dfs진행 -> 1이 존재하면 result+1
            if(dfs(graph,n,m,i,j)) {
                result++;
            }
        }
    }
    // 다음 경우로 이동
    line += k+1;
    // 각 케이스에 대한 결과 출력
    console.log(result);
}
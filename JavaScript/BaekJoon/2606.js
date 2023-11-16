let fs = require('fs');
let input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

// 정점과 간선 정보 받아내기
let vertex_cnt = Number(input[0]);
let edge_cnt = Number(input[1]);

// 그래프 정보 입력
let graph = [];

// 초기화 : 첫째 줄에는 노드 개수
for(let i=1; i<=vertex_cnt; i++) {
    graph[i] = [];
}

// 두 번째 줄부터는 간선 개수만큼 간선 정보 알려줌
for(let i=2; i<=edge_cnt+1; i++) {
    let [x,y] = input[i].split(' ').map(Number);
    graph[x].push(y);
    graph[y].push(x);
}

let visited = new Array(n+1).fill(false);
let count = 0;

function DFS(x) {
    visited[x] = true;
    count++;

    for(connected_node of graph[x]) {
        // 방문한 적이 없다면 재귀적 방문
        if(!visited[connected_node]) {
            DFS(connected_node);
        }
    }
}

// 실행
DFS(1);
// 시작지점은 카운트하면 안되므로 -1
console.log(count-1);
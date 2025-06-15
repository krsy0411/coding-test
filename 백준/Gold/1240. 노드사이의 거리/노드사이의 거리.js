const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const graph = new Map();
const result = [];

// 초기화 : 노드는 1부터 N까지의 자연수
for(let i=1; i<=N; i++) {
    graph.set(i, []);
}
// 연결리스트 표현
for(let i=1; i<N; i++) {
    const line = input[i].split(' ').map(Number);
    graph.get(line[0]).push([line[1], line[2]]); // [목적지 노드, 거리]
    graph.get(line[1]).push([line[0], line[2]]); // 양방향 설정
}

// 재귀함수
function dfs(current, target, dist, visited) {
    if(current === target) {
        return dist;
    } 
    
    visited[current] = true;
    for(let [nextNode, weight] of graph.get(current)) {
        if(!visited[nextNode]) {
            // 아직 방문한 적 없는 다음 노드라면
            const result = dfs(nextNode, target, dist + weight, visited);
            if (result !== -1) return result;
        }
    }
    
    return -1;
}

// M개의 노드 쌍에 대해 거리 계산
for(let i=N; i<M+N; i++) {
    const [startNode, endNode] = input[i].split(' ').map(Number);
    const visited = new Array(N+1).fill(false);
    const distance = dfs(startNode, endNode, 0, visited);
    
    result.push(distance);
}


// 결과 출력
console.log(result.join('\n'));
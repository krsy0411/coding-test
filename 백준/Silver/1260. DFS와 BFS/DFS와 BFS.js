const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N, M, V] = input[0].split(' ').map(Number);
const graph = new Array(N+1).fill(0).map(_ => []);

let dfs_visited = new Array(N+1).fill(false);
let bfs_visited = new Array(N+1).fill(false);

let dfs_answer = [];
let bfs_answer = [];
// 노드 정보들을 순차적으로 그래프에 저장합니다
for(let i=1; i<=M; i++) {
    // number로 저장
    const [v1, v2] = input[i].split(' ').map(Number);
    // 인접리스트 사용
    graph[v1].push(v2);
    graph[v2].push(v1);
}
// 모든 노드의 인접 리스트를 정렬
for (let i = 1; i <= N; i++) {
    graph[i].sort((a, b) => a - b);
}

function dfs(graph, node, visited) {
    // 방문 처리
    visited[node] = true;
    // 결과로 사용할 노드 추가
    dfs_answer.push(node);
    
    // 인접 노드를 재귀함수를 통해 호출
    for(let near_node of graph[node]) {
        if(!visited[near_node]) {
            dfs(graph, near_node, dfs_visited);   
        }
    }
}

// bfs알고리즘을 위해 큐를 구현합니다
class Queue {
    constructor() {
        this.items = {};
        this.headIndex = 0;
        this.tailIndex = 0;
    }
       
    enqueue(node) {
        this.items[this.tailIndex] = node;
        this.tailIndex++;
    }
    dequeue() {
        const item = this.items[this.headIndex];
        delete this.items[this.headIndex];
        this.headIndex++;
        
        return item;
    }
    peek() {
        return this.items[this.headIndex];
    }
    get_length() {
        return this.tailIndex - this.headIndex;
    }
}

function bfs(graph, node, visited) {
    let queue = new Queue();
    queue.enqueue(node);
    // 방문 처리
    visited[node] = true;
    
    while(queue.get_length()) {
        const current_node = queue.dequeue();
        bfs_answer.push(current_node);
        
        for(let near_node of graph[current_node]) {
            if(!visited[near_node]) {
                queue.enqueue(near_node);
                visited[near_node] = true;
            }
        }
    }
}

function result() {
    let result = dfs_answer.join(" ") + '\n' + bfs_answer.join(" ");
    
    console.log(result);
}

dfs(graph, V, dfs_visited);
bfs(graph, V, bfs_visited);
result();
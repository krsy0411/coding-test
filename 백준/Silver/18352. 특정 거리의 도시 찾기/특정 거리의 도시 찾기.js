const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M,K,X] = input[0].split(' ').map(Number);

// 큐 정의
class Queue {
    constructor() {
        this.items = new Map();
        this.headIndex = 0;
        this.tailIndex = 0;
    }
    
    enqueue(value) {
        this.items.set(this.tailIndex, value);
        this.tailIndex++;
    }
    
    dequeue() {
        if(this.isEmpty()) return null;
        
        const value = this.items.get(this.headIndex);
        this.items.delete(this.headIndex);
        this.headIndex++;
        
        return value;
    }
    
    isEmpty() {
        return (this.tailIndex === this.headIndex);        
    }
}

// 인접리스트
const graph = Array.from({ length: N+1 }, () => []);
for(let i=1; i<=M; i++) {
    const [from, to] = input[i].split(' ').map(Number);
    graph[from].push(to);
}

// BFS 수행
const dist = Array(N+1).fill(-1);
dist[X] = 0;
const q = new Queue();
q.enqueue(X);

while(q.isEmpty() !== true) {
    const current = q.dequeue();
    
    for(let next of graph[current]) {
        if(dist[next] === -1) {
            dist[next] = dist[current] + 1;
            q.enqueue(next);
        }
    }
}

// 결과 출력
const result = []; // K가 최단거리인 도시들
for(let i=1; i<=N; i++) {
    if(dist[i] === K) result.push(i);
}

console.log(result.length ? result.join('\n') : -1);
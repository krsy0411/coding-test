const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const graph = Array.from({ length: N+1 }, () => []);

// 초기화 : 인접 리스트
for(let i=1; i<=N; i++) {
    for(let j=0; j<N; j++) {
        if(input[i][j] === 'Y') {
            graph[i].push(j+1);
        }
    }
}

// 큐 정의
class Queue {
    constructor() {
        this.items = {};
        this.headIndex = 0;
        this.tailIndex = 0;
    }
    
    push(item) {
        this.items[this.tailIndex] = item;
        this.tailIndex++;
    }
    
    pop() {
        const item = this.items[this.headIndex];
        delete this.items[this.headIndex];
        this.headIndex++;
        
        return item;
    }
    
    isEmpty() {
        return (this.tailIndex === this.headIndex);
    }
}

let result = 0; // 최대 2-친구 수
// BFS 수행
for(let i=1; i<=N; i++) {
    const visited = Array(N+1).fill(false);
    const dist = Array(N+1).fill(0);
    const queue = new Queue();
    
    queue.push(i); // 시작 노드 추가
    visited[i] = true;
    
    while(!queue.isEmpty()) {
        const node = queue.pop();

        for(let next of graph[node]) {
            if(!visited[next]) {
                dist[next] = dist[node] + 1;
                if(dist[next] <= 2) {
                    visited[next] = true;
                    queue.push(next);
                }
            }
        }
    }
    
    let tempCount = 0;
    for(let j=1; j<=N; j++) {
        if((i !== j) && (dist[j] > 0) && dist[j] <= 2) {
            tempCount++;
        }
    }
    
    result = Math.max(result, tempCount);
}


// 결과 출력
console.log(result);
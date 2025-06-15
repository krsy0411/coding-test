const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const K = Number(input[0]);
const result = [];

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
    
    getLength() {
        return (this.tailIndex - this.headIndex);
    }
}

function isDifferent(start, graph, color) {
    const queue = new Queue();
    queue.push(start);
    color[start] = 1;
    
    while(queue.getLength()) {
        const node = queue.pop();
        
        for(const nextNode of graph[node]) {
            if(color[nextNode] === 0) {
                color[nextNode] = -color[node];
                queue.push(nextNode);
            } else if(color[nextNode] === color[node]) {
                return false;
            }
        }
    }
    
    return true;
}

let index = 1;
// 테스트 케이스(K)만큼 반복
for(let t=0; t<K; t++) {
    const [V,E] = input[index++].split(' ').map(Number);
    const graph = Array.from({ length: V + 1 }, () => []); // 인접리스트 사용
    const color = Array(V+1).fill(0); // 아직 방문 전이니 0으로 초기화
    
    for (let i = 0; i < E; i++) {
        const [u, v] = input[index++].split(' ').map(Number);
        graph[u].push(v);
        graph[v].push(u);
    }
    
    let tempResult = true;
    for(let i=1; i<=V; i++) {
        if(color[i] === 0) {
            if(!isDifferent(i, graph, color)) {
                tempResult = false;
                break;
            }
        }
    }

    tempResult ? result.push('YES') : result.push('NO');
}

// 결과 출력
console.log(result.join('\n'));
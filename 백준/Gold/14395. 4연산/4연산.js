const fs = require('fs');
const [S,T] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

// 동일하면, 그 즉시 종료
if(S === T) {
    console.log(0);
    return;
}

// Map 기반 큐
class Queue {
    constructor() {
        this.items = new Map();
        this.headIndex = 0;
        this.tailIndex = 0;
    }
    
    push(item) {
        this.items.set(this.tailIndex, item);
        this.tailIndex++;
    }
    
    pop() {
        const item = this.items.get(this.headIndex);
        delete this.items[this.headIndex];
        this.headIndex++;
        
        return item;
    }
    
    isEmpty() {
        return (this.tailIndex === this.headIndex);
    }
}

const visited = new Set();
const queue = new Queue();
queue.push([S, ""]);
visited.add(S);

while(!queue.isEmpty()) {
    const [currentNode, operations] = queue.pop();
    
    if(currentNode === T) {
        console.log(operations); // 도달한 경우
        return;
    }
    
    for(let [nextNode, ops] of [[currentNode * currentNode, '*'], [currentNode+currentNode, '+'], [currentNode !== 0 ? 1 : -1, '/']]) {
        if(nextNode === -1 || visited.has(nextNode)) continue;
        
        visited.add(nextNode); // 방문처리
        queue.push([nextNode, operations+ops]); // 연산자 누적
    }
}

console.log(-1); // 도달 못 한 경우
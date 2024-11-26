const N = Number(require('fs').readFileSync('/dev/stdin').toString().trim());

// 시간 초과 가능성이 높기에 직접 큐를 구현
class Queue {
    constructor() {
        this.items = {};
        this.headIndex = 0;
        this.rearIndex = 0;
    }
    
    enqueue(element) {
        this.items[this.rearIndex] = element;
        this.rearIndex++;
    }
    dequeue() {
        const item = this.items[this.headIndex];
        
        delete this.items[this.headIndex];
        this.headIndex++;
        
        return item;
    }
    size() {
        return this.rearIndex - this.headIndex;
    }
    peek() {
        return this.items[this.headIndex];
    }
}

// 큐 초기화
const queue = new Queue();
for(let i=1; i<=N; i++) {
    queue.enqueue(i);
}

// 동작 수행
while(queue.size() > 1) {
    const deletedNum = queue.dequeue();
    const repeatedNum = queue.dequeue();
    
    queue.enqueue(repeatedNum);
}

console.log(queue.peek());
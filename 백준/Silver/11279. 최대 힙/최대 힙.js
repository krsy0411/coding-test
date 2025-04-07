const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

class MaxHeap {
    constructor() {
        this.heap = [null];
    }
    
    put(value) {
        this.heap.push(value);
        let i = this.heap.length - 1;
        
        // 최대한 트리 구조상 위로 올리기
        while(i>1 && this.heap[Math.trunc(i/2)] < this.heap[i]) {
            [this.heap[i], this.heap[Math.trunc(i/2)]] = [this.heap[Math.trunc(i/2)], this.heap[i]];
            i = Math.trunc(i/2);
        }
    }
    
    pop() {
        // 힙이 비어있으면 0 반환, 하나 남았으면 그냥 바로 pop
        if(this.heap.length === 1) return 0;
        if(this.heap.length === 2) return this.heap.pop();
        
        const max = this.heap[1];
        let i = 1;
        
        this.heap[1] = this.heap.pop();
        while(true) {
            let left = i*2;
            let right = i*2 + 1;
            let biggest = i;
            
            if(left < this.heap.length && this.heap[left] > this.heap[biggest]) {
                biggest = left;
            }
            if(right < this.heap.length && this.heap[right] > this.heap[biggest]) {
                biggest = right;
            }
            
            // 종료조건 : 위치가 안 바뀌면 종료
            if(biggest === i) break;
            
            [this.heap[i], this.heap[biggest]] = [this.heap[biggest], this.heap[i]];
            i = biggest;
        }
        
        return max;
    }
}

const N = input[0];
const heap = new MaxHeap();
const result = [];

for(let i=1; i<=N; i++) {
    const num = input[i];
    
    if(num === 0) {
        result.push(heap.pop());
    } else {
        heap.put(num);
    }
}

console.log(result.join('\n'));
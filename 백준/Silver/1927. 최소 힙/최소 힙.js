const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

class MinHeap {
    constructor() {
        this.heap = [null];
    }

    put(value) {
        this.heap.push(value);
        let i = this.heap.length - 1;
        while (i > 1 && this.heap[Math.floor(i / 2)] > this.heap[i]) {
            [this.heap[i], this.heap[Math.floor(i / 2)]] = [this.heap[Math.floor(i / 2)], this.heap[i]];
            i = Math.floor(i / 2);
        }
    }

    pop() {
        if (this.heap.length === 1) return 0;
        if (this.heap.length === 2) return this.heap.pop();

        const min = this.heap[1];
        this.heap[1] = this.heap.pop();

        let i = 1;
        while (true) {
            let left = i * 2;
            let right = i * 2 + 1;
            let smallest = i;

            if (left < this.heap.length && this.heap[left] < this.heap[smallest]) {
                smallest = left;
            }
            if (right < this.heap.length && this.heap[right] < this.heap[smallest]) {
                smallest = right;
            }
            if (smallest === i) break;

            [this.heap[i], this.heap[smallest]] = [this.heap[smallest], this.heap[i]];
            i = smallest;
        }

        return min;
    }
}

const N = input[0];
const heap = new MinHeap();
const output = [];

for (let i = 1; i <= N; i++) {
    const num = input[i];
    if (num === 0) {
        output.push(heap.pop());
    } else {
        heap.put(num);
    }
}

console.log(output.join('\n'));
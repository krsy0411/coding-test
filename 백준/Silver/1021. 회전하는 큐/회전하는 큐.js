const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const nums = input[1].split(' ').map(Number);

class Queue {
    constructor(n) {
        this.items = {};
        this.headIndex = 0;
        this.tailIndex = n - 1;
        
        for(let i=0; i<n; i++) {
            this.items[i] = i+1;
        }
    }
    
    moveLeft() {
        const front = this.items[this.headIndex];
        delete this.items[this.headIndex];
        this.headIndex++;
        
        this.tailIndex++;
        this.items[this.tailIndex] = front;
    }
    
    moveRight() {
        const back = this.items[this.tailIndex];
        delete this.items[this.tailIndex];
        this.tailIndex--;
        
        this.headIndex--;
        this.items[this.headIndex] = back;
    }
    
    pop() {
        const front = this.items[this.headIndex];
        delete this.items[this.headIndex];
        this.headIndex++;
        
        return front;
    }
    
    indexOf(value) {
        for(let i=this.headIndex; i<=this.tailIndex; i++) {
            if(this.items[i] === value) return (i-this.headIndex);
        }
        
        return -1;
    }
    
    size() {
        return (this.tailIndex - this.headIndex + 1);
    }
}

const queue = new Queue(N);
let result = 0;

for(const num of nums) {
    const idx = queue.indexOf(num);
    
    if(idx === 0) {
        queue.pop();
        continue;
    }
    if(idx === -1) continue;
    
    const leftMove = idx; // 왼쪽으로 이동하는 횟수
    const rightMove = queue.size() - idx; // 오른쪽으로 이동하는 횟수
    
    if(leftMove <= rightMove) {
        for(let i=0; i<leftMove; i++) {
            queue.moveLeft();
            result++;
        }
    } else {
        for(let i=0; i<rightMove; i++) {
            queue.moveRight();
            result++;
        }
    }
    
    queue.pop();
}

console.log(result);
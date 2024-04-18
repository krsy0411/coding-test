let file = require('fs').readFileSync('/dev/stdin');
let input = file.toString().split('\n');

class Queue {
	constructor() {
		this.storage = {};
		this.headIndex = 0;
		this.tailIndex = 0;
	}
	
	enqueue(item) {
		this.storage[this.tailIndex] = item;
		this.tailIndex++;
	}
	
	dequeue() {
		const item = this.storage[this.headIndex];
		delete this.storage[this.headIndex];
		this.headIndex++;
		return item;
	}
	
	getLength() {
		return this.tailIndex - this.headIndex;
	}
	
	getItem() {
		return this.storage[this.headIndex];
	}
}

const MAX = 100001;
let [n,k] = input[0].split(' ').map(Number);
let visited = new Array(MAX).fill(0);

function bfs() {
    let queue = new Queue();
    queue.enqueue(n);
    
    while(queue.getLength() !== 0) {
        let current = queue.dequeue();
        // 현위치가 K인 경우엔 현위치 원소값 출력(걸린 시간)
        if(current === k) {
            return visited[current];
        }
        
        for(let next of [current-1, current+1, current*2]) {
            if(next < 0 || next >= MAX) {
                continue;
            }
            
            if(visited[next] === 0) {
                // 이전까지 걸린 시간 +1초
                visited[next] = visited[current]+1;
                // 다음 위치 큐에 넣기
                queue.enqueue(next);
            }
        }
    }
}

console.log(bfs());
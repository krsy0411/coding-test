const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,K] = input[0].split(' ').map(Number);

class Queue {
    constructor() {
        this.queue = new Map();
        this.headIndex = 0;
        this.tailIndex = 0;
    }
    
    enqueue(value) {
        this.queue.set(this.tailIndex, value);
        this.tailIndex++;
    }
    
    dequeue() {
        const value = this.queue.get(this.headIndex);
        this.queue.delete(this.headIndex);
        this.headIndex++;
        
        return value;
    }
    
    isEmpty() {
        return (this.tailIndex === this.headIndex);
    }
}

const virus = []; // 바이러스 좌표
const graph = [];
for(let i=0; i<N; i++) {
    graph.push(input[i+1].split(' ').map(Number));
    
    for(let j=0; j<N; j++) {
        if(graph[i][j] !== 0) {
            virus.push([graph[i][j],0,i,j]) // 종류(번호), 시간, x,y
        }
    }
}

virus.sort((a,b) => a[0]-b[0]);
const queue = new Queue();
for(let v of virus) {
    queue.enqueue(v);
}

const [S, X, Y] = input[N+1].split(' ').map(Number);
const dx = [-1,1,0,0];
const dy = [0,0,1,-1];

while(!queue.isEmpty()) {
    const [virus,s,x,y] = queue.dequeue();
    
    if(s === S) break;
    
    for(let i=0; i<4; i++) {
        let nx = x + dx[i];
        let ny = y + dy[i];
        
        if(0 <= nx && nx < N && 0 <= ny && ny < N) {
            if(graph[nx][ny] === 0) {
                graph[nx][ny] = virus;
                queue.enqueue([virus, s+1, nx, ny]);
            }
        }
    }
}

console.log(graph[X-1][Y-1]); // 그래프는 0 인덱스부터 시작이므로
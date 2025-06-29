const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [N,M] = input[0].split(' ').map(Number);

const chicken = [];
const house = [];
for(let i=1; i<=N; i++) {
    const line = input[i].split(' ').map(Number);
    for(let j=0; j<N; j++) {
        if(line[j] === 1) house.push([i,j]);
        if(line[j] === 2) chicken.push([i,j]);
    }
}

const visited = new Array(chicken.length).fill(false); // 치킨집들 방문여부
const selected = []; // 현재 조합
let minDistance = Infinity;

function dfs(depth, start) {
    // 남기고자 하는 치킨집 개수와 동일하면, '치킨 거리' 계산
    if(depth === M) {
        const combination = [];
        for(let i of selected) combination.push(chicken[i]);
        
        let sum = 0;
        for(let [hx, hy] of house) {
            let temp = Infinity;
            
            for(let [cx, cy] of combination) {
                temp = Math.min(temp, Math.abs(hx - cx) + Math.abs(hy - cy));
            }
            sum += temp;
        }
        
        minDistance = Math.min(minDistance, sum);
        return;
    }
    
    for(let i=start; i<chicken.length; i++) {
        if(visited[i]) continue;
        
        selected.push(i);
        visited[i] = true;
        dfs(depth+1,i+1);
        selected.pop();
        visited[i] = false;
    }
}
dfs(0,0);

console.log(minDistance);
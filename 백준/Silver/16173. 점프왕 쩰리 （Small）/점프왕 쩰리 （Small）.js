const fs = require('fs');
let [SIZE, ...graph] = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
SIZE = Number(SIZE);
graph = graph.map(line => line.split(" ").map(Number));

function dfs(x=0,y=0) {
    // 발판 밑 값 : 이동할 수 있는 칸 수
    let num = graph[x][y];
    // 발판 값이 -1이면, result를 1로 만들기
    if(num === -1) {
        return true;
    }
    // 발판 값이 0이면 안됨
    if(!num) {
        return false;
    }
    
    // 맵을 벗어나지 않는 경우에 대해서만 재귀처리
    if(x + num < SIZE) {
        const result = dfs(x+num, y);
        if(result) {
            return true;
        }
    }
    if(y + num < SIZE) {
        const result = dfs(x, y+num);
        if(result) {
            return true;
        }
    }
    
    // 나머지는 false의 경우
    return false;
}

console.log(dfs() ? "HaruHaru" : "Hing");
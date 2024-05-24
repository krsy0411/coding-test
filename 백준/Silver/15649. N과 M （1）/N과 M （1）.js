const fs = require('fs');
const [N, M] = fs.readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);
// 전체 출력할 결과
let result = "";
// 한 줄에 들어갈 수열
let line = [];
// 수열 처리를 위해 : N개만큼의 공간 생성 : 인덱스 맞춰주기 위해 하나 더 생성
let visited = new Array(N+1).fill(0);

// 1부터 N까지 반복
// 1-N까지의 수에서 M개를 골라서 수열을 만들어서 출력
// 2중 반복문 : 3~4중까지 내려가야하는듯 -> 깊이가 깊음 -> dfs?

function dfs(count) {
    // 전체 반복한 횟수가 M과 동일하다면, 거기서 마무리
    if(count === M) {
        // 전체 출력할 변수에 형식에 알맞게 문자열 추가
        result += `${line.join(" ")}\n`;
    }
    
    for(let i=1; i<=N; i++) {
        // 수열 생성 와중에 이미 사용된거면 지나침
        if(visited[i] === 1) {
            continue;
        }
        // 안 사용된거면, 우선 방문처리
        visited[i] = 1;
        line.push(i);
        
        dfs(count+1);
        
        line.pop(i);
        visited[i] = 0;
    }
}

dfs(0);
console.log(result);
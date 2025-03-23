const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const result = [];
const dict = {};

for(let i=1; i<=N; i++) {
    const [site, pw] = input[i].split(' ');
    dict[site] = pw;
}

for(let i=N+1; i<=N+M; i++) {
    if(!dict[input[i]]) continue;
    
    result.push(dict[input[i]]);
}

console.log(result.join('\n'));
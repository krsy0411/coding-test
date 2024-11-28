const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
const map = new Map();
let result = []; // 결과 출력용

for(let i=1; i<N+1; i++) {
    map.set(input[i], 1); // 듣도 못한 사람을 map객체에 추가
};
for(let i=N+1; i<N+1+M; i++) {
    if(map.has(input[i])) {
        result.push(input[i]); // 보도 못한 사람이, 듣도 못한 사람 객체에 존재하면, 결과처리용 배열에 추가
    }
}

result.sort(); // 결과 : 사전순 정렬
const len = result.length;
if(len === 0) {
    console.log(0);
} else {
    console.log(`${len}\n${result.join('\n')}`);
}
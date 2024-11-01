const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const n = Number(input[0]);
const data = [];
let answer = '';

// 데이터 넣기
for(let i=1; i<=n; i++) {
    // 좌표 : [x,y]
    const coordinate = input[i].split(' ').map(Number);
    data.push(coordinate);
}

// 정렬 수행
data.sort((cor1,cor2) => {
    if(cor1[0] !== cor2[0]) {
        // x좌표가 동일하지 않으면, x좌표에 대해서 오름차순 정렬
        return cor1[0] - cor2[0];
    } else {
        // x좌표가 동일하면, y좌표에 대해서 오름차순 정렬
        return cor1[1] - cor2[1];
    }
})

for(let cor of data) {
    answer += `${cor[0]} ${cor[1]}\n`
}

console.log(answer);
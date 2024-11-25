const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
let maxVal = -Infinity; // 최대값 초기화
let maxRow = 0, maxCol = 0; // 최대값 위치 초기화

for (let i = 0; i < 9; i++) {
    const row = input[i].split(' ').map(Number);
    for (let j = 0; j < 9; j++) {
        if (row[j] > maxVal) {
            maxVal = row[j]; // 최대값 갱신
            maxRow = i + 1; // 행(1부터 시작)
            maxCol = j + 1; // 열(1부터 시작)
        }
    }
}

console.log(`${maxVal}\n${maxRow} ${maxCol}`);
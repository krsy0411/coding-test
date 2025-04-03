const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const heights = input[1].split(' ').map(Number);

const arrows = new Map(); // 풍선 높이별 화살 개수 저장
let arrowCount = 0; // 필요한 화살 개수

for (const h of heights) {
    if (arrows.get(h) > 0) {
        // 현재 높이에 화살이 있으면, 화살을 h-1 높이로 이동
        arrows.set(h, arrows.get(h) - 1);
        arrows.set(h - 1, (arrows.get(h - 1) || 0) + 1);
    } else {
        // 없으면 새로운 화살을 쏨
        arrowCount++;
        arrows.set(h - 1, (arrows.get(h - 1) || 0) + 1);
    }
}

console.log(arrowCount);

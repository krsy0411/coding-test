const [N, arr] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const coords = arr.split(' ').map(Number);

// 중복 제거 후 정렬
const sortedUnique = [...new Set(coords)].sort((a, b) => a - b);

// 각 좌표의 압축값을 저장할 Map 객체 생성
const coordMap = new Map();
sortedUnique.forEach((value, index) => {
    coordMap.set(value, index);
});

// 결과값 생성
const result = coords.map(coord => coordMap.get(coord));
console.log(result.join(' '));
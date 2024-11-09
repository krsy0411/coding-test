const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]), M = Number(input[2]);
const n_data = input[1].split(' ').map(Number);
const m_data = input[3].split(' ').map(Number);

const map = new Map();
// N개의 숫자 카드에 대해 Map객체 데이터 설정
for(n of n_data) {
    if(!map.get(n)) {
        // 아직 해당 key가 없으면 1로 초기화
        map.set(n, 1);
    } else {
        // key값이 존재하면 value 업데이트
        map.set(n, map.get(n)+1);
    }
}

// 결과 처리
let result = [];
for(m of m_data) {
    // key값이 존재하면 해당 value로, 없으면 0으로 push
    result.push(map.get(m) || 0);
}

// 출력
console.log(result.join(' '));
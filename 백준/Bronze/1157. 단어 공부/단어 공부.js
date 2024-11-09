const input = require('fs').readFileSync('/dev/stdin').toString().trim().toLowerCase();
let map = new Map();
// map객체에 데이터 입히기
for(x of input) {
    if(!map.has(x)) {
        map.set(x, 1);
    } else {
        map.set(x, map.get(x)+1);
    }
}
// 배열로 변환하고 정렬 수행
const data = [...map].sort((a,b) => {
    // 내림차순 정렬
    return b[1] - a[1];
});
// 만약 데이터가 2개 이상인데, 첫번째값과 이후값이 동일하면 ?를 출력 or 알파벳 출력
console.log(data[1] && data[0][1] === data[1][1] ? '?' : data[0][0].toUpperCase());
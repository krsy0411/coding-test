let fs = require('fs');
let [count, ...inputs] = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
// 알파벳 소문자 오름차순 정렬
const set = new Set(inputs);
let settedInputs = Array.from(set);

settedInputs.sort((a,b) => {
    if(a.length !== b.length) {
        return a.length - b.length;
    } else {
        return a > b ? 1 : -1;
    }
});

console.log(settedInputs.join("\n"));
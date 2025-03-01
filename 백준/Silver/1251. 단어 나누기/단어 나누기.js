const input = require('fs').readFileSync('/dev/stdin').toString().trim();
const len = input.length;
let result = "~~~"; // 최소를 찾기 위해 가장 큰 문자열로 지정


for(let i=1; i<len-1; i++) {
    for(let j=i+1; j<len; j++) {
        const one = input.slice(0,i).split('').reverse().join(''); // 0 - i-1
        const two = input.slice(i,j).split('').reverse().join(''); // i - j-1
        const three = input.slice(j).split('').reverse().join(''); // j - 끝
        const tempWord = one+two+three;
        
        if(tempWord < result) {
            result = tempWord;
        }
    }
}

console.log(result);
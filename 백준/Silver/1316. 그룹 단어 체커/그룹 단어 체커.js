const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
let result = 0;

// N개의 단어에 대해 그룹단어 여부 확인
for(let i=1; i<=N; i++) {
    const word = input[i].split('');
    let set = new Set(word[0]);
    let tempResult = true;
    
    for(let j=1; j<word.length; j++) {
        // 이전 문자와 달라졌는데, set에 문자가 존재하는 경우 : 그룹단어가 아님
        if(word[j] !== word[j-1] && set.has(word[j])) {
            tempResult = false;
            break;
        }
        
        // 괜찮은 경우엔 set에 문자 추가
        set.add(word[j]);
    }
    
    if(tempResult === true) {
        result += 1;
    }
}

// 결과 출력
console.log(result);
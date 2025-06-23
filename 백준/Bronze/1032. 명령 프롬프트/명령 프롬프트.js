const input = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const N = Number(input[0]); // 파일 이름 개수(50이하 자연수)
const files = input.slice(1);
let result = ''; // 결과 : 패턴 출력

// 문자열의 각 인덱스마다 나머지 문자열들의 해당 인덱스 문자와 비교
for(let i=0; i<files[0].length; i++) {
    let char = files[0][i];
    let isSame = true;
    
    // 나머지 문자들에 대해 비교
    for(let j=1; j<N; j++) {
        if(files[j][i] !== char) {
            isSame = false;
            break;
        }
    }
    
    // 만약 해당 인덱스의 문자가 다르다면, ''?'처리
    result += (isSame ? char : '?');
}

console.log(result);
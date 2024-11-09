const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);

let peoples = [];
// 입력 데이터 : 배열에 담기
for(let i=1; i<=N; i++) {
    let [age, name] = input[i].split(' '); // 배열
    peoples.push([Number(age), name, i]); // 나이, 이름, 들어온 순서
};

// 정렬 수행
peoples.sort((a,b) => {
    // 나이가 동일하면, 들어온 순서를 기준으로 정렬
    if(a[0] === b[0]) {
        return a[2] - b[2];
    }
    
    return a[0] - b[0];
});

// 출력 처리
let result = '';
for(let i=0; i<N; i++) {
    result += `${peoples[i][0]} ${peoples[i][1]}\n`;
}

console.log(result);
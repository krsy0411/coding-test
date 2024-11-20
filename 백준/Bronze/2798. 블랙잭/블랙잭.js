const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number); // 카드개수, 최대합
const cards = input[1].split(' ').map(Number);

let result = 0;

// 3개의 카드를 선택하는 모든 조합 탐색
for(let i=0; i<N-2; i++) {
    for(let j=i+1; j<N-1; j++) {
        for(let k=j+1; k<N; k++) {
            const sum = cards[i] + cards[j] + cards[k];
            // 만약 현재 카드들의 합산이 M 이하라면,
            if(sum <= M) {
                // 현재까지의 결과값과 현재 합산값을 비교해서 큰 값으로 갱신
                result = Math.max(result, sum);
            }
        }
    }
}

// 결과 출력
console.log(result);
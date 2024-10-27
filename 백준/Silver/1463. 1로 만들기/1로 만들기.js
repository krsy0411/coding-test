// 입력 숫자
const input = Number(require('fs').readFileSync('/dev/stdin').toString());
// 메모이제이션을 위한 배열 : index는 해당 숫자, 값은 연산 횟수를 의미
const dp = new Array(input+1).fill(0);

for(let i=2; i<=input; i++) {
    // 우선 현재의 수에서 1을 빼는 경우
    dp[i] = dp[i-1] + 1;
    // 만약, 값이 2로 나누어 떨어지면
    if(i%2 === 0) {
        dp[i] = Math.min(dp[i], dp[i/2]+1);
    }
    // 만약, 값이 3으로 나누어 떨어지면
    if(i%3 === 0) {
        dp[i] = Math.min(dp[i],dp[i/3]+1);
    }
}

// 결과
console.log(dp[input]);
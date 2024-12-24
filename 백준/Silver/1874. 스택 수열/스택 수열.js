const [n, ...nums] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const result = []; // + or -
const stack = [];
let currentIndex = 0; // 현재 수열의 인덱스

for(let i=1; i<=n; i++) {            
        stack.push(i);
        result.push('+');    
        
        // 스택 최상단 값이 현재 수열 값과 같은 경우
        while(stack.length > 0 && stack[stack.length - 1] === nums[currentIndex]) {
            stack.pop();
            result.push('-');
            currentIndex += 1;
        }
}

// 스택에 원소가 남은 경우 -> 수열을 만들 수 없는 경우
if(stack.length > 0) {
    console.log('NO');
} else {
    // 수열을 만들 수 있는 경우
    console.log(result.join('\n'));
}
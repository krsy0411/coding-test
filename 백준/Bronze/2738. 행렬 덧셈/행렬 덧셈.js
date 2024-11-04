const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);
// 입력 데이터에 대한 행렬
const matrix1 = [];
const matrix2 = [];

// 행렬에 원소 저장
for(let i=1; i<=N; i++) {
    const row = input[i].split(' ').map(Number);
    matrix1.push(row);
}

// 두번째 행렬 데이터를 덧셈하고 결과처리용 변수에 저장
for(let i=N+1; i<=2*N; i++) {
    const row = input[i].split(' ').map(Number);
    matrix2.push(row);
}

// 두 행렬 덧셈하고 결과 출력
for(let i=0; i<N; i++) {
    let result = [];
    for(let j=0; j<M; j++) {
        result.push(matrix1[i][j] + matrix2[i][j]);
    }
    
    console.log(result.join(' '));
}
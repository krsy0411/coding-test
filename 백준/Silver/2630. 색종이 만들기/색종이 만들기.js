const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const result = [];

const N = Number(input[0]);
const paper = input.slice(1).map(row => row.split(' ').map(Number));

let white = 0;
let blue = 0;
// 함수 구현
function count(x,y,size) {
    const baseColor = paper[x][y];
    let same = true;
    
    // 사이즈 내에서 컬러들이 동일한지 확인
    for(let i=x; i<x+size; i++) {
        for(let j=y; j<y+size; j++) {
            if(paper[i][j] !== baseColor) {
                same = false;
                break;
            }
        }
        if(!same) break;
    }
    
    if(same) {
        if(baseColor === 0) white++;
        else blue++;
    } else {
        const newSize = size/2;
        
        // 새로 자른 사이즈를 기준으로 재귀
        count(x,y,newSize);
        count(x, y+newSize, newSize);
        count(x+newSize, y, newSize);
        count(x+newSize, y+newSize, newSize);
    }
}

count(0,0,N); // 함수 실행
console.log(`${white}\n${blue}`);
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0]);
const arr = input[1].split(' ').map(Number).reverse();
const result = [];

function lowerBound(array,target) {
    let left = 0;
    let right = array.length;
    
    while(left < right) {
        let mid = Math.trunc((left+right) / 2);
        
        if(array[mid] < target) {
            left = mid +1;
        } else {
            right = mid;
        }
    }
    
    return left;
}

for(x of arr) {
    const index = lowerBound(result, x);
    
    if(index === result.length) {
        result.push(x);
    } else {
        result[index] = x;
    }
}

console.log(n - result.length);
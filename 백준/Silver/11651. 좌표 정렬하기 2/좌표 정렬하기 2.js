const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const arr = input.slice(1).map(line => line.split(' ').map(Number));

arr.sort((a,b) => {
    let [xa,ya] = a; 
    let [xb,yb] = b;
    
    if(ya === yb) {
        return xa - xb;
    }
    
    return ya - yb;
});

console.log(arr.map(element => element.join(' ')).join('\n'));
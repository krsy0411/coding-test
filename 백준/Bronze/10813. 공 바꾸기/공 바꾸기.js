const inputs = require('fs').readFileSync('/dev/stdin').toString().split('\n');
const [n,m] = inputs[0].split(' ').map(value => Number(value));
let resultArray = new Array(n).fill(0).map((_, index) => index+1);

function change(a,b) {
    let temp = resultArray[a];
    resultArray[a] = resultArray[b];
    resultArray[b] = temp;
}

for(let i=1; i<=m; i++) {
    let [first,second] = inputs[i].split(' ').map(value => Number(value));
    if(first === second) {
        continue;
    }
    change(first-1, second-1);
}

console.log(resultArray.join(' '));
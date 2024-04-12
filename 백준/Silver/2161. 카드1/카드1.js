const fs = require('fs');
const filePath = process.platform === 'linux' ? '/dev/stdin' : './input.txt';
let n = +fs.readFileSync(filePath).toString();

let cards = Array.from({length: n}, (_,i) => i+1);
const answer = [];

while(answer.length != n) {
    answer.push(cards.shift());
    cards.push(cards.shift());
}

console.log(answer.join(" "));
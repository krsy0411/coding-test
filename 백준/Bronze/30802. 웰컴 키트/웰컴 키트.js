const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const sizes = input[1].split(' ').map(Number);
const [T,P] = input[2].split(' ').map(Number);

let tshirt = 0;
let totalPeople = 0;
for(let size of sizes) {
    tshirt += Math.ceil(size / T);
    totalPeople += size;
};

let penSet = Math.floor(totalPeople / P);
let penLeft = totalPeople % P;

console.log(`${tshirt}\n${penSet} ${penLeft}`)
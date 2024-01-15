const fs = require("fs");
let input = fs.readFileSync("/dev/stdin").toString().split("\n");

for(let i=0; i<input.length; i++) {
    if(input[i] !== '') {
        let oneLineArray = input[i].split(" ").map(item => Number(item));
        console.log(oneLineArray[0] + oneLineArray[1]);
    }
}
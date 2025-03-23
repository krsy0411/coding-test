const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N,M] = input[0].split(' ').map(Number);

const pokemonDict = {};
const pokemonList = [""];
// N개만큼의 입력 데이터 처리
for(let i=1; i<=N; i++) {
    const name = input[i];
    pokemonDict[name] = i;
    pokemonList[i] = name;
}

const result = [];
// M개만큼의 출력 데이터 처리
for(let i=N+1; i<=N+M; i++) {
    const test = input[i];
    
    if(isNaN(test)) {
        result.push(pokemonDict[test]); // 문자 테스트
    } else {
        result.push(pokemonList[Number(test)]); // 숫자 테스트
    }
}
    
console.log(result.join('\n'));
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const gradeMap = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
};

let totalScore = 0; // 총 점수
let totalCredit = 0; // 총 학점

// 입력 데이터 처리
for (let i = 0; i < 20; i++) {
    const [subject, credit, grade] = input[i].split(' ');
    const creditNum = parseFloat(credit); // 부동소수점으로 변환

    // P 등급은 계산에서 제외
    if (grade === 'P') continue;

    // 점수 계산
    totalScore += creditNum * gradeMap[grade];
    totalCredit += creditNum;
}

// 전공평점 계산 및 출력
const gpa = totalScore / totalCredit;
console.log(gpa.toFixed(6)); // 소수점 이하 6자리 출력
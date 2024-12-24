function solution(strings, n) {
    var answer = [...strings];
    
    answer.sort((a,b) => {
        if(a[n] === b[n]) {
            return a.localeCompare(b);
        }
        
        return a[n].localeCompare(b[n]);
    }) 
    
    return answer;
}
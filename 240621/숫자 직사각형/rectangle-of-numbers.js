const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split(" ");

const n = Number(input[0]);
const m = Number(input[1]);

arr = Array(n).fill(0).map(()=>Array(m).fill(0))
console.log(arr)

var cnt = 0

for(let i=0;i<n;i++){
    let ans = ''
    for(let j=0;j<m;j++){
        cnt+=1
        arr[i][j]=cnt
        ans+=`${arr[i][j]} `
    }
    console.log(ans)
}
const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split('\n');
let n = Number(input[0].split(" ")[0])
let m = Number(input[0].split(" ")[1])

let arr1 = input.slice(1,n+1).map((num) => num.split(' ').map(Number));
let arr2 = input.slice(n+1,n*2+1).map((row) => row.split(' ').map(Number));


for(let i=0;i<n;i++){
    ans = Array()
    for(let j=0;j<m;j++){
        if (arr1[i][j]==arr2[i][j]){
            ans.push(0)
        }
        else{
            ans.push(1)
        }
    }
    console.log(ans.join(" "))
}
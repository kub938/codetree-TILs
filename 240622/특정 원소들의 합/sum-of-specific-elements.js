const fs = require('fs')
const input = fs.readFileSync(0).toString().trim().split('\n')

let ans = 0
for(let i=0;i<4;i++){
    let arr = input[i].split(' ').map(Number)
    for(let j=0;j<i+1;j++){
        ans+=arr[j]
    }
}

console.log(ans)
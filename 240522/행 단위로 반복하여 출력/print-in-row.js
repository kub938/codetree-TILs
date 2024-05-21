const fs = require('fs');
let n = Number(fs.readFileSync(0).toString().trim())

for(let i=1;i<n+1;i++){
    let ans = ''
    for(let j=1;j<n+1;j++){
        ans+=j
    }
    console.log(ans)
}
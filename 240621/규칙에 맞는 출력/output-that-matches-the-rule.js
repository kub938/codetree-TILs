const fs = require('fs');
const n = Number(fs.readFileSync(0).toString().trim());

let i = n
while(i>0){
    ans = Array()
    for(let j=i;j<n+1;j++){
        ans.push(j)
    }
    console.log(ans.join(" "))
    i--
}
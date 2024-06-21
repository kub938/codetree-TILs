const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split("\n");

for(let i=0;i<3;i++){
    let ans = Array()
    for(let j=0;j<5;j=j+2){
        ans.push(input[i][j]*input[i+4][j])
    }
    console.log(ans.join(" "))
}
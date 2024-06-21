const fs = require('fs');
const input = fs.readFileSync(0).toString().trim().split('\n')
const n = Number(input[0])
const arr= input[1].split(' ').map(Number);

let ans = arr[1] - arr[0];
for(let i =0;i<n-1;i++){
    for(let j=i+1;j<n;j++){
        let result = Math.abs(arr[i]-arr[j])
        if (ans>result){
           ans = result 
        }
    }
}

console.log(ans)
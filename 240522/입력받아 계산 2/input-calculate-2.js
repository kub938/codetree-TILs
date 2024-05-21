const fs = require('fs');
let a = fs.readFileSync(0).toString().split(" ").map(Number);

let ans = a[0]*a[1]
console.log(ans)
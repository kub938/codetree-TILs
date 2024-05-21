const fs = require('fs');
let a = fs.readFileSync(0).toString().split(" ").map(Number);

console.log(a[0]+a[1])
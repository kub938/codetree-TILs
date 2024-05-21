const fs = require('fs');
let arr = fs.readFileSync(0).toString().split(" ").map(Number);
let a = arr[1]
let b = arr[0]

console.log(a,b)
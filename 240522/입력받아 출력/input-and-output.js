const fs = require('fs');
input = fs.readFileSync(0).toString().split("\n").map(Number)

console.log(input[0],input[1])
const fs = require('fs')
const input = Number(fs.readFileSync(0).toString().trim());

const result = input.toFixed(2)

console.log(result)
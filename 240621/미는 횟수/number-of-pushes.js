const fs = require('fs')
let input = fs.readFileSync(0).toString().trim().split('\n')

let s = input[0].split('')
let target = input[1].split('')

let ans = 0
let check = true
while(s.join(',')!=target){
    ans+=1
    if (ans>s.length){
        check = false
        break
    }
    let tmp = s.pop()
    s = [...tmp,...s]
}

if (check){
    console.log(ans)
}
else{
    console.log(-1)
}
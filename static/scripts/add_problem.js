let testcaseBtn = document.getElementById("tc-btn")
let testCases = document.getElementById("test-cases")
let cnt = 1

testcaseBtn.addEventListener("click" , function(){

    let style = `display: flex;
    flex-direction: row;
    justify-content: flex-start;
    gap: 10px;`
    testCases.innerHTML += `
    <div style = "${style}">
        <textarea style = "flex:3" name = ${"input" + cnt} rows="" cols=""></textarea>
        <textarea style = "flex:3" name = ${"output" + cnt} rows="" cols=""></textarea>
        <input style = "flex:1" type = "checkbox" name = ${"show" + cnt} class = "tc-checkbox">
    </div>
    `    

    cnt += 1
})

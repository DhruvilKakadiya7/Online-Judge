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
        <textarea name = ${"input" + cnt} rows="" cols=""></textarea>
        <textarea name = ${"output" + cnt} rows="" cols=""></textarea>
    </div>
    `    

    cnt += 1
})

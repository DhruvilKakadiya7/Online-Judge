function getId(t , s){
    let id = ""
    let skip = t.length
    for(let index = skip ; index < s.length ; index++){
        id += s[index]
    }
    console.log(id);
    return id
}

let comment_div = document.getElementById("comment-div")

let all_reply_span = comment_div.getElementsByClassName("reply-comment-span")


for(let i = 0 ; i < all_reply_span.length ; i++){
    let reply_btn = all_reply_span[i]
    reply_btn.onclick = function(event){
        let div = document.getElementById("div_" + getId("reply_" , event.target.id))
        if(div.style.display != "flex"){
            div.style.display = "flex"
        }
        else{
            div.style.display = "none"
        }
    }
}

let all_cancle_btn = comment_div.getElementsByClassName("cancle-class")
let all_reply_btn = comment_div.getElementsByClassName("reply-class")

for(let i = 0 ; i < all_cancle_btn.length ; i++){
    let cancle_btn = all_cancle_btn[i]
    cancle_btn.onclick = function(event){
        let div = document.getElementById("div_" + getId("cancel_btn_" , event.target.id))
        div.style.display = "none"
    }
}

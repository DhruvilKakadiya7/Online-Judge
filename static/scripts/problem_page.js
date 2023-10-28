let btn = document.getElementById("submit-btn")

btn.addEventListener("click" , function(){
    if(document.getElementById("id_source_file").files.length > 0){
        showToast("File submitted" , "info")
    }
    else{
        showToast("Select the file" , "error")
    }
})
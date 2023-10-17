
function showToast(message , type) {
    const toast = document.querySelector('.toast');
    const toastMessage = toast.querySelector('.toast-message');
    toastMessage.textContent = message;
    toast.classList.add('show');
    if(type == "info"){
        toast.style.backgroundColor = "yellow"
        toast.classList.add('info')
    }
    else{
        toast.style.backgroundColor = "red"
        toast.classList.add('info')
    }
    setTimeout(() => {
        toast.classList.remove('show');
        if(type == "info"){
            toast.classList.remove('info')
        }
        else{
            toast.classList.remove('error')
        }
    }, 2000); // Hide the toast after 3 seconds
}
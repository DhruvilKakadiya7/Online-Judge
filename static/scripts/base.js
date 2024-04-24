
let target = document.getElementById("change-theme")
const root = document.documentElement;


function setTheme(theme){
    window.localStorage.setItem("algobooth_theme" , JSON.stringify(theme))
}

function getTheme(theme){
    return JSON.parse(window.localStorage.getItem("algobooth_theme"))
}

function lightTheme(){
    root.style.setProperty('--color-a', '#9400FF');
    root.style.setProperty('--color-a-low', '#8ECDDD');
    root.style.setProperty('--color-a-theme-1', '#AED2FF');
    root.style.setProperty('--color-a-theme-2', '#E4F1FF');
    root.style.setProperty('--color-b', '#192655');
    root.style.setProperty('--color-c', '#3876BF');
    root.style.setProperty('background-color', 'white');
}

function darkTheme(){
    root.style.setProperty('--color-a', '#45FFCA');
    root.style.setProperty('--color-a-low', 'rgba(69,255,202,0.5)');
    root.style.setProperty('--color-a-theme-1', 'rgb(34, 34, 34)');
    root.style.setProperty('--color-a-theme-2', 'rgb(67, 66, 66)');
    root.style.setProperty('--color-b', 'yellow');
    root.style.setProperty('--color-c', 'white');
    root.style.setProperty('background-color', '#001524');
}

function toggleTheme(){
    if(getTheme() == "dark"){
        setTheme("light")
    }
    else{
        setTheme("dark")
    }
}

function applyTheme(){
    if(getTheme() == "dark"){
        darkTheme()
    }
    else{
        lightTheme()
    }
}

target.addEventListener("click" , function(){
    toggleTheme()
    applyTheme()
})

applyTheme()


function setUserID(id){
    window.localStorage.setItem("algobooth_user_id" , JSON.stringify(id))
}

function getUserID(id){
    let result = window.localStorage.getItem("algobooth_user_id")
    return JSON.parse(result)
}

if(getUserID){
    
}

// let drop = document.getElementById("profile-select").onchange = function(event){
//     let value = event.target.value
    
//     if(value == "profile_page"){
//         if(window.location.href.endsWith("profile_page/")){
//             ;
//         }
//         else{
//             console.log(window.location.href);
//             window.location.href = "profile_page"
//         }
//     }
//     else{
//         window.location.href = "logout"
//     }
// }


document.getElementById("drop-icon").onclick = function(){
    let menu = document.getElementById("menu")
    
    if(menu.style.display != "flex"){
        menu.style.display = "flex"
    }
    else{
        menu.style.display = "none"
    }
}
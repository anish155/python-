function Msg(){
    let click=document.getElementById("name").value.trim();
    if (click === ""){
        alert("Not input given!")
    }
    else{
        alert("Name stored Successfully!")
    }
}
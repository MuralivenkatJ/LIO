function dropdown()
{
    let dropdown_cont = document.getElementById("dropdown-cont")
    
    if( dropdown_cont.className.indexOf("w3-show") == -1 )
        dropdown_cont.className += " w3-show";
    else
        dropdown_cont.className = dropdown_cont.className.replace(" w3-show", "")
}

function dropdownm()
{
    let dropdown_cont = document.getElementById("dropdown-cont-m")

    if( dropdown_cont.className.indexOf("w3-show") == -1 )
        dropdown_cont.className += " w3-show";
    else
        dropdown_cont.className = dropdown_cont.className.replace(" w3-show", "")
}
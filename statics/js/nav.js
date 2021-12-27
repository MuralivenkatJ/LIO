function collapseBar()
{
    let bar = document.getElementById("collapse");

    /*  displaying the bar-block when width is small
        to do this the class name is 'w3-show'
        if the bar is clicked then 
        1) we will   add     'w3-show'                     if it doesnot have one
        2) we will   replace 'w3-show' with empty string   if it already have one
    */

    if(bar.className.indexOf("w3-show") == -1)         // it doesnot have 'w3-show' class
        bar.className += " w3-show";
    else
        bar.className = bar.className.replace(" w3-show", "");
}
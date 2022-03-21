var upload_page = document.getElementsByClassName("grid-cont")[0];
var main_page = document.getElementsByClassName("main")[0];
upload_page.addEventListener('click', function(e){
    close_form(e);
})

function open_form()
{
    upload_page.style.zIndex = "2";
    main_page.style.position = "fixed";
}


function close_form(e)
{
    form = document.getElementsByClassName("grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        upload_page.style.zIndex = "-2";
        main_page.style.position = "unset";
    }
}

$(document).ready(function()
{
    setHeight();
})

function setHeight()
{
    let screen = document.getElementsByClassName("screen")[0];
    let main   = document.getElementsByClassName("main")[0];

    let height = Math.max(upload_page.clientHeight, main.clientHeight, screen.clientHeight);

    console.log(upload_page.clientHeight, main.clientHeight, screen.clientHeight)

    screen.style.height = height.toString() + "px";
}
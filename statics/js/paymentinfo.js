var payment_page = document.getElementsByClassName("grid-cont")[0];
var main_page = document.getElementsByClassName("page")[0];

payment_page.addEventListener('click', function(e){
    close_form(e);
})

function open_form()
{
    payment_page.style.zIndex = "1";
    main_page.style.position = "fixed";
}

function close_form(e)
{
    let form = document.getElementsByClassName("grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        payment_page.style.zIndex = "-1";
        main_page.style.position = "unset";
    }
}
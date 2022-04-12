var main_page = document.getElementsByClassName("main")[0];

// LOGIN 1
function visible1(){
    let eye = document.getElementById('l1-eye')
    let input = document.getElementById('l1-pass-input')
    let type = input.getAttribute('type')
 
    if (type == "password")
       input.setAttribute('type','text')
    else 
       input.setAttribute('type','password')
}
 
var login_page1 = document.getElementsByClassName("l1-grid-cont")[0];
login_page1.addEventListener('click', function(e){
    close_form1(e);
})
 
function open_form1()
{
    main_page.style.position = "fixed";
    login_page1.style.zIndex = "1";
    login_page1.style.position = "absolute";
}
 
function close_form1(e)
{
    let form = document.getElementsByClassName("l1-grid")[0].getBoundingClientRect();
 
    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        main_page.style.position = "unset";
        login_page1.style.zIndex = "-2";
        login_page1.style.position = "fixed";
    }
}

// LOGIN 2
function visible2(){
    let eye = document.getElementById('l2-eye')
    let input = document.getElementById('l2-pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
         input.setAttribute('type','password')
}

var login_page2 = document.getElementsByClassName("l2-grid-cont")[0];
login_page2.addEventListener('click', function(e){
   close_form2(e);
})

function open_form2()
{
    main_page.style.position = "fixed";
    login_page2.style.zIndex = "1";
    login_page2.style.position = "absolute";
}

function close_form2(e)
{
    let form = document.getElementsByClassName("l2-grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.      clientY>form.bottom)
    {
        main_page.style.position = "unset";
        login_page2.style.zIndex = "-2";
        login_page2.style.position = "fixed";
    }
}


// LOGIN 3
function visible3(){
    let eye = document.getElementById('l3-eye')
    let input = document.getElementById('l3-pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
         input.setAttribute('type','password')
}

var login_page3 = document.getElementsByClassName("l3-grid-cont")[0];
login_page3.addEventListener('click', function(e){
   close_form3(e);
})

function open_form3()
{
    main_page.style.position = "fixed";
    login_page3.style.zIndex = "1";
    login_page3.style.position = "absolute";
}

function close_form3(e)
{
    let form = document.getElementsByClassName("l3-grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        main_page.style.position = "unset";
        login_page3.style.zIndex = "-2";
        login_page3.style.position = "fixed";
    }
}
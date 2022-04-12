var main_page = document.getElementsByClassName("main")[0];

// SIGN UP 1
function s1_visible(){
    let eye = document.getElementById('s1-eye')
    let input = document.getElementById('s1-pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
         input.setAttribute('type','password')
}

function s1_visible1(){
   let eye = document.getElementById('s1-eye1')
   let input = document.getElementById('s1-c_pass-input')
   let type = input.getAttribute('type')

   if (type == "password")
      input.setAttribute('type','text')
   else 
        input.setAttribute('type','password')
}

var sform1 = document.getElementsByClassName("s1-grid-cont")[0];
sform1.addEventListener('click', function(e){
    close_sform1(e)
})

function open_sform1()
{
    let lform = document.getElementsByClassName("l1-grid-cont")[0];
    main_page.style.position = "fixed";
    lform.style.zIndex = "-2";
    sform1.style.zIndex = "1";
    sform1.style.position = "absolute";
}

function close_sform1(e)
{
    let form = document.getElementsByClassName("s1-grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        main_page.style.position = "unset";
        sform1.style.zIndex = "-2";
        sform1.style.position = "fixed";
    }
}



// SIGN UP2
function s2_visible(){
    let eye = document.getElementById('s2-eye')
    let input = document.getElementById('s2-pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
        input.setAttribute('type','password')
}
function s2_visible1(){
    let eye = document.getElementById('s2-eye1')
    let input = document.getElementById('s2-c_pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
        input.setAttribute('type','password')
}

var sform2 = document.getElementsByClassName("s2-grid-cont")[0];
sform2.addEventListener('click', function(e){
    close_sform2(e)
})

function open_sform2()
{
    let lform = document.getElementsByClassName("l2-grid-cont")[0];
    main_page.style.position = "fixed";
    lform.style.zIndex = "-2";
    sform2.style.zIndex = "1";
    sform2.style.position = "absolute";
}

function close_sform2(e)
{
    let form = document.getElementsByClassName("s2-grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        main_page.style.position = "unset";
        sform2.style.zIndex = "-2";
        sform2.style.position = "fixed";
    }
}



// SIGN UP3
function s3_visible(){
    let eye = document.getElementById('s3-eye')
    let input = document.getElementById('s3-pass-input')
    let type = input.getAttribute('type')
 
    if (type == "password")
        input.setAttribute('type','text')
    else 
        input.setAttribute('type','password')
}
 
function s3_visible1(){
    let eye = document.getElementById('s3-eye1')
    let input = document.getElementById('s3-pass-input1')
    let type = input.getAttribute('type')
 
    if (type == "password")
        input.setAttribute('type','text')
    else 
        input.setAttribute('type','password')
}

var sform3 = document.getElementsByClassName("s3-grid-cont")[0];
sform3.addEventListener('click', function(e){
    close_sform3(e)
})

function open_sform3()
{
    let lform = document.getElementsByClassName("l3-grid-cont")[0];
    main_page.style.position = "fixed";
    lform.style.zIndex = "-2";
    sform3.style.zIndex = "1";
    sform3.style.position = "absolute";
}

function close_sform3(e)
{
    let form = document.getElementsByClassName("s3-grid")[0].getBoundingClientRect();

    if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
    {
        main_page.style.position = "unset";
        sform3.style.zIndex = "-2";
        sform3.style.position = "fixed";
    }
}

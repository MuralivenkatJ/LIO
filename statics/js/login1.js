function visible1(){
   let eye = document.getElementById('l1-eye')
   let input = document.getElementById('l1-pass-input')
   let type = input.getAttribute('type')

   if (type == "password")
      input.setAttribute('type','text')
   else 
      input.setAttribute('type','password')
}

var login_page = document.getElementsByClassName("l1-grid-cont")[0];
login_page.addEventListener('click', function(e){
   close_form1(e);
})

function open_form1()
{
   login_page.style.zIndex = "1";
}

function close_form1(e)
{
   let form = document.getElementsByClassName("l1-grid")[0].getBoundingClientRect();

   if( e.clientX<form.left || e.clientX>form.right || e.clientY<form.top || e.clientY>form.bottom)
   {
      login_page.style.zIndex = "-2";
   }
}
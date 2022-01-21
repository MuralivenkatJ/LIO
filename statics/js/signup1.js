function visible(){
    let eye = document.getElementById('eye')
    let input = document.getElementById('pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
         input.setAttribute('type','password')
}

function visible1(){
   let eye = document.getElementById('eye1')
   let input = document.getElementById('c_pass-input')
   let type = input.getAttribute('type')

   if (type == "password")
      input.setAttribute('type','text')
   else 
        input.setAttribute('type','password')
}
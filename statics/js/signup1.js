function visible(){
    let eye = document.getElementById('s1-eye')
    let input = document.getElementById('s1-pass-input')
    let type = input.getAttribute('type')

    if (type == "password")
       input.setAttribute('type','text')
    else 
         input.setAttribute('type','password')
}

function visible1(){
   let eye = document.getElementById('s1-eye1')
   let input = document.getElementById('s1-c_pass-input')
   let type = input.getAttribute('type')

   if (type == "password")
      input.setAttribute('type','text')
   else 
        input.setAttribute('type','password')
}
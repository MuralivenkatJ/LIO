function visible(){
   let eye = document.getElementById('eye')
   let input = document.getElementById('pass-input')
   let type = input.getAttribute('type')

   if (type == "password")
      input.setAttribute('type','text')
   else 
      input.setAttribute('type','password')
}
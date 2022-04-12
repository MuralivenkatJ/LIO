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
   let input = document.getElementById('s2-pass-input1')
   let type = input.getAttribute('type')

   if (type == "password")
      input.setAttribute('type','text')
   else 
       input.setAttribute('type','password')
}
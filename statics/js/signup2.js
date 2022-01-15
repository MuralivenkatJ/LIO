function validate()
{
   let pass1 = document.getElementById('pass-input').value;
   let pass2 = doucment.getElementById('c_pass-input').value;

   if(pass1 != pass2)
   {
      alert("Passwords do not match");
      return false;
   }
   return true;
}

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
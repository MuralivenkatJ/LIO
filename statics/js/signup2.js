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
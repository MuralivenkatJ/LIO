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
function readMoreD()
{
    let text = document.querySelector('#d-text')
    let readmore = document.querySelector('#d-readmore')

    let values = window.getComputedStyle(text)
    let overflow = values.getPropertyValue("overflow")

    if(overflow == "hidden")
    {
        text.style.overflow = "visible"
        text.style.height = "auto"
        readmore.innerHTML = "Read less"
    }
    else if(overflow == "visible")
    {
        text.style.overflow = "hidden"
        text.style.height = "50px"
        readmore.innerHTML = "Read more"
    }
}

function readMoreQ()
{
    let quali1 = document.getElementById("quali1")
    let quali2 = document.getElementById("quali2")

    quali1.style.display = "none"
    quali2.style.display = "block"
}

function readLessQ()
{
    let quali1 = document.getElementById("quali1")
    let quali2 = document.getElementById("quali2")

    quali1.style.display = "block"
    quali2.style.display = "none"
}
var media_query1 = window.matchMedia("(min-width: 700px)")
var media_query2 = window.matchMedia("(max-width: 700px)")

$(document).ready(function()
{
    loadvideo()
})

function loadvideo()
{
    let video_cont = document.getElementById("video-cont")
    let width = video_cont.clientWidth;
    var height = (9 / 16 * width) + 2;
    video_cont.style.height = height.toString() + "px";

    if(media_query1.matches)
    {
        let page = document.getElementById("page")
        let title_height = page.clientHeight - (height + 130)
        // title.style.height = title_height.toString() + "px"

        let title = document.getElementById("title")
        let desc = document.getElementById("desc")

        title.style.width = document.getElementById("video-cont").clientWidth.toString() + "px"
        desc.style.width = document.getElementById("video-cont").clientWidth.toString() + "px"
        title.style.height = "25px"
        desc.style.height = (title_height - 25).toString() + "px"
        desc.style['overflow-y'] = "scroll"
    }
    
}

$(window).resize(function() 
{ 
    location.reload()
});

function more()
{

    if(media_query2.matches)
    {
        let more = document.getElementById("more")
        let desc = document.getElementById("desc")

        let page = document.getElementById("page")
        
        if(desc.clientHeight == 15)
        {
            let video = document.getElementById("video")
            let v_height = video.clientHeight

            desc.style.height = ( window.innerHeight - (100 + v_height) ).toString() + "px"
            desc.style["overflow-y"] = "scroll"

            // page.style.height = "100vh"
            // page.style["overflow-y"] = "hidden"

            more.innerHTML = "&lt;"
        }
        else
        {
            desc.style.height = "15px"
            desc.style["overflow-y"] = "hidden"

            // page.style.height = "unset"
            // page.style["overflow-y"] = "unset"
            
            more.innerHTML = "&gt;"
        }
    }
    
}

var prev = null;
function play(details)
{
    let video = document.getElementById("video")
    let v_id = details.getAttribute("data-vId")
    video.setAttribute("src", `https://www.youtube.com/embed/${v_id}?rel=0&autoplay=1&modestbranding=1`)

    let title = document.getElementById("title")
    let desc = document.getElementById("desc")

    let divs = details.childNodes;
    let v_t = divs[7].textContent
    let v_d = "<span id='more' onclick='more()'>&gt;</span>" + divs[11].textContent

    title.innerHTML = v_t;
    desc.innerHTML = v_d;

    let cur = details;
    if(prev != null)
    {
        let old_val = prev.getAttribute("class")
        let new_val = old_val.replace(" w3-grey", "")
        prev.setAttribute("class", new_val)
    }
    let old_val = cur.getAttribute("class")
    let new_val = old_val + " w3-grey"
    cur.setAttribute("class", new_val)

    prev = cur;

    let more = document.getElementById("more")
    if(media_query2.matches)
        more.style.display = "block"
}
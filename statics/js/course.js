var media_query1 = window.matchMedia("(min-width: 700px)")
var media_query2 = window.matchMedia("(max-width: 700px)")

var player;
var duration;
var currentTime;
var timeInterval;

// This function will set the width and height of the video
function size()
{
    let video_cont = document.getElementById("video-cont")
    let w = video_cont.clientWidth;
    let h = (9 / 16 * w) + 2;
    video_cont.style.height = h.toString() + "px";

    player.setSize(width=w, height=h)
}

/* PLAYER API */ 
// 1. Loading the script
function loadScript() {

    if (typeof(YT)=='undefined' || typeof(YT.Player)=='undefined') 
    {
        var tag = document.createElement('script');
        tag.src = "https://www.youtube.com/iframe_api";
        var firstScriptTag = document.getElementsByTagName('script')[0];
        firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
    }
}

/* 2. Player object is created after loading the script
        soon after the script is loaded, that script will call onYouTubePlayerAPIReady() function. On calling this function we will create the player object.
*/
window.onYouTubePlayerAPIReady = function() {
    // console.log("youtube player api is ready");
};
function onYouTubePlayer(videoId)
{
    player = new YT.Player("player", {
        videoId: videoId,
        playerVars: {
            rel: 0,
            autoplay: 1
        }
    });

    loadvideo();
}

loadScript();

// Time tracker (if video is 90% completed then )
function timeTracker(index)
{
    timeInterval = setInterval(function(){
        if(duration == undefined || duration == 0)
            duration = parseInt(player.getDuration());
        currentTime = parseInt(player.getCurrentTime());
        // console.log(currentTime, duration);

        if( (currentTime >= (0.95*duration)) && index != -1)
        {
            updateStatus(index);
            index = -1;
        }
    }, 1000);
}

// Update watch status of the video
function updateStatus(index)
{
    let c_id = document.getElementsByClassName("content-container")[0].getAttribute("data-cId");

    $.get("http://127.0.0.1:8000/course/watched/"+c_id+"/"+index, function(data){
        console.error("data : ", data)
    })
}


/* On calling play() function we will change the title, desc and 
    also the video(which is done by loading the player with new 
    video id with the help of function loadVideoById())
*/
var prev = null;
function play(details)
{
    let video_cont = document.getElementById("video-cont");
    let image = document.getElementById("image");
    image.style.display = "none";
    video_cont.style.display = "block";


    //Creating player for the first time
    let v_id = details.getAttribute("data-vId");
    if(player == undefined)
    {
        onYouTubePlayer(v_id);
    }
    // loading the video
    else
    {
        player.loadVideoById({'videoId': v_id});
        duration = player.getDuration();
    }

    // Time tracker
    index = details.getAttribute("data-index");
    if(timeInterval)
        clearInterval(timeInterval);
    timeTracker(index);


    let title = document.getElementById("title")
    let desc = document.getElementById("desc")

    let divs = details.childNodes;
    let v_t = divs[5].textContent
    let v_d = "<span id='more' onclick='more()'>&gt;</span>" + divs[9].textContent

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

    if(height <= 20)
    {
        let image = document.getElementById("image");
        let width = image.clientWidth;
        height = (9 / 16 * width) + 2;
        image.style.height = height.toString() + "px";
    }

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

    if(player != undefined)
        size();
    
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
            let video = document.getElementById("player")
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
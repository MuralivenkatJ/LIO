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

function secondsToMinutes(duration)
{
    let hour = Math.floor(duration / 3600);
    let minute = Math.floor( (duration - hour*3600) / 60);
    let seconds = duration - (hour*3600) - (minute*60);

    let total_duration = ""
    if(hour > 0)
        total_duration += hour.toString() + ":";
    total_duration += minute.toString() + ":" + seconds.toString();

    return total_duration;
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
    console.log(typeof(YT.Player));
    player = new YT.Player("player", {
        videoId: videoId,
        playerVars: {
            rel: 0,
            autoplay: 1,
            controls: 0
        }
    });

    loadvideo();
}

loadScript();

// Time tracker (if video is 90% completed then )
function timeTracker(index)
{
    var progress_bar = document.getElementsByClassName("progress-bar")[0];
    var percent = 0;
    var time = document.getElementsByClassName("time")[0];

    timeInterval = setInterval(function(){
        if(duration == undefined || duration == 0)
            duration = parseInt(player.getDuration());
        currentTime = parseInt(player.getCurrentTime());
        // console.log(currentTime, duration);

        percent = (currentTime / duration) * 100;
        progress_bar.style.width = percent.toString() + "%";

        let t1 = secondsToMinutes(currentTime)
        let t2 = secondsToMinutes(duration)
        time.innerHTML = t1 + "/" + t2;

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

    if(prev == null)
        controllsOffTimeout = setTimeout(controlsOff1, 5000);

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



// CONTROLS
function pauseplay()
{
    let status = player.getPlayerState();
    let icon = document.getElementById("pauseplay-icon");
    let className = icon.getAttribute("class");
    let newClassName = '';

    if(status == 2)
    {
        player.playVideo()
        if(className.indexOf("fa-pause-circle") == -1)
        {
            newClassName = className.replace("fa-play-circle", "fa-pause-circle");
            icon.setAttribute("class", newClassName);
        }
    }
    else if(status == 1)
    {
        player.pauseVideo()
        if(className.indexOf("fa-play-circle") == -1)
        {
            newClassName = className.replace("fa-pause-circle", "fa-play-circle");
            icon.setAttribute("class", newClassName);
        }
    }

    clearTimeout(controllsOffTimeout);
    controllsOffTimeout = setTimeout(controlsOff1, 5000);
}

var seekInterval;
var seekToTime;
function previous10s()
{
    seekToTime = parseInt(player.getCurrentTime());
    seekToTime -= 10;
    player.seekTo(seekToTime, true);

    clearTimeout(controllsOffTimeout);
    controllsOffTimeout = setTimeout(controlsOff1, 5000);
}

function next10s()
{
    seekToTime = parseInt(player.getCurrentTime());
    seekToTime += 10;
    player.seekTo(seekToTime, true);
    
    clearTimeout(controllsOffTimeout);
    controllsOffTimeout = setTimeout(controlsOff1, 5000);
}

// CONTROLS ON
let layer = document.getElementsByClassName("layer")[0];
layer.addEventListener('click', function(e){
    controlsOn(e)
});
function controlsOn(e)
{
    let controls_cont = document.getElementById("controls-cont");
    controls_cont.style.zIndex = "2";
    var controllsOffTimeout = setTimeout(controlsOff1, 5000);
}

// CONTROLS OFF
let previous = document.getElementById("previous10s");
previous.addEventListener('click', function(e){
    controlsOff(e);
});
let pause = document.getElementById("pauseplay");
pause.addEventListener('click', function(e){
    controlsOff(e);
});
let next = document.getElementById("next10s");
next.addEventListener('click', function(e){
    controlsOff(e);
});
function controlsOff(e)
{
    if(controllsOffTimeout)
        clearTimeout(controllsOffTimeout);
    let rect = document.getElementsByClassName("fa")[0].getBoundingClientRect();

    if(e.clientX>rect.left && e.clientX<rect.right && e.clientY>rect.top && e.clientY<rect.bottom)
        return;

    rect = document.getElementsByClassName("fa")[1].getBoundingClientRect();
    if(e.clientX>rect.left && e.clientX<rect.right && e.clientY>rect.top && e.clientY<rect.bottom)
        return;
    
    rect = document.getElementsByClassName("fa")[2].getBoundingClientRect();
    if(e.clientX>rect.left && e.clientX<rect.right && e.clientY>rect.top && e.clientY<rect.bottom)
        return;
    
    let controls_cont = document.getElementById("controls-cont");
    controls_cont.style.zIndex = "-1";
}

function controlsOff1()
{
    let controls_cont = document.getElementById("controls-cont");
    controls_cont.style.zIndex = "-1";
}
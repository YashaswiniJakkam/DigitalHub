function responsive_nav() {
    var x = document.getElementById("nav-bar");
    if (x.className === "nav") {
        x.className += " responsive";
    } else {
        x.className = "nav";
    }
    console.log("Done")
}

function reveal(){
    var reveals = document.querySelectorAll(".reveal");
    for(var i=0;i<reveals.length;i++){
        var windowHeight = window.innerHeight;
        var elementTop = reveals[i].getBoundingClientRect().top;
        var elementVisible = 150;

        if(elementTop < windowHeight - elementVisible){
            reveals[i].classList.add("active");
        }else{
            reveals[i].classList.remove("active");
        }
    }
}

window.addEventListener("scroll",reveal);
window.addEventListener('load', function() {
    var loader = document.getElementById('loading');
    loader.classList.add("loader--hidden");
    // loader.style.display= "none";
});
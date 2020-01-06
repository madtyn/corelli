window.onload = function () {
    const display = document.querySelector('#countdown');
    let i = 5;
    let countdown = function() {
        display.textContent = String(i--);
    };
    setInterval(countdown, 1000)
};

function redirect(){
    var redirLink = document.querySelector('#redirLink')
    window.location.href = redirLink.href;
}

setTimeout(redirect, 6000); //2000 is equivalent to 2 seconds
let dateNext = document.querySelector('p.date-next strong')
dateNext.innerText = dateNext.innerText.length < 10 ? `0${dateNext.innerText}` : dateNext.innerText;
const d = dateNext.innerText.slice(0, 2)
const m = dateNext.innerText.slice(3, 5)
const y = dateNext.innerText.slice(6, 10)
const h = dateNext.innerText.slice(-5, -3)
const mins = dateNext.innerText.substr(-2)
const nowTime = new Date().getTime();
const endTime = new Date(y, m - 1, d, h, mins).getTime();
const spanD = document.querySelector('span.d');
const spanH = document.querySelector('span.h');
const spanM = document.querySelector('span.m');
const spanS = document.querySelector('span.s');
const timer = document.querySelector('p.timer');

setInterval(() => {
    const nowTime = new Date().getTime();
    // const time = Math.floor((endTime - nowTime) / 1000);
    const time = endTime - nowTime;
    let days = Math.floor((endTime / (1000 * 60 * 60 * 24)) - (nowTime / (1000 * 60 * 60 * 24)));
    let hours = Math.floor((endTime / (1000 * 60 * 60) - nowTime / (1000 * 60 * 60)) % 24);
    let minutes = Math.floor((endTime / (1000 * 60) - nowTime / (1000 * 60)) % 60);
    let secs = Math.floor((endTime / (1000) - nowTime / (1000)) % 60);

    // hours = hours < 10 ? `0${hours}` : hours;
    // secs = secs < 10 ? `0${secs}` : secs;

    spanD.innerText = `${days} d.`;
    spanH.innerText = `${hours} g.`;
    spanM.innerText = minutes < 10 ? `0${minutes} m.` : `${minutes} m.`;
    spanS.innerText = secs < 10 ? `0${secs} s.` : `${secs} s.`;


    if (days == 0) {
        spanD.style.display = 'none';
    };

    if (days == 0 && hours == 0) {
        spanH.style.display = 'none';
        spanM.innerText = `${minutes} m.`;
        spanM.style.color = 'red';
        spanS.style.color = 'red';
    };

    if (days == 0 && hours == 0 && minutes == 0) {
        spanM.style.display = 'none';
        spanS.innerText = `${secs} s.`;
        spanS.style.color = 'red';
    };

    if (days <= 0 && hours <= 0 && minutes <= 0 && secs <= 0) {
        timer.style.display = 'none';
        spanD.style.display = 'none';
        spanH.style.display = 'none';
        spanM.style.display = 'none';
        spanS.style.display = 'none';
    };





    // timer.innerText = (`${days} d. ${hours} g. ${minutes} m. ${secs} s.`)

    // if (days == 1) {
    //     days = `${days} dzień`
    // } else {
    //     days = `${days} dni`
    // }

    // if (hours == 0) {
    //     hours = `${hours} godzin`
    // } else if (hours == 1) {
    //     hours = `${hours} godzina`
    // } else {
    //     hpurs = `${hours} godzin`
    // }
}, 1000)
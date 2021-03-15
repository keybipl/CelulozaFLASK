const clubs = {
    budowlani: "budowlani.png",
    celuloza: "logo.png",
    wartas: "warta.jpg",
    piast: "piast.png",
    wartag: "wartag.png",
    lubuszanin: "lubuszanin.png",
    roza: "roza.jpg",
    orzel: "orzel.gif",
    toroma: "toroma.png",
    zjednoczeni: "zjednoczeni.gif",
    spartak: "spartak.jpg",
    gkp: "gkp.jpg",
    polonia: "polonia.jpg",
    lucznik: "lucznik.jpg",
    kasztelania: "kasztelania.png",
    radowiak: "radowiak.jpg",
    blekitni: "blekitni.jpg",
}

const change = [...document.querySelectorAll('.change')];
const club = [...document.querySelectorAll('.club')]

for (let i = 0; i < change.length; i++) {
    if (club[i].innerText == 'Budowlani Murzynowo') {
        change[i].src = `/static/images/${clubs.budowlani}`;
    };
    if (club[i].innerText == 'Warta Słońsk') {
        change[i].src = `/static/images/${clubs.wartas}`;
    };
    if (club[i].innerText == 'Piast Karnin (Gorzów Wielkopolski)') {
        change[i].src = `/static/images/${clubs.piast}`;
    };
    if (club[i].innerText == 'Warta II Gorzów Wielkopolski') {
        change[i].src = `/static/images/${clubs.wartag}`;
    };
    if (club[i].innerText == 'Lubuszanin Drezdenko') {
        change[i].src = `/static/images/${clubs.lubuszanin}`;
    };
    if (club[i].innerText == 'Róża Różanki') {
        change[i].src = `/static/images/${clubs.roza}`;
    };
    if (club[i].innerText == 'Orzeł Międzyrzecz') {
        change[i].src = `/static/images/${clubs.orzel}`;
    };
    if (club[i].innerText == 'Toroma Torzym') {
        change[i].src = `/static/images/${clubs.toroma}`;
    };
    if (club[i].innerText == 'Zjednoczeni Przytoczna') {
        change[i].src = `/static/images/${clubs.zjednoczeni}`;
    };
    if (club[i].innerText == 'Spartak Deszczno') {
        change[i].src = `/static/images/${clubs.spartak}`;
    };
    if (club[i].innerText == 'GKP Pszczew') {
        change[i].src = `/static/images/${clubs.gkp}`;
    };
    if (club[i].innerText == 'Polonia Lipki Wielkie') {
        change[i].src = `/static/images/${clubs.polonia}`;
    };
    if (club[i].innerText == 'Łucznik Strzelce Krajeńskie') {
        change[i].src = `/static/images/${clubs.lucznik}`;
    };
    if (club[i].innerText == 'Kasztelania Santok') {
        change[i].src = `/static/images/${clubs.kasztelania}`;
    };
    if (club[i].innerText == 'Radowiak Drezdenko') {
        change[i].src = `/static/images/${clubs.radowiak}`;
    };
    if (club[i].innerText == 'Błękitni Lubno') {
        change[i].src = `/static/images/${clubs.blekitni}`;
    };

}
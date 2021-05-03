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
    pomologia: "pomologia.png",
    rakow: "rakow.png",
    miedz: "miedz.jpg",
    stilon: "stilon.jpg",
    brzeg: "brzeg.png"
}

const change = [...document.querySelectorAll('.change')];
const club = [...document.querySelectorAll('.club')]

for (let i = 0; i < change.length; i++) {
    if (club[i].innerText.toUpperCase() == 'Budowlani Murzynowo'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.budowlani}`;
    };
    if (club[i].innerText.toUpperCase() == 'TS Celuloza'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.celuloza}`;
    };
    if (club[i].innerText.toUpperCase() == 'Warta Słońsk'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.wartas}`;
    };
    if (club[i].innerText.toUpperCase() == 'Piast Karnin (Gorzów Wielkopolski)'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.piast}`;
    };
    if (club[i].innerText.toUpperCase() == 'Warta II Gorzów Wielkopolski'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.wartag}`;
    };
    if (club[i].innerText.toUpperCase() == 'Lubuszanin Drezdenko'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.lubuszanin}`;
    };
    if (club[i].innerText.toUpperCase() == 'Róża Różanki'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.roza}`;
    };
    if (club[i].innerText.toUpperCase() == 'Orzeł Międzyrzecz'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.orzel}`;
    };
    if (club[i].innerText.toUpperCase() == 'Toroma Torzym'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.toroma}`;
    };
    if (club[i].innerText.toUpperCase() == 'Zjednoczeni Przytoczna'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.zjednoczeni}`;
    };
    if (club[i].innerText.toUpperCase() == 'Spartak Deszczno'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.spartak}`;
    };
    if (club[i].innerText.toUpperCase() == 'GKP Pszczew'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.gkp}`;
    };
    if (club[i].innerText.toUpperCase() == 'Polonia Lipki Wielkie'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.polonia}`;
    };
    if (club[i].innerText.toUpperCase() == 'Łucznik Strzelce Krajeńskie'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.lucznik}`;
    };
    if (club[i].innerText.toUpperCase() == 'Kasztelania Santok'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.kasztelania}`;
    };
    if (club[i].innerText.toUpperCase() == 'Radowiak Drezdenko'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.radowiak}`;
    };
    if (club[i].innerText.toUpperCase() == 'Błękitni Lubno'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.blekitni}`;
    };
    if (club[i].innerText.toUpperCase() == 'PLUKS POMOLOGIA PRÓSZKÓW'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.pomologia}`;
    };
    if (club[i].innerText.toUpperCase() == 'RKS RAKÓW CZĘSTOCHOWA S.A.'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.rakow}`;
    };
    if (club[i].innerText.toUpperCase() == 'MIEDŹ LEGNICA'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.miedz}`;
    };
    if (club[i].innerText.toUpperCase() == 'STILON GORZÓW WLKP.'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.stilon}`;
    };
    if (club[i].innerText.toUpperCase() == 'BTP STAL BRZEG'.toUpperCase()) {
        change[i].src = `/static/images/${clubs.brzeg}`;
    };

}
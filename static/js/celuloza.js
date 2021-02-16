const column = [...document.querySelectorAll('.all')];

for (let i = 0; i < column.length; i++) {
    let a = column[i].innerText
    if (a == 'Celuloza Kostrzyn nad Odrą' || a == 'TS CELULOZA KOSTRZYN N/O') {
        column[i].parentElement.style.backgroundColor = 'rgba(13, 110, 253, 0.1)';
        column[i].style.fontWeight = 'bold';
        column[i].style.textTransform = 'uppercase';
        column[i].innerText = 'TS Celuloza'
    };
}
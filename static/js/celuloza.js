const column = [...document.querySelectorAll('.all')];
const term = [...document.querySelectorAll('.term')];

for (let i = 0; i < column.length; i++) {
    let a = column[i].innerText
    if (a == 'Celuloza Kostrzyn nad Odrą' || a == 'TS CELULOZA KOSTRZYN N/O') {
        column[i].parentElement.style.backgroundColor = 'rgba(13, 110, 253, 0.1)';
        column[i].style.fontWeight = 'bold';
        column[i].style.textTransform = 'uppercase';
        column[i].innerText = 'TS Celuloza'
    };
}

for (let i = 0; i < term.length; i++) {
    t = term[i].innerText
    a = t.replace(' ', '.').replace('lipca', '07').replace('sierpnia', '08').replace('września', '09').replace('października', '10').replace('listopada', '11').replace('marca', '03').replace('kwietnia', '04').replace('maja', '05').replace('czerwca', '06')
    term[i].innerText = a
}
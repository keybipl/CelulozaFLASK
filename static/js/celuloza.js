const column = [...document.querySelectorAll('.all')];

for (let i = 0; i < column.length; i++) {
    let a = column[i].innerText
    if (a == 'Celuloza Kostrzyn nad Odrą') {
        column[i].parentElement.style.backgroundColor = 'rgba(219, 219, 219, 0.5)';
        column[i].style.fontWeight = 'bold';
        column[i].style.textTransform = 'uppercase';
    };
}
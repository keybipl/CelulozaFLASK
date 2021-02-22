const news = [...document.querySelectorAll('.news')];
const newsLink = [...document.querySelectorAll('.news-link')];
const pFirst = [...document.querySelectorAll('.news p:first-child')];
const pLast = [...document.querySelectorAll('.news p:last-child')];

for (let i = 0; i < news.length; i++) {
    if (news[i].innerText.length > 500) {
        a = news[i].innerHTML;
        // b = a.slice(0, 500);
        b = pFirst[i].innerHTML;
        news[i].innerHTML = b;
        // p = document.querySelector('.news p:last-child');
        console.log(b);
        const node = document.createElement("a");
        node.href = newsLink[i].href;
        const textnode = document.createTextNode('   ...więcej');
        node.appendChild(textnode);
        news[i].appendChild(node);
    }
}
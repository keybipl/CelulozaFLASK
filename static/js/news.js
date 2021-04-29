const news = [...document.querySelectorAll('.news')];
const newsLink = [...document.querySelectorAll('.news-link')];
const pFirst = [...document.querySelectorAll('.news p:first-child')];

for (let i = 0; i < news.length; i++) {
    if (news[i].innerText.length > 800) {
        a = news[i].innerHTML;
        b = pFirst[i].innerHTML;
        news[i].innerHTML = b;
        console.log(b);
        const node = document.createElement("a");
        node.href = newsLink[i].href;
        const textnode = document.createTextNode('   ...więcej');
        node.appendChild(textnode);
        news[i].appendChild(node);
    }
}
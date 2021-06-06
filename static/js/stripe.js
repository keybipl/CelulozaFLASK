const stripe = document.querySelector(".stripe");
const navbar = document.querySelector(".navbar");
const header = document.querySelector("header");

console.log(stripe);

window.addEventListener("scroll", function () {
    stripe.style.display = "none";
    navbar.style.top = "0";
    header.style.height = "100px";
})




// window.onscroll = function() {scrollFunction()};
//
// function bottom() {
//   if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
//     stripe.style.display = "block";
//   } else {
//     stripe.style.display = "none";
//   }
// }
//
// // When the user clicks on the button, scroll to the bottom of the document
// function bottom() {
//   document.body.scrollTop = 0;
//   document.documentElement.scrollTop = 5555550;
// }
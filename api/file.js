//old
const links = [
" ",
];

var chooseRandom = Math.floor(Math.random() * links.length);

document.getElementById("image").innerHTML = " " + links[chooseRandom] + " ";

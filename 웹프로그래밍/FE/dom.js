// DOM = Document Object Model
// html 최상위 엘리먼트 = document
document.getElementById("nav-cart-count");
document.getElementById("nav-cart-count").style.display = "none"; // 삭제
document.getElementById("nav-cart-count").style.display = "block"; // 요소를 표시, 줄바꿈을 해줌
document.getElementById("nav-cart-count").innerText = "있어";

// querySelector는 DOM을 찾는데 유용
document.querySelector("div"); // div를 찾아줌
document.querySelector("#nav-cart-count"); // id를 찾아줌
document.querySelector(".nav-cart-count"); // class를 찾아줌
document.querySelector("body .nav-line-2");
document.querySelector("nav-line-2 > .nav-arrow");

// 참고로 querySelectorAll은 모든 DOM을 찾아준다.
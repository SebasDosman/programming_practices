const track = document.querySelector(".carousel"); 
const [slideOne, slideTwo] = Array.from(track.children); 
const dotsNav = document.querySelector(".carousel-buttons");
const [dotOne, dotTwo] = Array.from(dotsNav.children);


dotOne.addEventListener("click", (e) => {
    slideOne.classList.add("active");
    slideTwo.classList.remove("active");
    dotOne.classList.add("selected");
    dotTwo.classList.remove("selected");
});

dotTwo.addEventListener("click", (e) => {
    slideTwo.classList.add("active");
    slideOne.classList.remove("active");
    dotTwo.classList.add("selected");
    dotOne.classList.remove("selected");
});
const audio = document.querySelector("audio");
const play = document.querySelector(".play");
const playIcon = document.querySelector(".play .fa-solid");
// const repeat = document.querySelector(".repeat");
// const repeatIcon = document.querySelector(".repeat .fa-solid");

const PAUSE_ICON = "fa-solid fa-circle-pause";
const PLAY_ICON = "fa-solid fa-circle-play";
// const REPEAT_ICON = "fa-solid fa-repeat";


play.addEventListener("click", () => {
  if (audio.paused) {
    audio.play();
    playIcon.className = PAUSE_ICON;
  } else {
    audio.pause();
    playIcon.className = PLAY_ICON;
  }
});

audio.addEventListener("ended", () => {
  playIcon.className = PLAY_ICON;
});

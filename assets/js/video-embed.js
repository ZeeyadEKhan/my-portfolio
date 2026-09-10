// Demo video embeds: the poster and play button sit above the iframe so the
// page shows a still until the visitor asks for the video. One click reveals
// the player. Nothing autoplays.
(function () {
  document.querySelectorAll('.video-embed').forEach(function (box) {
    var play = box.querySelector('.video-play');
    var poster = box.querySelector('.video-poster');
    function reveal() { box.classList.add('is-playing'); }
    if (play) play.addEventListener('click', reveal);
    if (poster) poster.addEventListener('click', reveal);
  });
})();

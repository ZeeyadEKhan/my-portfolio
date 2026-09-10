// Demo video embeds: the poster and play button sit above a hidden iframe so
// the page shows a still until the visitor asks for the video. One click
// reveals the player. Nothing autoplays. While the iframe src is still the
// REPLACE_WITH_VIDEO_EMBED placeholder the poster stays put, so a visitor
// never sees a broken frame.
(function () {
  document.querySelectorAll('.video-embed').forEach(function (box) {
    var iframe = box.querySelector('iframe');
    var play = box.querySelector('.video-play');
    var poster = box.querySelector('.video-poster');
    var src = iframe ? iframe.getAttribute('src') || '' : '';
    var ready = src && src.indexOf('REPLACE_WITH_VIDEO_EMBED') === -1;
    function reveal() { if (ready) box.classList.add('is-playing'); }
    if (play) play.addEventListener('click', reveal);
    if (poster) poster.addEventListener('click', reveal);
  });
})();

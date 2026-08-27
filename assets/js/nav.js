// Mobile disclosure menu. Inert at desktop widths: the toggle button is
// display:none above 640px and this script only acts when it is visible.
(function () {
  var btn = document.querySelector('.nav-toggle');
  var nav = document.getElementById('site-nav');
  if (!btn || !nav) return;

  function isOpen() { return btn.getAttribute('aria-expanded') === 'true'; }

  function open() {
    btn.setAttribute('aria-expanded', 'true');
    document.body.classList.add('nav-open');
    var first = nav.querySelector('a');
    if (first) first.focus();
  }

  function close(returnFocus) {
    btn.setAttribute('aria-expanded', 'false');
    document.body.classList.remove('nav-open');
    if (returnFocus) btn.focus();
  }

  btn.addEventListener('click', function () {
    isOpen() ? close(true) : open();
  });

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && isOpen()) close(true);
  });

  nav.addEventListener('click', function (e) {
    if (e.target.closest('a')) close(false);
  });
})();

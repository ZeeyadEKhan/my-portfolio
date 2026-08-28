/* Lightbox accessibility layer, shared by every case study page.
   Each page ships its own small lightbox script; this file adds the
   dialog behaviors they lack without touching their open and close
   logic: dialog semantics on dynamically built overlays, focus moved
   to the close button on open, Tab trapped inside the overlay, and
   focus returned to the thumbnail that opened it. Loaded with defer,
   so the page's own lightbox (including Lumi's dynamically created
   overlay) already exists when this runs. */
(function () {
  var overlay = document.getElementById('lightbox') ||
                document.querySelector('.lightbox-overlay');
  if (!overlay) return;

  if (!overlay.hasAttribute('role')) overlay.setAttribute('role', 'dialog');
  if (!overlay.hasAttribute('aria-modal')) overlay.setAttribute('aria-modal', 'true');
  if (!overlay.hasAttribute('aria-label')) overlay.setAttribute('aria-label', 'Image viewer');

  var opener = null;

  /* Capture phase so this runs regardless of the page's own handlers. */
  document.addEventListener('click', function (e) {
    var img = e.target.closest && e.target.closest('.img-wrap img, .img-cell img, .hero-img, .content img');
    if (img) opener = img;
  }, true);

  function isOpen() {
    return overlay.classList.contains('open') || overlay.classList.contains('active');
  }

  function focusables() {
    return Array.prototype.filter.call(
      overlay.querySelectorAll('button, [href], [tabindex]:not([tabindex="-1"])'),
      function (el) { return el.offsetParent !== null || overlay.contains(el); }
    );
  }

  var wasOpen = false;
  new MutationObserver(function () {
    var open = isOpen();
    if (open && !wasOpen) {
      var f = focusables();
      if (f.length) f[0].focus();
    } else if (!open && wasOpen && opener) {
      if (!opener.hasAttribute('tabindex')) opener.setAttribute('tabindex', '-1');
      opener.focus();
    }
    wasOpen = open;
  }).observe(overlay, { attributes: true, attributeFilter: ['class'] });

  document.addEventListener('keydown', function (e) {
    if (e.key !== 'Tab' || !isOpen()) return;
    var f = focusables();
    if (!f.length) return;
    var first = f[0], last = f[f.length - 1];
    if (e.shiftKey && (document.activeElement === first || !overlay.contains(document.activeElement))) {
      e.preventDefault();
      last.focus();
    } else if (!e.shiftKey && (document.activeElement === last || !overlay.contains(document.activeElement))) {
      e.preventDefault();
      first.focus();
    }
  }, true);
})();

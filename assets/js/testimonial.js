// Renders a pull quote into .case-testimonial only when /data/testimonials.json
// has an entry for the page's data-project slug. With no entry (or a fetch
// failure) the slot stays empty and takes up no space.
//
// Entry shape, keyed by project slug:
//   "legaleey": { "quote": "...", "name": "...", "role": "...", "org": "..." }
// quote and name are required; role and org are optional.
(function () {
  var slot = document.querySelector('.case-testimonial[data-project]');
  if (!slot) return;
  var slug = slot.getAttribute('data-project');
  fetch('/data/testimonials.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) {
      if (!data) return;
      var t = data[slug];
      if (!t || !t.quote || !t.name) return;
      var quote = document.createElement('blockquote');
      quote.className = 'case-quote';
      var text = document.createElement('p');
      text.className = 'case-quote-text';
      text.textContent = t.quote;
      var attrib = document.createElement('footer');
      attrib.className = 'case-quote-attrib';
      attrib.textContent = [t.name, t.role, t.org].filter(Boolean).join(', ');
      quote.appendChild(text);
      quote.appendChild(attrib);
      slot.appendChild(quote);
    })
    .catch(function () {});
})();

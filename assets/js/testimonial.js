// "What collaborators say" — renders into .case-testimonial[data-project]
// only when /data/testimonials.json has entries for that slug. The data file
// ships as {} so nothing renders anywhere until real quotes exist.
//
// HOW TO ENABLE once real quotes are available:
//   1. Add an entry to /data/testimonials.json keyed by the page slug
//      (the data-project value; case studies use their folder name,
//      the About page uses "about"):
//        "legaleey": [
//          { "quote": "...", "name": "...", "role": "...", "relationship": "..." }
//        ]
//      quote and name are required; role and relationship are optional.
//      One to three quotes per page render; extras are ignored.
//   2. For the About page, also uncomment the slot div and the script tag
//      marked in about.html.
// No placeholder or sample quotes may ever be added to the JSON.
(function () {
  var slot = document.querySelector('.case-testimonial[data-project]');
  if (!slot) return;
  var slug = slot.getAttribute('data-project');
  fetch('/data/testimonials.json')
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (data) {
      if (!data) return;
      var entries = data[slug];
      if (!entries) return;
      if (!Array.isArray(entries)) entries = [entries];
      entries = entries.filter(function (t) { return t && t.quote && t.name; }).slice(0, 3);
      if (!entries.length) return;

      var heading = document.createElement('p');
      heading.className = 'case-testimonial-heading';
      heading.textContent = 'What collaborators say';
      slot.appendChild(heading);

      entries.forEach(function (t) {
        var quote = document.createElement('blockquote');
        quote.className = 'case-quote';
        var text = document.createElement('p');
        text.className = 'case-quote-text';
        text.textContent = t.quote;
        var attrib = document.createElement('footer');
        attrib.className = 'case-quote-attrib';
        attrib.textContent = [t.name, t.role, t.relationship].filter(Boolean).join(', ');
        quote.appendChild(text);
        quote.appendChild(attrib);
        slot.appendChild(quote);
      });
    })
    .catch(function () {});
})();

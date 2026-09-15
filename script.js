// Navigation remains ordinary anchor links when JavaScript is unavailable.
const chapters = [...document.querySelectorAll('.chapter-nav a')];
const sections = chapters.map(link => document.querySelector(link.hash));
let pending = false;

function updateChapter() {
  const headerBottom = document.querySelector('.site-header').getBoundingClientRect().bottom;
  let active = null;
  for (const section of sections) {
    if (section.getBoundingClientRect().top <= headerBottom + 100) active = section.id;
  }
  for (const link of chapters) {
    if (link.hash === `#${active}`) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
  pending = false;
}

function scheduleUpdate() {
  if (!pending) {
    pending = true;
    requestAnimationFrame(updateChapter);
  }
}

window.addEventListener('scroll', scheduleUpdate, { passive: true });
window.addEventListener('resize', scheduleUpdate);
window.addEventListener('pageshow', scheduleUpdate);
updateChapter();

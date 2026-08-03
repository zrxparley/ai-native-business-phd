// 教材导航交互

// Toggle sidebar
function toggleSidebar() {
  const sidebar = document.getElementById('sidebar');
  const main = document.getElementById('mainContent');
  if (sidebar.classList.contains('collapsed')) {
    sidebar.classList.remove('collapsed');
    sidebar.classList.remove('mobile-open');
    main.classList.remove('sidebar-collapsed');
  } else {
    sidebar.classList.add('collapsed');
    main.classList.add('sidebar-collapsed');
  }
}

// TOC search filter
function filterTOC() {
  const query = document.getElementById('tocSearch').value.toLowerCase();
  const items = document.querySelectorAll('.toc-item');
  items.forEach(item => {
    const text = item.textContent.toLowerCase();
    if (text.includes(query) || query === '') {
      item.classList.remove('hidden');
    } else {
      item.classList.add('hidden');
    }
  });
}

// Smooth scroll to anchor
function navTo(event, anchor) {
  event.preventDefault();
  const target = document.getElementById(anchor);
  if (target) {
    const offset = 70;
    const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
    window.scrollTo({ top: top, behavior: 'smooth' });
  }
}

// Index page search
function filterIndexCards() {
  const query = document.getElementById('indexSearch').value.toLowerCase();
  const cards = document.querySelectorAll('.index-card');
  let visibleSections = new Set();
  cards.forEach(card => {
    const text = card.textContent.toLowerCase();
    if (text.includes(query) || query === '') {
      card.classList.remove('hidden');
      // Track which section this card belongs to
      const section = card.closest('.index-card-grid');
      if (section) {
        const title = section.previousElementSibling;
        if (title) visibleSections.add(title);
      }
    } else {
      card.classList.add('hidden');
    }
  });
  // Show/hide section titles
  document.querySelectorAll('.index-section-title').forEach(title => {
    title.style.display = visibleSections.has(title) || query === '' ? '' : 'none';
    if (query !== '' && visibleSections.has(title)) {
      title.style.display = '';
    } else if (query !== '') {
      title.style.display = 'none';
    } else {
      title.style.display = '';
    }
  });
}

// Highlight active TOC item on scroll
function updateActiveTOC() {
  const headings = document.querySelectorAll('.content-body h1, .content-body h2, .content-body h3');
  const tocLinks = document.querySelectorAll('.toc-item a');
  if (!headings.length || !tocLinks.length) return;

  let activeId = '';
  const scrollPos = window.scrollY + 100;

  headings.forEach(h => {
    if (h.offsetTop <= scrollPos) {
      activeId = h.id;
    }
  });

  tocLinks.forEach(link => {
    const href = link.getAttribute('href').replace('#', '');
    if (href === activeId) {
      link.style.color = '#fff';
      link.style.borderLeftColor = 'var(--sidebar-active)';
      link.style.background = 'var(--sidebar-hover)';
    } else {
      link.style.color = '';
      link.style.borderLeftColor = '';
      link.style.background = '';
    }
  });
}

// Throttled scroll listener
let scrollTimeout;
window.addEventListener('scroll', () => {
  if (scrollTimeout) cancelAnimationFrame(scrollTimeout);
  scrollTimeout = requestAnimationFrame(updateActiveTOC);
});

// Init
document.addEventListener('DOMContentLoaded', () => {
  // Auto-scroll TOC to current position
  updateActiveTOC();

  // Handle initial hash
  if (window.location.hash) {
    const target = document.getElementById(window.location.hash.slice(1));
    if (target) {
      setTimeout(() => {
        const offset = 70;
        const top = target.getBoundingClientRect().top + window.pageYOffset - offset;
        window.scrollTo({ top: top });
      }, 300);
    }
  }
});

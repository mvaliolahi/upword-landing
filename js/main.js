/* ============================================
   Upword Landing — Main JavaScript
   ============================================ */

(function () {
  'use strict';

  /* ===== Persian numeral conversion ===== */
  function toPersianDigits(num) {
    const persian = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
    return String(num).replace(/\d/g, (d) => persian[d]);
  }

  /* ===== Scroll progress bar ===== */
  const progressBar = document.getElementById('scrollProgress');
  function updateScrollProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    progressBar.style.width = pct + '%';
  }

  /* ===== Navbar scrolled state ===== */
  const navbar = document.getElementById('navbar');
  function updateNavbar() {
    if (window.scrollY > 20) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
  }

  function onScroll() {
    updateScrollProgress();
    updateNavbar();
  }
  window.addEventListener('scroll', onScroll, { passive: true });

  /* ===== Mobile nav toggle ===== */
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  navToggle.addEventListener('click', () => {
    navToggle.classList.toggle('active');
    navLinks.classList.toggle('open');
  });
  navLinks.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      navToggle.classList.remove('active');
      navLinks.classList.remove('open');
    });
  });

  /* ===== Reveal on scroll ===== */
  const revealEls = document.querySelectorAll(
    '.feature-card, .step, .testimonial, .faq-item, .screen-mockup, .mascot-content, .mascot-visual, .section-head, .stats-row > *'
  );
  revealEls.forEach((el, i) => {
    el.classList.add('reveal');
    el.setAttribute('data-delay', String((i % 4) + 1));
  });

  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12, rootMargin: '0px 0px -50px 0px' }
  );
  revealEls.forEach((el) => io.observe(el));

  /* ===== Number counter animation ===== */
  function animateCounter(el) {
    const target = parseInt(el.getAttribute('data-count'), 10);
    const suffix = el.getAttribute('data-suffix') || '';
    const duration = 1800;
    const startTime = performance.now();

    function tick(now) {
      const elapsed = now - startTime;
      const progress = Math.min(elapsed / duration, 1);
      // ease-out cubic
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * target);
      el.textContent = toPersianDigits(current) + suffix;
      if (progress < 1) {
        requestAnimationFrame(tick);
      } else {
        el.textContent = toPersianDigits(target) + suffix;
      }
    }
    requestAnimationFrame(tick);
  }

  const counters = document.querySelectorAll('[data-count]');
  const counterIO = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterIO.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.5 }
  );
  counters.forEach((el) => counterIO.observe(el));

  /* ===== Lottie animations ===== */
  function loadLottie(containerId, path, opts) {
    const el = document.getElementById(containerId);
    if (!el || typeof lottie === 'undefined') return;
    lottie.loadAnimation({
      container: el,
      renderer: 'svg',
      loop: opts && opts.loop !== undefined ? opts.loop : true,
      autoplay: opts && opts.autoplay !== undefined ? opts.autoplay : true,
      path: path,
      rendererSettings: {
        preserveAspectRatio: 'xMidYMid meet',
      },
    });
  }

  // Hero floating turtles
  loadLottie('heroTurtle1', 'assets/lottie/turtle-swimming.json');
  loadLottie('heroTurtle2', 'assets/lottie/turtle-water.json');

  // Steps turtles
  loadLottie('stepTurtle1', 'assets/lottie/turtle-show.json');
  loadLottie('stepTurtle2', 'assets/lottie/turtle-success.json');
  loadLottie('stepTurtle3', 'assets/lottie/turtle-progress.json');

  // Mascot turtle (large, central)
  loadLottie('mascotTurtle', 'assets/lottie/turtle-ninja.json');

  // Screenshot achievement turtle
  loadLottie('achievementTurtle', 'assets/lottie/turtle-success.json', { loop: true });

  // Final CTA turtle
  loadLottie('ctaTurtle', 'assets/lottie/turtle-meditation.json');

  /* ===== Smooth scroll for anchor links (with navbar offset) ===== */
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href === '#' || href === '#!') return;
      const target = document.querySelector(href);
      if (!target) return;
      e.preventDefault();
      const offset = 72; // navbar height
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  /* ===== FAQ: only one open at a time ===== */
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach((item) => {
    item.addEventListener('toggle', () => {
      if (item.open) {
        faqItems.forEach((other) => {
          if (other !== item) other.open = false;
        });
      }
    });
  });

  /* ===== Initial calls ===== */
  updateScrollProgress();
  updateNavbar();
})();

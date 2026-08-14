/* ============================================
   AREEBA ZAFAR - PORTFOLIO JAVASCRIPT
   Typewriter, Scroll Reveal, Counters, Nav Links
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ============ NAVBAR ============
  const navbar = document.getElementById('navbar');
  let lastScroll = 0;

  // Show navbar after a short delay
  setTimeout(() => {
    navbar.classList.add('visible');
    // Ensure navbar is translated down initially
    navbar.style.transform = 'translateY(0)';
  }, 300);

  window.addEventListener('scroll', () => {
    const currentScroll = window.pageYOffset;

    if (currentScroll > 50) {
      navbar.classList.add('scrolled');
      navbar.style.borderBottomColor = 'rgba(34, 211, 238, 0.15)';
    } else {
      navbar.classList.remove('scrolled');
      navbar.style.borderBottomColor = 'transparent';
    }

    lastScroll = currentScroll;
  });

  // ============ ACTIVE NAV LINK ============
  const sections = document.querySelectorAll('section[id]');
  const navLinksAll = document.querySelectorAll('nav a, .mobile-menu a');

  function setActiveNav() {
    const scrollY = window.pageYOffset + 120;

    sections.forEach(section => {
      const sectionTop = section.offsetTop;
      const sectionHeight = section.offsetHeight;
      const sectionId = section.getAttribute('id');

      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        navLinksAll.forEach(link => {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + sectionId) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  window.addEventListener('scroll', setActiveNav);

  // ============ FIX DESKTOP NAV DIV WRAPPERS ============
  // Nav links are wrapped in div[tabindex="0"] - add keyboard & click support
  document.querySelectorAll('nav div[tabindex="0"]').forEach(div => {
    div.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        const link = div.querySelector('a');
        if (link) link.click();
      }
    });
  });

  // ============ MOBILE MENU ============
  const mobileMenuBtn = document.getElementById('mobileMenuBtn');
  const mobileMenu = document.getElementById('mobileMenu');

  mobileMenuBtn.addEventListener('click', () => {
    mobileMenuBtn.classList.toggle('active');
    mobileMenu.classList.toggle('active');
    document.body.style.overflow = mobileMenu.classList.contains('active') ? 'hidden' : '';
  });

  // Close mobile menu on link click
  document.querySelectorAll('.mobile-menu a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenuBtn.classList.remove('active');
      mobileMenu.classList.remove('active');
      document.body.style.overflow = '';
    });
  });

  // ============ TYPEWRITER EFFECT ============
  const typewriterEl = document.getElementById('typewriter');
  const roles = [
    'Software Engineer',
    'Full-Stack Developer',
    'Computer Science Graduate',
    'AI/ML Enthusiast',
    'Problem Solver'
  ];
  let roleIndex = 0;
  let charIndex = 0;
  let isDeleting = false;
  let typeSpeed = 80;

  function typeWriter() {
    if (!typewriterEl) return;
    const currentRole = roles[roleIndex];

    if (!isDeleting) {
      typewriterEl.textContent = currentRole.substring(0, charIndex + 1);
      charIndex++;

      if (charIndex === currentRole.length) {
        isDeleting = true;
        typeSpeed = 2000; // Pause at end
      } else {
        typeSpeed = 80 + Math.random() * 40;
      }
    } else {
      typewriterEl.textContent = currentRole.substring(0, charIndex - 1);
      charIndex--;

      if (charIndex === 0) {
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        typeSpeed = 400; // Pause before new word
      } else {
        typeSpeed = 40;
      }
    }

    setTimeout(typeWriter, typeSpeed);
  }

  // Start typewriter
  setTimeout(typeWriter, 800);

  // ============ COUNTER ANIMATION ============
  function animateCounters() {
    const counters = document.querySelectorAll('[data-count]');
    counters.forEach(counter => {
      const target = parseInt(counter.dataset.count);
      const duration = 2000;
      const startTime = performance.now();

      function updateCounter(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        const eased = 1 - Math.pow(1 - progress, 4); // easeOutQuart
        const current = Math.round(eased * target);

        counter.textContent = current + (target >= 6 ? '+' : '');

        if (progress < 1) {
          requestAnimationFrame(updateCounter);
        }
      }

      requestAnimationFrame(updateCounter);
    });
  }

  // Start counters
  setTimeout(animateCounters, 1000);

  // ============ SCROLL REVEAL ANIMATIONS ============
  const observerOptions = {
    root: null,
    rootMargin: '0px 0px -50px 0px',
    threshold: 0.1
  };

  const scrollObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0) scale(1) translateZ(0)';
      }
    });
  }, observerOptions);

  // Observe all parent animate components
  document.querySelectorAll('[style*="opacity:0"], .reveal-item').forEach(el => {
    scrollObserver.observe(el);
  });

  // ============ SMOOTH SCROLL ============
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const targetId = this.getAttribute('href');
      const target = document.querySelector(targetId);
      if (target) {
        // Account for fixed navbar height and add offset to reduce blank space
        const navbarHeight = document.getElementById('navbar')?.offsetHeight || 64;
        const targetTop = target.getBoundingClientRect().top + window.pageYOffset - navbarHeight + 35;
        window.scrollTo({ top: targetTop, behavior: 'smooth' });
      }

      // Close mobile menu if open
      const mobileMenu = document.getElementById('mobileMenu');
      const mobileMenuBtn = document.getElementById('mobileMenuBtn');
      if (mobileMenu && mobileMenu.classList.contains('active')) {
        mobileMenu.classList.remove('active');
        mobileMenuBtn.classList.remove('active');
        document.body.style.overflow = '';
      }
    });
  });

  // ============ CONTACT FORM ============
  window.handleSubmit = function(e) {
    e.preventDefault();

    const btn = e.target.querySelector('.btn-submit');
    const originalHTML = btn.innerHTML;

    btn.innerHTML = 'Sending...';
    btn.disabled = true;

    const formData = new FormData(e.target);
    const data = {
        access_key: "82deeb8a-ce3d-43b8-b05d-d0cffbc12dc1",
        name: formData.get('name'),
        email: formData.get('email'),
        message: formData.get('message'),
        subject: "New Client Contact from Portfolio!",
        from_name: "Portfolio Contact Form"
    };

    fetch("https://api.web3forms.com/submit", {
        method: "POST",
        headers: { 
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
      btn.innerHTML = 'Message Sent!';
      btn.style.background = 'linear-gradient(135deg, #10b981, #059669)';

      setTimeout(() => {
        btn.innerHTML = originalHTML;
        btn.style.background = '';
        btn.disabled = false;
        e.target.reset();
      }, 3000);
    })
    .catch(error => {
      console.error(error);
      btn.innerHTML = 'Error!';
      btn.style.background = '#ef4444'; // red
      setTimeout(() => {
        btn.innerHTML = originalHTML;
        btn.style.background = '';
        btn.disabled = false;
      }, 3000);
    });
  };

  // ============ PROJECTS FILTER V2 ============
  function initProjectsFilter() {
    const filterBtns = document.querySelectorAll('.proj-filter-btn');
    const projectCards = document.querySelectorAll('.project-card-v2');

    if (!filterBtns.length || !projectCards.length) return;

    filterBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        // Remove active class from all buttons
        filterBtns.forEach(b => b.classList.remove('active'));
        // Add active class to clicked button
        btn.classList.add('active');

        const filterValue = btn.getAttribute('data-pfilter');

        projectCards.forEach(card => {
          // Add transition effect
          card.style.transition = 'transform 0.3s ease, opacity 0.3s ease';
          card.style.opacity = '0';
          card.style.transform = 'scale(0.95)';
          
          setTimeout(() => {
            if (filterValue === 'all' || card.getAttribute('data-pcategory') === filterValue) {
              card.classList.remove('pc-hidden');
              // Trigger reflow
              void card.offsetWidth;
              card.style.opacity = '1';
              card.style.transform = 'translateY(0) scale(1) translateZ(0)';
            } else {
              card.classList.add('pc-hidden');
            }
          }, 300);
        });
      });
    });
  }
  initProjectsFilter();

  // ============ CONTACT FAB TOGGLE ============
  const fabBtn = document.getElementById('fabBtn');
  const fabMenu = document.getElementById('fabMenu');
  const fabIconOpen = document.getElementById('fabIconOpen');
  const fabIconClose = document.getElementById('fabIconClose');
  
  if (fabBtn && fabMenu) {
    let fabOpen = false;
    fabBtn.addEventListener('click', () => {
      fabOpen = !fabOpen;
      if (fabOpen) {
        fabMenu.classList.remove('fab-hidden');
        fabMenu.classList.add('fab-visible');
        
        fabIconOpen.style.transform = 'scale(0)';
        fabIconOpen.style.opacity = '0';
        
        fabIconClose.style.transform = 'scale(1)';
        fabIconClose.style.opacity = '1';
      } else {
        fabMenu.classList.add('fab-hidden');
        fabMenu.classList.remove('fab-visible');
        
        fabIconOpen.style.transform = 'scale(1)';
        fabIconOpen.style.opacity = '1';
        
        fabIconClose.style.transform = 'scale(0)';
        fabIconClose.style.opacity = '0';
      }
    });

    // Close FAB when clicking outside
    document.addEventListener('click', (e) => {
      if (fabOpen && !fabBtn.contains(e.target) && !fabMenu.contains(e.target)) {
        fabBtn.click();
      }
    });
  }

  console.log('🚀 Portfolio loaded successfully — Made by Areeba Zafar');
});

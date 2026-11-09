with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ============================================================
# FIX 1: Navbar - reduce "Home" active underline thickness (h-0.5 → h-px)
# also reduce AZ logo size
# ============================================================

# AZ logo: w-10 h-10 md:w-12 md:h-12 → w-8 h-8 md:w-9 md:h-9, text-lg → text-sm
html = html.replace(
    'w-10 h-10 md:w-12 md:h-12 rounded-lg bg-gradient-to-br from-cyan-600 via-blue-800 to-purple-600 flex items-center justify-center shadow-lg shadow-cyan-600/30',
    'w-8 h-8 md:w-9 md:h-9 rounded-lg bg-gradient-to-br from-cyan-500 via-violet-600 to-purple-600 flex items-center justify-center shadow-lg shadow-cyan-500/20'
)
html = html.replace(
    '<span class="text-lg md:text-xl font-bold text-white">AZ</span>',
    '<span class="text-sm md:text-base font-bold text-white">AZ</span>'
)
# Areeba Zafar name in navbar - reduce size
html = html.replace(
    '<span class="text-lg md:text-xl font-semibold text-foreground hidden sm:block">Areeba Zafar</span>',
    '<span class="text-sm md:text-base font-semibold text-foreground hidden sm:block">Areeba Zafar</span>'
)

# Active underline - all nav links: h-0.5 → style with height 1px instead of 2px
# The underline is "h-0.5" which is 2px, replace with inline 1px
html = html.replace(
    'absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-cyan-400 via-blue-500 to-purple-500 transition-transform duration-300 origin-left scale-x-0 group-hover:scale-x-100',
    'absolute bottom-0 left-0 right-0 bg-gradient-to-r from-cyan-400 via-violet-500 to-purple-500 transition-transform duration-300 origin-left scale-x-0 group-hover:scale-x-100'
)
# fix height inline
html = html.replace(
    'absolute bottom-0 left-0 right-0 bg-gradient-to-r from-cyan-400 via-violet-500 to-purple-500 transition-transform duration-300 origin-left scale-x-0 group-hover:scale-x-100',
    'absolute bottom-0 left-0 right-0 bg-gradient-to-r from-cyan-400 via-violet-500 to-purple-500 transition-transform duration-300 origin-left scale-x-0 group-hover:scale-x-100" style="height:1px'
)

print("FIX 1 (navbar/logo): DONE")

# ============================================================
# FIX 2: Hero heading - reduce font size, weight
# "Hi, I'm" h1: 3.8rem → 2.6rem, weight 800 → 700
# "Areeba Zafar" h1: 4rem → 3.2rem, weight 800 → 700
# typewriter h2: 2rem → 1.3rem
# ============================================================
html = html.replace(
    'style="font-size: 3.8rem; font-weight: 800; line-height: 1.1; margin-bottom: 2px; color: white;"',
    'style="font-size: 2.6rem; font-weight: 700; line-height: 1.1; margin-bottom: 2px; color: white;"'
)
html = html.replace(
    'style="font-size: 4rem; font-weight: 800; line-height: 1.1; margin-bottom: 12px;"',
    'style="font-size: 3.2rem; font-weight: 700; line-height: 1.1; margin-bottom: 12px;"'
)
html = html.replace(
    'style="font-size: 2rem; font-weight: 600; margin-bottom: 20px; color: #06b6d4;"',
    'style="font-size: 1.3rem; font-weight: 500; margin-bottom: 20px; color: #22d3ee;"'
)
print("FIX 2 (hero heading size): DONE")

# ============================================================
# FIX 3: Buttons - reduce padding and font size
# btn-primary-shimmer and btn-glass inline styles already in CSS,
# we override via inline style on the anchor
# ============================================================
html = html.replace(
    '<a href="#contact" class="btn-primary-shimmer" style="text-decoration:none;">',
    '<a href="#contact" class="btn-primary-shimmer" style="text-decoration:none;padding:9px 20px;font-size:0.82rem;">'
)
html = html.replace(
    '<a href="Areeba_Zafar_Resume.pdf" download="Areeba_Zafar_Resume.pdf" class="btn-glass" style="text-decoration:none;">',
    '<a href="Areeba_Zafar_Resume.pdf" download="Areeba_Zafar_Resume.pdf" class="btn-glass" style="text-decoration:none;padding:9px 20px;font-size:0.82rem;">'
)
# also reduce icon size 18 → 15
html = html.replace(
    '<a href="#contact" class="btn-primary-shimmer" style="text-decoration:none;padding:9px 20px;font-size:0.82rem;">Get In Touch\n              <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18"',
    '<a href="#contact" class="btn-primary-shimmer" style="text-decoration:none;padding:9px 20px;font-size:0.82rem;">Get In Touch\n              <svg xmlns="http://www.w3.org/2000/svg" width="15" height="15"'
)
print("FIX 3 (buttons): DONE")

# ============================================================
# FIX 4: Remove Bank Management System project (lines 625-656)
# ============================================================
old_bank = """
            <!-- Project 4: Bank -->
            <div class="project-card-v2 reveal-item" data-pcategory="desktop">
              <div class="pc-glow pc-glow-amber"></div>
              <div class="pc-inner">
                <div class="pc-header">
                  <div class="pc-icon-wrap pc-icon-amber">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M3 5V19A9 3 0 0 0 21 19V5"></path><path d="M3 12A9 3 0 0 0 21 12"></path></svg>
                  </div>
                  <div class="pc-badges">
                    <span class="pc-badge pc-badge-amber">Database</span>
                  </div>
                </div>
                <div class="pc-body">
                  <span class="pc-year">2024</span>
                  <h3 class="pc-title">Bank Management System</h3>
                  <p class="pc-desc">Database-driven bank account management handling customer operations, deposits, withdrawals, and transaction records.</p>
                </div>
                <div class="pc-tech-row">
                  <span class="tech-tag">MySQL</span>
                  <span class="tech-tag">SQL Queries</span>
                </div>
                <div class="pc-footer">
                  <a href="https://github.com/areeba-zafar01" target="_blank" rel="noopener noreferrer" class="pc-link pc-link-primary">
                    <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                      <path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path>
                      <path d="M9 18c-4.51 2-5-2-7-2"></path>
                    </svg>
                    Source Code
                  </a>
                </div>
              </div>
            </div>"""

if old_bank in html:
    html = html.replace(old_bank, "")
    print("FIX 4 (removed bank project): DONE")
else:
    print("FIX 4 (bank project): NOT FOUND - check whitespace")

# ============================================================
# FIX 5: Education section - completely redesign as modern cards
# Replace the two plain cards with premium glassmorphism cards
# + add Certificates subsection
# ============================================================
old_edu = """          <div class="max-w-[800px] mx-auto grid grid-cols-1 md:grid-cols-2 gap-6 reveal-item items-stretch">

            <!-- BSCS Card -->
            <div class="w-full h-full rounded-xl border bg-card text-card-foreground shadow-sm card-hover border-border/50 py-10 px-6 flex flex-col items-center justify-center gap-4 text-center">
              <div class="w-14 h-14 rounded-full bg-gradient-to-br from-cyan-500/20 via-blue-500/20 to-purple-500/20 border border-cyan-500/30 flex items-center justify-center text-2xl">
                🎓
              </div>
              <h3 class="text-xl font-bold" style="background: linear-gradient(to right, #22d3ee, #a855f7); -webkit-background-clip: text; background-clip: text; color: transparent;">Bachelor of Computer Science</h3>
              <p class="text-base text-foreground/80 font-medium">University of Gujrat</p>
              <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-muted border text-sm text-muted-foreground">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar h-4 w-4">
                  <rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect>
                  <line x1="16" x2="16" y1="2" y2="6"></line>
                  <line x1="8" x2="8" y1="2" y2="6"></line>
                  <line x1="3" x2="21" y1="10" y2="10"></line>
                </svg>
                2022 — 2026
              </div>
            </div>

            <!-- FSc Card -->
            <div class="w-full h-full rounded-xl border bg-card text-card-foreground shadow-sm card-hover border-border/50 py-10 px-6 flex flex-col items-center justify-center gap-4 text-center">
              <div class="w-14 h-14 rounded-full bg-gradient-to-br from-purple-500/20 via-pink-500/20 to-rose-500/20 border border-purple-500/30 flex items-center justify-center text-2xl">
                📚
              </div>
              <h3 class="text-xl font-bold" style="background: linear-gradient(to right, #a855f7, #ec4899); -webkit-background-clip: text; background-clip: text; color: transparent;">FSc Pre-Engineering</h3>
              <p class="text-base text-foreground/80 font-medium">Punjab College, Phalia</p>
              <div class="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-muted border text-sm text-muted-foreground">
                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-calendar h-4 w-4">
                  <rect width="18" height="18" x="3" y="4" rx="2" ry="2"></rect>
                  <line x1="16" x2="16" y1="2" y2="6"></line>
                  <line x1="8" x2="8" y1="2" y2="6"></line>
                  <line x1="3" x2="21" y1="10" y2="10"></line>
                </svg>
                2020 — 2022
              </div>
            </div>

          </div>"""

new_edu = """          <!-- Education Cards -->
          <div class="max-w-[860px] mx-auto grid grid-cols-1 md:grid-cols-2 gap-5 reveal-item items-stretch mb-14">

            <!-- BSCS Card -->
            <div class="edu-card edu-card-cyan">
              <div class="edu-card-top">
                <div class="edu-icon edu-icon-cyan">🎓</div>
                <div class="edu-year-badge edu-badge-cyan">2022 — 2026</div>
              </div>
              <div class="edu-card-body">
                <h3 class="edu-degree">Bachelor of Computer Science</h3>
                <p class="edu-school">University of Gujrat</p>
                <div class="edu-meta">
                  <span class="edu-meta-item">🏆 CGPA: 3.71 / 4.00</span>
                  <span class="edu-meta-item">📍 Gujrat, Pakistan</span>
                </div>
                <div class="edu-tags">
                  <span class="edu-tag">Full Stack Dev</span>
                  <span class="edu-tag">AI / ML</span>
                  <span class="edu-tag">Data Structures</span>
                </div>
              </div>
            </div>

            <!-- FSc Card -->
            <div class="edu-card edu-card-purple">
              <div class="edu-card-top">
                <div class="edu-icon edu-icon-purple">📚</div>
                <div class="edu-year-badge edu-badge-purple">2020 — 2022</div>
              </div>
              <div class="edu-card-body">
                <h3 class="edu-degree">FSc Pre-Engineering</h3>
                <p class="edu-school">Punjab College, Phalia</p>
                <div class="edu-meta">
                  <span class="edu-meta-item">📍 Phalia, Pakistan</span>
                  <span class="edu-meta-item">🔬 Science Stream</span>
                </div>
                <div class="edu-tags">
                  <span class="edu-tag">Physics</span>
                  <span class="edu-tag">Mathematics</span>
                  <span class="edu-tag">Chemistry</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Certifications -->
          <div class="max-w-[860px] mx-auto reveal-item">
            <div class="text-center mb-8">
              <h3 style="font-size:1.3rem;font-weight:700;color:#f1f5f9;margin-bottom:6px;">Certifications</h3>
              <div class="w-12 h-0.5 gradient-primary mx-auto rounded-full"></div>
            </div>
            <div class="cert-grid">
              <div class="cert-card cert-card-cyan">
                <div class="cert-icon">🌐</div>
                <div class="cert-info">
                  <h4 class="cert-title">Web Development Bootcamp</h4>
                  <p class="cert-issuer">Udemy · 2024</p>
                </div>
                <span class="cert-badge cert-badge-cyan">Completed</span>
              </div>
              <div class="cert-card cert-card-violet">
                <div class="cert-icon">🐍</div>
                <div class="cert-info">
                  <h4 class="cert-title">Python for Data Science</h4>
                  <p class="cert-issuer">Coursera · 2024</p>
                </div>
                <span class="cert-badge cert-badge-violet">Completed</span>
              </div>
              <div class="cert-card cert-card-pink">
                <div class="cert-icon">⚛</div>
                <div class="cert-info">
                  <h4 class="cert-title">React — The Complete Guide</h4>
                  <p class="cert-issuer">Udemy · 2025</p>
                </div>
                <span class="cert-badge cert-badge-pink">Completed</span>
              </div>
              <div class="cert-card cert-card-emerald">
                <div class="cert-icon">🗄</div>
                <div class="cert-info">
                  <h4 class="cert-title">SQL & Database Design</h4>
                  <p class="cert-issuer">LinkedIn Learning · 2024</p>
                </div>
                <span class="cert-badge cert-badge-emerald">Completed</span>
              </div>
            </div>
          </div>"""

if old_edu in html:
    html = html.replace(old_edu, new_edu)
    print("FIX 5 (education redesign + certs): DONE")
else:
    print("FIX 5 (education): NOT FOUND")

# ============================================================
# FIX 6: Replace dull plain blue via-blue-500 accents with violet
# in project cards tech-tags & pc-link color
# ============================================================
# Update "dull blue" gradient in project badge area
# (The pc-badge-cyan already uses cyan which is fine,
# but via-blue-500 in gradient backgrounds → via-violet-500)
# This is already partially done above in navbar. Let's target about section cards
html = html.replace(
    'bg-gradient-to-br from-cyan-500/20 via-blue-500/20 to-purple-500/20 flex items-center justify-center mb-4 border border-cyan-500/30',
    'bg-gradient-to-br from-cyan-500/20 via-violet-500/20 to-purple-500/20 flex items-center justify-center mb-4 border border-cyan-500/30'
)

print("FIX 6 (blue → violet accent): DONE")

# ============================================================
# FIX 7: pc-inner flex direction fix - ensure consistent card layout
# Add display:flex flex-direction:column to .pc-inner via CSS injection
# ============================================================
# Already handled in CSS. But let's also ensure pc-body has flex-grow
# We'll add a style block at end of <head>

head_injection = """
  <style>
    /* ---- navbar tweaks ---- */
    #navbar .container-custom > div { height: 56px; }

    /* ---- hero heading ---- */
    /* (handled inline) */

    /* ---- buttons ---- */
    .btn-primary-shimmer { padding: 9px 20px !important; font-size: 0.82rem !important; gap: 6px !important; }
    .btn-glass { padding: 9px 20px !important; font-size: 0.82rem !important; gap: 6px !important; }
    .btn-primary-shimmer svg, .btn-glass svg { width: 14px; height: 14px; }

    /* ---- project card fix ---- */
    .pc-inner { display: flex; flex-direction: column; height: 100%; }
    .pc-body { flex: 1; }
    .pc-title { font-size: 1rem; font-weight: 700; color: #f1f5f9; margin: 4px 0 8px; line-height: 1.35; }
    .pc-desc { font-size: 0.82rem; color: #94a3b8; line-height: 1.6; }
    .pc-year { font-size: 0.72rem; font-weight: 600; color: #64748b; letter-spacing: 0.08em; text-transform: uppercase; }
    .pc-footer { margin-top: auto; padding-top: 12px; }
    .tech-tag { font-size: 0.72rem; padding: 3px 10px; border-radius: 4px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: #94a3b8; }

    /* ---- education redesign ---- */
    .edu-card {
      border-radius: 16px;
      border: 1px solid;
      padding: 24px;
      background: rgba(15,23,42,0.6);
      backdrop-filter: blur(12px);
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }
    .edu-card:hover { transform: translateY(-4px); }
    .edu-card-cyan { border-color: rgba(6,182,212,0.25); box-shadow: 0 0 24px rgba(6,182,212,0.07); }
    .edu-card-cyan:hover { box-shadow: 0 8px 32px rgba(6,182,212,0.18); }
    .edu-card-purple { border-color: rgba(139,92,246,0.25); box-shadow: 0 0 24px rgba(139,92,246,0.07); }
    .edu-card-purple:hover { box-shadow: 0 8px 32px rgba(139,92,246,0.18); }

    .edu-card-top { display: flex; align-items: center; justify-content: space-between; }
    .edu-icon {
      width: 52px; height: 52px; border-radius: 14px;
      display: flex; align-items: center; justify-content: center;
      font-size: 1.5rem;
    }
    .edu-icon-cyan { background: linear-gradient(135deg, rgba(6,182,212,0.2), rgba(99,102,241,0.2)); border: 1px solid rgba(6,182,212,0.3); }
    .edu-icon-purple { background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(236,72,153,0.2)); border: 1px solid rgba(139,92,246,0.3); }

    .edu-year-badge { font-size: 0.75rem; font-weight: 600; padding: 4px 12px; border-radius: 50px; }
    .edu-badge-cyan { background: rgba(6,182,212,0.12); color: #22d3ee; border: 1px solid rgba(6,182,212,0.3); }
    .edu-badge-purple { background: rgba(139,92,246,0.12); color: #c084fc; border: 1px solid rgba(139,92,246,0.3); }

    .edu-card-body { display: flex; flex-direction: column; gap: 10px; }
    .edu-degree { font-size: 1.08rem; font-weight: 700; color: #f1f5f9; line-height: 1.3; }
    .edu-school { font-size: 0.88rem; color: #94a3b8; font-weight: 500; }
    .edu-meta { display: flex; flex-wrap: wrap; gap: 10px; }
    .edu-meta-item { font-size: 0.78rem; color: #64748b; }
    .edu-tags { display: flex; flex-wrap: wrap; gap: 6px; }
    .edu-tag { font-size: 0.72rem; padding: 3px 10px; border-radius: 4px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: #94a3b8; }

    /* ---- certifications ---- */
    .cert-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
    @media (max-width: 600px) { .cert-grid { grid-template-columns: 1fr; } }

    .cert-card {
      display: flex; align-items: center; gap: 14px;
      padding: 16px 18px; border-radius: 14px;
      border: 1px solid; background: rgba(15,23,42,0.5);
      backdrop-filter: blur(8px);
      transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .cert-card:hover { transform: translateY(-2px); }
    .cert-card-cyan { border-color: rgba(6,182,212,0.2); }
    .cert-card-cyan:hover { box-shadow: 0 4px 20px rgba(6,182,212,0.15); }
    .cert-card-violet { border-color: rgba(139,92,246,0.2); }
    .cert-card-violet:hover { box-shadow: 0 4px 20px rgba(139,92,246,0.15); }
    .cert-card-pink { border-color: rgba(236,72,153,0.2); }
    .cert-card-pink:hover { box-shadow: 0 4px 20px rgba(236,72,153,0.15); }
    .cert-card-emerald { border-color: rgba(16,185,129,0.2); }
    .cert-card-emerald:hover { box-shadow: 0 4px 20px rgba(16,185,129,0.15); }

    .cert-icon { font-size: 1.5rem; flex-shrink: 0; }
    .cert-info { flex: 1; min-width: 0; }
    .cert-title { font-size: 0.85rem; font-weight: 600; color: #e2e8f0; line-height: 1.3; }
    .cert-issuer { font-size: 0.75rem; color: #64748b; margin-top: 2px; }
    .cert-badge { font-size: 0.65rem; font-weight: 600; padding: 3px 9px; border-radius: 50px; flex-shrink: 0; }
    .cert-badge-cyan { background: rgba(6,182,212,0.12); color: #22d3ee; border: 1px solid rgba(6,182,212,0.3); }
    .cert-badge-violet { background: rgba(139,92,246,0.12); color: #c084fc; border: 1px solid rgba(139,92,246,0.3); }
    .cert-badge-pink { background: rgba(236,72,153,0.12); color: #f472b6; border: 1px solid rgba(236,72,153,0.3); }
    .cert-badge-emerald { background: rgba(16,185,129,0.12); color: #34d399; border: 1px solid rgba(16,185,129,0.3); }

    /* ---- replace plain blue in gradient accents ---- */
    /* via-blue-500 → via-violet-500 for a richer look */
    /* handled via CSS specificity override */
    .gradient-text {
      background: linear-gradient(135deg, #22d3ee, #818cf8, #c084fc) !important;
      -webkit-background-clip: text !important;
      background-clip: text !important;
      color: transparent !important;
    }
    .gradient-primary { background: linear-gradient(to right, #22d3ee, #818cf8, #c084fc) !important; }

    /* project card colors - replace dull blue */
    .pc-badge-cyan { background: rgba(6,182,212,0.15); color: #22d3ee; border: 1px solid rgba(6,182,212,0.3); }
    .pc-link-primary { color: #22d3ee; }
    .pc-link-primary:hover { color: #c084fc; }

    /* active nav link styling */
    nav a[href="#home"] { color: #22d3ee !important; font-weight: 600; }
  </style>
"""

html = html.replace("</head>", head_injection + "</head>")
print("FIX 7 (injected style block): DONE")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nAll fixes applied!")

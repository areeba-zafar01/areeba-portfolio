with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ===== 1. HERO: Replace blob avatar with modern conic glow card + floating chips =====
old_img = """        <div class=\"relative w-full flex items-center justify-center lg:justify-end order-1 lg:order-2 mb-8 lg:mb-0\" style=\"opacity:0;transform:translateX(50px) translateZ(0)\">
          <div class=\"hero-image-container\">
              <div class=\"hero-blob\">
                  <div class=\"profile-placeholder\" style=\"overflow: hidden; padding: 0;\">
                      <img src=\"avatar.png\" alt=\"Areeba Zafar\" style=\"width: 100%; height: 100%; object-fit: cover; border-radius: inherit;\">
                  </div>
              </div>
          </div>
        </div>"""

new_img = """        <div class=\"relative w-full flex items-center justify-center lg:justify-end order-1 lg:order-2 mb-8 lg:mb-0\" style=\"opacity:0;transform:translateX(50px) translateZ(0)\">
          <div class=\"hero-avatar-wrapper\">
            <div class=\"hero-conic-glow\"></div>
            <div class=\"hero-avatar-card\">
              <div class=\"hero-avatar-inner\">
                <img src=\"avatar.png\" alt=\"Areeba Zafar\" class=\"hero-avatar-img\">
              </div>
            </div>
            <span class=\"floating-chip chip-1\">
              <svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#38bdf8\" stroke-width=\"2\"><polyline points=\"16 18 22 12 16 6\"></polyline><polyline points=\"8 6 2 12 8 18\"></polyline></svg>
              Next.js
            </span>
            <span class=\"floating-chip chip-2\">
              <svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#c084fc\" stroke-width=\"2\"><rect x=\"2\" y=\"7\" width=\"20\" height=\"14\" rx=\"2\"></rect><path d=\"M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16\"></path></svg>
              Software Eng.
            </span>
            <span class=\"floating-chip chip-3\">
              <svg width=\"14\" height=\"14\" viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"#f472b6\" stroke-width=\"2\"><path d=\"M22 12h-4l-3 9L9 3l-3 9H2\"></path></svg>
              AI / ML
            </span>
            <span class=\"floating-chip chip-4\">
              <span style=\"width:8px;height:8px;background:#22c55e;border-radius:50%;box-shadow:0 0 8px #22c55e;animation:pulse 2s infinite;\"></span>
              Open to Remote
            </span>
          </div>
        </div>"""

if old_img in html:
    html = html.replace(old_img, new_img)
    print("Hero avatar: UPGRADED")
else:
    print("Hero avatar: NOT FOUND (check whitespace)")

# ===== 2. HERO: Replace raw inline buttons with class-based shimmer buttons =====
old_btn_start = "Get In Touch\n              <svg xmlns"
new_link_check = "btn-primary-shimmer"

if new_link_check not in html:
    # Patch "Get In Touch" anchor style attribute to use class instead
    html = html.replace(
        'href="#contact" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 28px; background: linear-gradient(to right, #06b6d4, #3b82f6, #a855f7); color: white; font-weight: 600; font-size: 0.95rem; border-radius: 8px; text-decoration: none; box-shadow: 0 4px 15px rgba(6,182,212,0.3); transition: all 0.3s ease; white-space: nowrap;" onmouseover="this.style.transform=\'translateY(-2px)\'; this.style.boxShadow=\'0 8px 25px rgba(6,182,212,0.4)\';" onmouseout="this.style.transform=\'translateY(0)\'; this.style.boxShadow=\'0 4px 15px rgba(6,182,212,0.3)\';"',
        'href="#contact" class="btn-primary-shimmer" style="text-decoration:none;"'
    )
    html = html.replace(
        'href="Areeba_Zafar_Resume.pdf" download="Areeba_Zafar_Resume.pdf" style="display: inline-flex; align-items: center; gap: 8px; padding: 12px 28px; background: transparent; color: #e2e8f0; font-weight: 600; font-size: 0.95rem; border-radius: 8px; text-decoration: none; border: 2px solid rgba(6,182,212,0.5); transition: all 0.3s ease; white-space: nowrap;" onmouseover="this.style.borderColor=\'rgba(6,182,212,0.8)\'; this.style.background=\'rgba(6,182,212,0.08)\'; this.style.transform=\'translateY(-2px)\';" onmouseout="this.style.borderColor=\'rgba(6,182,212,0.5)\'; this.style.background=\'transparent\'; this.style.transform=\'translateY(0)\';"',
        'href="Areeba_Zafar_Resume.pdf" download="Areeba_Zafar_Resume.pdf" class="btn-glass" style="text-decoration:none;"'
    )
    print("Buttons: UPGRADED")
else:
    print("Buttons: already upgraded")

# ===== 3. HERO: Upgrade stats to glass metrics strip =====
old_stats = """<div class=\"grid grid-cols-3 gap-4 sm:gap-8 pt-8 lg:pt-12 max-w-xl\" style=\"opacity:0;transform:translateY(30px) translateZ(0)\">
            <div class=\"text-center lg:text-left\">
              <div class=\"text-2xl sm:text-3xl font-bold gradient-text\" data-count=\"8\">0</div>
              <div class=\"text-xs sm:text-sm text-muted-foreground mt-1\">Projects Built</div>
            </div>
            <div class=\"text-center lg:text-left\">
              <div class=\"text-2xl sm:text-3xl font-bold gradient-text\" data-count=\"15\">0</div>
              <div class=\"text-xs sm:text-sm text-muted-foreground mt-1\">Technologies</div>
            </div>
            <div class=\"text-center lg:text-left\">
              <div class=\"text-2xl sm:text-3xl font-bold gradient-text\">BSCS</div>
              <div class=\"text-xs sm:text-sm text-muted-foreground mt-1\">Degree Earned</div>
            </div>
          </div>"""

new_stats = """<div class=\"metrics-strip max-w-xl\" style=\"opacity:0;transform:translateY(30px) translateZ(0)\">
            <div class=\"text-center\">
              <div class=\"text-2xl sm:text-3xl font-bold gradient-text\" data-count=\"8\">0</div>
              <div class=\"text-xs sm:text-sm mt-1\" style=\"color:#94a3b8;\">Projects Built</div>
            </div>
            <div class=\"text-center\" style=\"border-left:1px solid rgba(255,255,255,0.08);border-right:1px solid rgba(255,255,255,0.08);\">
              <div class=\"text-2xl sm:text-3xl font-bold gradient-text\" data-count=\"15\">0</div>
              <div class=\"text-xs sm:text-sm mt-1\" style=\"color:#94a3b8;\">Technologies</div>
            </div>
            <div class=\"text-center\">
              <div class=\"text-2xl sm:text-3xl font-bold gradient-text\">3.71</div>
              <div class=\"text-xs sm:text-sm mt-1\" style=\"color:#94a3b8;\">CGPA / 4.00</div>
            </div>
          </div>"""

if old_stats in html:
    html = html.replace(old_stats, new_stats)
    print("Stats strip: UPGRADED")
else:
    print("Stats strip: NOT FOUND")

# ===== 4. SKILLS: Replace plain flat tags with bento grid cards =====
old_skills_section = """          <div class=\"space-y-12\">
            <div class=\"space-y-4 reveal-item\">
              <h3 class=\"text-xl font-semibold text-foreground mb-4\">Frontend Technologies</h3>
              <div class=\"flex flex-wrap gap-3\">
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 text-cyan-300 border-cyan-500/30\">HTML5</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 text-cyan-300 border-cyan-500/30\">CSS3</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 text-cyan-300 border-cyan-500/30\">JavaScript</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 text-cyan-300 border-cyan-500/30\">React</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 text-cyan-300 border-cyan-500/30\">Next.js</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-cyan-500/20 via-blue-500/20 to-purple-500/20 text-cyan-300 border-cyan-500/30\">Vite</span>
              </div>
            </div>
            <div class=\"space-y-4 reveal-item\">
              <h3 class=\"text-xl font-semibold text-foreground mb-4\">Backend &amp; Database</h3>
              <div class=\"flex flex-wrap gap-3\">
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">Python</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">FastAPI</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">MySQL</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">Prisma ORM</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">REST APIs</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">Node.js</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">PostgreSQL</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-indigo-500/20 via-purple-500/20 to-pink-500/20 text-indigo-300 border-indigo-500/30\">TypeScript</span>
              </div>
            </div>
            <div class=\"space-y-4 reveal-item\">
              <h3 class=\"text-xl font-semibold text-foreground mb-4\">AI / Machine Learning</h3>
              <div class=\"flex flex-wrap gap-3\">
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-rose-500/20 text-purple-300 border-purple-500/30\">XGBoost</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-rose-500/20 text-purple-300 border-purple-500/30\">ResNet18</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-rose-500/20 text-purple-300 border-purple-500/30\">Data Analysis</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-purple-500/20 via-pink-500/20 to-rose-500/20 text-purple-300 border-purple-500/30\">FastAPI ML Integration</span>
              </div>
            </div>
            <div class=\"space-y-4 reveal-item\">
              <h3 class=\"text-xl font-semibold text-foreground mb-4\">Tools &amp; Platforms</h3>
              <div class=\"flex flex-wrap gap-3\">
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">Git</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">GitHub</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">JWT Auth</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">bcrypt</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">Web Audio API</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">Vercel</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">Postman</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">VS Code</span>
                <span class=\"px-4 py-2 rounded-lg border text-sm font-medium transition-all cursor-default bg-gradient-to-r from-pink-500/20 via-rose-500/20 to-orange-500/20 text-pink-300 border-pink-500/30\">Cursor</span>
              </div>
            </div>
          </div>"""

new_skills_section = """          <div class=\"bento-grid\">

            <!-- FRONTEND BENTO -->
            <div class=\"bento-card reveal-item\">
              <div class=\"bento-header\">
                <div class=\"bento-icon\" style=\"background:linear-gradient(135deg,rgba(6,182,212,0.25),rgba(99,102,241,0.25));\">🎨</div>
                <div>
                  <h3 style=\"font-size:1.05rem;font-weight:700;color:#f1f5f9;\">Frontend</h3>
                  <p style=\"font-size:0.78rem;color:#64748b;\">UI & Interfaces</p>
                </div>
              </div>
              <div class=\"bento-tags\">
                <span class=\"bento-tag\">⚡ Next.js</span>
                <span class=\"bento-tag\">⚛ React</span>
                <span class=\"bento-tag\">🟨 JavaScript</span>
                <span class=\"bento-tag\">🔷 TypeScript</span>
                <span class=\"bento-tag\">🎨 HTML5</span>
                <span class=\"bento-tag\">💅 CSS3</span>
                <span class=\"bento-tag\">⚡ Vite</span>
              </div>
            </div>

            <!-- BACKEND BENTO -->
            <div class=\"bento-card reveal-item\">
              <div class=\"bento-header\">
                <div class=\"bento-icon\" style=\"background:linear-gradient(135deg,rgba(139,92,246,0.25),rgba(236,72,153,0.25));\">⚙️</div>
                <div>
                  <h3 style=\"font-size:1.05rem;font-weight:700;color:#f1f5f9;\">Backend & Database</h3>
                  <p style=\"font-size:0.78rem;color:#64748b;\">APIs & Data</p>
                </div>
              </div>
              <div class=\"bento-tags\">
                <span class=\"bento-tag\">🟢 Node.js</span>
                <span class=\"bento-tag\">🐍 Python</span>
                <span class=\"bento-tag\">🚀 FastAPI</span>
                <span class=\"bento-tag\">🐘 PostgreSQL</span>
                <span class=\"bento-tag\">🗄 MySQL</span>
                <span class=\"bento-tag\">🔺 Prisma ORM</span>
                <span class=\"bento-tag\">🌐 REST APIs</span>
              </div>
            </div>

            <!-- AI / ML BENTO -->
            <div class=\"bento-card reveal-item\">
              <div class=\"bento-header\">
                <div class=\"bento-icon\" style=\"background:linear-gradient(135deg,rgba(244,63,94,0.25),rgba(251,146,60,0.25));\">🤖</div>
                <div>
                  <h3 style=\"font-size:1.05rem;font-weight:700;color:#f1f5f9;\">AI / Machine Learning</h3>
                  <p style=\"font-size:0.78rem;color:#64748b;\">Models & Intelligence</p>
                </div>
              </div>
              <div class=\"bento-tags\">
                <span class=\"bento-tag\">📊 XGBoost</span>
                <span class=\"bento-tag\">🧠 ResNet18</span>
                <span class=\"bento-tag\">📈 Data Analysis</span>
                <span class=\"bento-tag\">🔗 ML Integration</span>
              </div>
            </div>

            <!-- TOOLS BENTO -->
            <div class=\"bento-card reveal-item\">
              <div class=\"bento-header\">
                <div class=\"bento-icon\" style=\"background:linear-gradient(135deg,rgba(16,185,129,0.25),rgba(6,182,212,0.25));\">🛠</div>
                <div>
                  <h3 style=\"font-size:1.05rem;font-weight:700;color:#f1f5f9;\">Tools & Platforms</h3>
                  <p style=\"font-size:0.78rem;color:#64748b;\">Dev Environment</p>
                </div>
              </div>
              <div class=\"bento-tags\">
                <span class=\"bento-tag\">🐱 Git / GitHub</span>
                <span class=\"bento-tag\">▲ Vercel</span>
                <span class=\"bento-tag\">📮 Postman</span>
                <span class=\"bento-tag\">💙 VS Code</span>
                <span class=\"bento-tag\">🔮 Cursor</span>
                <span class=\"bento-tag\">🔑 JWT Auth</span>
                <span class=\"bento-tag\">🔒 bcrypt</span>
              </div>
            </div>

          </div>"""

if old_skills_section in html:
    html = html.replace(old_skills_section, new_skills_section)
    print("Skills bento grid: UPGRADED")
else:
    print("Skills section: NOT FOUND - check diff carefully")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nAll upgrades done! Checks:")
print("  hero-conic-glow:", "hero-conic-glow" in html)
print("  floating-chip:", "floating-chip" in html)
print("  btn-primary-shimmer:", "btn-primary-shimmer" in html)
print("  metrics-strip:", "metrics-strip" in html)
print("  bento-grid:", "bento-grid" in html)

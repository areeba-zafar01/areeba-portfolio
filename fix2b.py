with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# FIX 6: Replace dull plain blue via-blue-500 accents with violet in about cards
html = html.replace(
    'bg-gradient-to-br from-cyan-500/20 via-blue-500/20 to-purple-500/20 flex items-center justify-center mb-4 border border-cyan-500/30',
    'bg-gradient-to-br from-cyan-500/20 via-violet-500/20 to-purple-500/20 flex items-center justify-center mb-4 border border-cyan-500/30'
)
print("FIX 6 (blue->violet accent): DONE")

# FIX 7: Inject style block before </head>
style_already = "cert-grid" in html
if not style_already:
    head_injection = """
  <style>
    /* navbar tweaks */
    #navbar .container-custom > div { height: 56px; }

    /* buttons */
    .btn-primary-shimmer { padding: 9px 20px !important; font-size: 0.82rem !important; gap: 6px !important; }
    .btn-glass { padding: 9px 20px !important; font-size: 0.82rem !important; gap: 6px !important; }
    .btn-primary-shimmer svg, .btn-glass svg { width: 14px; height: 14px; }

    /* project card fix */
    .pc-inner { display: flex; flex-direction: column; height: 100%; }
    .pc-body { flex: 1; }
    .pc-title { font-size: 1rem; font-weight: 700; color: #f1f5f9; margin: 4px 0 8px; line-height: 1.35; }
    .pc-desc { font-size: 0.82rem; color: #94a3b8; line-height: 1.6; }
    .pc-year { font-size: 0.72rem; font-weight: 600; color: #64748b; letter-spacing: 0.08em; text-transform: uppercase; }
    .pc-footer { margin-top: auto; padding-top: 12px; }
    .tech-tag { font-size: 0.72rem; padding: 3px 10px; border-radius: 4px; background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); color: #94a3b8; }

    /* education redesign */
    .edu-card {
      border-radius: 16px; border: 1px solid;
      padding: 24px; background: rgba(15,23,42,0.6);
      backdrop-filter: blur(12px);
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      display: flex; flex-direction: column; gap: 16px;
    }
    .edu-card:hover { transform: translateY(-4px); }
    .edu-card-cyan { border-color: rgba(6,182,212,0.25); box-shadow: 0 0 24px rgba(6,182,212,0.07); }
    .edu-card-cyan:hover { box-shadow: 0 8px 32px rgba(6,182,212,0.18); }
    .edu-card-purple { border-color: rgba(139,92,246,0.25); box-shadow: 0 0 24px rgba(139,92,246,0.07); }
    .edu-card-purple:hover { box-shadow: 0 8px 32px rgba(139,92,246,0.18); }

    .edu-card-top { display: flex; align-items: center; justify-content: space-between; }
    .edu-icon {
      width: 52px; height: 52px; border-radius: 14px;
      display: flex; align-items: center; justify-content: center; font-size: 1.5rem;
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

    /* certifications */
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

    /* gradient override - richer violet instead of blue */
    .gradient-text {
      background: linear-gradient(135deg, #22d3ee, #818cf8, #c084fc) !important;
      -webkit-background-clip: text !important;
      background-clip: text !important;
      color: transparent !important;
    }
    .gradient-primary { background: linear-gradient(to right, #22d3ee, #818cf8, #c084fc) !important; }

    /* project card colors */
    .pc-badge-cyan { background: rgba(6,182,212,0.15); color: #22d3ee; border: 1px solid rgba(6,182,212,0.3); }
    .pc-link-primary { color: #22d3ee; }
    .pc-link-primary:hover { color: #c084fc; }
  </style>
"""
    html = html.replace("</head>", head_injection + "</head>")
    print("FIX 7 (injected style block): DONE")
else:
    print("FIX 7: style block already present")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("All remaining fixes applied!")

# Quick verification
checks = [
    ("Bank project removed", "Bank Management System"),
    ("Education new cards", "edu-card-cyan"),
    ("Certificates", "cert-grid"),
    ("Hero size reduced", "2.6rem"),
    ("AZ logo smaller", "w-8 h-8"),
]
print("\nVerification:")
with open("index.html", "r", encoding="utf-8") as f:
    final = f.read()
for label, token in checks:
    if label == "Bank project removed":
        found = token not in final
        status = "OK  " if found else "MISS"
    else:
        found = token in final
        status = "OK  " if found else "MISS"
    print(f"  [{status}] {label}")

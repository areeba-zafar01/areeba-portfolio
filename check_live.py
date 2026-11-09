import urllib.request
try:
    r = urllib.request.urlopen('https://areeba-portfolio-bice.vercel.app/', timeout=20)
    content = r.read().decode('utf-8')
    checks = ['hero-conic-glow', 'floating-chip', 'btn-primary-shimmer', 'metrics-strip', 'bento-grid', 'Open to Remote', '3.71', 'WorkTrack', 'Ali Habib']
    for c in checks:
        status = "OK  " if c in content else "MISS"
        print(f"  [{status}] {c}")
except Exception as e:
    print("Error:", e)

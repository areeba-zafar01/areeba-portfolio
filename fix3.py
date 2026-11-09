with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Fix hero heading sizes
html = html.replace(
    'style="font-size: 3.8rem; font-weight: 800; line-height: 1.1; margin-bottom: 2px; color: white;"',
    'style="font-size: 2.4rem; font-weight: 700; line-height: 1.1; margin-bottom: 2px; color: white;"'
)
html = html.replace(
    'style="font-size: 4rem; font-weight: 800; line-height: 1.1; margin-bottom: 12px;"',
    'style="font-size: 3rem; font-weight: 700; line-height: 1.1; margin-bottom: 12px;"'
)
html = html.replace(
    'style="font-size: 2rem; font-weight: 600; margin-bottom: 20px; color: #06b6d4;"',
    'style="font-size: 1.25rem; font-weight: 500; margin-bottom: 20px; color: #22d3ee;"'
)
print("Hero headings: DONE")

# Fix AZ logo size
html = html.replace(
    'w-10 h-10 md:w-12 md:h-12 rounded-lg bg-gradient-to-br from-cyan-600 via-blue-800 to-purple-600 flex items-center justify-center shadow-lg shadow-cyan-600/30',
    'w-8 h-8 md:w-9 md:h-9 rounded-lg bg-gradient-to-br from-cyan-500 via-violet-600 to-purple-600 flex items-center justify-center shadow-lg shadow-cyan-500/20'
)
html = html.replace(
    '<span class="text-lg md:text-xl font-bold text-white">AZ</span>',
    '<span class="text-sm font-bold text-white">AZ</span>'
)
html = html.replace(
    '<span class="text-lg md:text-xl font-semibold text-foreground hidden sm:block">Areeba Zafar</span>',
    '<span class="text-sm font-semibold text-foreground hidden sm:block">Areeba Zafar</span>'
)
print("AZ logo + name: DONE")

# Fix bank project
old_bank = '            <!-- Project 4: Bank -->\n            <div class="project-card-v2 reveal-item" data-pcategory="desktop">'
if old_bank in html:
    # find start and end of bank card
    start = html.find('\n            <!-- Project 4: Bank -->')
    end = html.find('\n\n            <!-- Project 5:', start)
    html = html[:start] + html[end:]
    print("Bank project removed: DONE")
else:
    print("Bank: not found with that pattern, trying alternate")
    if "Bank Management System" in html:
        # find the bank card differently
        start = html.find("<!-- Project 4: Bank -->")
        if start == -1:
            start = html.find("Bank Management System") - 500
        end_marker = html.find("<!-- Project 5:", start)
        if end_marker > start:
            html = html[:start-13] + html[end_marker:]
            print("Bank project removed (alt): DONE")
        else:
            print("Bank project: could not auto-remove, check manually")
    else:
        print("Bank already removed!")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

# Verify
with open("index.html", "r", encoding="utf-8") as f:
    final = f.read()
print("\nFinal verification:")
print("  Hero 2.4rem:", "2.4rem" in final)
print("  AZ w-8:", "w-8 h-8" in final)
print("  Bank removed:", "Bank Management System" not in final)
print("  Edu cards:", "edu-card-cyan" in final)
print("  Certs:", "cert-grid" in final)

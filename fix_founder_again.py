import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the founder image tag
content = re.sub(
    r'<img alt="Sabla Singh - Founder &amp; Master Educator".*?/>',
    r'<img alt="Sabla Singh - Founder &amp; Master Educator" class="w-full h-[500px] object-cover object-[center_top] filter transition-all duration-700 hover:scale-105" src="founder.jpg"/>',
    content,
    flags=re.DOTALL
)

# And replace the parent divs
content = re.sub(
    r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none"></div>\s*<div class="relative overflow-hidden shadow-2xl bg-dark-emerald">',
    r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none rounded-t-[10rem]"></div>\n  <div class="relative overflow-hidden shadow-2xl bg-dark-emerald rounded-t-[10rem]">',
    content
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Finally replaced!")

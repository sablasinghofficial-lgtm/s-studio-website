import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the about founder block
about_pattern = r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none"></div>.*?</div>'
# Wait, this will match too much. Let's be specific.
about_pattern = r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none"></div>\s*<div class="relative overflow-hidden shadow-2xl bg-dark-emerald">\s*<img alt="Sabla Singh - Founder[^"]+" class="[^"]+" src="[^"]+"/>\s*</div>'

# Let's just find the img src and replace it, and then modify the classes of its parent divs.
def replacer(match):
    return '''<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none rounded-t-[10rem]"></div>
  <div class="relative overflow-hidden shadow-2xl bg-dark-emerald rounded-t-[10rem]">
  <img alt="Sabla Singh - Founder &amp; Master Educator" class="w-full h-auto object-cover object-[center_top] filter transition-all duration-700 hover:scale-105" src="founder.jpg"/>
  </div>'''

content = re.sub(r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none"></div>\s*<div class="relative overflow-hidden shadow-2xl bg-dark-emerald">\s*<img alt="Sabla Singh - Founder &amp; Master Educator" class="[^"]+" src="[^"]+"/>\s*</div>', replacer, content)

# Fix the Lightbox link in gallery
content = re.sub(r"onclick=\"openLightbox\('https://image-hosting\.storage\.googleapis\.com/sablasingh_founder_master_artist_portrait\.webp'", "onclick=\"openLightbox('founder.jpg'", content)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed founder photos and lightbox!")

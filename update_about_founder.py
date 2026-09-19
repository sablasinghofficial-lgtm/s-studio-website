import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Modify the container and img tag for About Section
# Old container:
old_container = r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none"></div>\s*<div class="relative overflow-hidden shadow-2xl bg-dark-emerald">\s*<img alt="Sabla Singh - Founder[^"]+" class="[^"]+" src="[^"]+"/>\s*</div>'

# New container with arched frame and founder.jpg
new_container = '''<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none rounded-t-[10rem]"></div>
  <div class="relative overflow-hidden shadow-2xl bg-dark-emerald rounded-t-[10rem]">
  <img alt="Sabla Singh - Founder &amp; Master Educator" class="w-full h-[500px] object-cover object-[center_top] filter transition-all duration-700 hover:scale-105" src="founder.jpg"/>
  </div>'''

content = re.sub(old_container, new_container, content, flags=re.DOTALL)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated About section founder image with frame!")

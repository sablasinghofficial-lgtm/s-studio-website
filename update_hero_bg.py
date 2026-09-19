import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the image src
old_img_pattern = r'<img alt="Sabla Singh Luxury Atelier Ranchi Interior" class="([^"]+)" src="[^"]+"/>'
new_img = r'<img alt="Sabla Singh Academy Makeup Artist" class="\1" src="hero-bg.jpg"/>'
content = re.sub(old_img_pattern, new_img, content)

# Adjust the gradient slightly to reveal the subject more on the right
content = content.replace(
    'from-deep-forest via-deep-forest/85 to-deep-forest/40',
    'from-deep-forest via-deep-forest/80 to-transparent'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated hero image!")

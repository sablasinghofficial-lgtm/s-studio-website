import re

with open('original_code.html', 'r', encoding='utf-8') as f:
    orig = f.read()

with open('code.html', 'r', encoding='utf-8') as f:
    curr = f.read()

# Find all original image sources that use googleusercontent
orig_images = re.findall(r'<img alt="([^"]+)"[^>]+src="(https://lh3.googleusercontent.com/[^"]+)"', orig)
orig_lightboxes = re.findall(r'onclick="openLightbox\(\'([^\']+)\', \'([^\']+)\'\)"', orig)

# Restore images
for alt, src in orig_images:
    if "Founder" in alt: 
        continue # Leave founder.jpg
    if "Sabla Singh Luxury Atelier Ranchi Interior" in alt:
        continue # This is the hero-bg.jpg
    # Replace in curr
    # We find <img alt="ALT" ... src="founder.jpg"/> and replace founder.jpg with src
    pattern = r'(<img alt="' + re.escape(alt) + r'"[^>]+src=")founder\.jpg(")'
    curr = re.sub(pattern, r'\g<1>' + src + r'\g<2>', curr)

# Restore lightboxes
for lb_src, lb_title in orig_lightboxes:
    if "Founder" in lb_title:
        continue # Leave founder.jpg
    # Replace in curr
    pattern = r'(onclick="openLightbox\(\')founder\.jpg(\', \'' + re.escape(lb_title) + r'\'\)")'
    curr = re.sub(pattern, r'\g<1>' + lb_src + r'\g<2>', curr)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(curr)
print("Restored original images!")

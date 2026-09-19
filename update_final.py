import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Services bullet points
# HD & Airbrush
old_hd = r'<p class="text-xs text-charcoal-subtle mt-2 font-light leading-relaxed">\s*Micro-fine silicon and silicone-water emulsions calibrated for flawless 8K lens capture, ensuring up to 18 hours of luminous, sweat-resistant perfection.\s*</p>'
new_hd = '''<ul class="text-xs text-charcoal-subtle mt-3 font-light leading-relaxed space-y-2 list-disc pl-4">
    <li>Flawless 8K lens capture</li>
    <li>Up to 18 hours long-lasting</li>
    <li>Sweat-resistant perfection</li>
</ul>'''
content = re.sub(old_hd, new_hd, content)

# Luxury Skin
old_skin = r'<p class="text-xs text-charcoal-subtle mt-2 font-light leading-relaxed">\s*Oxygen-infused facials, gold foil revitalizations, and targeted pigmentation therapies engineered to hydrate, repair, and illuminate the epidermis.\s*</p>'
new_skin = '''<ul class="text-xs text-charcoal-subtle mt-3 font-light leading-relaxed space-y-2 list-disc pl-4">
    <li>Oxygen-infused facials</li>
    <li>Gold foil revitalizations</li>
    <li>Targeted pigmentation therapies</li>
    <li>Hydrates, repairs &amp; illuminates</li>
</ul>'''
content = re.sub(old_skin, new_skin, content)

# Bridal Couture
old_bridal = r'<p class="text-xs text-charcoal-subtle mt-2 font-light leading-relaxed">\s*End-to-end bespoke bridal curation: personalized color profiling, jewelry and lehenga drapery orchestration, accompanied by Sabla Singh\'s hallmark bridal calm.\s*</p>'
new_bridal = '''<ul class="text-xs text-charcoal-subtle mt-3 font-light leading-relaxed space-y-2 list-disc pl-4">
    <li>Bespoke bridal curation</li>
    <li>Personalized color profiling</li>
    <li>Jewelry &amp; lehenga drapery</li>
    <li>Signature bridal styling</li>
</ul>'''
content = re.sub(old_bridal, new_bridal, content)

# 2. Fix Founder Photo
# Remove the offset border div, make the image container perfectly arched with a thick border
old_founder_container = r'<div class="absolute -top-4 -left-4 w-full h-full border-2 border-champagne/40 pointer-events-none rounded-t-\[10rem\]"></div>\s*<div class="relative overflow-hidden shadow-2xl bg-dark-emerald rounded-t-\[10rem\]">'
new_founder_container = '''<div class="relative overflow-hidden shadow-2xl bg-dark-emerald rounded-t-full border-[8px] border-champagne/40">'''
content = re.sub(old_founder_container, new_founder_container, content)

# 3. Explore Courses redirect
old_explore = r'<a class="gold-shimmer-btn text-deep-forest font-semibold text-xs uppercase tracking-mega-wide px-8 py-4 border border-champagne" href="#academy">\s*Explore Courses\s*</a>'
new_explore = '''<a class="gold-shimmer-btn text-deep-forest font-semibold text-xs uppercase tracking-mega-wide px-8 py-4 border border-champagne" href="http://www.sablasinghacademy.com" target="_blank">\n            Explore Courses\n          </a>'''
content = re.sub(old_explore, new_explore, content)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated services, founder photo, and explore courses link!")

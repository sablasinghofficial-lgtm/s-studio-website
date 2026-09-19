import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

link_html = '''</div>
  <!-- Academy Website Link -->
  <div class="mt-12 mb-12 text-center w-full">
    <a href="http://www.sablasinghacademy.com" target="_blank" class="gold-shimmer-btn inline-block text-deep-forest font-semibold text-xs tracking-mega-wide uppercase px-8 py-4 border border-champagne shadow-xl">
        Visit S Studio Academy Website ?
    </a>
  </div>
  <!-- Right: Reservation & Inquiry Form -->'''

content = re.sub(r'</div>\s*<!-- Right: Reservation & Inquiry Form -->', link_html, content)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Link added successfully!")

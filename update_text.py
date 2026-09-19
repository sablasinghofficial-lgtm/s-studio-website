import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 2004-2024 to 2004-Present
content = content.replace("2004-2024", "2004-Present")

# 2. Location
content = content.replace(
    "OPPOSITE SARALA BIRLA UNIVERSITY, RANCHI",
    "NEAR SARALA BIRLA UNIVERSITY OPPOSITE SIDE S STUDIO"
)

# 3. Replace Brand Names
content = content.replace("Sabla Singh Academy", "S Studio")
content = content.replace("SABLA SINGH <br/>", "S STUDIO <br/>")
content = content.replace("The Sabla Singh Difference", "The S Studio Difference")
content = content.replace("Sabla Singh Gallery", "S Studio Gallery")
content = content.replace("Sabla Singh Bride", "S Studio Bride")
content = content.replace("Sabla Singh Luxury Atelier", "S Studio Luxury Atelier")
content = content.replace("Sabla Singh Atelier", "S Studio Atelier")

# Also for some "Sabla Singh" references that are clearly brand
content = content.replace("Welcome to Sabla Singh", "Welcome to S Studio")
content = content.replace("Experience the Sabla Singh Difference", "Experience the S Studio Difference")

# 4. Add Academy Link
link_html = '''</div>
  <!-- Academy Website Link -->
  <div class="mt-12 text-center">
    <a href="http://www.sablasinghacademy.com" target="_blank" class="gold-shimmer-btn inline-block text-deep-forest font-semibold text-xs tracking-mega-wide uppercase px-8 py-4 border border-champagne shadow-xl">
        Visit S Studio Academy Website ?
    </a>
  </div>
  <!-- Right: Reservation & Inquiry Form -->'''

content = content.replace('</div>\n  <!-- Right: Reservation & Inquiry Form -->', link_html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated texts and links!")

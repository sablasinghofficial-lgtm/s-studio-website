import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

orig_bg = "url('https://lh3.googleusercontent.com/aida-public/AB6AXuD8IcrMhXDoawDWFeT40LpIH6pKrWD9QUMMs5fSecGuOmYiGq5S0qhHHlvHzQ-eJegNVwTw4ZvcruoizZ-N1opNPGl0FZth6x-aoJ8TkTwbjJSFKnaTYvAmONTmlbRrIdtn6m3kK_OPDjjFmJczLvpwAU3d55lALvbRwqH0jv70xzGUVzzlx10HdXxHy_KhMWz7lACleUyaFO7BHWpikr87hrtRXxeJ3XK0b0hsv339nt-7axKfpJG7NA')"

content = content.replace("url('founder.jpg')", orig_bg)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed background image!")

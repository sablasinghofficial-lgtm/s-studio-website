import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the classes to force a shift to the right
content = content.replace(
    'class="w-full h-full object-cover object-[20%_center] filter brightness-90 scale-105',
    'class="w-full h-full object-cover object-left filter brightness-90 scale-[1.3] origin-left'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Shifted extreme right!")

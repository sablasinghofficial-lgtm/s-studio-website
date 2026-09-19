import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert the translation and restore normal cover behavior
content = content.replace(
    'class="w-full h-full object-cover object-center filter brightness-90 translate-x-[10%] lg:translate-x-[20%] transition-transform duration-1000 ease-out"',
    'class="w-full h-full object-cover object-[70%_center] filter brightness-90 scale-105 transition-transform duration-1000 ease-out"'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Reverted shift!")

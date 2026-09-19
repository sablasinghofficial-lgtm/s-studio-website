import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace object-center with object-[20%_center] to shift the image content to the right
content = content.replace(
    'class="w-full h-full object-cover object-center filter',
    'class="w-full h-full object-cover object-[20%_center] filter'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Shifted image right!")

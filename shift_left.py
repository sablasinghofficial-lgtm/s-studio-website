import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reduce translation slightly to move it left
content = content.replace(
    'translate-x-[15%] lg:translate-x-[25%]',
    'translate-x-[10%] lg:translate-x-[20%]'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Shifted slightly left!")

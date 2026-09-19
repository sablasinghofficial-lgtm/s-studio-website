import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Adjust the grid container to translate it up (using negative top margin)
content = content.replace(
    'py-20 lg:py-32 grid lg:grid-cols-12 gap-12 items-center"',
    'py-20 lg:py-32 grid lg:grid-cols-12 gap-12 items-center -mt-16 lg:-mt-24"'
)

# 2. Tighten the space between elements
content = content.replace(
    '<div class="lg:col-span-8 space-y-6 text-left">',
    '<div class="lg:col-span-8 space-y-4 text-left">'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Adjusted spacing!")

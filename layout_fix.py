import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Re-apply the right shift to the photo
content = content.replace(
    'class="w-full h-full object-cover object-[70%_center] filter brightness-90 scale-105 transition-transform duration-1000 ease-out"',
    'class="w-full h-full object-cover object-center filter brightness-90 translate-x-[15%] lg:translate-x-[25%] transition-transform duration-1000 ease-out"'
)

# 2. Adjust the margins (make the max-w larger so it stretches more to the left and right)
# Header
content = content.replace(
    '<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between">',
    '<div class="max-w-[90rem] w-full mx-auto px-6 sm:px-8 lg:px-16 h-20 flex items-center justify-between">'
)

# Hero Section text container
content = content.replace(
    '<div class="relative z-10 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-20 lg:py-32 grid lg:grid-cols-12 gap-12 items-center -mt-16 lg:-mt-24">',
    '<div class="relative z-10 max-w-[90rem] w-full mx-auto px-6 sm:px-8 lg:px-16 py-20 lg:py-32 grid lg:grid-cols-12 gap-12 items-center -mt-16 lg:-mt-24">'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored photo to right and reduced left margin for text!")

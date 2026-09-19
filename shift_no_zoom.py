import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Use translation to shift the image right without scaling
content = content.replace(
    'class="w-full h-full object-cover object-right filter brightness-90 scale-[1.1] translate-x-[5%] lg:translate-x-[10%] transition-transform duration-1000 ease-out"',
    'class="w-full h-full object-cover object-center filter brightness-90 translate-x-[15%] lg:translate-x-[25%] transition-transform duration-1000 ease-out"'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Shifted right without zooming!")

import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Reduce scale from 1.3 to 1.1 and adjust position
# object-left filter brightness-90 scale-[1.3] origin-left
content = content.replace(
    'class="w-full h-full object-cover object-left filter brightness-90 scale-[1.3] origin-left transition-transform duration-1000 ease-out"',
    'class="w-full h-full object-cover object-right filter brightness-90 scale-[1.1] translate-x-[5%] lg:translate-x-[10%] transition-transform duration-1000 ease-out"'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Adjusted photo size and position!")

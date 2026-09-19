import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace ALL instances of old address pattern 1
content = re.sub(
    r'Circular Road, Lalpur, Landmark: Near Nucleus Mall,\s*<br/>\s*Ranchi, Jharkhand\s*-\s*834001,\s*India',
    'Near Sarala Birla University, S Studio,<br/>\n                    Ranchi, Jharkhand, India',
    content
)

# Replace ALL instances of old address pattern 2
content = re.sub(
    r'Circular Road, Lalpur,\s*<br/>\s*Ranchi, Jharkhand\s*834001',
    'Near Sarala Birla University,<br/>\n              S Studio, Ranchi, Jharkhand',
    content
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('All locations fixed with regex!')

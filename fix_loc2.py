with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix remaining location 1 (contact section with extra spaces)
content = content.replace(
    'Circular Road, Lalpur, Landmark: Near Nucleus Mall,<br/>\n                    Ranchi, Jharkhand - 834001, India',
    'Near Sarala Birla University, S Studio,<br/>\n                    Ranchi, Jharkhand, India'
)

# Fix remaining location 2 (footer with different spacing)
content = content.replace(
    'Circular Road, Lalpur,<br/>\n              Ranchi, Jharkhand 834001',
    'Near Sarala Birla University,<br/>\n              S Studio, Ranchi, Jharkhand'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('All locations fixed!')

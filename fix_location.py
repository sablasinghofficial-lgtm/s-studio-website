with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace location 1: Contact/Footer section
content = content.replace(
    'Circular Road, Lalpur, Landmark: Near Nucleus Mall,<br/>\n                   Ranchi, Jharkhand - 834001, India',
    'Near Sarala Birla University, S Studio,<br/>\n                   Ranchi, Jharkhand, India'
)

# Replace location 2: Footer address
content = content.replace(
    'Circular Road, Lalpur,<br/>\n             Ranchi, Jharkhand 834001',
    'Near Sarala Birla University,<br/>\n             S Studio, Ranchi, Jharkhand'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Location updated!')

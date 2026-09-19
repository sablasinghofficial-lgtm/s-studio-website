import re
with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Just replace the URL
content = re.sub(r'https://lh3.googleusercontent.com/aida-public/[A-Za-z0-9_-]+', 'founder.jpg', content)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced all remaining googleusercontent links!")

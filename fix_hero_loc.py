with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix hero section location
content = content.replace(
    'NEAR SARALA BIRLA UNIVERSITY OPPOSITE SIDE S STUDIO',
    'NEAR SARALA BIRLA UNIVERSITY S STUDIO'
)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Hero location fixed!')

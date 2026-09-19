import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the title span and cursor
content = content.replace('<span id="typewriter-title">SABLA SINGH</span><span class="text-warm-ivory animate-pulse">|</span>', 'SABLA SINGH')

# Optionally remove the JS that drives typewriter-title if it's there
content = re.sub(r'// Typewriter Effect for Title.*?if\(titleElement\) \{.*?\}(?=\n\s*//|\n\s*</script>)', '', content, flags=re.DOTALL)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Fixed!")

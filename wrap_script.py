import re
with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the raw JS with wrapped JS
bad_script = r'''    // Scroll Spy for Navbar Highlighting.*?\}\);\s*\}\);'''
good_script = '''<script>
    // Scroll Spy for Navbar Highlighting
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('nav a');

    window.addEventListener('scroll', () => {
        let current = '';
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            if (scrollY >= (sectionTop - 200)) {
                current = section.getAttribute('id');
            }
        });

        navLinks.forEach(link => {
            link.classList.remove('text-champagne', 'border-b', 'border-champagne');
            if (link.getAttribute('href') === '#' + current) {
                link.classList.add('text-champagne', 'border-b', 'border-champagne');
            }
        });
    });
</script>'''

content = re.sub(bad_script, good_script, content, flags=re.DOTALL)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Wrapped script!")

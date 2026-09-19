import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update Logo in Header
content = content.replace(
    '<img src="logo.png" alt="Sabla Singh Academy" class="h-16 sm:h-20 w-auto object-contain mix-blend-screen group-hover:brightness-110 transition-all duration-300">',
    '<img src="logo_transparent.png" alt="Sabla Singh Academy" class="h-10 sm:h-14 w-auto object-contain group-hover:brightness-110 transition-all duration-300">'
)

# Update Logo in Footer
content = content.replace(
    '<img src="logo.png" alt="Sabla Singh Academy" class="h-16 w-auto object-contain mix-blend-screen">',
    '<img src="logo_transparent.png" alt="Sabla Singh Academy" class="h-12 w-auto object-contain">'
)

# 2. Update Founder image in About section
old_about_img = r'<img alt="Sabla Singh - Founder &amp; Master Educator" class="w-full h-auto object-cover object-center filter grayscale-\[15%\] hover:grayscale-0 transition-all duration-700" src="[^"]+"/>'
new_about_img = r'<img alt="Sabla Singh - Founder &amp; Master Educator" class="w-full h-auto object-cover object-top filter transition-all duration-700 rounded-t-full shadow-lg border-b-4 border-champagne" src="founder.jpg"/>'
content = re.sub(old_about_img, new_about_img, content)

# 3. Update Founder image in Gallery
old_gallery_img = r'<img alt="Founder Sabla Singh" class="w-full h-80 object-cover object-top group-hover:scale-110 transition-transform duration-700" src="[^"]+"/>'
new_gallery_img = r'<img alt="Founder Sabla Singh" class="w-full h-80 object-cover object-top group-hover:scale-110 transition-transform duration-700" src="founder.jpg"/>'
content = re.sub(old_gallery_img, new_gallery_img, content)

# 4. Add Scroll Spy for Navbar
scroll_spy_script = '''
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
'''

# Insert script before </body>
content = content.replace('</body>', scroll_spy_script + '\n</body>')

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated logo, images, and nav spy!")

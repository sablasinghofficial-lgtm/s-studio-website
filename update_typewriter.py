import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the HTML part
html_replacement = '''<h1 class="font-luxury-title text-4xl sm:text-6xl xl:text-7xl font-light text-warm-ivory leading-tight tracking-tight">
          <span id="typewriter-title">SABLA SINGH</span><span class="text-warm-ivory animate-pulse">|</span> <br/>
<span class="italic font-luxury-sub font-normal text-champagne" id="typewriter-text">Academy &amp; Atelier</span><span class="text-champagne animate-pulse">|</span>
</h1>'''

pattern_html = r'<h1 class="font-luxury-title text-4xl sm:text-6xl xl:text-7xl font-light text-warm-ivory leading-tight tracking-tight">.*?</h1>'
content = re.sub(pattern_html, html_replacement, content, flags=re.DOTALL)

# Now update the JS part to include the second typewriter
js_replacement = '''
  <script>
    // Typewriter Effect for Hero Section
    const typeWriterElement = document.getElementById('typewriter-text');
    if(typeWriterElement) {
        const words = ['Academy & Atelier', 'Luxury Beauty Studio', 'Bridal Destination', 'Pro Masterclass'];
        let wordIndex = 0;
        let charIndex = 0;
        let isDeleting = false;
        
        function type() {
            const currentWord = words[wordIndex];
            if (isDeleting) {
                typeWriterElement.innerText = currentWord.substring(0, charIndex - 1);
                charIndex--;
            } else {
                typeWriterElement.innerText = currentWord.substring(0, charIndex + 1);
                charIndex++;
            }
            
            let typingSpeed = isDeleting ? 40 : 120;
            
            if (!isDeleting && charIndex === currentWord.length) {
                typingSpeed = 2000; // Pause at end of word
                isDeleting = true;
            } else if (isDeleting && charIndex === 0) {
                isDeleting = false;
                wordIndex = (wordIndex + 1) % words.length;
                typingSpeed = 500; // Pause before new word
            }
            
            setTimeout(type, typingSpeed);
        }
        
        type();
    }

    // Typewriter Effect for Title
    const titleElement = document.getElementById('typewriter-title');
    if(titleElement) {
        const titleWords = ['SABLA SINGH', 'SABLA SINGH'];
        let tWordIndex = 0;
        let tCharIndex = 0;
        let tIsDeleting = false;
        
        function typeTitle() {
            const currentWord = titleWords[tWordIndex];
            if (tIsDeleting) {
                titleElement.innerText = currentWord.substring(0, tCharIndex - 1);
                tCharIndex--;
            } else {
                titleElement.innerText = currentWord.substring(0, tCharIndex + 1);
                tCharIndex++;
            }
            
            let typingSpeed = tIsDeleting ? 40 : 120;
            
            if (!tIsDeleting && tCharIndex === currentWord.length) {
                typingSpeed = 3000; // Pause at end of word
                tIsDeleting = true;
            } else if (tIsDeleting && tCharIndex === 0) {
                tIsDeleting = false;
                tWordIndex = (tWordIndex + 1) % titleWords.length;
                typingSpeed = 500; // Pause before new word
            }
            
            setTimeout(typeTitle, typingSpeed);
        }
        
        typeTitle();
    }
  </script>
'''

pattern_js = r'<script>\s*// Typewriter Effect for Hero Section.*?</script>'
content = re.sub(pattern_js, js_replacement, content, flags=re.DOTALL)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added title typewriter!")

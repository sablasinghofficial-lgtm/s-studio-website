with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_script = '''
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
  </script>
'''

content = content.replace('</body>', js_script + '</body>')

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Script added!")

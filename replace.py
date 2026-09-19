import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

replacement = '''<div class="lg:col-span-8 space-y-6 text-left">
<div class="inline-flex items-center space-x-3 px-3.5 py-1.5 border border-champagne/40 bg-dark-emerald/70 backdrop-blur-sm rounded-none">
<span class="w-1.5 h-1.5 rounded-full bg-champagne animate-pulse"></span>
<p class="text-[11px] sm:text-xs font-medium tracking-mega-wide uppercase text-champagne">
            OPPOSITE SARALA BIRLA UNIVERSITY, RANCHI
          </p>
</div>
<h1 class="font-luxury-title text-4xl sm:text-6xl xl:text-7xl font-light text-warm-ivory leading-tight tracking-tight">
          SABLA SINGH <br/>
<span class="italic font-luxury-sub font-normal text-champagne" id="typewriter-text">Academy &amp; Atelier</span><span class="text-champagne animate-pulse">|</span>
</h1>
<p class="text-champagne font-luxury-sub text-2xl sm:text-3xl font-light italic tracking-wide">
          "Elevating Beauty to an Art Form."
        </p>
<p class="max-w-2xl text-warm-ivory/80 text-sm sm:text-base md:text-lg font-light leading-relaxed">
          Discover a world where sophisticated aesthetics meet masterful technique. We specialize in crafting flawless, personalized bridal looks and offering world-class beauty education, empowering you to shine with unmatched elegance.
        </p>
<div class="pt-2 text-xs tracking-ultra-wide uppercase font-semibold text-champagne/90 border-l-2 border-champagne pl-4">
          LUXURY BRIDAL MAKEUP &middot; ADVANCED SKINCARE &middot; MASTERCLASS ACADEMY
        </div>
<!-- Action CTAs -->'''

pattern = r'<div class="lg:col-span-8 space-y-6 text-left">.*?<!-- Action CTAs -->'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Replaced!")

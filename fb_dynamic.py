import re

with open('code.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add dynamic fetching logic to code.html
dynamic_script = '''
    <script type="module">
      import { getDocs, collection } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";
      
      // Load Services
      async function loadServices() {
        if(!window.db) return;
        const snap = await getDocs(collection(window.db, "services"));
        if(snap.empty) return; // fallback to hardcoded if empty
        const cont = document.querySelector('#services-grid, .grid-cols-1.md\\\\:grid-cols-3');
        if(!cont) return;
        
        let h = '';
        snap.forEach(doc => {
          const d = doc.data();
          h += `<div class="bg-deep-forest border border-champagne/20 p-8 hover:border-champagne/40 transition-colors group">
            <h3 class="font-luxury-title text-2xl text-champagne mb-4 group-hover:text-warm-ivory transition-colors">${d.name}</h3>
            <p class="text-xs text-champagne/60 tracking-[0.2em] uppercase mb-6">${d.tag||""}</p>
            <ul class="space-y-3 mb-8">
              ${(d.pts||[]).map(p=>`<li class="text-warm-ivory/70 text-sm font-light flex items-start gap-3"><span class="text-champagne mt-1">?</span>${p}</li>`).join("")}
            </ul>
          </div>`;
        });
        cont.innerHTML = h;
      }

      // Load Gallery
      async function loadGallery() {
        if(!window.db) return;
        const snap = await getDocs(collection(window.db, "gallery"));
        if(snap.empty) return;
        const cont = document.getElementById('gallery-grid');
        if(!cont) return;

        let h = '';
        snap.forEach(doc => {
          const d = doc.data();
          h += `<div class="gallery-item group relative overflow-hidden aspect-[4/5] ${d.category}">
            <img alt="${d.title}" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105" src="${d.src}"/>
            <div class="absolute inset-0 bg-gradient-to-t from-deep-forest via-deep-forest/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-500 flex flex-col justify-end p-6">
              <span class="text-[10px] tracking-widest uppercase text-champagne mb-2">${d.category}</span>
              <h3 class="text-warm-ivory font-luxury-title text-xl">${d.title}</h3>
            </div>
          </div>`;
        });
        cont.innerHTML = h;
      }

      // Load Testimonials
      async function loadTestimonials() {
        if(!window.db) return;
        const snap = await getDocs(collection(window.db, "testimonials"));
        if(snap.empty) return;
        
        // Find testimonials container
        const conts = document.querySelectorAll('.grid-cols-1.md\\\\:grid-cols-2');
        let cont = null;
        for(let i=0; i<conts.length; i++){
          if(conts[i].innerHTML.includes('Pooja Verma') || conts[i].innerHTML.includes('Dr. Ritika Sahay')) {
            cont = conts[i];
            break;
          }
        }
        if(!cont) return;

        let h = '';
        snap.forEach(doc => {
          const d = doc.data();
          h += `<div class="p-8 border border-champagne/20 bg-warm-ivory/5 relative">
            <div class="text-champagne text-4xl font-luxury-title absolute top-4 left-4 opacity-50">"</div>
            <p class="text-warm-ivory/80 font-light italic leading-relaxed relative z-10 pt-4">"${d.txt}"</p>
            <div class="mt-6 pt-6 border-t border-champagne/10">
              <h4 class="text-champagne font-medium tracking-wide uppercase text-xs">${d.name}</h4>
              <p class="text-warm-ivory/40 text-[10px] tracking-wider uppercase mt-1">${d.ttl||""}</p>
            </div>
          </div>`;
        });
        cont.innerHTML = h;
      }

      window.addEventListener('DOMContentLoaded', () => {
        setTimeout(()=>{
          loadServices();
          loadGallery();
          loadTestimonials();
        }, 500); // small delay to ensure firebase loads
      });
    </script>
'''

if "loadServices()" not in html:
    html = html.replace('</body>', dynamic_script + '\n</body>')
    with open('code.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("code.html dynamic fetching injected!")
else:
    print("Already injected.")

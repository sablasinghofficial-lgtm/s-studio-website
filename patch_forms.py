import re

with open('code.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Patch handleFormSubmit to also save to localStorage
old_form = """function handleFormSubmit(event) {
        event.preventDefault();
        const overlay = document.getElementById('form-success-overlay');"""

new_form = """function handleFormSubmit(event) {
        event.preventDefault();
        // Save to admin panel localStorage
        try {
          const form = event.target;
          const inputs = form.querySelectorAll('input, select, textarea');
          let data = { id: Date.now().toString(), date: new Date().toISOString(), status: 'new' };
          inputs.forEach(i => {
            if (i.name || i.id) {
              const key = i.name || i.id;
              if (key.toLowerCase().includes('name')) data.name = i.value;
              else if (key.toLowerCase().includes('phone') || key.toLowerCase().includes('tel')) data.phone = i.value;
              else if (key.toLowerCase().includes('email')) data.email = i.value;
              else if (key.toLowerCase().includes('service') || i.tagName === 'SELECT') data.service = i.value || i.options?.[i.selectedIndex]?.text || i.value;
              else if (key.toLowerCase().includes('message') || key.toLowerCase().includes('note')) data.message = i.value;
            }
          });
          if (!data.name) data.name = 'Website Visitor';
          if (!data.service) data.service = 'General Enquiry';
          const qs = JSON.parse(localStorage.getItem('ss_queries') || '[]');
          qs.push(data);
          localStorage.setItem('ss_queries', JSON.stringify(qs));
        } catch(e) {}
        const overlay = document.getElementById('form-success-overlay');"""

content = content.replace(old_form, new_form)

# Patch handleModalSubmit to also save to bookings localStorage
old_modal = """function handleModalSubmit(event) {
        event.preventDefault();
        const successOverlay = document.getElementById('modal-success-overlay');"""

new_modal = """function handleModalSubmit(event) {
        event.preventDefault();
        // Save to admin panel bookings
        try {
          const form = event.target;
          const inputs = form.querySelectorAll('input, select, textarea');
          let data = { id: Date.now().toString(), date: new Date().toISOString() };
          inputs.forEach(i => {
            if (i.name || i.id) {
              const key = (i.name || i.id).toLowerCase();
              if (key.includes('name')) data.name = i.value;
              else if (key.includes('phone') || key.includes('tel')) data.phone = i.value;
              else if (key.includes('service') || i.tagName === 'SELECT') data.service = i.value || i.options?.[i.selectedIndex]?.text || i.value;
            }
          });
          if (!data.name) data.name = 'Website Visitor';
          if (!data.service) { const sel = document.getElementById('modal-service-select'); data.service = sel ? (sel.options[sel.selectedIndex]?.text || sel.value) : 'Session Booking'; }
          const bs = JSON.parse(localStorage.getItem('ss_bookings') || '[]');
          bs.push(data);
          localStorage.setItem('ss_bookings', JSON.stringify(bs));
        } catch(e) {}
        const successOverlay = document.getElementById('modal-success-overlay');"""

content = content.replace(old_modal, new_modal)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("code.html patched to save form data to admin!")

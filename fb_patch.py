import re

with open('code.html', 'r', encoding='utf-8') as f:
    html = f.read()

firebase_init = '''
<!-- Firebase SDK -->
<script type="module">
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";
  import { getFirestore, collection, addDoc } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";

  const firebaseConfig = {
    apiKey: "AIzaSyAWFB7kp8Z-z91PPSQTs8vFLxAiwwt_F6g",
    authDomain: "fir-studio-86aaa.firebaseapp.com",
    projectId: "fir-studio-86aaa",
    storageBucket: "fir-studio-86aaa.firebasestorage.app",
    messagingSenderId: "767609525579",
    appId: "1:767609525579:web:5abbde4b39f462083ec4ce",
    measurementId: "G-CFD7R0C8Y7"
  };

  const app = initializeApp(firebaseConfig);
  window.db = getFirestore(app);
  window.addDoc = addDoc;
  window.collection = collection;
</script>
'''

if "firebase-app.js" not in html:
    html = html.replace('</body>', firebase_init + '\n</body>')

new_handle_form = '''async function handleFormSubmit(event) {
      event.preventDefault();
      
      const form = event.target;
      const inputs = form.querySelectorAll('input, select, textarea');
      const data = {
        name: inputs[0].value,
        phone: inputs[1].value,
        email: inputs[2] ? inputs[2].value : '',
        service: inputs[3] ? inputs[3].value : '',
        message: inputs[4] ? inputs[4].value : '',
        date: new Date().toISOString(),
        status: 'new'
      };

      try {
        if(window.db) {
          await window.addDoc(window.collection(window.db, "queries"), data);
        }
        const overlay = document.getElementById('form-success-overlay');
        overlay.classList.remove('hidden');
      } catch (e) {
        console.error("Error adding query:", e);
      }
    }'''

html = re.sub(r'function handleFormSubmit\(event\).*?overlay\.classList\.remove\(\'hidden\'\);\s*\}', new_handle_form, html, flags=re.DOTALL)

new_modal_submit = '''async function handleModalSubmit(event) {
      event.preventDefault();
      const form = event.target;
      const inputs = form.querySelectorAll('input, textarea');
      const data = {
        name: inputs[0].value,
        phone: inputs[1].value,
        service: inputs[2].value,
        notes: inputs[3] ? inputs[3].value : '',
        date: new Date().toISOString()
      };

      try {
        if(window.db) {
          await window.addDoc(window.collection(window.db, "bookings"), data);
        }
        document.getElementById('booking-form').classList.add('hidden');
        document.getElementById('booking-success').classList.remove('hidden');
      } catch (e) {
        console.error("Error adding booking:", e);
      }
    }'''

html = re.sub(r'function handleModalSubmit\(event\).*?document\.getElementById\(\'booking-success\'\)\.classList\.remove\(\'hidden\'\);\s*\}', new_modal_submit, html, flags=re.DOTALL)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("code.html Firebase forms injected!")

admin_html = open('admin_template.txt', 'r', encoding='utf-8').read()
open('admin.html', 'w', encoding='utf-8').write(admin_html)
print(f'Done! Size: {len(admin_html)} bytes')

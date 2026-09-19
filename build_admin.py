# build_admin.py - S Studio Full Admin Panel Generator (Firebase & Cloudinary)
import os

def w(f, text):
    f.write(text)

with open('admin.html', 'w', encoding='utf-8') as f:
    w(f, '<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    w(f, '<meta charset="UTF-8"/>\n<meta name="viewport" content="width=device-width,initial-scale=1.0"/>\n')
    w(f, '<title>S Studio | Cloud Admin Panel</title>\n')
    w(f, '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,400&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet"/>\n')
    w(f, '<style>\n')
    w(f, '*{font-family:Jost,sans-serif;box-sizing:border-box;margin:0;padding:0}\n')
    w(f, 'body{background:#041E16;color:#F5F0E8;min-height:100vh}\n')
    w(f, '.fl{font-family:"Cormorant Garamond",serif}\n')
    w(f, '.sb{width:248px;background:#031812;border-right:1px solid rgba(201,169,110,.15);position:fixed;top:0;left:0;height:100%;display:flex;flex-direction:column;z-index:40}\n')
    w(f, '.sbi{width:100%;text-align:left;padding:11px 16px;font-size:13px;color:rgba(245,240,232,.7);background:none;border:none;border-left:3px solid transparent;cursor:pointer;display:flex;align-items:center;gap:10px;transition:all .2s}\n')
    w(f, '.sbi:hover,.sbi.on{border-left-color:#C9A96E;background:rgba(201,169,110,.08);color:#F5F0E8}\n')
    w(f, '.main{margin-left:248px;display:flex;flex-direction:column;min-height:100vh}\n')
    w(f, '.topbar{background:rgba(4,24,18,.9);border-bottom:1px solid rgba(201,169,110,.15);padding:13px 26px;display:flex;align-items:center;justify-content:space-between;position:sticky;top:0;z-index:30;backdrop-filter:blur(8px)}\n')
    w(f, '.content{padding:24px 26px;flex:1}\n')
    w(f, '.sect{display:none}.sect.on{display:block}\n')
    w(f, '.scard{background:linear-gradient(135deg,#0A3D2B,#062C20);border:1px solid rgba(201,169,110,.28)}\n')
    w(f, '.card{background:rgba(10,61,43,.38);border:1px solid rgba(201,169,110,.13);padding:18px;margin-bottom:12px;transition:border-color .25s}\n')
    w(f, '.card:hover{border-color:rgba(201,169,110,.3)}\n')
    w(f, '.inp{width:100%;background:#062C20;border:1px solid rgba(201,169,110,.28);color:#F5F0E8;font-size:13px;padding:9px 13px;outline:none;transition:border-color .2s}\n')
    w(f, '.inp:focus{border-color:#C9A96E}\n')
    w(f, 'textarea.inp{resize:vertical}\n')
    w(f, '.bg{background:linear-gradient(135deg,#C9A96E,#A07840);color:#062C20;font-weight:600;cursor:pointer;border:none;transition:all .25s;font-size:11px;text-transform:uppercase;letter-spacing:.18em}\n')
    w(f, '.bg:hover{background:linear-gradient(135deg,#E8CC8E,#C9A96E)}\n')
    w(f, '.btn-sm{font-size:10px;text-transform:uppercase;letter-spacing:.13em;padding:4px 11px;cursor:pointer;border:none;transition:all .25s;white-space:nowrap}\n')
    w(f, '.be{background:rgba(201,169,110,.12);color:#C9A96E;border:1px solid rgba(201,169,110,.28)}.be:hover{background:rgba(201,169,110,.22)}\n')
    w(f, '.bd{background:rgba(239,68,68,.09);color:#f87171;border:1px solid rgba(239,68,68,.22)}.bd:hover{background:rgba(239,68,68,.18)}\n')
    w(f, '.bv{background:rgba(34,197,94,.09);color:#4ade80;border:1px solid rgba(34,197,94,.22)}.bv:hover{background:rgba(34,197,94,.16)}\n')
    w(f, '.tabb{font-size:11px;text-transform:uppercase;letter-spacing:.18em;padding:7px 15px;border:1px solid rgba(201,169,110,.28);background:none;color:rgba(245,240,232,.5);cursor:pointer;transition:all .2s}\n')
    w(f, '.tabb.on{background:#C9A96E;color:#062C20;border-color:#C9A96E}\n')
    w(f, '.tg{font-size:9px;padding:2px 8px;border-radius:20px;text-transform:uppercase;letter-spacing:.07em;display:inline-block}\n')
    w(f, '.tn{background:rgba(34,197,94,.13);color:#22c55e;border:1px solid rgba(34,197,94,.28)}\n')
    w(f, '.tr{background:rgba(201,169,110,.13);color:#C9A96E;border:1px solid rgba(201,169,110,.28)}\n')
    w(f, '.tp{background:rgba(234,179,8,.13);color:#eab308;border:1px solid rgba(234,179,8,.28)}\n')
    w(f, '.gth{aspect-ratio:1;overflow:hidden;border:2px solid rgba(201,169,110,.25);position:relative;cursor:pointer}\n')
    w(f, '.gth img{width:100%;height:100%;object-fit:cover;transition:transform .3s}\n')
    w(f, '.gth:hover img{transform:scale(1.05)}\n')
    w(f, '.gover{position:absolute;inset:0;background:rgba(4,24,18,.88);opacity:0;transition:opacity .28s;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:6px;padding:10px}\n')
    w(f, '.gth:hover .gover{opacity:1}\n')
    w(f, '.nd{width:7px;height:7px;background:#22c55e;border-radius:50%;display:inline-block;animation:pu 1.5s infinite}\n')
    w(f, '@keyframes pu{0%,100%{opacity:1}50%{opacity:.35}}\n')
    w(f, '.mo{background:rgba(3,24,18,.96);backdrop-filter:blur(10px);position:fixed;inset:0;z-index:50;display:none;align-items:center;justify-content:center}\n')
    w(f, '.mbox{background:#0A3D2B;border:1px solid rgba(201,169,110,.32);width:100%;max-width:540px;margin:16px;padding:30px;position:relative;max-height:90vh;overflow-y:auto}\n')
    w(f, '.uz{border:2px dashed rgba(201,169,110,.35);cursor:pointer;text-align:center;padding:16px;color:rgba(245,240,232,.45);font-size:13px;transition:all .28s;display:block}\n')
    w(f, '.uz:hover{border-color:#C9A96E;color:#C9A96E;background:rgba(201,169,110,.04)}\n')
    w(f, 'input[type=file]{display:none}\n')
    w(f, '#ls{position:fixed;inset:0;z-index:60;display:flex;align-items:center;justify-content:center;background:radial-gradient(ellipse at center,#0A3D2B,#041E16)}\n')
    w(f, '.lbox{background:rgba(6,44,32,.88);border:1px solid rgba(201,169,110,.28);width:100%;max-width:400px;margin:16px;padding:38px;backdrop-filter:blur(20px)}\n')
    w(f, '::-webkit-scrollbar{width:4px}::-webkit-scrollbar-thumb{background:#C9A96E;border-radius:3px}\n')
    w(f, '.lbl{display:block;font-size:10px;text-transform:uppercase;letter-spacing:.18em;color:rgba(201,169,110,.6);margin-bottom:4px}\n')
    w(f, '.gr2{display:grid;grid-template-columns:1fr 1fr;gap:10px}\n')
    w(f, '.g4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}\n')
    
    # Loaders
    w(f, '.loader{width:16px;height:16px;border:2px solid rgba(201,169,110,.3);border-top-color:#C9A96E;border-radius:50%;animation:spin 1s linear infinite;display:inline-block;vertical-align:middle;margin-right:6px}\n')
    w(f, '@keyframes spin{to{transform:rotate(360deg)}}\n')
    
    w(f, '</style>\n</head>\n<body>\n')

    # LOGIN
    w(f, '<div id="ls">\n<div class="lbox">\n')
    w(f, '<div style="text-align:center;margin-bottom:24px">\n')
    w(f, '<img src="logo_transparent.png" alt="" onerror="this.style.display=\'none\'" style="height:50px;display:block;margin:0 auto 9px;object-fit:contain"/>\n')
    w(f, '<p class="fl" style="font-size:24px;color:#C9A96E;font-weight:300">S Studio</p>\n')
    w(f, '<p style="font-size:10px;letter-spacing:.28em;text-transform:uppercase;color:rgba(245,240,232,.36);margin-top:3px">Admin Control Panel</p>\n')
    w(f, '<div style="height:1px;background:rgba(201,169,110,.25);width:46px;margin:11px auto 0"></div>\n</div>\n')
    w(f, '<div id="lerr" style="display:none;background:rgba(127,29,29,.25);border:1px solid rgba(239,68,68,.25);color:#fca5a5;font-size:12px;text-align:center;padding:8px;margin-bottom:11px">Invalid credentials.</div>\n')
    w(f, '<form onsubmit="doLogin(event)">\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Email</label><input id="lemail" class="inp" type="text" placeholder="Login Email"/></div>\n')
    w(f, '<div style="margin-bottom:15px"><label class="lbl">Password</label><div style="position:relative"><input id="lpass" class="inp" type="password" placeholder="Password" style="padding-right:46px"/><button type="button" onclick="togglePw()" style="position:absolute;right:10px;top:50%;transform:translateY(-50%);background:none;border:none;color:rgba(201,169,110,.5);font-size:10px;text-transform:uppercase;cursor:pointer">Show</button></div></div>\n')
    w(f, '<button type="submit" id="lbtn" class="bg" style="width:100%;padding:12px">Access Admin Panel &rarr;</button>\n')
    w(f, '</form>\n</div>\n</div>\n')

    # MAIN PANEL
    w(f, '<div id="ap" style="display:none">\n')
    w(f, '<div class="main">\n')

    # SIDEBAR
    w(f, '<aside class="sb">\n')
    w(f, '<div style="padding:18px 20px;border-bottom:1px solid rgba(201,169,110,.15)">\n')
    w(f, '<img src="logo_transparent.png" alt="" onerror="this.style.display=\'none\'" style="height:32px;object-fit:contain;display:block;margin-bottom:5px"/>\n')
    w(f, '<p class="fl" style="color:#C9A96E;font-size:16px;font-weight:300">S Studio</p>\n')
    w(f, '<p style="font-size:9px;letter-spacing:.18em;text-transform:uppercase;color:rgba(245,240,232,.26)">Admin Panel</p>\n</div>\n')
    w(f, '<nav style="flex:1;padding:10px 8px;overflow-y:auto">\n')
    w(f, '<p style="font-size:9px;text-transform:uppercase;letter-spacing:.18em;color:rgba(245,240,232,.24);padding:0 10px;margin:7px 0 5px">Main</p>\n')
    w(f, '<button class="sbi on" onclick="sp(this,\'dashboard\')" id="nb-dashboard"><span style="color:#C9A96E">&#9672;</span>Dashboard</button>\n')
    w(f, '<button class="sbi" onclick="sp(this,\'queries\')" id="nb-queries"><span style="color:#C9A96E">&#9993;</span>Queries<span id="qbadge" style="margin-left:auto;background:#22c55e;color:#fff;font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700">0</span></button>\n')
    w(f, '<button class="sbi" onclick="sp(this,\'bookings\')" id="nb-bookings"><span style="color:#C9A96E">&#9711;</span>Bookings<span id="bbadge" style="margin-left:auto;background:#C9A96E;color:#062C20;font-size:9px;padding:1px 6px;border-radius:20px;font-weight:700">0</span></button>\n')
    w(f, '<button class="sbi" onclick="sp(this,\'gallery\')" id="nb-gallery"><span style="color:#C9A96E">&#8862;</span>Gallery</button>\n')
    w(f, '<p style="font-size:9px;text-transform:uppercase;letter-spacing:.18em;color:rgba(245,240,232,.24);padding:0 10px;margin:11px 0 5px">Content</p>\n')
    w(f, '<button class="sbi" onclick="sp(this,\'services\')" id="nb-services"><span style="color:#C9A96E">&#10022;</span>Services</button>\n')
    w(f, '<button class="sbi" onclick="sp(this,\'testimonials\')" id="nb-testimonials"><span style="color:#C9A96E">&#10077;</span>Testimonials</button>\n')
    w(f, '<button class="sbi" onclick="sp(this,\'settings\')" id="nb-settings"><span style="color:#C9A96E">&#9881;</span>Settings</button>\n')
    w(f, '<a href="code.html" target="_blank" class="sbi" style="display:flex;text-decoration:none"><span style="color:#C9A96E">&#8599;</span>View Website</a>\n')
    w(f, '</nav>\n<div style="padding:12px 17px;border-top:1px solid rgba(201,169,110,.15)">\n')
    w(f, '<p style="font-size:12px;color:#C9A96E;font-weight:500">Sabla Singh</p>\n')
    w(f, '<p style="font-size:10px;color:rgba(245,240,232,.3)">Sablasingh@0404</p>\n')
    w(f, '<button onclick="doLogout()" style="margin-top:5px;background:none;border:none;font-size:10px;text-transform:uppercase;letter-spacing:.13em;color:rgba(239,68,68,.48);cursor:pointer">&#8617; Logout</button>\n')
    w(f, '</div>\n</aside>\n')

    # TOPBAR
    w(f, '<header class="topbar">\n')
    w(f, '<div><h1 id="ptitle" class="fl" style="font-size:20px;color:#C9A96E;font-weight:300">Dashboard</h1><p id="psub" style="font-size:10px;text-transform:uppercase;letter-spacing:.18em;color:rgba(245,240,232,.3);margin-top:1px">Overview &amp; Analytics</p></div>\n')
    w(f, '<div style="display:flex;align-items:center;gap:13px"><div style="display:flex;align-items:center;gap:6px"><span class="nd" id="livend"></span><span style="font-size:11px;color:rgba(245,240,232,.38)" id="livetxt">Connecting...</span></div><div style="text-align:right"><p id="cdate" style="font-size:12px;color:rgba(245,240,232,.48)"></p><p id="ctime" style="font-size:10px;color:rgba(245,240,232,.26)"></p></div></div>\n')
    w(f, '</header>\n')

    # CONTENT AREA
    w(f, '<div class="content">\n')

    # --- DASHBOARD ---
    w(f, '<div class="sect on" id="s-dashboard">\n')
    w(f, '<div class="g4" style="margin-bottom:22px">\n')
    w(f, '<div class="scard" style="padding:20px"><p style="font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:rgba(201,169,110,.62);margin-bottom:5px">Total Queries</p><p class="fl" id="sqs" style="font-size:36px;color:#C9A96E;font-weight:300"><span class="loader"></span></p><p style="font-size:10px;color:rgba(245,240,232,.32);margin-top:5px">Form submissions</p></div>\n')
    w(f, '<div class="scard" style="padding:20px"><p style="font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:rgba(201,169,110,.62);margin-bottom:5px">Unread</p><p class="fl" id="snew" style="font-size:36px;color:#C9A96E;font-weight:300"><span class="loader"></span></p><p style="font-size:10px;color:rgba(245,240,232,.32);margin-top:5px">New messages</p></div>\n')
    w(f, '<div class="scard" style="padding:20px"><p style="font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:rgba(201,169,110,.62);margin-bottom:5px">Bookings</p><p class="fl" id="sbs" style="font-size:36px;color:#C9A96E;font-weight:300"><span class="loader"></span></p><p style="font-size:10px;color:rgba(245,240,232,.32);margin-top:5px">Session requests</p></div>\n')
    w(f, '<div class="scard" style="padding:20px"><p style="font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:rgba(201,169,110,.62);margin-bottom:5px">Gallery Photos</p><p class="fl" id="sgl" style="font-size:36px;color:#C9A96E;font-weight:300"><span class="loader"></span></p><p style="font-size:10px;color:rgba(245,240,232,.32);margin-top:5px">Published</p></div>\n')
    w(f, '</div>\n')
    w(f, '<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">\n')
    w(f, '<div style="background:rgba(10,61,43,.38);border:1px solid rgba(201,169,110,.16);padding:20px"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px"><h3 class="fl" style="font-size:17px;color:#C9A96E;font-weight:300">Recent Queries</h3><button onclick="sp(document.getElementById(\'nb-queries\'),\'queries\')" style="font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:rgba(201,169,110,.5);background:none;border:none;cursor:pointer">View All &rarr;</button></div><div id="rql"><p style="font-size:13px;color:rgba(245,240,232,.32);text-align:center;padding:22px 0"><span class="loader"></span> Loading...</p></div></div>\n')
    w(f, '<div style="background:rgba(10,61,43,.38);border:1px solid rgba(201,169,110,.16);padding:20px"><div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px"><h3 class="fl" style="font-size:17px;color:#C9A96E;font-weight:300">Recent Bookings</h3><button onclick="sp(document.getElementById(\'nb-bookings\'),\'bookings\')" style="font-size:10px;text-transform:uppercase;letter-spacing:.16em;color:rgba(201,169,110,.5);background:none;border:none;cursor:pointer">View All &rarr;</button></div><div id="rbl"><p style="font-size:13px;color:rgba(245,240,232,.32);text-align:center;padding:22px 0"><span class="loader"></span> Loading...</p></div></div>\n')
    w(f, '</div>\n')
    w(f, '<div style="margin-top:18px;background:rgba(10,61,43,.38);border:1px solid rgba(201,169,110,.16);padding:20px"><h3 class="fl" style="font-size:17px;color:#C9A96E;font-weight:300;margin-bottom:12px">Quick Actions</h3><div class="g4">\n')
    w(f, '<button onclick="sp(document.getElementById(\'nb-gallery\'),\'gallery\')" style="background:#062C20;border:1px solid rgba(201,169,110,.22);padding:16px;text-align:center;cursor:pointer;width:100%"><p style="font-size:20px;color:#C9A96E;margin-bottom:5px">&#8853;</p><p style="font-size:11px;color:rgba(245,240,232,.6)">Add Photo</p></button>\n')
    w(f, '<button onclick="sp(document.getElementById(\'nb-queries\'),\'queries\')" style="background:#062C20;border:1px solid rgba(201,169,110,.22);padding:16px;text-align:center;cursor:pointer;width:100%"><p style="font-size:20px;color:#C9A96E;margin-bottom:5px">&#9993;</p><p style="font-size:11px;color:rgba(245,240,232,.6)">View Queries</p></button>\n')
    w(f, '<a href="code.html" target="_blank" style="background:#062C20;border:1px solid rgba(201,169,110,.22);padding:16px;text-align:center;text-decoration:none;display:block"><p style="font-size:20px;color:#C9A96E;margin-bottom:5px">&#8599;</p><p style="font-size:11px;color:rgba(245,240,232,.6)">Open Website</p></a>\n')
    w(f, '</div></div>\n</div>\n')

    # --- QUERIES ---
    w(f, '<div class="sect" id="s-queries">\n')
    w(f, '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">\n')
    w(f, '<div style="display:flex;gap:5px"><button onclick="fq(\'all\')" class="tabb on" id="qt-all">All</button><button onclick="fq(\'new\')" class="tabb" id="qt-new">New</button><button onclick="fq(\'read\')" class="tabb" id="qt-read">Read</button></div>\n')
    w(f, '<div style="display:flex;gap:7px"><button onclick="openAddQ()" class="bg" style="padding:8px 16px">+ Add Query</button></div>\n')
    w(f, '</div>\n<div id="qc"><p style="text-align:center;padding:45px 0;color:rgba(245,240,232,.3)"><span class="loader"></span> Loading queries...</p></div>\n</div>\n')

    # --- BOOKINGS ---
    w(f, '<div class="sect" id="s-bookings">\n')
    w(f, '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px">\n')
    w(f, '<p style="font-size:13px;color:rgba(245,240,232,.5)">Session booking requests.</p>\n')
    w(f, '<div style="display:flex;gap:7px"><button onclick="openAddB()" class="bg" style="padding:8px 16px">+ Add Booking</button></div>\n')
    w(f, '</div>\n<div id="bc"><p style="text-align:center;padding:45px 0;color:rgba(245,240,232,.3)"><span class="loader"></span> Loading bookings...</p></div>\n</div>\n')

    # --- GALLERY ---
    w(f, '<div class="sect" id="s-gallery">\n')
    w(f, '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px"><p style="font-size:13px;color:rgba(245,240,232,.5)">Manage gallery photos.</p><button onclick="openAddPhoto()" class="bg" style="padding:9px 20px">+ Add New Photo</button></div>\n')
    w(f, '<div id="ga" style="display:grid;grid-template-columns:repeat(4,1fr);gap:13px"><p style="grid-column:span 4;text-align:center;color:rgba(245,240,232,.3)"><span class="loader"></span> Loading gallery...</p></div>\n</div>\n')

    # --- SERVICES ---
    w(f, '<div class="sect" id="s-services">\n')
    w(f, '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px"><p style="font-size:13px;color:rgba(245,240,232,.5)">Manage service listings.</p><button onclick="openAddSvc()" class="bg" style="padding:9px 20px">+ Add Service</button></div>\n')
    w(f, '<div id="svc-list"><p style="text-align:center;color:rgba(245,240,232,.3)"><span class="loader"></span> Loading services...</p></div>\n</div>\n')

    # --- TESTIMONIALS ---
    w(f, '<div class="sect" id="s-testimonials">\n')
    w(f, '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:16px"><p style="font-size:13px;color:rgba(245,240,232,.5)">Manage client testimonials.</p><button onclick="openAddT()" class="bg" style="padding:9px 20px">+ Add Testimonial</button></div>\n')
    w(f, '<div id="test-list"><p style="text-align:center;color:rgba(245,240,232,.3)"><span class="loader"></span> Loading testimonials...</p></div>\n</div>\n')

    # --- SETTINGS ---
    w(f, '<div class="sect" id="s-settings">\n')
    w(f, '<div style="display:grid;grid-template-columns:1fr 1fr;gap:18px">\n')
    w(f, '<div style="background:rgba(10,61,43,.38);border:1px solid rgba(201,169,110,.16);padding:20px"><h3 class="fl" style="font-size:18px;color:#C9A96E;font-weight:300;margin-bottom:13px">Account Details</h3><div style="margin-bottom:11px"><label class="lbl">Email</label><input value="Sablasingh@0404" readonly class="inp" style="opacity:.62;cursor:not-allowed"/></div><div><label class="lbl">Password</label><input type="password" value="sablasingh123" readonly class="inp" style="opacity:.62;cursor:not-allowed"/></div></div>\n')
    w(f, '<div style="background:rgba(10,61,43,.38);border:1px solid rgba(201,169,110,.16);padding:20px"><h3 class="fl" style="font-size:18px;color:#C9A96E;font-weight:300;margin-bottom:13px">Business Info</h3><div style="font-size:13px;color:rgba(245,240,232,.65)">\n')
    w(f, '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid rgba(201,169,110,.09)"><span style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(245,240,232,.32)">Brand</span><span style="font-size:12px">S Studio</span></div>\n')
    w(f, '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid rgba(201,169,110,.09)"><span style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(245,240,232,.32)">Location</span><span style="font-size:12px">Near Sarala Birla University, Ranchi</span></div>\n')
    w(f, '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid rgba(201,169,110,.09)"><span style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(245,240,232,.32)">Phone</span><span style="font-size:12px">+91 94311 02938</span></div>\n')
    w(f, '<div style="display:flex;justify-content:space-between;padding:6px 0;border-bottom:1px solid rgba(201,169,110,.09)"><span style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(245,240,232,.32)">WhatsApp</span><span style="font-size:12px">+91 70048 12345</span></div>\n')
    w(f, '<div style="display:flex;justify-content:space-between;padding:6px 0"><span style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(245,240,232,.32)">Academy</span><a href="http://www.sablasinghacademy.com" target="_blank" style="color:#C9A96E;font-size:11px">sablasinghacademy.com</a></div>\n')
    w(f, '</div></div>\n')
    w(f, '</div>\n</div>\n')
    w(f, '</div>\n</div>\n</div>\n</div>\n')

    # MODALS
    # Query Modal
    w(f, '<div class="mo" id="qm"><div class="mbox">\n')
    w(f, '<button onclick="closeQM()" style="position:absolute;top:11px;right:13px;background:none;border:none;color:rgba(245,240,232,.38);font-size:19px;cursor:pointer">&times;</button>\n')
    w(f, '<h3 class="fl" id="qm-title" style="font-size:21px;color:#C9A96E;font-weight:300;margin-bottom:18px">Query Details</h3>\n')
    w(f, '<div id="qm-view"></div>\n')
    w(f, '<div id="qm-form" style="display:none">\n')
    w(f, '<div class="gr2" style="margin-bottom:10px">\n')
    w(f, '<div><label class="lbl">Name *</label><input id="qe-name" class="inp" type="text"/></div>\n')
    w(f, '<div><label class="lbl">Phone</label><input id="qe-phone" class="inp" type="text"/></div>\n')
    w(f, '<div><label class="lbl">Email</label><input id="qe-email" class="inp" type="text"/></div>\n')
    w(f, '<div><label class="lbl">Service *</label><input id="qe-service" class="inp" type="text"/></div>\n')
    w(f, '<div style="grid-column:span 2"><label class="lbl">Message</label><textarea id="qe-message" class="inp" style="height:75px"></textarea></div>\n')
    w(f, '<div><label class="lbl">Status</label><select id="qe-status" class="inp"><option value="new">New</option><option value="read">Read</option></select></div>\n')
    w(f, '</div>\n<div style="display:flex;gap:9px;margin-top:13px"><button onclick="saveQ()" class="bg" style="flex:1;padding:10px" id="qm-sbtn">Save</button><button onclick="closeQM()" style="flex:1;padding:10px;font-size:11px;text-transform:uppercase;letter-spacing:.16em;background:none;border:1px solid rgba(201,169,110,.25);color:rgba(245,240,232,.55);cursor:pointer">Cancel</button></div>\n')
    w(f, '</div>\n')
    w(f, '<div id="qm-btns" style="display:flex;gap:9px;margin-top:14px">\n')
    w(f, '<a id="qwa" href="#" target="_blank" class="bg" style="flex:1;padding:10px;text-decoration:none;text-align:center;display:block">&#128232; WhatsApp</a>\n')
    w(f, '<button onclick="editQ()" style="flex:1;padding:10px;font-size:11px;text-transform:uppercase;letter-spacing:.16em;background:none;border:1px solid rgba(201,169,110,.25);color:#C9A96E;cursor:pointer">&#9998; Edit</button>\n')
    w(f, '<button onclick="delQ()" style="padding:10px 14px;font-size:11px;text-transform:uppercase;letter-spacing:.13em;background:none;border:1px solid rgba(239,68,68,.25);color:#f87171;cursor:pointer">&#128465;</button>\n')
    w(f, '</div>\n</div></div>\n')

    # Booking Modal
    w(f, '<div class="mo" id="bm"><div class="mbox">\n')
    w(f, '<button onclick="closeBM()" style="position:absolute;top:11px;right:13px;background:none;border:none;color:rgba(245,240,232,.38);font-size:19px;cursor:pointer">&times;</button>\n')
    w(f, '<h3 class="fl" id="bm-title" style="font-size:21px;color:#C9A96E;font-weight:300;margin-bottom:18px">Booking</h3>\n')
    w(f, '<div class="gr2" style="margin-bottom:10px">\n')
    w(f, '<div><label class="lbl">Name *</label><input id="be-name" class="inp" type="text"/></div>\n')
    w(f, '<div><label class="lbl">Phone</label><input id="be-phone" class="inp" type="text"/></div>\n')
    w(f, '<div style="grid-column:span 2"><label class="lbl">Service *</label><input id="be-service" class="inp" type="text" placeholder="e.g. Bridal Couture Makeup"/></div>\n')
    w(f, '<div style="grid-column:span 2"><label class="lbl">Notes</label><textarea id="be-notes" class="inp" style="height:65px"></textarea></div>\n')
    w(f, '</div>\n<div style="display:flex;gap:9px;margin-top:13px"><button onclick="saveB()" class="bg" style="flex:1;padding:10px" id="bm-sbtn">Save Booking</button><button onclick="closeBM()" style="flex:1;padding:10px;font-size:11px;text-transform:uppercase;letter-spacing:.16em;background:none;border:1px solid rgba(201,169,110,.25);color:rgba(245,240,232,.55);cursor:pointer">Cancel</button></div>\n')
    w(f, '</div></div>\n')

    # Photo Modal (Cloudinary Integrated)
    w(f, '<div class="mo" id="pm"><div class="mbox">\n')
    w(f, '<button onclick="closePM()" style="position:absolute;top:11px;right:13px;background:none;border:none;color:rgba(245,240,232,.38);font-size:19px;cursor:pointer">&times;</button>\n')
    w(f, '<h3 class="fl" id="pm-title" style="font-size:21px;color:#C9A96E;font-weight:300;margin-bottom:18px">Add New Photo</h3>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Photo Title *</label><input id="pt-title" class="inp" type="text" placeholder="e.g. Bridal Look"/></div>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Category</label><select id="pt-cat" class="inp"><option value="bridal">Bridal</option><option value="makeup">Makeup</option><option value="studio">Studio</option><option value="academy">Academy</option></select></div>\n')
    w(f, '<div style="margin-bottom:11px;display:none"><label class="lbl">Image URL</label><input id="pt-url" class="inp" type="text" readonly/></div>\n')
    w(f, '<label for="pt-file" class="uz" id="pt-file-lbl" style="margin-bottom:11px">&#128193; Click to Upload Photo</label><input type="file" id="pt-file" accept="image/*" onchange="uploadToCloudinary(event)"/>\n')
    w(f, '<div id="pt-prev" style="display:none;margin-bottom:11px"><img id="pt-previmg" src="" style="width:100%;height:130px;object-fit:cover;border:1px solid rgba(201,169,110,.22)"/></div>\n')
    w(f, '<div style="display:flex;gap:9px;margin-top:13px"><button onclick="savePhoto()" class="bg" style="flex:1;padding:10px" id="pm-sbtn">Save Photo</button><button onclick="closePM()" style="flex:1;padding:10px;font-size:11px;text-transform:uppercase;letter-spacing:.16em;background:none;border:1px solid rgba(201,169,110,.25);color:rgba(245,240,232,.55);cursor:pointer">Cancel</button></div>\n')
    w(f, '</div></div>\n')

    # Service Modal
    w(f, '<div class="mo" id="svcm"><div class="mbox">\n')
    w(f, '<button onclick="closeSvcM()" style="position:absolute;top:11px;right:13px;background:none;border:none;color:rgba(245,240,232,.38);font-size:19px;cursor:pointer">&times;</button>\n')
    w(f, '<h3 class="fl" id="svcm-title" style="font-size:21px;color:#C9A96E;font-weight:300;margin-bottom:18px">Add Service</h3>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Service Name *</label><input id="sv-name" class="inp" type="text" placeholder="e.g. HD Makeup"/></div>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Tagline / Label</label><input id="sv-tag" class="inp" type="text" placeholder="e.g. Custom Consultation"/></div>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Bullet Points (one per line)</label><textarea id="sv-pts" class="inp" style="height:95px" placeholder="Point 1&#10;Point 2&#10;Point 3"></textarea></div>\n')
    w(f, '<div style="display:flex;gap:9px;margin-top:13px"><button onclick="saveSvc()" class="bg" style="flex:1;padding:10px" id="svcm-sbtn">Save Service</button><button onclick="closeSvcM()" style="flex:1;padding:10px;font-size:11px;text-transform:uppercase;letter-spacing:.16em;background:none;border:1px solid rgba(201,169,110,.25);color:rgba(245,240,232,.55);cursor:pointer">Cancel</button></div>\n')
    w(f, '</div></div>\n')

    # Testimonial Modal
    w(f, '<div class="mo" id="tm"><div class="mbox">\n')
    w(f, '<button onclick="closeTM()" style="position:absolute;top:11px;right:13px;background:none;border:none;color:rgba(245,240,232,.38);font-size:19px;cursor:pointer">&times;</button>\n')
    w(f, '<h3 class="fl" id="tm-title" style="font-size:21px;color:#C9A96E;font-weight:300;margin-bottom:18px">Add Testimonial</h3>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Client Name *</label><input id="te-name" class="inp" type="text"/></div>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Designation / Title</label><input id="te-ttl" class="inp" type="text" placeholder="e.g. Bridal Client"/></div>\n')
    w(f, '<div style="margin-bottom:11px"><label class="lbl">Testimonial *</label><textarea id="te-txt" class="inp" style="height:90px"></textarea></div>\n')
    w(f, '<div style="display:flex;gap:9px;margin-top:13px"><button onclick="saveT()" class="bg" style="flex:1;padding:10px" id="tm-sbtn">Save</button><button onclick="closeTM()" style="flex:1;padding:10px;font-size:11px;text-transform:uppercase;letter-spacing:.16em;background:none;border:1px solid rgba(201,169,110,.25);color:rgba(245,240,232,.55);cursor:pointer">Cancel</button></div>\n')
    w(f, '</div></div>\n')

    # Firebase SDK & JS
    w(f, '<script type="module">\n')
    w(f, 'import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-app.js";\n')
    w(f, 'import { getFirestore, collection, addDoc, getDocs, doc, updateDoc, deleteDoc, onSnapshot } from "https://www.gstatic.com/firebasejs/10.12.0/firebase-firestore.js";\n')
    w(f, 'const firebaseConfig = {\n')
    w(f, '  apiKey: "AIzaSyAWFB7kp8Z-z91PPSQTs8vFLxAiwwt_F6g",\n')
    w(f, '  authDomain: "fir-studio-86aaa.firebaseapp.com",\n')
    w(f, '  projectId: "fir-studio-86aaa",\n')
    w(f, '  storageBucket: "fir-studio-86aaa.firebasestorage.app",\n')
    w(f, '  messagingSenderId: "767609525579",\n')
    w(f, '  appId: "1:767609525579:web:5abbde4b39f462083ec4ce",\n')
    w(f, '  measurementId: "G-CFD7R0C8Y7"\n')
    w(f, '};\n')
    w(f, 'const app = initializeApp(firebaseConfig);\n')
    w(f, 'const db = getFirestore(app);\n')
    w(f, 'window.db = db; window.collection = collection; window.addDoc = addDoc; window.doc = doc; window.updateDoc = updateDoc; window.deleteDoc = deleteDoc;\n')

    # Data globals
    w(f, 'window.queries = []; window.bookings = []; window.gallery = []; window.services = []; window.testimonials = [];\n')
    
    # Listeners
    w(f, 'onSnapshot(collection(db, "queries"), (snap) => { window.queries = snap.docs.map(d=>({id:d.id, ...d.data()})); if(document.getElementById("ap").style.display!=="none") refresh(); });\n')
    w(f, 'onSnapshot(collection(db, "bookings"), (snap) => { window.bookings = snap.docs.map(d=>({id:d.id, ...d.data()})); if(document.getElementById("ap").style.display!=="none") refresh(); });\n')
    w(f, 'onSnapshot(collection(db, "gallery"), (snap) => { window.gallery = snap.docs.map(d=>({id:d.id, ...d.data()})); if(document.getElementById("ap").style.display!=="none") refresh(); });\n')
    w(f, 'onSnapshot(collection(db, "services"), (snap) => { window.services = snap.docs.map(d=>({id:d.id, ...d.data()})); if(document.getElementById("ap").style.display!=="none") refresh(); });\n')
    w(f, 'onSnapshot(collection(db, "testimonials"), (snap) => { window.testimonials = snap.docs.map(d=>({id:d.id, ...d.data()})); if(document.getElementById("ap").style.display!=="none") refresh(); });\n')
    w(f, 'document.getElementById("livend").style.animation = "pu 1.5s infinite";\n')
    w(f, 'document.getElementById("livetxt").textContent = "Live Connected";\n')

    # Expose globals for onclick events (since it's a module script)
    w(f, 'window.cQId=null; window.cBId=null; window.cPhId=null; window.cSvId=null; window.cTId=null; window.cQF="all";\n')
    
    # Cloudinary Config
    w(f, 'const C_NAME = "iqlwz76c"; const C_PRESET = "ml_default";\n')
    
    w(f, 'window.uploadToCloudinary = async function(e) {\n')
    w(f, '  const file = e.target.files[0]; if(!file) return;\n')
    w(f, '  const fd = new FormData(); fd.append("file", file); fd.append("upload_preset", C_PRESET);\n')
    w(f, '  const lbl = document.getElementById("pt-file-lbl");\n')
    w(f, '  lbl.innerHTML = "<span class=\'loader\'></span> Uploading..."; lbl.style.pointerEvents = "none";\n')
    w(f, '  try {\n')
    w(f, '    const res = await fetch(`https://api.cloudinary.com/v1_1/${C_NAME}/image/upload`, { method: "POST", body: fd });\n')
    w(f, '    const data = await res.json();\n')
    w(f, '    document.getElementById("pt-url").value = data.secure_url;\n')
    w(f, '    document.getElementById("pt-previmg").src = data.secure_url;\n')
    w(f, '    document.getElementById("pt-prev").style.display = "block";\n')
    w(f, '    lbl.innerHTML = "&#10003; Upload Complete";\n')
    w(f, '  } catch (err) {\n')
    w(f, '    console.error(err); lbl.innerHTML = "Upload Failed. Try again.";\n')
    w(f, '  } finally { lbl.style.pointerEvents = "auto"; }\n')
    w(f, '};\n')

    # Auth logic
    w(f, 'window.doLogin = function(e){e.preventDefault();const em=document.getElementById("lemail").value.trim(),pw=document.getElementById("lpass").value.trim();if(em==="Sablasingh@0404"&&pw==="sablasingh123"){document.getElementById("ls").style.display="none";document.getElementById("ap").style.display="block";refresh();}else{document.getElementById("lerr").style.display="block";}}\n')
    w(f, 'window.doLogout = function(){document.getElementById("ls").style.display="flex";document.getElementById("ap").style.display="none";}\n')
    w(f, 'window.togglePw = function(){const i=document.getElementById("lpass"),b=i.nextElementSibling;i.type=i.type==="password"?"text":"password";b.textContent=i.type==="password"?"Show":"Hide";}\n')

    # Nav
    w(f, 'const pages=["dashboard","queries","bookings","gallery","services","testimonials","settings"];\n')
    w(f, 'const titles={dashboard:["Dashboard","Overview & Analytics"],queries:["Queries","Client Messages & Enquiries"],bookings:["Bookings","Session Booking Requests"],gallery:["Gallery Manager","Add, Edit & Remove Photos"],services:["Services","Add, Edit & Delete Service Listings"],testimonials:["Testimonials","Add, Edit & Delete Client Reviews"],settings:["Settings","Account & Business Info"]};\n')
    w(f, 'window.sp = function(btn,name){pages.forEach(p=>{const el=document.getElementById("s-"+p);if(el)el.classList.remove("on");const nb=document.getElementById("nb-"+p);if(nb)nb.classList.remove("on");});const el=document.getElementById("s-"+name);if(el)el.classList.add("on");if(btn)btn.classList.add("on");document.getElementById("ptitle").textContent=titles[name][0];document.getElementById("psub").textContent=titles[name][1];if(name==="gallery")window.rga();else if(name==="queries")window.rqs("all");else if(name==="bookings")window.rbs();else if(name==="dashboard")window.rdash();else if(name==="services")window.rsvc();else if(name==="testimonials")window.rtest();}\n')

    # Dashboard render
    w(f, 'window.rdash = function(){const q=window.queries,b=window.bookings,g=window.gallery,nq=q.filter(x=>x.status==="new").length;document.getElementById("sqs").textContent=q.length;document.getElementById("snew").textContent=nq;document.getElementById("sbs").textContent=b.length;document.getElementById("sgl").textContent=g.length;document.getElementById("qbadge").textContent=nq;document.getElementById("bbadge").textContent=b.length;const rl=document.getElementById("rql");rl.innerHTML=q.length===0?"<p style=\'font-size:13px;color:rgba(245,240,232,.3);text-align:center;padding:20px 0\'>No queries yet.</p>":q.slice().sort((x,y)=>new Date(y.date)-new Date(x.date)).slice(0,4).map(x=>`<div style="background:rgba(6,44,32,.65);border-left:3px solid ${x.status==="new"?"#22c55e":"rgba(201,169,110,.35)"};padding:11px 13px;margin-bottom:7px;cursor:pointer" onclick="viewQ(\'${x.id}\')"><div style="display:flex;align-items:center;justify-content:space-between"><p style="font-size:13px;font-weight:500;color:#F5F0E8">${x.name}</p><span class="tg ${x.status==="new"?"tn":"tr"}" style="font-size:9px">${x.status}</span></div><p style="font-size:11px;color:#C9A96E;margin-top:2px">${x.service}</p></div>`).join("");const bl=document.getElementById("rbl");bl.innerHTML=b.length===0?"<p style=\'font-size:13px;color:rgba(245,240,232,.3);text-align:center;padding:20px 0\'>No bookings yet.</p>":b.slice().sort((x,y)=>new Date(y.date)-new Date(x.date)).slice(0,4).map(x=>`<div style="background:rgba(6,44,32,.65);border-left:3px solid rgba(201,169,110,.35);padding:11px 13px;margin-bottom:7px"><p style="font-size:13px;font-weight:500;color:#F5F0E8">${x.name||"Anonymous"}</p><p style="font-size:11px;color:#C9A96E;margin-top:2px">${x.service}</p></div>`).join("");}\n')

    # Queries
    w(f, 'window.rqs = function(f){window.cQF=f;["all","new","read"].forEach(x=>{const b=document.getElementById("qt-"+x);if(!b)return;b.classList.toggle("on",x===f);});const q=window.queries,fl=f==="all"?q:q.filter(x=>x.status===f),c=document.getElementById("qc");c.innerHTML=fl.length===0?`<p style="text-align:center;padding:45px 0;color:rgba(245,240,232,.3)">No ${f==="all"?"":f} queries.</p>`:fl.slice().sort((x,y)=>new Date(y.date)-new Date(x.date)).map(x=>`<div class="card" style="border-left:4px solid ${x.status==="new"?"#22c55e":"rgba(201,169,110,.35)"}"><div style="display:flex;align-items:start;justify-content:space-between"><div style="flex:1"><div style="display:flex;align-items:center;gap:9px;margin-bottom:5px"><p style="font-size:14px;font-weight:500;color:#F5F0E8">${x.name}</p><span class="tg ${x.status==="new"?"tn":"tr"}">${x.status}</span></div><p style="font-size:12px;color:#C9A96E">&#128203; ${x.service}</p><p style="font-size:11px;color:rgba(245,240,232,.5);margin-top:3px">&#128222; ${x.phone||"N/A"} &nbsp;|&nbsp; &#9993; ${x.email||"N/A"}</p>${x.message?`<p style="font-size:11px;color:rgba(245,240,232,.35);margin-top:4px">${x.message.substring(0,65)}...</p>`:""}</div><div style="display:flex;flex-direction:column;gap:5px;margin-left:10px"><button onclick="viewQ(\'${x.id}\')" class="btn-sm bv">&#128065; View</button><button onclick="editQById(\'${x.id}\')" class="btn-sm be">&#9998; Edit</button><button onclick="delQById(\'${x.id}\')" class="btn-sm bd">&#128465; Del</button></div></div></div>`).join("");}\n')
    w(f, 'window.fq = function(f){window.rqs(f);}\n')
    w(f, 'window.viewQ = async function(id){const x=window.queries.find(a=>a.id===id);if(!x)return;window.cQId=id; if(x.status==="new") { await window.updateDoc(window.doc(window.db, "queries", id), {status:"read"}); } document.getElementById("qm-title").textContent="Query Details";document.getElementById("qm-view").style.display="";document.getElementById("qm-form").style.display="none";document.getElementById("qm-btns").style.display="flex";document.getElementById("qm-view").innerHTML=`<div style="display:grid;grid-template-columns:1fr 1fr;gap:11px"><div><p style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(201,169,110,.55);margin-bottom:3px">Name</p><p style="font-size:14px;color:#F5F0E8">${x.name}</p></div><div><p style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(201,169,110,.55);margin-bottom:3px">Phone</p><p style="font-size:14px;color:#F5F0E8">${x.phone||"N/A"}</p></div><div><p style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(201,169,110,.55);margin-bottom:3px">Email</p><p style="font-size:14px;color:#F5F0E8">${x.email||"N/A"}</p></div><div><p style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(201,169,110,.55);margin-bottom:3px">Service</p><p style="font-size:14px;color:#C9A96E">${x.service}</p></div><div style="grid-column:span 2"><p style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(201,169,110,.55);margin-bottom:3px">Message</p><p style="font-size:14px;color:rgba(245,240,232,.75)">${x.message||"—"}</p></div><div style="grid-column:span 2"><p style="font-size:10px;text-transform:uppercase;letter-spacing:.15em;color:rgba(201,169,110,.55);margin-bottom:3px">Submitted</p><p style="font-size:12px;color:rgba(245,240,232,.42)">${new Date(x.date).toLocaleString("en-IN")}</p></div></div>`;const ph=(x.phone||"").replace(/\\D/g,"");document.getElementById("qwa").href=`https://wa.me/${ph||"917004812345"}?text=${encodeURIComponent("Hello "+x.name+"! Thank you for your enquiry about "+x.service+" at S Studio. We will contact you shortly.")}`;document.getElementById("qm").style.display="flex";}\n')
    w(f, 'window.editQById = function(id){const x=window.queries.find(a=>a.id===id);if(!x)return;window.cQId=id;document.getElementById("qm-title").textContent="Edit Query";document.getElementById("qm-view").style.display="none";document.getElementById("qm-form").style.display="block";document.getElementById("qm-btns").style.display="none";document.getElementById("qe-name").value=x.name||"";document.getElementById("qe-phone").value=x.phone||"";document.getElementById("qe-email").value=x.email||"";document.getElementById("qe-service").value=x.service||"";document.getElementById("qe-message").value=x.message||"";document.getElementById("qe-status").value=x.status||"new";document.getElementById("qm-sbtn").textContent="Update Query";document.getElementById("qm").style.display="flex";}\n')
    w(f, 'window.editQ = function(){const id=window.cQId;window.closeQM();window.editQById(id);}\n')
    w(f, 'window.openAddQ = function(){window.cQId=null;document.getElementById("qm-title").textContent="Add New Query";document.getElementById("qm-view").style.display="none";document.getElementById("qm-form").style.display="block";document.getElementById("qm-btns").style.display="none";["qe-name","qe-phone","qe-email","qe-service","qe-message"].forEach(id=>document.getElementById(id).value="");document.getElementById("qe-status").value="new";document.getElementById("qm-sbtn").textContent="Add Query";document.getElementById("qm").style.display="flex";}\n')
    w(f, 'window.saveQ = async function(){const name=document.getElementById("qe-name").value.trim(),svc=document.getElementById("qe-service").value.trim();if(!name||!svc){alert("Name and Service required.");return;}const btn=document.getElementById("qm-sbtn");btn.innerHTML="<span class=\'loader\'></span>"; const data = {name,phone:document.getElementById("qe-phone").value.trim(),email:document.getElementById("qe-email").value.trim(),service:svc,message:document.getElementById("qe-message").value.trim(),status:document.getElementById("qe-status").value}; if(window.cQId){await window.updateDoc(window.doc(window.db,"queries",window.cQId), data);}else{data.date=new Date().toISOString();await window.addDoc(window.collection(window.db,"queries"), data);} window.closeQM();}\n')
    w(f, 'window.delQById = async function(id){if(!confirm("Delete this query?"))return; await window.deleteDoc(window.doc(window.db, "queries", id));}\n')
    w(f, 'window.delQ = function(){if(!window.cQId||!confirm("Delete?"))return;window.delQById(window.cQId);window.closeQM();}\n')
    w(f, 'window.closeQM = function(){document.getElementById("qm").style.display="none";window.cQId=null;document.getElementById("qm-sbtn").textContent="Save";}\n')

    # Bookings
    w(f, 'window.rbs = function(){const b=window.bookings,c=document.getElementById("bc");c.innerHTML=b.length===0?"<p style=\'text-align:center;padding:45px 0;color:rgba(245,240,232,.3)\'>No bookings yet.</p>":b.slice().sort((x,y)=>new Date(y.date)-new Date(x.date)).map((x)=>`<div class="card" style="border-left:4px solid rgba(201,169,110,.35)"><div style="display:flex;align-items:start;justify-content:space-between"><div style="flex:1"><div style="display:flex;align-items:center;gap:9px;margin-bottom:5px"><p style="font-size:14px;font-weight:500;color:#F5F0E8">${x.name||"Anonymous"}</p><span class="tg tp">Pending</span></div><p style="font-size:12px;color:#C9A96E">&#128203; ${x.service}</p><p style="font-size:11px;color:rgba(245,240,232,.5);margin-top:3px">&#128222; ${x.phone||"N/A"}</p>${x.notes?`<p style="font-size:11px;color:rgba(245,240,232,.35);margin-top:4px">${x.notes}</p>`:""}</div><div style="display:flex;flex-direction:column;gap:5px;margin-left:10px"><button onclick="editB(\'${x.id}\')" class="btn-sm be">&#9998; Edit</button><button onclick="delB(\'${x.id}\')" class="btn-sm bd">&#128465; Del</button></div></div></div>`).join("");}\n')
    w(f, 'window.openAddB = function(){window.cBId=null;["be-name","be-phone","be-service","be-notes"].forEach(id=>document.getElementById(id).value="");document.getElementById("bm-title").textContent="Add New Booking";document.getElementById("bm-sbtn").textContent="Add Booking";document.getElementById("bm").style.display="flex";}\n')
    w(f, 'window.editB = function(id){const x=window.bookings.find(a=>a.id===id);if(!x)return;window.cBId=id;document.getElementById("be-name").value=x.name||"";document.getElementById("be-phone").value=x.phone||"";document.getElementById("be-service").value=x.service||"";document.getElementById("be-notes").value=x.notes||"";document.getElementById("bm-title").textContent="Edit Booking";document.getElementById("bm-sbtn").textContent="Update Booking";document.getElementById("bm").style.display="flex";}\n')
    w(f, 'window.saveB = async function(){const name=document.getElementById("be-name").value.trim(),svc=document.getElementById("be-service").value.trim();if(!name||!svc){alert("Name and Service required.");return;}const btn=document.getElementById("bm-sbtn");btn.innerHTML="<span class=\'loader\'></span>"; const data={name,phone:document.getElementById("be-phone").value.trim(),service:svc,notes:document.getElementById("be-notes").value.trim()}; if(window.cBId){await window.updateDoc(window.doc(window.db,"bookings",window.cBId), data);}else{data.date=new Date().toISOString();await window.addDoc(window.collection(window.db,"bookings"), data);} window.closeBM();}\n')
    w(f, 'window.delB = async function(id){if(!confirm("Delete?"))return;await window.deleteDoc(window.doc(window.db,"bookings",id));}\n')
    w(f, 'window.closeBM = function(){document.getElementById("bm").style.display="none";window.cBId=null;document.getElementById("bm-sbtn").textContent="Save";}\n')

    # Gallery
    w(f, 'window.rga = function(){const g=window.gallery,el=document.getElementById("ga");el.innerHTML=g.length===0?"<p style=\'grid-column:span 4;text-align:center;color:rgba(245,240,232,.3)\'>No photos found.</p>":g.map(x=>`<div class="gth"><img src="${x.src}" alt="${x.title}" onerror="this.style.background=\'#0A3D2B\'"/><div class="gover"><p style="font-size:11px;color:#C9A96E;text-align:center;font-weight:500;margin-bottom:4px">${x.title}</p><span class="tg tr" style="font-size:9px">${x.category}</span><div style="display:flex;gap:6px;margin-top:7px"><button onclick="editPhoto(\'${x.id}\')" class="btn-sm be" style="font-size:9px">&#9998; Edit</button><button onclick="delPhoto(\'${x.id}\')" class="btn-sm bd" style="font-size:9px">&#128465; Del</button></div></div></div>`).join("");}\n')
    w(f, 'window.openAddPhoto = function(){window.cPhId=null;document.getElementById("pm-title").textContent="Add New Photo";document.getElementById("pm-sbtn").textContent="Add Photo";document.getElementById("pt-title").value="";document.getElementById("pt-url").value="";document.getElementById("pt-cat").value="bridal";document.getElementById("pt-prev").style.display="none";document.getElementById("pt-file-lbl").innerHTML="&#128193; Click to Upload Photo"; document.getElementById("pm").style.display="flex";}\n')
    w(f, 'window.editPhoto = function(id){const x=window.gallery.find(a=>a.id===id);if(!x)return;window.cPhId=id;document.getElementById("pm-title").textContent="Edit Photo";document.getElementById("pm-sbtn").textContent="Update Photo";document.getElementById("pt-title").value=x.title;document.getElementById("pt-url").value=x.src;document.getElementById("pt-cat").value=x.category;document.getElementById("pt-previmg").src=x.src;document.getElementById("pt-prev").style.display="block";document.getElementById("pt-file-lbl").innerHTML="&#128193; Click to Upload New Photo"; document.getElementById("pm").style.display="flex";}\n')
    w(f, 'window.savePhoto = async function(){const t=document.getElementById("pt-title").value.trim(),s=document.getElementById("pt-url").value.trim(),c=document.getElementById("pt-cat").value;if(!t||!s){alert("Title and image required.");return;}const btn=document.getElementById("pm-sbtn");btn.innerHTML="<span class=\'loader\'></span>"; const data={title:t,src:s,category:c}; if(window.cPhId){await window.updateDoc(window.doc(window.db,"gallery",window.cPhId), data);}else{await window.addDoc(window.collection(window.db,"gallery"), data);} window.closePM();}\n')
    w(f, 'window.delPhoto = async function(id){if(!confirm("Remove this photo?"))return;await window.deleteDoc(window.doc(window.db,"gallery",id));}\n')
    w(f, 'window.closePM = function(){document.getElementById("pm").style.display="none";window.cPhId=null;document.getElementById("pm-sbtn").textContent="Save";}\n')

    # Services
    w(f, 'window.rsvc = function(){const sv=window.services,c=document.getElementById("svc-list");c.innerHTML=sv.length===0?"<p style=\'text-align:center;color:rgba(245,240,232,.3)\'>No services found.</p>":sv.map(x=>`<div class="card"><div style="display:flex;align-items:start;justify-content:space-between"><div style="flex:1"><h3 class="fl" style="font-size:17px;color:#C9A96E;font-weight:300;margin-bottom:7px">${x.name}</h3><ul style="list-style:disc;padding-left:16px;color:rgba(245,240,232,.6);font-size:12px;line-height:1.9">${(x.pts||[]).map(p=>`<li>${p}</li>`).join("")}</ul><p style="font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:rgba(201,169,110,.45);margin-top:7px">${x.tag||""}</p></div><div style="display:flex;flex-direction:column;gap:5px;margin-left:13px"><button onclick="editSvc(\'${x.id}\')" class="btn-sm be">&#9998; Edit</button><button onclick="delSvc(\'${x.id}\')" class="btn-sm bd">&#128465; Delete</button></div></div></div>`).join("");}\n')
    w(f, 'window.openAddSvc = function(){window.cSvId=null;document.getElementById("svcm-title").textContent="Add Service";document.getElementById("svcm-sbtn").textContent="Add Service";["sv-name","sv-tag","sv-pts"].forEach(id=>document.getElementById(id).value="");document.getElementById("svcm").style.display="flex";}\n')
    w(f, 'window.editSvc = function(id){const x=window.services.find(a=>a.id===id);if(!x)return;window.cSvId=id;document.getElementById("svcm-title").textContent="Edit Service";document.getElementById("svcm-sbtn").textContent="Update Service";document.getElementById("sv-name").value=x.name||"";document.getElementById("sv-tag").value=x.tag||"";document.getElementById("sv-pts").value=(x.pts||[]).join("\\n");document.getElementById("svcm").style.display="flex";}\n')
    w(f, 'window.saveSvc = async function(){const name=document.getElementById("sv-name").value.trim(),tag=document.getElementById("sv-tag").value.trim(),pts=document.getElementById("sv-pts").value.split("\\n").map(p=>p.trim()).filter(p=>p);if(!name){alert("Service name required.");return;}const btn=document.getElementById("svcm-sbtn");btn.innerHTML="<span class=\'loader\'></span>"; const data={name,tag,pts}; if(window.cSvId){await window.updateDoc(window.doc(window.db,"services",window.cSvId), data);}else{await window.addDoc(window.collection(window.db,"services"), data);} window.closeSvcM();}\n')
    w(f, 'window.delSvc = async function(id){if(!confirm("Delete this service?"))return;await window.deleteDoc(window.doc(window.db,"services",id));}\n')
    w(f, 'window.closeSvcM = function(){document.getElementById("svcm").style.display="none";window.cSvId=null;document.getElementById("svcm-sbtn").textContent="Save";}\n')

    # Testimonials
    w(f, 'window.rtest = function(){const ts=window.testimonials,c=document.getElementById("test-list");c.innerHTML=ts.length===0?"<p style=\'text-align:center;color:rgba(245,240,232,.3)\'>No testimonials found.</p>":ts.map(x=>`<div class="card"><div style="display:flex;align-items:start;justify-content:space-between"><div style="flex:1"><p class="fl" style="font-size:15px;color:rgba(245,240,232,.8);font-style:italic;margin-bottom:9px">"${x.txt}"</p><p style="font-size:13px;color:#C9A96E;font-weight:500">${x.name}</p><p style="font-size:10px;text-transform:uppercase;letter-spacing:.14em;color:rgba(245,240,232,.3);margin-top:2px">${x.ttl||""}</p></div><div style="display:flex;flex-direction:column;gap:5px;margin-left:13px"><button onclick="editT(\'${x.id}\')" class="btn-sm be">&#9998; Edit</button><button onclick="delT(\'${x.id}\')" class="btn-sm bd">&#128465; Delete</button></div></div></div>`).join("");}\n')
    w(f, 'window.openAddT = function(){window.cTId=null;document.getElementById("tm-title").textContent="Add Testimonial";document.getElementById("tm-sbtn").textContent="Add";["te-name","te-ttl","te-txt"].forEach(id=>document.getElementById(id).value="");document.getElementById("tm").style.display="flex";}\n')
    w(f, 'window.editT = function(id){const x=window.testimonials.find(a=>a.id===id);if(!x)return;window.cTId=id;document.getElementById("tm-title").textContent="Edit Testimonial";document.getElementById("tm-sbtn").textContent="Update";document.getElementById("te-name").value=x.name||"";document.getElementById("te-ttl").value=x.ttl||"";document.getElementById("te-txt").value=x.txt||"";document.getElementById("tm").style.display="flex";}\n')
    w(f, 'window.saveT = async function(){const name=document.getElementById("te-name").value.trim(),txt=document.getElementById("te-txt").value.trim();if(!name||!txt){alert("Name and text required.");return;}const btn=document.getElementById("tm-sbtn");btn.innerHTML="<span class=\'loader\'></span>"; const data={name,ttl:document.getElementById("te-ttl").value.trim(),txt}; if(window.cTId){await window.updateDoc(window.doc(window.db,"testimonials",window.cTId), data);}else{await window.addDoc(window.collection(window.db,"testimonials"), data);} window.closeTM();}\n')
    w(f, 'window.delT = async function(id){if(!confirm("Delete this testimonial?"))return;await window.deleteDoc(window.doc(window.db,"testimonials",id));}\n')
    w(f, 'window.closeTM = function(){document.getElementById("tm").style.display="none";window.cTId=null;document.getElementById("tm-sbtn").textContent="Save";}\n')

    # Export & utils
    w(f, 'window.refresh = function(){window.rdash(); if(window.cQF) window.rqs(window.cQF); window.rbs(); window.rga(); window.rsvc(); window.rtest(); }\n')
    w(f, 'function tick(){const n=new Date();document.getElementById("cdate").textContent=n.toLocaleDateString("en-IN",{weekday:"long",day:"numeric",month:"long"});document.getElementById("ctime").textContent=n.toLocaleTimeString("en-IN",{hour:"2-digit",minute:"2-digit"});}\n')
    w(f, 'setInterval(tick,1000);tick();\n')
    w(f, '</script>\n</body>\n</html>\n')

print(f"admin.html generated with Firebase & Cloudinary! Size: {os.path.getsize('admin.html'):,} bytes")

"""Shared layout, icons and helpers for the PreetoMind Academy site generator."""
import html

# ---------------------------------------------------------------------------
# EDIT THESE once the founder supplies verified details, then run build.py.
# Leave a value empty ("") to show an editable placeholder on the site.
# ---------------------------------------------------------------------------
CONFIG = {
    "whatsapp_number": "917979073971",   # digits with country code, e.g. "919876543210"
    "email": "preetomindacadmy@gmail.com",             # e.g. "admissions@preetomindacademy.in"
    "form_endpoint": "https://formsubmit.co/preetomindacadmy@gmail.com",  # FormSubmit: emails every submission to the founder
    "site_url": "",          # final public URL, e.g. "https://sites.google.com/view/preetomind-academy"
}

ACADEMY = "PreetoMind Academy"
TAGLINE = "LEARN • GROW • EXCEL"
HEADLINE = "Building Strong Foundations, Creating Bright Futures."

PAGES = [
    # (file, nav label, group)
    ("index.html", "Home", None),
    ("about.html", "About PreetoMind Academy", "About"),
    ("founder.html", "About the Founder", "About"),
    ("teaching-methodology.html", "Teaching Methodology", "About"),
    ("courses.html", "Courses", None),
    ("study-materials.html", "Study Materials & Resources", "Learning"),
    ("assessment-and-progress.html", "Assessment & Progress", "Learning"),
    ("testimonials.html", "Testimonials", None),
    ("faq.html", "FAQs", None),
    ("join-our-team.html", "Join Us", None),
    ("contact.html", "Contact", None),
]

ICONS = {
 "book": '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>',
 "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
 "user": '<path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/>',
 "video": '<path d="m22 8-6 4 6 4V8Z"/><rect x="2" y="6" width="14" height="12" rx="2"/>',
 "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><path d="M14 2v6h6"/><path d="M16 13H8"/><path d="M16 17H8"/><path d="M10 9H8"/>',
 "clipboard": '<rect x="8" y="2" width="8" height="4" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><path d="m9 14 2 2 4-4"/>',
 "target": '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
 "chart": '<path d="M3 3v18h18"/><path d="M18 17V9"/><path d="M13 17V5"/><path d="M8 17v-3"/>',
 "help": '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
 "refresh": '<path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"/><path d="M8 16H3v5"/>',
 "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
 "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 5L2 7"/>',
 "phone": '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/>',
 "chat": '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
 "award": '<circle cx="12" cy="8" r="6"/><path d="M15.477 12.89 17 22l-5-3-5 3 1.523-9.11"/>',
 "pen": '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
 "microscope": '<path d="M6 18h8"/><path d="M3 22h18"/><path d="M14 22a7 7 0 1 0 0-14h-1"/><path d="M9 14h2"/><path d="M9 12a2 2 0 0 1-2-2V6h6v4a2 2 0 0 1-2 2Z"/><path d="M12 6V3a1 1 0 0 0-1-1H9a1 1 0 0 0-1 1v3"/>',
 "leaf": '<path d="M11 20A7 7 0 0 1 9.8 6.1C15.5 5 17 4.48 19 2c1 2 2 4.18 2 8 0 5.5-4.78 10-10 10Z"/><path d="M2 21c0-3 1.85-5.36 5.08-6C9.5 14.52 12 13 13 12"/>',
 "dna": '<path d="M2 15c6.667-6 13.333 0 20-6"/><path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993"/><path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993"/><path d="m17 6-2.5-2.5"/><path d="m14 8-1-1"/><path d="m7 18 2.5 2.5"/><path d="m3.5 14.5.5.5"/><path d="m20 9 .5.5"/><path d="m6.5 12.5 1 1"/><path d="m16.5 10.5 1 1"/><path d="m10 16 1.5 1.5"/>',
 "cap": '<path d="M22 10v6"/><path d="M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/>',
 "language": '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
 "check": '<path d="M20 6 9 17l-5-5"/>',
 "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>',
 "bulb": '<path d="M15 14c.2-1 .7-1.7 1.5-2.5 1-.9 1.5-2.2 1.5-3.5A6 6 0 0 0 6 8c0 1 .2 2.2 1.5 3.5.7.7 1.3 1.5 1.5 2.5"/><path d="M9 18h6"/><path d="M10 22h4"/>',
 "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
 "school": '<path d="m4 6 8-4 8 4"/><path d="m18 10 4 2v8a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2v-8l4-2"/><path d="M14 22v-4a2 2 0 0 0-4 0v4"/><path d="M18 5v17"/><path d="M6 5v17"/><circle cx="12" cy="9" r="2"/>',
 "layers": '<path d="m12 2 10 5-10 5L2 7z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
 "trend": '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
 "search": '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
 "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
 "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
 "image": '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/>',
 "quote": '<path d="M3 21c3 0 7-1 7-8V5c0-1.25-.756-2.017-2-2H4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2 1 0 1 0 1 1v1c0 1-1 2-2 2s-1 .008-1 1.031V20c0 1 0 1 1 1z"/><path d="M15 21c3 0 7-1 7-8V5c0-1.25-.757-2.017-2-2h-4c-1.25 0-2 .75-2 1.972V11c0 1.25.75 2 2 2h.75c0 2.25.25 4-2.75 4v3c0 1 0 1 1 1z"/>',
 "caret": '<path d="m6 9 6 6 6-6"/>',
 "edit": '<path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/><path d="M18.5 2.5a2.12 2.12 0 0 1 3 3L12 15l-4 1 1-4Z"/>',
 "info": '<circle cx="12" cy="12" r="10"/><path d="M12 16v-4"/><path d="M12 8h.01"/>',
 "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
 "flask": '<path d="M9 3h6"/><path d="M10 3v6.5L4.5 19a2 2 0 0 0 1.7 3h11.6a2 2 0 0 0 1.7-3L14 9.5V3"/><path d="M7 15h10"/>',
 "home": '<path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><path d="M9 22V12h6v10"/>',
 "send": '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
}

WA_SVG = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.47 14.38c-.3-.15-1.75-.86-2.02-.96-.27-.1-.47-.15-.67.15-.2.3-.77.96-.94 1.16-.17.2-.35.22-.64.07-.3-.15-1.25-.46-2.38-1.47-.88-.79-1.47-1.76-1.65-2.05-.17-.3-.02-.46.13-.6.13-.14.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.2-.24-.58-.49-.5-.67-.5h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.07 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.31 1.26.49 1.7.63.71.22 1.36.19 1.87.12.57-.09 1.75-.72 2-1.41.25-.69.25-1.29.17-1.41-.07-.12-.27-.2-.57-.35zM12.05 21.5h-.01a9.43 9.43 0 0 1-4.8-1.31l-.35-.2-3.57.93.95-3.48-.22-.36a9.42 9.42 0 0 1-1.45-5.03c0-5.2 4.24-9.44 9.46-9.44a9.4 9.4 0 0 1 6.68 2.77 9.38 9.38 0 0 1 2.77 6.68c0 5.21-4.24 9.44-9.46 9.44zm8.05-17.5A11.32 11.32 0 0 0 12.05.66C5.77.66.66 5.77.66 12.04c0 2 .53 3.96 1.52 5.69L.57 23.64l6.05-1.59a11.36 11.36 0 0 0 5.43 1.38h.01c6.27 0 11.38-5.1 11.38-11.38 0-3.04-1.18-5.9-3.34-8.05z"/></svg>')


def icon(name, cls=""):
    c = f' class="{cls}"' if cls else ""
    return (f'<svg{c} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


def ph(text):
    """Inline editable placeholder."""
    return f'<span class="ph" title="Editable placeholder - replace with verified information">[{html.escape(text)}]</span>'


def ph_label(text="Editable - founder to supply"):
    return f'<div class="ph-label">{icon("edit")}{html.escape(text)}</div>'


# ---- contact helpers -------------------------------------------------------
def wa_href(msg="Hello PreetoMind Academy, I would like to know more about admissions."):
    n = CONFIG["whatsapp_number"].strip().replace("+", "").replace(" ", "")
    if not n:
        return "contact.html#whatsapp"
    from urllib.parse import quote
    return f"https://wa.me/{n}?text={quote(msg)}"


def wa_text():
    n = CONFIG["whatsapp_number"].strip().lstrip("+")
    if not n:
        return None
    if n.startswith("91") and len(n) == 12:
        return f"+91 {n[2:7]} {n[7:]}"
    return "+" + n


def mail_href(subject="Admission Enquiry - PreetoMind Academy"):
    e = CONFIG["email"].strip()
    from urllib.parse import quote
    return f"mailto:{e}?subject={quote(subject)}" if e else "contact.html#email"


def form_open(form_id, subject):
    """<form> tag plus the hidden FormSubmit control fields."""
    ep = CONFIG["form_endpoint"].strip()
    action = f'action="{ep}" method="POST" data-endpoint="{ep}"' if ep else 'action="#" method="POST" data-endpoint=""'
    return (f'<form id="{form_id}" class="js-form" {action}>'
            f'<input type="hidden" name="_subject" value="{html.escape(subject)}">'
            '<input type="hidden" name="_template" value="table">'
            '<input type="hidden" name="_captcha" value="false">'
            '<input type="text" name="_honey" style="display:none" tabindex="-1" autocomplete="off">')


def form_status(unconnected_html, success_text):
    ep = CONFIG["form_endpoint"].strip()
    out = f'<div class="notice form-status" data-status="success" role="status">{icon("check")}<p><strong>Submitted successfully.</strong> {success_text}</p></div>'
    out += f'<div class="notice form-status" data-status="error" role="alert">{icon("info")}<p><strong>Could not send right now.</strong> Please try again, or contact us on <a href="{wa_href()}">WhatsApp</a> or by <a href="{mail_href()}">email</a>.</p></div>'
    if not ep:
        out += f'<div class="notice form-status" data-status="unconnected" role="status">{icon("info")}<p>{unconnected_html}</p></div>'
    return out


def contact_value(kind):
    m = {"whatsapp": (wa_text(), "WHATSAPP NUMBER"),
         "email": (CONFIG["email"].strip() or None, "OFFICIAL EMAIL ADDRESS")}
    val, placeholder = m[kind]
    return html.escape(val) if val else ph(placeholder)


# ---- layout ----------------------------------------------------------------
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
         '<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@500;600;700;800&family=Open+Sans:wght@400;600&display=swap" rel="stylesheet">')


def brand_block():
    return (f'<a class="brand" href="index.html" aria-label="{ACADEMY} - Home">'
            f'<img class="brand-logo" src="assets/preetomind-logo.svg" alt="{ACADEMY} logo" width="52" height="52">'
            f'<span class="brand-text"><span class="brand-name">PREETOMIND <span>ACADEMY</span></span>'
            f'<span class="brand-tag">{TAGLINE}</span></span></a>')


def nav(current):
    groups = {}
    items = []
    for f, label, g in PAGES:
        if g:
            if g not in groups:
                groups[g] = []
                items.append(("group", g))
            groups[g].append((f, label))
        else:
            items.append(("link", (f, label)))
    out = ['<nav class="main-nav" id="main-nav" aria-label="Main navigation"><ul>']
    for kind, val in items:
        if kind == "link":
            f, label = val
            cur = ' aria-current="page"' if f == current else ""
            out.append(f'<li><a href="{f}"{cur}>{label}</a></li>')
        else:
            sub = groups[val]
            active = " active" if any(f == current for f, _ in sub) else ""
            out.append(f'<li class="has-dd{active}"><button class="dd-toggle" type="button" aria-expanded="false">{val}{icon("caret","caret")}</button><ul class="dropdown">')
            for f, label in sub:
                cur = ' aria-current="page"' if f == current else ""
                out.append(f'<li><a href="{f}"{cur}>{label}</a></li>')
            out.append('</ul></li>')
    cur = ' aria-current="page"' if current == "admission-enquiry.html" else ""
    out.append(f'<li class="nav-cta"><a class="btn btn-primary btn-sm" href="admission-enquiry.html"{cur}>Admission Enquiry</a></li>')
    out.append('</ul></nav>')
    return "".join(out)


def header(current):
    return f'''<a class="skip-link" href="#main">Skip to main content</a>
<header class="site-header">
  <div class="topbar"><div class="container">
    <span class="tb-hide">Founder-led online academy &middot; Live interactive classes on Google Meet</span>
    <span class="tb-links">
      <a href="{wa_href()}">{icon("chat")}WhatsApp</a>
      <a href="{mail_href()}" class="tb-hide">{icon("mail")}Email</a>
    </span>
  </div></div>
  <div class="container nav-wrap">
    {brand_block()}
    <button class="menu-toggle" type="button" aria-controls="main-nav" aria-expanded="false" aria-label="Open menu">{icon("menu")}</button>
    {nav(current)}
  </div>
</header>'''


def footer():
    depts = [("Foundation Education (Classes 1–8)", "courses.html#foundation"),
             ("Secondary Education (Classes 9–10)", "courses.html#secondary"),
             ("Senior Secondary Biology (11–12)", "courses.html#senior-secondary-biology"),
             ("NEET Biology & CUET UG/PG", "courses.html#competitive-exams"),
             ("Higher Education (B.Sc.)", "courses.html#higher-education"),
             ("English Grammar & Vocabulary", "courses.html#language-development")]
    quick = [("Home", "index.html"), ("About PreetoMind Academy", "about.html"), ("About the Founder", "founder.html"),
             ("Teaching Methodology", "teaching-methodology.html"), ("Study Materials", "study-materials.html"),
             ("Assessment & Progress", "assessment-and-progress.html"), ("Testimonials", "testimonials.html"),
             ("Admission Enquiry", "admission-enquiry.html"), ("FAQs", "faq.html"), ("Join Our Team", "join-our-team.html"), ("Contact Us", "contact.html")]
    return f'''<footer class="site-footer">
  <div class="container footer-grid">
    <div>
      {brand_block()}
      <p class="footer-statement">{HEADLINE}</p>
      <p>A founder-led online educational institution offering concept-based teaching, live interactive classes and personalised academic guidance.</p>
      <p class="mb-0"><strong style="color:#fff">Founder:</strong> Preety Kumari</p>
    </div>
    <div><h4>Quick Links</h4><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for t, h in quick)}</ul></div>
    <div><h4>Academic Departments</h4><ul>{"".join(f'<li><a href="{h}">{t}</a></li>' for t, h in depts)}</ul></div>
    <div><h4>Contact</h4><ul class="footer-contact">
      <li>{icon("chat")}<span>WhatsApp: <a href="{wa_href()}">{contact_value("whatsapp")}</a></span></li>
      <li>{icon("mail")}<span>Email: <a href="{mail_href()}">{contact_value("email")}</a></span></li>
    </ul>
    <p class="small mt-2">For course fees and admission details, please contact PreetoMind Academy directly.</p>
    <a class="btn btn-whatsapp btn-sm" href="{wa_href()}">{WA_SVG}Chat on WhatsApp</a>
    </div>
  </div>
  <div class="container footer-bottom">
    <span>&copy; <span id="year">2026</span> PreetoMind Academy. All rights reserved. &middot; {TAGLINE}</span>
    <span><a href="privacy-policy.html">Privacy Policy</a> &middot; <a href="terms-and-conditions.html">Terms &amp; Conditions</a></span>
  </div>
</footer>
<a class="wa-float" href="{wa_href()}" aria-label="Contact PreetoMind Academy on WhatsApp">{WA_SVG}<span>WhatsApp Us</span></a>'''


def page(current, title, description, body, schema=None):
    canonical = ""
    if CONFIG["site_url"]:
        path = "" if current == "index.html" else current
        canonical = f'<link rel="canonical" href="{CONFIG["site_url"].rstrip("/")}/{path}">'
    sch = f'<script type="application/ld+json">{schema}</script>' if schema else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(description)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">
<meta property="og:image" content="assets/preetomind-logo.svg">
<meta name="theme-color" content="#1E1F22">
{canonical}
<link rel="icon" href="assets/preetomind-logo.svg" type="image/svg+xml">
{FONTS}
<link rel="stylesheet" href="assets/styles.css">
{sch}
</head>
<body>
{header(current)}
<main id="main">
{body}
</main>
{footer()}
<script src="assets/main.js"></script>
</body>
</html>'''


def page_hero(title, intro, crumb=None, eyebrow=None):
    c = f'<div class="breadcrumb"><a href="index.html">Home</a> / {crumb or title}</div>'
    e = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ""
    return f'<section class="page-hero"><div class="container">{c}{e}<h1>{title}</h1><p>{intro}</p></div></section>'


def cta_band(title="Interested in joining PreetoMind Academy?",
             text="Contact us directly for admissions, course details, and further guidance."):
    return f'''<section><div class="container"><div class="cta-band">
  <div><h2>{title}</h2><p>{text}</p></div>
  <div class="btn-row">
    <a class="btn btn-whatsapp" href="{wa_href()}">{WA_SVG}WhatsApp</a>
    <a class="btn btn-primary" href="admission-enquiry.html">Admission Enquiry {icon("arrow")}</a>
  </div>
</div></div></section>'''


def feature(ic, title, text):
    return f'<div class="feature"><div class="ic">{icon(ic)}</div><div><h4>{title}</h4><p>{text}</p></div></div>'


def checklist(items, two=False):
    cls = "checklist two-col" if two else "checklist"
    return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


FOUNDER_PHOTO_SVG = '''<svg viewBox="0 0 400 500" role="img" aria-label="Placeholder for the founder's professional photograph">
<rect width="400" height="500" fill="#F1EDE8"/>
<circle cx="200" cy="190" r="78" fill="#DCD5CC"/>
<path d="M60 500c0-92 63-158 140-158s140 66 140 158z" fill="#DCD5CC"/>
<circle cx="330" cy="70" r="26" fill="none" stroke="#E8731A" stroke-width="4" opacity=".5"/>
<circle cx="70" cy="110" r="10" fill="#E8731A" opacity=".35"/>
</svg>'''


def founder_photo(note=True):
    n = '<div class="ph-note">Add the founder’s professional photograph here (alt text: “Preety Kumari, Founder of PreetoMind Academy”)</div>' if note else ""
    return f'<div class="founder-frame"><div class="founder-photo">{FOUNDER_PHOTO_SVG}{n}</div></div>'


HERO_ART = '''<svg viewBox="0 0 420 300" role="img" aria-label="Illustration of a DNA double helix, a plant cell and an open book representing Biology and Science learning">
<defs><linearGradient id="g1" x1="0" x2="1"><stop offset="0" stop-color="#E8731A"/><stop offset="1" stop-color="#F3A15A"/></linearGradient></defs>
<g fill="none" stroke-linecap="round">
  <path d="M40 30 C 110 80, 110 140, 40 190 S -30 300, 40 350" stroke="url(#g1)" stroke-width="5" transform="translate(30,-40)"/>
  <path d="M120 30 C 50 80, 50 140, 120 190 S 190 300, 120 350" stroke="#fff" stroke-width="5" opacity=".85" transform="translate(-50,-40)"/>
  <g stroke="#8a8d93" stroke-width="3">
    <path d="M58 8 L 102 8"/><path d="M66 38 L 94 38"/><path d="M80 68 L 80 68"/><path d="M66 98 L 94 98"/><path d="M52 128 L 108 128"/><path d="M66 158 L 94 158"/><path d="M66 218 L 94 218"/><path d="M52 248 L 108 248"/><path d="M66 278 L 94 278"/>
  </g>
</g>
<g transform="translate(170,26)">
  <ellipse cx="110" cy="80" rx="105" ry="72" fill="#2A2C30" stroke="#E8731A" stroke-width="3"/>
  <ellipse cx="110" cy="80" rx="86" ry="56" fill="none" stroke="#4a4d53" stroke-width="2" stroke-dasharray="4 6"/>
  <circle cx="118" cy="78" r="22" fill="#E8731A" opacity=".9"/><circle cx="118" cy="78" r="8" fill="#1E1F22"/>
  <ellipse cx="60" cy="58" rx="16" ry="8" fill="#5b5f66"/><ellipse cx="165" cy="105" rx="18" ry="8" fill="#5b5f66"/>
  <ellipse cx="70" cy="110" rx="12" ry="6" fill="#5b5f66"/><circle cx="165" cy="50" r="6" fill="#F3A15A"/>
</g>
<g transform="translate(190,190)">
  <path d="M0 20 Q 55 0 110 20 L 110 100 Q 55 80 0 100 Z" fill="#fff"/>
  <path d="M110 20 Q 165 0 220 20 L 220 100 Q 165 80 110 100 Z" fill="#F1EDE8"/>
  <path d="M110 20 L110 100" stroke="#E8731A" stroke-width="3"/>
  <g stroke="#b9b3ab" stroke-width="3" stroke-linecap="round"><path d="M20 40 L 90 34"/><path d="M20 56 L 90 50"/><path d="M20 72 L 70 68"/><path d="M130 34 L 200 40"/><path d="M130 50 L 200 56"/><path d="M130 66 L 180 70"/></g>
</g>
</svg>'''

DOC_THUMB = '''<svg viewBox="0 0 120 80" aria-hidden="true"><rect x="30" y="6" width="60" height="70" rx="4" fill="#fff" stroke="#d8d2ca" stroke-width="2"/>
<rect x="38" y="16" width="30" height="5" rx="2" fill="#E8731A" opacity=".7"/><g fill="#e3ddd5"><rect x="38" y="28" width="44" height="4" rx="2"/><rect x="38" y="37" width="44" height="4" rx="2"/><rect x="38" y="46" width="34" height="4" rx="2"/><rect x="38" y="55" width="40" height="4" rx="2"/></g></svg>'''

"""Generate the PreetoMind Academy static site into ../site. Run: python3 build.py"""
import os
from pages_a import home, about, founder, courses, methodology
from pages_c import careers
from pages_b import study_materials, assessment, testimonials, admission, contact, faq, privacy, terms

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "site")
BUILDERS = {
    "index.html": home, "about.html": about, "founder.html": founder, "courses.html": courses,
    "teaching-methodology.html": methodology, "study-materials.html": study_materials,
    "assessment-and-progress.html": assessment, "testimonials.html": testimonials,
    "admission-enquiry.html": admission, "contact.html": contact, "faq.html": faq,
    "join-our-team.html": careers, "privacy-policy.html": privacy, "terms-and-conditions.html": terms,
}
for name, fn in BUILDERS.items():
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f:
        f.write(fn())
print(f"Built {len(BUILDERS)} pages into {os.path.normpath(OUT)}")

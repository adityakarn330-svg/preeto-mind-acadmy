from core import *
from pages_a import DEPARTMENTS, SUPPORT, testimonial_slot


# ============================================================== STUDY MATERIALS
def study_materials():
    samples = [
     ("Biology Notes", "Sample Biology Notes", "Concise, well-structured notes with key definitions, labelled diagrams and important points for quick revision.", "e.g. Class 11 – Cell: The Unit of Life"),
     ("Chapter-wise Material", "Chapter-wise Study Material", "Complete chapter coverage organised topic by topic, following the school or university syllabus.", "e.g. Class 10 Science – Life Processes"),
     ("Worksheet", "Practice Worksheet", "Topic-wise worksheets that reinforce understanding through varied question types.", "e.g. Class 7 Science – Nutrition in Plants"),
     ("Practice Questions", "Practice Questions & PYQs", "Exam-oriented practice questions and Previous Year Questions for board and competitive examinations.", "e.g. NEET Biology – Human Physiology"),
     ("Assignment", "Academic Assignment", "Structured assignments that build application skills, written expression and consistency.", "e.g. B.Sc. Zoology – unit assignment"),
     ("English", "Grammar & Vocabulary Sheet", "Grammar rules with examples, vocabulary lists and sentence-formation exercises.", "e.g. Tenses – practice sheet"),
    ]
    cards = "".join(f'''<article class="card resource"><div class="thumb">{DOC_THUMB}</div><span class="tag">{tag}</span><h3>{t}</h3><p>{d}</p>
<div class="ph-block" style="padding:14px;margin-top:auto">{ph_label("Founder to upload sample")}<p class="small mb-0">Title: {ph(ex)}<br>File: {ph("Link to sample PDF / Google Drive preview")}</p></div></article>''' for tag, t, d, ex in samples)
    body = f'''
{page_hero("Study Materials and Learning Resources", "A preview of the academic resources that support every PreetoMind Academy student, prepared with care to show the quality of our teaching.", crumb="Study Materials", eyebrow="Learning Resources")}
<section><div class="container">
  <div class="notice">{icon("lock")}<p>The samples below are shown to demonstrate our teaching quality. <strong>Complete study materials are exclusive to enrolled students</strong> and are shared privately through Google Classroom and designated learning channels.</p></div>
  <div class="grid g-3">{cards}</div>
</div></section>
<section class="section-alt"><div class="container"><div class="split">
  <div><div class="eyebrow">What Enrolled Students Receive</div><h2>Resources That Support Every Stage of Learning</h2>
  <p>Study materials are planned alongside classes. They help students revise what they learned, practise regularly and prepare for examinations.</p></div>
  <div class="card">{checklist(["Chapter-wise notes and study materials", "Worksheets and practice assignments", "Daily Practice Problems (DPPs)", "Previous Year Questions (PYQs)", "Weekly tests and assessments", "Revision material before examinations"])}</div>
</div></div></section>
{cta_band()}
'''
    return page("study-materials.html", "Study Materials | Biology Notes, Worksheets & Practice Questions | PreetoMind Academy",
                "Preview PreetoMind Academy’s learning resources: Biology notes, chapter-wise study materials, worksheets, practice questions and assignments. Full materials are for enrolled students.", body)


# ============================================================== ASSESSMENT
def assessment():
    steps = [
     ("Regular homework and practice", "Students complete homework, worksheets and DPPs to reinforce what they learn in each class."),
     ("Weekly tests and assessments", "Weekly tests check understanding, retention and how well students apply concepts."),
     ("Performance analysis", "Test results and classwork are reviewed to understand each student’s strengths and challenges."),
     ("Monthly progress reports", "A clear monthly summary of performance, effort and areas for improvement."),
     ("Identification of learning gaps", "Specific topics or skills that need attention are identified early."),
     ("Revision and additional academic support", "Targeted revision, extra practice and doubt-solving to close learning gaps."),
     ("Parent communication and progress updates", "Parents are kept informed so they can support their child’s learning at home."),
    ]
    facilities = [
     ("book", "Chapter-wise notes and study materials"), ("file", "Worksheets and practice assignments"), ("edit", "Daily Practice Problems (DPPs)"),
     ("layers", "Previous Year Questions (PYQs)"), ("clipboard", "Weekly tests and assessments"), ("chart", "Monthly performance reports"),
     ("home", "Homework support"), ("help", "Doubt-solving sessions"), ("refresh", "Revision classes"),
     ("target", "Exam preparation"), ("users", "Parent-teacher communication"), ("trend", "Student progress updates"),
    ]
    body = f'''
{page_hero("Student Assessment and Progress System", "A continuous, structured process that tracks progress, identifies learning gaps early and supports steady improvement.", crumb="Assessment & Progress", eyebrow="Academic Monitoring")}
<section><div class="container"><div class="split wide-right">
  <div><div class="eyebrow">Our Approach</div><h2>Continuous Improvement, Not Marks Alone</h2>
    <p>Marks are one measure of learning, but not the only one. Our assessment system looks at understanding, consistency, effort and improvement over time.</p>
    <p>Each assessment is used to guide what happens next, whether that is more practice, revision, a change of approach or extra support. Students and parents always know where things stand and what the next step is.</p>
    <div class="statement mt-3" style="padding:26px">{icon("trend")}<p style="font-size:1.05rem">Every test is a step towards improvement, not just a score.</p></div>
  </div>
  <div class="steps">{"".join(f'<div class="step"><div><h4>{t}</h4><p class="small">{d}</p></div></div>' for t, d in steps)}</div>
</div></div></section>
<section class="section-alt"><div class="container">
  <div class="section-head center"><div class="eyebrow">Student Academic Support System</div><h2>Every Facility Our Students Receive</h2>
  <p class="lead">PreetoMind Academy follows a structured academic support system. Each facility below is part of a planned routine of teaching, practice, assessment and feedback.</p></div>
  <div class="grid g-4">{"".join(f'<div class="feature"><div class="ic">{icon(ic)}</div><div><h4 style="font-size:.95rem">{t}</h4></div></div>' for ic, t in facilities)}</div>
</div></section>
{cta_band()}
'''
    return page("assessment-and-progress.html", "Student Assessment & Progress System | Weekly Tests & Monthly Reports | PreetoMind Academy",
                "How PreetoMind Academy monitors learning: homework, weekly tests, performance analysis, monthly progress reports, learning-gap support and regular parent communication.", body)


# ============================================================== TESTIMONIALS
def testimonials():
    body = f'''
{page_hero("Testimonials", "Genuine feedback from PreetoMind Academy students and parents, shared with their permission.", eyebrow="Student & Parent Feedback")}
<section><div class="container">
  <div class="notice">{icon("shield")}<p>We publish only authentic testimonials received from our students and parents. Names and photographs are shown only with consent. We do not use fictional reviews or ratings.</p></div>
  <div class="grid g-3">{"".join(testimonial_slot() for _ in range(6))}</div>
</div></section>
<section class="section-alt"><div class="container"><div class="split">
  <div><div class="eyebrow">Share Your Experience</div><h2>Are You a PreetoMind Academy Student or Parent?</h2>
  <p>We would value your feedback. Please share your experience with us on WhatsApp or by email. With your permission, we may publish it here using your first name, class or course, and an optional photograph.</p></div>
  <div class="btn-row"><a class="btn btn-whatsapp" href="{wa_href("Hello PreetoMind Academy, I would like to share feedback.")}">{WA_SVG}Share on WhatsApp</a><a class="btn btn-dark" href="{mail_href("Feedback for PreetoMind Academy")}">{icon("mail")}Share by Email</a></div>
</div></div></section>
{cta_band()}
'''
    return page("testimonials.html", "Testimonials | Student & Parent Feedback | PreetoMind Academy",
                "Read genuine feedback from PreetoMind Academy students and parents about our online classes, teaching and academic support.", body)


# ============================================================== ADMISSION
def admission():
    classes = ["Class 1–5 (Foundation)", "Class 6–8 (Foundation)", "Class 9–10 (Secondary)", "Class 11–12 Biology",
               "NEET Biology", "CUET UG", "CUET PG", "B.Sc. Subjects", "English Grammar & Vocabulary", "Other"]
    timings = ["Morning", "Afternoon", "Evening", "Weekend", "Flexible / Discuss"]
    steps = [("Submit an enquiry", "Fill in the form or contact us on WhatsApp or email."),
             ("Discuss academic requirements", "We understand the student’s class, subjects and learning needs."),
             ("Attend a demo class", "Experience our teaching approach before deciding."),
             ("Confirm course fees directly with the founder", "Fee details are shared personally, not published online."),
             ("Complete admission after confirmation", "Admission is finalised only after confirmation by the founder.")]
    body = f'''
{page_hero("Admission Enquiry", "Take the first step towards structured, personalised learning. Share a few details and we will get in touch with you.", eyebrow="Admissions")}
<section><div class="container"><div class="split wide-right" style="align-items:start">
  <div>
    <div class="eyebrow">Admission Process</div><h2>How Admission Works</h2>
    <div class="steps">{"".join(f'<div class="step"><div><h4>{t}</h4><p class="small">{d}</p></div></div>' for t, d in steps)}</div>
    <div class="notice mt-3">{icon("info")}<p><strong>Important:</strong> Submitting an enquiry does not confirm admission. Admission approval and confirmation are made by the founder.</p></div>
    <div class="notice">{icon("info")}<p>For course fees and admission details, please contact PreetoMind Academy directly.</p></div>
  </div>
  <div class="form-card">
    <h2 style="font-size:1.5rem">Admission Enquiry Form</h2>
    <p class="small muted">Fields marked <span class="hl">*</span> are required.</p>
    {form_open("admission-form", "New Admission Enquiry - PreetoMind Academy")}
      <div class="form-grid">
        <div><label for="f-student">Student's Full Name <span class="req">*</span></label><input id="f-student" name="student_name" autocomplete="name" required></div>
        <div><label for="f-parent">Parent / Guardian Name <span class="req">*</span></label><input id="f-parent" name="parent_name" required></div>
        <div><label for="f-class">Student's Class / Course <span class="req">*</span></label><select id="f-class" name="class_course" required><option value="">Select class / course</option>{"".join(f"<option>{c}</option>" for c in classes)}</select></div>
        <div><label for="f-school">School / College Name</label><input id="f-school" name="school_college"></div>
        <div class="full"><label for="f-subjects">Subjects Interested In <span class="req">*</span></label><input id="f-subjects" name="subjects" placeholder="e.g. Biology, Science, English Grammar" required></div>
        <div><label for="f-mobile">Parent's Mobile Number <span class="req">*</span></label><input id="f-mobile" name="parent_mobile" type="tel" inputmode="tel" autocomplete="tel" pattern="[0-9+ ()-]{{8,20}}" placeholder="+91" required></div>
        <div><label for="f-email">Email Address <span class="req">*</span></label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
        <div><label for="f-timing">Preferred Class Timing</label><select id="f-timing" name="preferred_timing"><option value="">Select timing</option>{"".join(f"<option>{t}</option>" for t in timings)}</select></div>
        <div><label for="f-city">Current City <span class="req">*</span></label><input id="f-city" name="city" autocomplete="address-level2" required></div>
        <div class="full"><label for="f-msg">Additional Message / Query</label><textarea id="f-msg" name="message"></textarea></div>
        <div class="full"><label style="display:flex;gap:10px;align-items:flex-start;font-weight:500;font-family:var(--font-body)"><input type="checkbox" required style="width:auto;margin-top:5px"> <span>I agree that PreetoMind Academy may use these details to respond to this enquiry, as described in the <a href="privacy-policy.html">Privacy Policy</a>. <span class="req">*</span></span></label></div>
      </div>
      <button class="btn btn-primary mt-2" type="submit" style="width:100%">{icon("send")}Submit Admission Enquiry</button>
      <p class="form-note">Your enquiry will be sent to PreetoMind Academy. We will contact you to discuss your requirements.</p>
      {form_status(f"<strong>Form not yet connected.</strong> Until it is, please contact us on <a href='{wa_href()}'>WhatsApp</a> or by <a href='{mail_href()}'>email</a>.", "Thank you. Your enquiry has reached PreetoMind Academy and we will contact you soon. Please note that this does not confirm admission.")}
    </form>
  </div>
</div></div></section>
'''
    return page("admission-enquiry.html", "Admission Enquiry | Join PreetoMind Academy Online Classes",
                "Submit an admission enquiry to PreetoMind Academy for online classes in Classes 1–12, Biology, NEET Biology, CUET UG/PG, B.Sc. subjects and English Grammar & Vocabulary.", body)


# ============================================================== CONTACT
def contact():
    cards = [
     ("whatsapp", "wa", "WhatsApp", "The quickest way to reach us for admissions and course information.", wa_href(), "Chat on WhatsApp", "btn-whatsapp"),
     ("email", "", "Email", "Write to us with detailed queries, documents or feedback.", mail_href(), "Send an Email", "btn-primary"),
    ]
    out = []
    for kind, cls, title, desc, href, label, btn in cards:
        ic = WA_SVG if kind == "whatsapp" else icon("phone" if kind == "phone" else "mail")
        bi = WA_SVG if kind == "whatsapp" else icon("phone" if kind == "phone" else "mail")
        out.append(f'''<article class="card contact-card" id="{kind}"><div class="icon-badge {cls}">{ic}</div><h3>{title}</h3><p>{desc}</p>
<div class="value-line">{contact_value(kind)}</div><a class="btn {btn}" href="{href}">{bi}{label}</a></article>''')
    body = f'''
{page_hero("Contact Us", "For admissions, course information, and academic enquiries, please contact PreetoMind Academy directly.", eyebrow="Get in Touch")}
<section><div class="container">
  <div class="grid g-2">{"".join(out)}</div>
  <div class="grid g-2 mt-4">
    <div class="card" style="background:var(--neutral)"><h3>Prefer to Fill a Form?</h3><p>Send us your details through the Admission Enquiry form and we will get back to you.</p><a class="btn btn-outline" href="admission-enquiry.html">Go to Admission Enquiry {icon("arrow")}</a></div>
    <div class="card" style="background:var(--neutral)"><h3>Course Fees</h3><p>For course fees and admission details, please contact PreetoMind Academy directly. Fee details are discussed personally with the founder.</p><a class="btn btn-outline" href="faq.html">Read FAQs {icon("arrow")}</a></div>
  </div>
</div></section>
'''
    return page("contact.html", "Contact PreetoMind Academy | WhatsApp & Email",
                "Contact PreetoMind Academy directly on WhatsApp or by email for admissions, course information and academic enquiries.", body)


# ============================================================== FAQ
FAQS = [
 ("Are classes conducted online?", "Yes. All PreetoMind Academy classes are conducted live online. Students attend interactive classes from home through Google Meet."),
 ("Which classes and subjects are available?", "We offer six academic departments: Foundation Education for Classes 1–8 (all subjects); Secondary Education for Classes 9–10 (all subjects except Mathematics); Senior Secondary Biology for Classes 11–12; Competitive Exam Preparation for NEET Biology, CUET UG and CUET PG; Higher Education support for B.Sc. subjects; and Language Development in English Grammar and English Vocabulary. See the <a href=\"courses.html\">Courses</a> page for details."),
 ("How are live classes conducted?", "Classes are held live on Google Meet. They are interactive: students are encouraged to take part, ask questions and clear doubts during class. Recorded lectures are not part of our programme. Learning happens through live teaching supported by study materials and practice."),
 ("Will students receive notes and worksheets?", "Yes. Enrolled students receive chapter-wise notes, worksheets, practice assignments, Daily Practice Problems (DPPs) and Previous Year Questions (PYQs) where relevant. These are shared privately through Google Classroom and designated learning channels."),
 ("Are weekly tests conducted?", "Yes. Weekly tests and assessments are a regular part of our academic system. They help us check understanding, identify learning gaps and plan revision."),
 ("How can parents track student progress?", "Parents receive monthly performance reports and regular progress updates. We also keep in touch with parents directly, so they always know how their child is doing and where support is needed."),
 ("How can students enrol?", "Submit an <a href=\"admission-enquiry.html\">admission enquiry</a> or contact us directly. We will discuss your academic requirements, arrange a demo class and share course fee details directly. Admission is completed only after confirmation by the founder. Submitting an enquiry does not confirm admission."),
 ("How can parents contact the founder?", "Parents can contact PreetoMind Academy directly by WhatsApp or email. Details are on the <a href=\"contact.html\">Contact Us</a> page."),
 ("How are class routines and planners shared?", "After admission, students receive their academic planner and class routine by email. Google Classroom access is shared through the student’s registered email address, and weekly academic updates are shared through the designated learning channels."),
 ("How can students attend a demo class?", "Contact us through the <a href=\"admission-enquiry.html\">Admission Enquiry</a> form, WhatsApp or email. After we understand the student’s requirements, we will arrange a suitable demo class."),
]


def faq():
    items = "".join(f'<details><summary>{q}</summary><div class="answer"><p>{a}</p></div></details>' for q, a in FAQS)
    import json, re
    schema = json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub(r"<[^>]+>", "", a)}} for q, a in FAQS]}, ensure_ascii=False)
    body = f'''
{page_hero("Frequently Asked Questions", "Answers to common questions about our online classes, study materials, assessments and admission process.", crumb="FAQs", eyebrow="Help")}
<section><div class="container"><div class="faq">{items}</div>
<p class="center mt-3 muted">Still have a question? <a href="contact.html">Contact PreetoMind Academy directly.</a></p></div></section>
{cta_band()}
'''
    return page("faq.html", "FAQs | Online Classes, Tests, Admissions & Demo Classes | PreetoMind Academy",
                "Frequently asked questions about PreetoMind Academy: online live classes, subjects offered, notes and worksheets, weekly tests, progress tracking, enrolment and demo classes.", body, schema)


# ============================================================== POLICIES
def policy_page(file, title, intro, desc, sections, seo_title):
    toc = "".join(f'<li><a href="#s{i+1}">{t}</a></li>' for i, (t, _) in enumerate(sections))
    content = "".join(f'<h2 id="s{i+1}">{i+1}. {t}</h2>{c}' for i, (t, c) in enumerate(sections))
    body = f'''
{page_hero(title, intro)}
<section><div class="container policy-layout">
  <aside class="toc"><h4>Contents</h4><ol>{toc}</ol></aside>
  <div class="prose">
    <p class="small muted">Last updated: {ph("Date of publication")}</p>
    {content}
  </div>
</div></section>
'''
    return page(file, seo_title, desc, body)


def privacy():
    S = [
     ("Introduction", "<p>This Privacy Policy explains how PreetoMind Academy (“we”, “us”) collects, uses and handles personal information shared with us through this website, particularly the Admission Enquiry form, and through our direct communication channels.</p>"),
     ("Information We Collect", "<p>When you submit an admission enquiry, we collect the information you provide:</p><ul><li>Student’s full name</li><li>Parent / guardian name</li><li>Student’s class or course</li><li>School or college name</li><li>Subjects of interest</li><li>Parent’s mobile number</li><li>Email address</li><li>Preferred class timing</li><li>Current city</li><li>Any additional message or query you choose to include</li></ul><p>When you apply to join our team, we collect your name, email address, mobile number, city, education details, the team and role you are applying for, your skills, availability, any link you share and your message.</p><p>We may also receive information you share when you contact us by WhatsApp or email.</p>"),
     ("How Forms Are Delivered", "<p>Our website forms are delivered to the academy’s email address through FormSubmit (formsubmit.co), a third-party form-forwarding service. The details you enter are transmitted to FormSubmit solely so that they can be emailed to us; we do not use the service for any other purpose. Please review FormSubmit’s own privacy policy for details of its processing.</p>"),
     ("Why We Collect This Information", "<p>We collect this information to understand the student’s academic requirements and to respond to your enquiry. It helps us suggest a suitable course, arrange a demo class, and discuss course details and fees with you directly.</p>"),
     ("How We Use Your Information", "<ul><li>To respond to your admission enquiry and academic questions</li><li>To contact you about course details, demo classes and the admission process</li><li>For enrolled students: to share class routines, academic planners, Google Classroom access, study materials, progress reports and academic updates</li><li>To communicate with parents about student progress</li></ul><p>We do not sell your personal information. We do not use it for unrelated marketing.</p>"),
     ("How Information Is Handled and Protected", f"<p>Enquiry information is received by the academy through {ph('name the actual service, e.g. Google Forms / Google Sheets')} and email, and it is accessed only by the founder or people authorised by the academy for academic and administrative purposes. We take reasonable care to keep this information private. However, no online service can be guaranteed to be completely secure.</p><p>Google Classroom and Google Meet are provided by Google. Your use of those services is also subject to Google’s own terms and privacy policy.</p>"),
     ("Information Displayed Publicly", "<p>We do not display students’ or parents’ personal information publicly without appropriate permission. Testimonials, names, photographs or student work are published only with the consent of the student and/or parent, as appropriate.</p>"),
     ("How Long We Keep Information", f"<p>We keep enquiry information only as long as needed to respond to the enquiry and, for enrolled students, for academic and administrative purposes. {ph('Founder to state actual retention period, if any')}</p>"),
     ("Corrections and Deletion", f"<p>Parents or students may ask us to correct their personal information or, where applicable, to delete it. To make a request, contact us at {contact_value('email')} or on WhatsApp. We will respond within a reasonable time.</p>"),
     ("Children’s Information", "<p>Many of our students are minors. Enquiries for students under 18 should be submitted by, or with the knowledge of, a parent or guardian.</p>"),
     ("Changes to This Policy", "<p>We may update this Privacy Policy when our practices change. The updated version will be posted on this page with a revised date.</p>"),
     ("Contact", f"<p>For any questions about this policy, contact PreetoMind Academy at {contact_value('email')} or on WhatsApp at {contact_value('whatsapp')}.</p>"),
    ]
    return policy_page("privacy-policy.html", "Privacy Policy", "How PreetoMind Academy collects, uses and protects information shared through our website and communication channels.",
                       "PreetoMind Academy’s Privacy Policy: what information the admission enquiry form collects, why, how it is used and protected, and how to request correction or deletion.", S,
                       "Privacy Policy | PreetoMind Academy")


def terms():
    S = [
     ("General Website Usage", "<p>By using this website, you agree to these Terms and Conditions. The website gives information about PreetoMind Academy’s courses, teaching methods and admission process. Please use it lawfully and do not misuse its content or features.</p>"),
     ("Course and Academic Information", "<p>We aim to keep course and academic information on this website accurate and up to date. Course content, subjects, schedules and academic arrangements may be updated from time to time. For the latest details, please contact the academy directly.</p>"),
     ("Admission Enquiry and Confirmation", "<p>Submitting an admission enquiry does not confirm admission. The admission process includes discussing academic requirements, attending a demo class, and confirming course fees directly with the founder. Admission is complete only after confirmation by the founder, who may approve or decline admission at her discretion.</p>"),
     ("Course Fees", "<p>Course fees are not published on this website. All fee details are shared and agreed directly with the founder before admission. PreetoMind Academy does not collect payments through this website.</p>"),
     ("Class Schedules and Communication", "<p>Live classes are held on Google Meet. Enrolled students receive their academic planner and class routine by email. Google Classroom access is shared through the student’s registered email address. Students and parents should keep their registered contact details up to date and check them regularly for academic updates.</p>"),
     ("Study Material Usage and Copyright", "<p>All study materials, notes, worksheets, DPPs, assessments and other content provided by PreetoMind Academy are the intellectual property of the academy and are for the personal, non-commercial use of enrolled students only. They must not be copied, shared, sold, uploaded or distributed without written permission. Website content, including text, logo and design, is also protected and may not be reused without permission.</p>"),
     ("Conduct During Online Classes", "<ul><li>Join classes on time using the registered account or link provided</li><li>Behave respectfully towards the teacher and other students</li><li>Do not record, photograph, screenshot or share classes or class materials without permission</li><li>Do not share class links or Google Classroom access with anyone else</li><li>Use chat and microphone features appropriately and only for academic purposes</li></ul><p>PreetoMind Academy may take appropriate action, including removal from a class, if these guidelines are not followed.</p>"),
     ("Changes to Academic Arrangements", "<p>Where necessary, PreetoMind Academy may reschedule classes, adjust timings, or modify course plans or academic arrangements. We will inform students and parents of any such changes through the registered communication channels as early as reasonably possible.</p>"),
     ("Limitation", "<p>We are committed to quality teaching and academic support. However, examination results depend on many factors, including the student’s own effort, so specific marks or outcomes cannot be guaranteed.</p>"),
     ("Changes to These Terms", "<p>We may update these Terms and Conditions from time to time. The latest version will always be available on this page.</p>"),
     ("Contact", f"<p>For questions about these terms, contact PreetoMind Academy at {contact_value('email')} or on WhatsApp at {contact_value('whatsapp')}.</p>"),
    ]
    return policy_page("terms-and-conditions.html", "Terms and Conditions", "Please read these terms about using our website, admissions, classes and study materials.",
                       "PreetoMind Academy’s Terms and Conditions covering website use, course information, admissions, class schedules, study material copyright and online class conduct.", S,
                       "Terms and Conditions | PreetoMind Academy")

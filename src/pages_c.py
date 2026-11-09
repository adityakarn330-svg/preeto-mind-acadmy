from core import *

TECH_ROLES = [
 ("video", "Website & Google Sites Assistant", "Help maintain and update the academy website, add new pages and resources, and keep links, forms and content accurate.",
  ["Basic understanding of websites or Google Sites", "Attention to detail", "Comfortable with Google Workspace (Docs, Drive, Forms)"]),
 ("image", "Design & Visual Content Creator", "Create clean, on-brand graphics for study materials, social media and the website: posters, worksheet layouts, diagrams and simple illustrations.",
  ["Canva, Figma or similar design tools", "Good sense of layout and typography", "Interest in educational and Biology illustrations"]),
 ("chat", "Social Media & Digital Outreach", "Plan and schedule posts, write short educational captions, and help the academy reach students and parents online.",
  ["Clear written English", "Familiarity with Instagram, YouTube or LinkedIn", "Consistency and basic analytics awareness"]),
 ("layers", "Tech & Classroom Support", "Support the smooth running of live classes and Google Classroom: scheduling, resource uploads, attendance sheets and simple automation with Google Sheets or Forms.",
  ["Comfortable with Google Meet and Google Classroom", "Organised and reliable", "Spreadsheet or basic scripting skills are a plus"]),
]
TEACH_ROLES = [
 ("school", "Teaching Assistant – Foundation (Classes 1–8)", "Support live classes, check homework and worksheets, and help younger students with practice and doubts under the founder's guidance.",
  ["Strong school-level fundamentals in Science, English or Social Science", "Patience and clear communication", "Currently pursuing or completed graduation"]),
 ("dna", "Biology Subject Mentor (Classes 9–12)", "Assist with doubt-solving sessions, prepare practice questions and PYQ sets, and support revision for board and NEET Biology aspirants.",
  ["B.Sc. / M.Sc. student in Zoology, Botany, Life Sciences or related field", "Sound NCERT Biology knowledge", "Ability to explain diagrams and concepts clearly"]),
 ("file", "Academic Content Creator", "Draft chapter-wise notes, worksheets, Daily Practice Problems and assessments following the academy's format and quality standards.",
  ["Strong subject knowledge in the chosen area", "Clear, accurate written English", "Comfortable with Google Docs and basic formatting"]),
 ("language", "English Grammar & Vocabulary Tutor", "Conduct practice sessions, check written work and build vocabulary exercises for learners in the Language Development programme.",
  ["Excellent English grammar and vocabulary", "Experience teaching, tutoring or peer mentoring", "Encouraging, learner-friendly approach"]),
]


def role_card(ic, title, desc, reqs):
    return (f'<article class="card"><div class="icon-badge">{icon(ic)}</div><h3>{title}</h3><p>{desc}</p>'
            f'<h4 class="small" style="margin-top:14px">What we look for</h4>{checklist(reqs)}</article>')


def careers():
    unconn = (f"<strong>Form not yet connected.</strong> Until it is, please apply by <a href='{mail_href('Application - PreetoMind Academy Team')}'>email</a> "
              f"or <a href='{wa_href('Hello PreetoMind Academy, I would like to apply to join your team.')}'>WhatsApp</a>.")
    teams = ["Tech Team", "Teaching Team", "Open to either"]
    roles = [r[1] for r in TECH_ROLES] + [r[1] for r in TEACH_ROLES] + ["Other / General application"]
    avail = ["Weekday mornings", "Weekday evenings", "Weekends", "Flexible"]
    steps = [("Apply online", "Fill in the application form below or email your CV."),
             ("Shortlisting", "We review applications and contact shortlisted candidates."),
             ("Interaction / task", "A short conversation with the founder, plus a demo session or sample task depending on the role."),
             ("Onboarding", "Selected candidates receive role details, expectations and an orientation.")]
    body = f'''
{page_hero("Join Our Team", "PreetoMind Academy invites motivated students to join our Tech Team and Teaching Team. Learn by doing, contribute to real education work, and grow with a founder-led academy.", crumb="Join Our Team", eyebrow="We're Hiring")}
<section><div class="container"><div class="split wide-left">
  <div><div class="eyebrow">Student Opportunities</div><h2>Work With Us While You Study</h2>
    <p>We are building a small, committed team of students who care about education. Whether you are good with technology and design or you love teaching and your subject, there is a place for you to contribute and learn.</p>
    <p>Roles are designed around student schedules, with clear tasks and direct mentoring from the founder. You will gain practical experience, build a portfolio and make a real difference to young learners.</p>
    <div class="pill-row"><span class="pill">Flexible, remote roles</span><span class="pill">Mentoring by the founder</span><span class="pill">Certificate of experience</span><span class="pill">Portfolio-worthy work</span></div>
  </div>
  <div class="card" style="background:var(--neutral)"><h3>Role Details</h3>
    <p class="small">Engagement type: {ph("Internship / part-time / volunteer")}<br>Duration: {ph("e.g. 3–6 months")}<br>Stipend or honorarium: {ph("Founder to confirm")}<br>Weekly commitment: {ph("e.g. 6–10 hours")}<br>Location: Remote (online)</p>
    <p class="small muted mb-0">Exact terms are confirmed directly with the founder before onboarding.</p></div>
</div></div></section>

<section class="section-alt" id="tech-team"><div class="container">
  <div class="section-head"><div class="eyebrow">Tech Team</div><h2>Technology, Design &amp; Digital Roles</h2>
  <p class="lead">For students who enjoy building, designing and organising things online.</p></div>
  <div class="grid g-2">{"".join(role_card(*r) for r in TECH_ROLES)}</div>
</div></section>

<section id="teaching-team"><div class="container">
  <div class="section-head"><div class="eyebrow">Teaching Team</div><h2>Teaching, Mentoring &amp; Content Roles</h2>
  <p class="lead">For students with strong subject knowledge who want to help others learn.</p></div>
  <div class="grid g-2">{"".join(role_card(*r) for r in TEACH_ROLES)}</div>
</div></section>

<section class="section-dark"><div class="container">
  <div class="section-head center"><div class="eyebrow">Selection Process</div><h2>How to Apply</h2></div>
  <div class="steps h" style="grid-template-columns:repeat(4,1fr)">{"".join(f'<div class="step"><div><h4>{t}</h4><p class="small">{d}</p></div></div>' for t, d in steps)}</div>
</div></section>

<section id="apply"><div class="container"><div class="split wide-right" style="align-items:start">
  <div><div class="eyebrow">Application</div><h2>Apply Now</h2>
    <p>Fill in the form and tell us which team and role interest you. If you have a CV, portfolio, GitHub or sample lesson, add a link; it helps us understand your work.</p>
    <p>You can also apply by email at <a href="{mail_href("Application - PreetoMind Academy Team")}">{contact_value("email")}</a> with the subject "Application – Tech Team" or "Application – Teaching Team".</p>
    <div class="notice">{icon("info")}<p>Applying does not guarantee selection. Shortlisted candidates will be contacted by the founder. We respect your privacy and use your details only for recruitment, as described in our <a href="privacy-policy.html">Privacy Policy</a>.</p></div>
  </div>
  <div class="form-card">
    <h2 style="font-size:1.5rem">Team Application Form</h2>
    <p class="small muted">Fields marked <span class="hl">*</span> are required.</p>
    {form_open("team-form", "New Team Application - PreetoMind Academy")}
      <div class="form-grid">
        <div><label for="c-name">Full Name <span class="req">*</span></label><input id="c-name" name="full_name" autocomplete="name" required></div>
        <div><label for="c-email">Email Address <span class="req">*</span></label><input id="c-email" name="email" type="email" autocomplete="email" required></div>
        <div><label for="c-phone">Mobile / WhatsApp Number <span class="req">*</span></label><input id="c-phone" name="phone" type="tel" inputmode="tel" pattern="[0-9+ ()-]{{8,20}}" placeholder="+91" required></div>
        <div><label for="c-city">Current City <span class="req">*</span></label><input id="c-city" name="city" required></div>
        <div class="full"><label for="c-college">College / University, Course and Year <span class="req">*</span></label><input id="c-college" name="education" placeholder="e.g. B.Sc. Zoology, 2nd year, XYZ College" required></div>
        <div><label for="c-team">Team Applying For <span class="req">*</span></label><select id="c-team" name="team" required><option value="">Select team</option>{"".join(f"<option>{t}</option>" for t in teams)}</select></div>
        <div><label for="c-role">Preferred Role <span class="req">*</span></label><select id="c-role" name="role" required><option value="">Select role</option>{"".join(f"<option>{r}</option>" for r in roles)}</select></div>
        <div class="full"><label for="c-skills">Relevant Skills / Subjects <span class="req">*</span></label><input id="c-skills" name="skills" placeholder="e.g. Biology, Canva, Google Sites, English Grammar" required></div>
        <div><label for="c-avail">Availability</label><select id="c-avail" name="availability"><option value="">Select availability</option>{"".join(f"<option>{a}</option>" for a in avail)}</select></div>
        <div><label for="c-link">CV / Portfolio / LinkedIn Link</label><input id="c-link" name="link" type="url" placeholder="https://"></div>
        <div class="full"><label for="c-msg">Why do you want to join PreetoMind Academy? <span class="req">*</span></label><textarea id="c-msg" name="message" required></textarea></div>
        <div class="full"><label style="display:flex;gap:10px;align-items:flex-start;font-weight:500;font-family:var(--font-body)"><input type="checkbox" required style="width:auto;margin-top:5px"> <span>I agree that PreetoMind Academy may use these details for recruitment purposes, as described in the <a href="privacy-policy.html">Privacy Policy</a>. <span class="req">*</span></span></label></div>
      </div>
      <button class="btn btn-primary mt-2" type="submit" style="width:100%">{icon("send")}Submit Application</button>
      {form_status(unconn, "Thank you for applying. Your application has reached PreetoMind Academy; shortlisted candidates will be contacted by email or WhatsApp.")}
    </form>
  </div>
</div></div></section>
'''
    return page("join-our-team.html", "Join Our Team | Student Tech & Teaching Roles | PreetoMind Academy",
                "PreetoMind Academy is hiring students for its Tech Team (website, design, social media, classroom support) and Teaching Team (teaching assistants, Biology mentors, content creators, English tutors). Apply online.", body)


def home_hiring_section():
    return f'''
<section><div class="container"><div class="split wide-left">
  <div><div class="eyebrow">We're Hiring</div><h2>Students: Join the PreetoMind Academy Team</h2>
    <p class="lead">Are you a student who loves technology, design or teaching? Work with us on real projects, learn directly from the founder and build experience that matters.</p>
    <div class="btn-row"><a class="btn btn-primary" href="join-our-team.html#tech-team">Tech Team Roles {icon("arrow")}</a><a class="btn btn-outline" href="join-our-team.html#teaching-team">Teaching Team Roles {icon("arrow")}</a></div>
  </div>
  <div class="grid">
    {feature("video","Tech Team","Website and Google Sites support, design and visual content, social media, classroom tech support.")}
    {feature("cap","Teaching Team","Teaching assistants, Biology subject mentors, academic content creators, English Grammar tutors.")}
    {feature("award","What you gain","Flexible remote roles, mentoring from the founder, a certificate of experience and portfolio-worthy work.")}
  </div>
</div></div></section>'''

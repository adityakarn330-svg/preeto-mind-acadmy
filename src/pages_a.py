from core import *
from pages_c import home_hiring_section

DEPARTMENTS = [
 dict(id="foundation", icon="school", name="Foundation Education", level="Classes 1–8",
      subjects="All subjects",
      summary="Strong fundamentals and concept clarity across all school subjects, supported by regular practice, homework support and chapter-wise preparation.",
      intro="The early school years shape how a child learns for life. Our Foundation Education programme helps young learners understand every chapter clearly, build good study habits and approach school with confidence.",
      focus=["Strong fundamentals", "Concept clarity", "Regular practice", "Homework support", "Worksheets", "Chapter-wise preparation"]),
 dict(id="secondary", icon="book", name="Secondary Education", level="Classes 9–10",
      subjects="All subjects except Mathematics",
      summary="Complete school syllabus coverage with conceptual learning, chapter-wise notes, regular tests and focused board-examination preparation.",
      intro="Classes 9 and 10 build the base for board examinations and future subject choices. Students receive structured, chapter-wise teaching across all subjects except Mathematics, with regular testing and revision.",
      focus=["School syllabus coverage", "Conceptual learning", "Chapter-wise notes", "Examination preparation", "Regular tests", "Revision"]),
 dict(id="senior-secondary-biology", icon="dna", name="Senior Secondary Biology", level="Classes 11–12",
      subjects="Biology",
      summary="NCERT-based conceptual Biology with detailed explanations, diagrams, important concepts, practice questions and board-exam preparation.",
      intro="Senior Secondary Biology needs both depth and precision. Lessons follow the NCERT framework, explaining each concept in detail with labelled diagrams, so students can write accurate board answers and build a base for competitive examinations.",
      focus=["NCERT-based conceptual understanding", "Detailed Biology explanations", "Diagrams and important concepts", "Practice questions", "Board examination preparation"]),
 dict(id="competitive-exams", icon="target", name="Competitive Exam Preparation", level="NEET Biology · CUET UG/PG",
      subjects="NEET Biology, CUET UG, CUET PG",
      summary="Concept-first preparation for NEET Biology and CUET UG/PG with practice questions, Previous Year Questions, revision and assessment.",
      intro="Competitive examinations reward strong concepts and consistent practice. Preparation combines concept building with practice questions, Previous Year Questions (PYQs), regular revision and assessment so students learn to apply what they know under exam conditions.",
      focus=["Conceptual preparation", "Practice questions", "Previous Year Questions (PYQs)", "Examination-oriented learning", "Revision and assessment"]),
 dict(id="higher-education", icon="cap", name="Higher Education", level="B.Sc. Subjects",
      subjects="B.Sc. subjects",
      summary="Subject-oriented academic support for B.Sc. students with detailed notes, conceptual explanations and university-exam preparation.",
      intro="Undergraduate study demands independent understanding of detailed subject matter. We help B.Sc. students master their syllabus through clear conceptual explanations, detailed notes and structured preparation for university examinations.",
      focus=["Subject-oriented academic learning", "Detailed notes", "Conceptual explanations", "University examination preparation", "Practice and revision"]),
 dict(id="language-development", icon="language", name="Language Development", level="English Grammar & Vocabulary",
      subjects="English Grammar, English Vocabulary",
      summary="Build grammar fundamentals, a richer vocabulary, correct sentence formation, better writing skills and confidence in English.",
      intro="Good English supports learning in every subject. This programme strengthens grammar fundamentals and vocabulary step by step, helping learners form correct sentences, write clearly and use English with confidence.",
      focus=["Grammar fundamentals", "Vocabulary development", "Sentence formation", "Writing skills", "Language confidence"]),
]

WHY = [
 ("bulb", "Concept-based teaching", "Every topic is taught from the basics, so students understand the reasons as well as the facts."),
 ("video", "Live interactive online classes", "Real-time classes on Google Meet where students take part and ask questions freely."),
 ("user", "Personalised student attention", "Guidance and practice adapted to each learner’s needs and pace."),
 ("book", "Chapter-wise study materials", "Well-organised notes for every chapter to support learning and revision."),
 ("file", "Worksheets and assignments", "Structured practice that reinforces each concept after it is taught."),
 ("edit", "Daily Practice Problems", "Short, regular DPPs that build consistency and accuracy."),
 ("clipboard", "Weekly assessments", "Regular tests that show students where they stand."),
 ("help", "Regular doubt-solving", "Dedicated time to clear doubts before they become learning gaps."),
 ("chart", "Academic progress monitoring", "Continuous tracking of each student’s performance and improvement."),
 ("target", "Exam-oriented preparation", "Focused preparation for school, board, university and competitive examinations."),
]

SUPPORT = [
 ("video", "Live online teaching", "Interactive classes conducted on Google Meet."),
 ("book", "Study materials", "Chapter-wise notes shared through designated learning channels."),
 ("file", "Worksheets", "Topic-wise practice after every lesson."),
 ("edit", "DPPs", "Daily Practice Problems for steady, consistent practice."),
 ("layers", "PYQs", "Previous Year Questions for exam familiarity."),
 ("clipboard", "Weekly tests", "Regular assessment of learning and retention."),
 ("refresh", "Revision classes", "Planned revision before tests and examinations."),
 ("help", "Doubt-solving sessions", "Focused time to clarify questions and difficult topics."),
 ("chart", "Monthly performance reports", "A clear summary of progress, strengths and areas to improve."),
 ("users", "Parent communication", "Regular updates so parents stay informed and involved."),
]


def dept_card(i, d, link=True):
    more = f'<a class="more" href="courses.html#{d["id"]}">View department {icon("arrow")}</a>' if link else ""
    return (f'<article class="card dept-card"><span class="dept-num" aria-hidden="true">0{i}</span>'
            f'<div class="icon-badge">{icon(d["icon"])}</div><div class="meta">{d["level"]}</div>'
            f'<h3>{d["name"]}</h3><p>{d["summary"]}</p>{more}</article>')


# ============================================================== HOME
def home():
    schema = ('{"@context":"https://schema.org","@type":"EducationalOrganization","name":"PreetoMind Academy",'
              '"slogan":"Learn • Grow • Excel","description":"A founder-led online educational institution offering live '
              'interactive classes, concept-based teaching and personalised academic guidance.",'
              '"founder":{"@type":"Person","name":"Preety Kumari"}}')
    body = f'''
<section class="hero"><div class="container">
  <div>
    <div class="hero-brand">PREETOMIND ACADEMY</div>
    <h1>Building Strong Foundations, <em>Creating Bright Futures.</em></h1>
    <div class="tagline">{TAGLINE}</div>
    <p class="intro">PreetoMind Academy is a founder-led online educational institution committed to providing quality education, building strong academic foundations, and developing confident learners through concept-based teaching, interactive live classes, and personalised academic guidance.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="courses.html">Explore Our Courses {icon("arrow")}</a>
      <a class="btn btn-outline-light" href="contact.html">Contact Us Directly for Admissions</a>
    </div>
  </div>
  <div class="hero-art"><div class="art-card">{HERO_ART}
    <div class="hero-stats">
      <div class="hero-stat"><strong>6</strong><span>Academic departments</span></div>
      <div class="hero-stat"><strong>Live</strong><span>Classes on Google Meet</span></div>
      <div class="hero-stat"><strong>Weekly</strong><span>Tests &amp; assessments</span></div>
    </div>
  </div></div>
</div></section>

<section><div class="container">
  <div class="section-head center"><div class="eyebrow">Academic Departments</div>
    <h2>Six Departments, One Commitment to Quality Education</h2>
    <p class="lead">From the first school years to university and competitive examinations, every department follows the same structured, concept-based approach.</p></div>
  <div class="grid g-3">{"".join(dept_card(i+1, d) for i, d in enumerate(DEPARTMENTS))}</div>
</div></section>

<section class="section-alt"><div class="container">
  <div class="split wide-right">
    <div><div class="eyebrow">Why Choose PreetoMind Academy?</div>
      <h2>Structured Teaching. Personal Guidance. Steady Progress.</h2>
      <p class="lead">Students do not just attend classes at PreetoMind Academy. They learn within a complete academic system that covers clear teaching, regular practice, assessment and feedback.</p>
      <a class="btn btn-dark mt-2" href="teaching-methodology.html">Our Teaching Methodology {icon("arrow")}</a>
    </div>
    <div class="grid g-2">{"".join(feature(*w) for w in WHY)}</div>
  </div>
</div></section>

<section><div class="container">
  <div class="split wide-right">
    {founder_photo()}
    <div>
      <div class="eyebrow">Meet the Founder</div>
      <h2 class="founder-name">Preety Kumari</h2>
      <div class="founder-role">Founder – PreetoMind Academy | Educator | Creative Writer</div>
      <div class="pill-row"><span class="pill">B.Sc. Zoology with Research</span><span class="pill">Biology &amp; Science</span><span class="pill">English Grammar &amp; Vocabulary</span><span class="pill">Literary Award Recipient</span></div>
      <p>Preety Kumari founded PreetoMind Academy to give students what she believes every learner deserves: clear concepts, consistent practice and personal academic attention. With a B.Sc. in Zoology with Research, she brings a strong scientific foundation to her teaching of Biology and Science.</p>
      <p>Alongside her experience in online tutoring, she teaches English Grammar and Vocabulary and creates educational content for her students. She is also a creative writer and a recipient of literary recognition. This mix of scientific discipline and creative expression shapes how she teaches: precise and thorough, but also engaging and encouraging.</p>
      <p class="small muted">Professional certifications and literary achievements: {ph("Founder to add verified certification and award names")}</p>
      <a class="btn btn-outline" href="founder.html">About the Founder {icon("arrow")}</a>
    </div>
  </div>
</div></section>

<section class="section-dark"><div class="container">
  <div class="section-head center"><div class="eyebrow">Learning Support</div>
    <h2>How Every Student Is Supported</h2>
    <p class="lead">A structured academic support system that keeps learning on track from the first class to the final examination.</p></div>
  <div class="grid g-3" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{"".join(feature(*s) for s in SUPPORT)}</div>
</div></section>

<section class="section-alt"><div class="container">
  <div class="section-head center"><div class="eyebrow">Testimonials</div>
    <h2>What Students and Parents Say</h2>
    <p class="lead">We publish only genuine feedback from our students and parents, with their permission.</p></div>
  <div class="grid g-3">
    {"".join(testimonial_slot() for _ in range(3))}
  </div>
  <p class="center mt-3"><a class="btn btn-outline" href="testimonials.html">View All Testimonials {icon("arrow")}</a></p>
</div></section>
{home_hiring_section()}

{cta_band()}
'''
    return page("index.html", "PreetoMind Academy | Online Classes, Biology, NEET & CUET Preparation",
                "PreetoMind Academy is a founder-led online academy offering live interactive classes for Classes 1–12, Biology, NEET Biology, CUET UG/PG, B.Sc. subjects and English Grammar & Vocabulary.",
                body, schema)


def testimonial_slot():
    return f'''<article class="card testimonial ph-block">
  {ph_label("Testimonial slot - genuine feedback only")}
  {icon("quote","q")}
  <p>{ph("Student or parent feedback, published with permission")}</p>
  <div class="who"><div class="avatar">{icon("user")}</div>
    <div><strong>{ph("First name")}</strong><br><span class="small">{ph("Class / Course")} &middot; {ph("Student / Parent")}</span></div></div>
</article>'''


# ============================================================== ABOUT
VALUES = [
 ("Quality Education", "Careful, well-prepared teaching in every class and every department."),
 ("Conceptual Understanding", "Understanding the reasons behind ideas, not memorising without meaning."),
 ("Discipline and Consistency", "Regular classes, practice and assessment that build steady progress."),
 ("Individual Student Attention", "Recognising each learner’s strengths, pace and needs."),
 ("Academic Excellence", "High standards and encouragement to reach full potential."),
 ("Creativity and Critical Thinking", "Encouraging curiosity, questioning and original thought."),
 ("Confidence and Lifelong Learning", "Helping students become confident, independent learners."),
 ("Integrity and Responsibility", "Honesty, respect and responsibility in all academic work."),
]


def about():
    body = f'''
{page_hero("About PreetoMind Academy", "A founder-led online educational institution built on quality teaching, strong conceptual foundations and personalised academic guidance.", eyebrow="Who We Are")}
<section><div class="container"><div class="split wide-left">
  <div>
    <div class="eyebrow">Our Institution</div>
    <h2>Quality Education, Delivered Personally</h2>
    <p>PreetoMind Academy is a founder-led online educational institution that supports learners at every stage, including school education, Senior Secondary Biology, competitive examinations, higher education and language development.</p>
    <p>The academy was built on a simple belief: students achieve more when they truly understand what they learn. Every class is planned to build strong conceptual foundations, followed by consistent academic practice, regular assessment and clear feedback.</p>
    <p>Because the academy is founder-led, teaching stays student-centred. Each learner is known individually, their progress is followed closely, and their guidance is adapted to their needs. Parents stay informed through regular communication and progress updates.</p>
    <p>The goal is not only better marks, but lasting academic confidence: students who can think clearly, express themselves well and prepare for examinations with assurance.</p>
  </div>
  <div class="card" style="background:var(--neutral)">
    <h3>What We Emphasise</h3>
    {checklist(["Quality education", "Strong conceptual foundations", "Student-centred teaching", "Consistent academic practice", "Personalised guidance", "Academic confidence", "Examination preparation"])}
  </div>
</div></div></section>

<section class="section-alt"><div class="container"><div class="grid g-2">
  <div class="card" style="border-top:4px solid var(--orange)"><div class="icon-badge dark">{icon("target")}</div>
    <div class="eyebrow">Our Vision</div>
    <p style="font-family:var(--font-head);font-size:1.15rem;font-weight:600;color:var(--charcoal);line-height:1.55">“To provide quality and accessible education, build strong academic foundations and conceptual understanding, and prepare learners for school examinations and competitive examinations.”</p></div>
  <div class="card" style="border-top:4px solid var(--charcoal)"><div class="icon-badge">{icon("trend")}</div>
    <div class="eyebrow">Our Mission</div>
    <p style="font-family:var(--font-head);font-size:1.15rem;font-weight:600;color:var(--charcoal);line-height:1.55">To create a structured and supportive online learning environment where students receive clear explanations, regular academic practice, personalised guidance, and opportunities to improve their knowledge and confidence.</p></div>
</div></div></section>

<section><div class="container">
  <div class="section-head center"><div class="eyebrow">Educational Values</div><h2>The Eight Values That Guide Us</h2>
  <p class="lead">These values shape how we teach, how we support students and how we work with parents.</p></div>
  <div class="grid g-4">{"".join(f'<div class="card value"><span class="num">0{i+1}</span><div><h4>{t}</h4><p class="small mb-0">{d}</p></div></div>' for i, (t, d) in enumerate(VALUES))}</div>
</div></section>

<section class="section-alt"><div class="container">
  <div class="section-head center"><div class="eyebrow">Who We Support</div><h2>Learners Across Six Academic Departments</h2></div>
  <div class="grid g-3">{"".join(dept_card(i+1, d) for i, d in enumerate(DEPARTMENTS))}</div>
</div></section>
{cta_band()}
'''
    return page("about.html", "About PreetoMind Academy | Founder-Led Online Education",
                "Learn about PreetoMind Academy, a founder-led online educational institution: our vision, mission and eight educational values for quality, concept-based learning.", body)


# ============================================================== FOUNDER
def founder():
    sections = [
     ("cap", "Educational Qualifications", f'''<p>Preety Kumari holds a <strong>B.Sc. in Zoology with Research</strong>. Her undergraduate training in Zoology, including its research component, gives her a thorough understanding of biological concepts and a scientific approach to explaining them.</p>
       <p class="small">{ph("Institution / university name and year of completion")} &middot; {ph("Research project title or area, if to be shown")}</p>'''),
     ("video", "Teaching Experience and Online Tutoring", f'''<p>She has experience in online tutoring, teaching students in live sessions and adapting explanations to each learner’s level. That experience is the basis of PreetoMind Academy’s live, interactive and personalised teaching model.</p>
       <p class="small">{ph("Teaching experience duration")} &middot; {ph("Classes / levels taught")} &middot; {ph("Any verified tutoring roles or platforms")}</p>'''),
     ("microscope", "Subject Expertise – Biology and Science", f'''<p>Biology and Science are her core subjects. She teaches them with an emphasis on concept clarity, accurate terminology, well-labelled diagrams and a real understanding of life processes, from cell structure to human physiology, genetics and ecology.</p>'''),
     ("language", "English Grammar and Vocabulary Teaching", f'''<p>Alongside the sciences, she teaches English Grammar and Vocabulary. She helps learners master grammar rules, expand their vocabulary, form correct sentences and write with clarity and confidence.</p>'''),
     ("award", "Professional Certifications and Achievements", f'''<p>Her verified professional certifications and achievements are listed below.</p>
       <ul class="checklist"><li>{ph("Certification name – issuing organisation – year")}</li><li>{ph("Certification name – issuing organisation – year")}</li><li>{ph("Achievement – details to be verified")}</li></ul>'''),
     ("file", "Academic Content Creation and Educational Work", f'''<p>She creates educational content for her students, including chapter-wise notes, worksheets, Daily Practice Problems and assessments, so each student has well-structured material that supports classroom learning.</p>
       <p class="small">{ph("Any other verified educational work, publications or platforms")}</p>'''),
     ("pen", "Literary Journey – Creative Writing and Literary Awards", f'''<p>Preety Kumari is also a creative writer and a literary award recipient. Her writing reflects the same qualities she brings to the classroom: careful thought, clear expression and a love of language.</p>
       <ul class="checklist"><li>{ph("Award name – awarding body – year")}</li><li>{ph("Published work / anthology / platform, if applicable")}</li></ul>'''),
     ("bulb", "Teaching Philosophy and Educational Vision", f'''<p>Her philosophy is simple: every student can do well when concepts are explained clearly, practice is consistent and guidance is personal. She aims to build confidence as well as knowledge, and to help students become disciplined, curious and independent learners who are ready for examinations and for life.</p>'''),
    ]
    blocks = "".join(f'<article class="card"><div class="icon-badge">{icon(ic)}</div><div class="eyebrow">0{i+1}</div><h3>{t}</h3>{c}</article>' for i, (ic, t, c) in enumerate(sections))
    body = f'''
{page_hero("About the Founder – Preety Kumari", "Educator, creative writer and the academic leader behind PreetoMind Academy.", crumb="About the Founder")}
<section><div class="container"><div class="split wide-right">
  {founder_photo()}
  <div>
    <h2 class="founder-name">Preety Kumari</h2>
    <div class="founder-role">Founder and Academic Educator, PreetoMind Academy</div>
    <div class="pill-row"><span class="pill">Creative Writer</span><span class="pill">Literary Award Recipient</span><span class="pill">B.Sc. Zoology with Research</span></div>
    <p>Preety Kumari is the founder and academic educator of PreetoMind Academy. She leads the academy’s teaching, curriculum planning and student guidance, and she is closely involved in every learner’s progress.</p>
    <p>With a background in Zoology with Research, experience in online tutoring and a deep interest in language and literature, she combines scientific precision with creative communication. Her commitment to education is personal. She believes that dedicated teaching, structured practice and genuine care can change how a student learns.</p>
    <div class="statement mt-3" style="padding:28px">{icon("quote")}<p style="font-size:1.08rem">{ph("Founder’s personal message or quote, in her own words")}<span class="by">— Preety Kumari, Founder</span></p></div>
  </div>
</div></div></section>
<section class="section-alt"><div class="container"><div class="grid g-4">
  {feature("users","Leadership","Leads the academy’s teaching, planning and student support personally.")}
  {feature("shield","Dedication","Committed to every learner’s progress and wellbeing.")}
  {feature("pen","Creativity","A creative writer who brings expressive clarity to teaching.")}
  {feature("user","Student-centred","Adapts guidance and practice to individual needs.")}
</div></div></section>
{cta_band("Learn with Preety Kumari", "Contact PreetoMind Academy directly to discuss your academic requirements and arrange a demo class.")}
'''
    return page("founder.html", "Preety Kumari – Founder of PreetoMind Academy | Biology Educator & Creative Writer",
                "Meet Preety Kumari, Founder and Academic Educator of PreetoMind Academy: B.Sc. Zoology with Research, Biology and Science educator, English Grammar teacher and creative writer.", body)


# ============================================================== COURSES
def courses():
    nav_chips = "".join(f'<a class="pill" href="#{d["id"]}">{d["name"]}</a>' for d in DEPARTMENTS)
    blocks = []
    for i, d in enumerate(DEPARTMENTS):
        alt = ' class="section-alt"' if i % 2 == 0 else ""
        blocks.append(f'''<section id="{d["id"]}"{alt}><div class="container"><div class="split wide-left">
  <div>
    <div class="eyebrow">Department {i+1}</div>
    <h2>{d["name"]}</h2>
    <div class="pill-row"><span class="pill">{d["level"]}</span><span class="pill">Subjects: {d["subjects"]}</span></div>
    <p>{d["intro"]}</p>
    <div class="btn-row mt-2"><a class="btn btn-primary btn-sm" href="admission-enquiry.html">Enquire About This Course</a><a class="btn btn-outline btn-sm" href="{wa_href("Hello PreetoMind Academy, I would like details about " + d["name"] + ".")}">Ask on WhatsApp</a></div>
  </div>
  <div class="card"><div class="icon-badge dark">{icon(d["icon"])}</div><h3>Focus Areas</h3>{checklist(d["focus"])}</div>
</div></div></section>''')
    body = f'''
{page_hero("Courses and Academic Departments", "Six academic departments covering school education, Senior Secondary Biology, competitive examinations, higher education and English language development.", crumb="Courses", eyebrow="Programmes")}
<section style="padding:40px 0"><div class="container">
  <div class="notice">{icon("info")}<p>All classes are conducted live online through Google Meet. <strong>For course fees and admission details, please contact PreetoMind Academy directly.</strong></p></div>
  <div class="pill-row mb-0">{nav_chips}</div>
</div></section>
{"".join(blocks)}
<section><div class="container">
  <div class="section-head center"><div class="eyebrow">Included in Every Programme</div><h2>Structured Academic Support</h2></div>
  <div class="grid g-3" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{"".join(feature(*s) for s in SUPPORT)}</div>
</div></section>
{cta_band("Find the Right Course", "Tell us the class, course and subjects you are interested in, and we will guide you through the next steps.")}
'''
    return page("courses.html", "Online Courses | Classes 1–12, Biology, NEET, CUET, B.Sc. & English | PreetoMind Academy",
                "Explore PreetoMind Academy’s online courses: Foundation (Classes 1–8), Secondary (9–10), Senior Secondary Biology (11–12), NEET Biology, CUET UG/PG, B.Sc. subjects and English Grammar & Vocabulary.", body)


# ============================================================== METHODOLOGY
def methodology():
    approaches = [
     ("bulb", "Concept-Based Learning", "Concepts are explained from the basics using simple language, examples, illustrations and structured explanations.",
      ["Start from fundamentals before moving to advanced ideas", "Simple language and relatable, real-life examples", "Diagrams, illustrations and visual explanations", "Structured, step-by-step progression through each chapter", "Regular connections between topics for deeper understanding"]),
     ("video", "Interactive Live Classes", "Interactive online classes are conducted through Google Meet, encouraging participation, questions and regular doubt-solving.",
      ["Live, real-time teaching on Google Meet", "Students are encouraged to participate and ask questions", "Regular doubt-solving built into every class", "Quick checks for understanding during lessons", "A focused, disciplined and respectful online classroom"]),
     ("user", "Personalised Student Attention", "Academic guidance and practice are adapted to each student’s learning needs and progress.",
      ["Understanding each learner’s strengths and challenges", "Practice adapted to individual pace and level", "Targeted support for identified learning gaps", "Ongoing monitoring of progress", "Regular communication with parents"]),
    ]
    cards = "".join(f'''<article class="card" style="border-top:4px solid var(--orange)"><div class="icon-badge dark">{icon(ic)}</div><div class="eyebrow">Approach 0{i+1}</div><h3>{t}</h3><p>{d}</p>{checklist(items)}</article>''' for i, (ic, t, d, items) in enumerate(approaches))
    cycle = [("Learn", "Concept explained clearly in a live class."), ("Practise", "Worksheets, assignments and DPPs."), ("Assess", "Weekly tests and performance analysis."),
             ("Review", "Doubt-solving and revision of weak areas."), ("Improve", "Progress shared with students and parents.")]
    body = f'''
{page_hero("Teaching Methodology", "Three core approaches that help every PreetoMind Academy student understand deeply, practise consistently and progress with confidence.", eyebrow="How We Teach")}
<section><div class="container">
  <div class="grid g-3">{cards}</div>
</div></section>
<section class="section-alt"><div class="container">
  <div class="section-head center"><div class="eyebrow">The Learning Cycle</div><h2>From Understanding to Improvement</h2>
  <p class="lead">Every topic moves through a structured cycle so that learning is reinforced, checked and improved.</p></div>
  <div class="steps h">{"".join(f'<div class="step"><div><h4>{t}</h4><p class="small">{d}</p></div></div>' for t, d in cycle)}</div>
</div></section>
<section><div class="container"><div class="split">
  <div><div class="eyebrow">Online Learning &amp; Communication</div><h2>How Our Online Classroom Works</h2>
    <p>All live classes are conducted through <strong>Google Meet</strong>. <strong>Google Classroom</strong> is used privately to share academic resources, homework, worksheets and related learning materials with enrolled students.</p>
    <p class="small muted">For student privacy, Google Classroom links and student logins are never published on this website.</p></div>
  <div class="grid">
    {feature("video","Live classes on Google Meet","Interactive, real-time teaching sessions for every course.")}
    {feature("lock","Private Google Classroom","Access is shared through the student’s registered email address.")}
    {feature("calendar","Planner and class routine by email","Students receive their academic planner and class routine through email.")}
    {feature("mail","Materials and weekly updates","Study materials and weekly academic updates are shared through the designated learning channels.")}
  </div>
</div></div></section>
{cta_band("Experience a Class Yourself", "Contact us to discuss your requirements and arrange a demo class.")}
'''
    return page("teaching-methodology.html", "Teaching Methodology | Concept-Based Live Online Classes | PreetoMind Academy",
                "How PreetoMind Academy teaches: concept-based learning, interactive live classes on Google Meet and personalised student attention, supported by a structured learning cycle.", body)

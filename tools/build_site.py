"""Build the course website from the lesson content defined below.

Run:  python tools\\build_site.py
Output: index.html and lessons\\lesson-NN.html

Prose is kept identical to SYLLABUS.md. Edit content here and in SYLLABUS.md together.
"""

import os
import html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LESSON_DIR = os.path.join(ROOT, "lessons")

COURSE = {
    "title": "AI 10X Engineer",
    "subtitle": "A semester of engineering practice with AI agents",
    "institution": "Technion",
    "year": "2027",
    "status": "Draft, under construction",
    "updated": "2026-08-25",
    "instructors": "Delivered by Avi Salmon and Yuval Vered, Intel Israel",
}

INTRO = [
    "This course is a full semester of hands-on practice in using AI at an engineering level, the "
    "way working engineers and practical professionals actually use it. AI here is not a "
    "replacement for the engineer, and this is not vibe coding. AI is an agentic tool that "
    "magnifies engineering capability. The participant becomes, in effect, a first-line manager of "
    "AI agents: learning to delegate, direct, review and hold them accountable, while remaining the "
    "responsible engineer behind the result.",
    "Over the semester we cover the methods, workflows and techniques that make this work in "
    "practice, together with a short grounding in AI theory, from classical machine learning "
    "through to transformers, so that the tools are used with understanding rather than by "
    "imitation.",
    "The course is project based. Each topic opens with a short lecture on how the thing is done, "
    "and is followed immediately by hands-on practice. At the end of the semester every participant "
    "presents a working project in their own professional field, built on the methodology, skills "
    "and techniques taught in this syllabus.",
]

FACTS = [
    ("Course name", "AI 10X Engineer"),
    ("Course number", "TBD"),
    ("Semester", "TBD"),
    ("Credit points", "TBD"),
    ("Language", "TBD"),
    ("Format", "TBD"),
    ("Weekly hours", "TBD"),
]

REQUIREMENTS = (
    "Every participant works on their own laptop for the whole semester. The course assumes a paid "
    "AI coding assistant with a real token budget, on the order of twenty dollars per month, such "
    "as Claude Code or an equivalent service, since the practical sessions depend on running agents "
    "rather than occasional free-tier queries. Participants also install an integrated development "
    "environment, Visual Studio Code, Cursor or an equivalent, and work inside it for the rest of "
    "the course. Working in a real project, with files, a repository and a running program in front "
    "of you, is a requirement of the course rather than a preference."
)

GRADING = [
    ("Attendance", "10%"),
    ("Personal static website, assignment from lesson 2", "10%"),
    ("ESP32 hackathon result, lesson 7", "20%"),
    ("Personal project specification", "30%"),
    ("Personal project demonstration", "30%"),
]

LESSONS = [
    {
        "num": 1,
        "slug": "lesson-01",
        "title": "Introduction to the 10X engineer",
        "kind": "Lecture",
        "tagline": "The three levels of AI knowledge, and the capabilities an engineer needs above "
                   "engineering knowledge itself.",
        "body": [
            "The opening lecture sets the frame for the whole semester. It presents the three "
            "levels of AI knowledge and where a practicing engineer needs to sit on that scale. "
            "Level one is the user level: working with AI products as they are given, through a "
            "chat window or a built-in feature. Level two is the practical level: building with "
            "AI, directing agents, wiring tools and models into a working process, and judging the "
            "output as an engineer rather than accepting it. Level three is the deep level: "
            "understanding how the models themselves work, from classical machine learning through "
            "to transformers, enough to reason about what the system can and cannot do. The course "
            "is aimed at level two, with as much of level three as is needed to work at level two "
            "responsibly.",
            "The lecture then turns to the engineer. We discuss the skills and capabilities the new "
            "engineer is expected to have in the AI era, and specifically the capabilities that sit "
            "above engineering knowledge itself: framing a problem clearly enough to hand it off, "
            "delegating work to agents and verifying what comes back, judging quality and "
            "correctness under uncertainty, and taking responsibility for a result produced with "
            "tools the engineer did not write. These are the abilities an engineer has to maintain "
            "in order to stay relevant in the industry as it is now, and they are the abilities the "
            "rest of the course trains.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "TBD"),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 2,
        "slug": "lesson-02",
        "title": "Level one, the user level",
        "kind": "Lecture",
        "tagline": "Everything anyone can do with AI tools today, and why none of it is yet "
                   "engineering.",
        "body": [
            "The second lecture covers level one in full, so that it can then be set aside. We go "
            "through the usable tricks and working methods that anyone can apply on the AI tools "
            "available today, both the free tiers and the paid ones. We run deep research properly, "
            "and we use NotebookLM to turn source material into podcasts and visual summaries. We "
            "build a personal static website and host it on GitHub for free. Time permitting, we "
            "also look at generating music, images and video, and other things of that kind.",
            "The point of the lecture is deliberately double. Everyone can do a great deal at this "
            "level, and they should: these tools are genuinely useful and worth knowing. But none "
            "of it is engineering. The lecture therefore also addresses the illusion of knowledge "
            "that level one produces, the confidence that comes from vibe coding and from output "
            "that looks finished, and the sense of expertise that follows from it. Participants "
            "should leave understanding that this level is a game, enjoyable and useful, and that "
            "it is not the standard expected from an experienced engineer working with AI.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "TBD"),
            ("Home assignment", "Build a personal website and host it for free on GitHub."),
            ("Deliverable", "A live URL to the participant's personal site, plus the repository it "
                            "is served from."),
        ],
    },
    {
        "num": 3,
        "slug": "lesson-03",
        "title": "Introduction to level two, the practical level",
        "kind": "Lecture and practice",
        "tagline": "Real projects in a real IDE: Python, virtual environments, git, and ownership "
                   "of the result.",
        "body": [
            "The third lecture is where the course proper begins. Level two is the practical level, "
            "and its defining property is ownership: we are responsible for the result, whoever or "
            "whatever produced it. Participants start writing Python scripts and small Python GUI "
            "applications inside a real development environment, whether VS Code, Cursor or another "
            "IDE, so that there is an actual project in front of them rather than a chat window. We "
            "set up a virtual environment, work with git, make commits, and track versions of the "
            "work as it changes.",
            "Alongside the mechanics, the lecture puts the question of ownership on the table "
            "directly. If AI wrote the code, who is answerable for it, and what does an engineer "
            "have to do before signing off on it. The lecture is largely hands-on: participants "
            "write and run Python throughout the session rather than only watching.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "Writing Python scripts and a simple Python GUI, creating and using a "
                         "virtual environment, initializing a repository and committing work in "
                         "tracked steps."),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 4,
        "slug": "lesson-04",
        "title": "Skills, APIs, MCP and project memory",
        "kind": "Lecture and practice",
        "tagline": "The layer that turns a chat assistant into a working tool, and where a project "
                   "keeps what it knows.",
        "body": [
            "The fourth lecture builds the layer that turns a chat assistant into a working tool. "
            "We start with skills: packaged, reusable instructions that give an agent a defined "
            "competence it can apply repeatedly rather than being re-explained each time. We then "
            "work with APIs directly, calling external services from our own code and understanding "
            "what the agent can and cannot reach on its own. From there we cover MCP, what the "
            "protocol is for, what it actually does, and why a standard interface between models "
            "and tools matters once more than one tool is involved.",
            "The lecture then widens to the harness around the model: the surrounding tooling that "
            "decides what the model sees, what it is allowed to do, and how its output is captured "
            "and checked. A significant part of the session is devoted to project memory, meaning "
            "where information about a project is kept so that it survives beyond a single "
            "conversation. We distinguish between the different approaches, memory that belongs to "
            "the project and lives in files and repositories under our control, and memory that "
            "belongs to the AI system and is managed for us, and we discuss when each is "
            "appropriate and what each one costs.",
            "The practice for this lecture is to build a working application on top of free APIs.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "Building a small application that consumes one or more free public APIs."),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 5,
        "slug": "lesson-05",
        "title": "Formal process, specs and the virtual AI team",
        "kind": "Lecture and practice",
        "tagline": "Specifications, backlogs and agile method applied to a team of agents you "
                   "manage yourself.",
        "body": [
            "The fifth lecture moves from single tasks to real projects. A larger project cannot be "
            "held in one prompt or one conversation, so it needs a formal process around it. We "
            "work with specifications, backlogs and agile practice, and we borrow directly from the "
            "world of software engineering and engineering team process, because these methods were "
            "designed for exactly the problem we now have: coordinating work across several actors "
            "toward a result none of them holds in full.",
            "On top of that process we build a virtual AI team. The participant stops acting as a "
            "single operator and starts acting as the manager of that team: deciding what work "
            "exists, who takes which part, in what order, and what counts as done. The lecture "
            "treats this management side seriously, because it is the skill that determines whether "
            "the process holds together.",
            "The second focus is formal documentation. We use markdown files as the working "
            "substrate of the project, holding the specification, the backlog, the decisions and "
            "the state of the work, so that the process is stable, inspectable and reproducible "
            "rather than living in a chat history. Throughout, the human stays in the loop as the "
            "point where the work is reviewed and approved.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "TBD"),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 6,
        "slug": "lesson-06",
        "title": "Learning a new technology with AI as teacher and mediator",
        "kind": "Practice",
        "tagline": "An ESP32 kit, no tutorial, and one task: make it work.",
        "body": [
            "The sixth lecture is pure practice, and its subject is the situation an engineer meets "
            "constantly: an unfamiliar technology, a deadline, and no time to become an expert "
            "first. Here AI acts as teacher and as mediator between the participant and the "
            "hardware, and the exercise is to find out how well that works and where it fails.",
            "Each participant receives an ESP32 kit with no tutorial, no guided instructions and no "
            "prepared example to copy. The task is to reach the point of controlling the device. "
            "Everything needed, identifying the board, setting up the toolchain, understanding the "
            "pins, writing and flashing firmware, and debugging what comes back, has to be worked "
            "out through the AI, the documentation it points to, and the participant's own judgment "
            "about which of its answers to trust.",
            "The lesson being taught is transferable and is not specific to the ESP32. What matters "
            "is the method: how to interrogate an unfamiliar domain through AI, how to tell a "
            "confident wrong answer from a correct one before you know the field well enough to see "
            "it, and how to converge on working hardware without a tutorial.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "Bring up an ESP32 board from nothing and control it, working without "
                         "tutorials."),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 7,
        "slug": "lesson-07",
        "title": "ESP32 hackathon",
        "kind": "Competition",
        "tagline": "Two hours, unseen tasks, one week of AI-acquired knowledge. Graded on speed.",
        "body": [
            "The seventh session is a hackathon built on the ESP32 kit handed out in lesson 6. "
            "Participants have had a week with the hardware, and whatever they know about it they "
            "learned through AI rather than from a course on embedded systems. This session tests "
            "what that week was worth.",
            "The format is a timed competition among the participants. Tasks are handed out at the "
            "start of the session and are not published in advance, so nobody can prepare a "
            "solution beforehand. Each participant works for two hours and completes as many tasks "
            "as they can. Grading is based on the time taken to complete each task, which makes "
            "speed the measured quantity rather than elegance.",
            "The purpose is to put the claim of the course under real conditions. The participants "
            "hold only shallow knowledge of the technology, acquired in a week, and are asked to "
            "produce working results under time pressure on problems they have not seen. What the "
            "session demonstrates is how much a practical engineer can actually deliver at that "
            "speed using agentic AI tools, and where the limits of the approach show up.",
        ],
        "fields": [
            ("Format", "Two hours, individual competition, tasks revealed at the start."),
            ("Grading", "Based on time to complete each task."),
            ("Deliverable", "Working solutions to as many of the assigned tasks as possible, "
                            "demonstrated on the participant's own hardware."),
        ],
    },
    {
        "num": 8,
        "slug": "lesson-08",
        "title": "Classical AI, from statistics to the eve of the transformer",
        "kind": "Theory",
        "tagline": "The vocabulary and methods that came before large language models, and when "
                   "they remain the right choice.",
        "body": [
            "The eighth lecture is theory. It covers artificial intelligence as it existed before "
            "large language models: statistical methods and classical machine learning, and the "
            "line of technologies that led up to, but does not include, the transformer era.",
            "The emphasis is on terminology and on the methods themselves. Participants should come "
            "out able to read the vocabulary of the field and know what the standard techniques do: "
            "supervised and unsupervised learning, regression and classification, clustering, "
            "feature engineering, evaluation and the reasons models fail on data they have not "
            "seen. This matters partly because the current generation of systems is built on these "
            "foundations and its own vocabulary is inherited from them.",
            "The lecture also makes a practical argument. Not every problem needs a large language "
            "model. Many tasks are solved better, faster, more cheaply and far more predictably by "
            "a classical method, and an engineer who reaches for the largest available model every "
            "time is choosing a cannon for work that calls for a smaller instrument. We look at "
            "cases where the classical approach is the correct engineering choice, and at how to "
            "tell which situation you are in.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "TBD"),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 9,
        "slug": "lesson-09",
        "title": "Large language models and transformers",
        "kind": "Theory",
        "tagline": "The architecture and the mathematics, and how knowing them makes for better "
                   "agentic flows.",
        "body": [
            "The ninth lecture continues the theory and picks up where lesson 8 stopped. It follows "
            "the development of large language models and the transformer architecture that made "
            "them possible, and covers both the ideas and the mathematics underneath them: "
            "tokenization and embeddings, attention and why it replaced what came before, the "
            "structure of a transformer block, and what training and inference actually consist of.",
            "The reason for teaching the mathematics is practical rather than academic. Much of "
            "what appears mysterious about working with these systems follows directly from how "
            "they operate. Context limits, the cost of long inputs, sensitivity to how a prompt is "
            "phrased, the difference between what a model knows and what it has been given to read, "
            "and the reasons a confident answer can still be wrong, all become predictable once the "
            "mechanism is understood. Participants who know what happens behind the scene design "
            "better agentic flows: they structure context deliberately, decide what to put in front "
            "of the model and what to keep out, and stop expecting behaviour the architecture "
            "cannot provide.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "TBD"),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 10,
        "slug": "lesson-10",
        "title": "Physical AI",
        "kind": "Theory",
        "tagline": "AI that perceives and acts in the world, and the research being done on it at "
                   "the Technion.",
        "body": [
            "The tenth lecture is the third and last of the theory sessions, and it turns to "
            "physical AI: systems that perceive and act in the physical world rather than only "
            "producing text. This is the direction the field is moving in now, and it is the point "
            "where the course's own hardware work connects to current research.",
            "The lecture covers the terminology and the problems that define the area. Perception "
            "from real sensors, control under uncertainty, the gap between a model trained in "
            "simulation and the same model running on a real device, latency and safety constraints "
            "that do not exist when the output is text, and what it means for a learned policy to "
            "act on the world with consequences that cannot be undone.",
            "The second half presents research being carried out at the Technion in this area, so "
            "that participants see the work as it is actually being done, by whom, and on what "
            "problems, rather than as a survey of the literature.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "TBD"),
            ("Deliverable", "TBD"),
        ],
    },
    {
        "num": 11,
        "slug": "lesson-11",
        "title": "Personal project, definition and start of work",
        "kind": "Working session",
        "tagline": "Each participant defines a project in their own field and begins building it.",
        "body": [
            "The eleventh session is a working week devoted to the personal project that each "
            "participant will develop and later present. Each participant chooses a subject from "
            "their own professional field and defines a project built at level two, using the tools "
            "and methodologies taught in the course. It can be a simulator, an analysis tool, a "
            "tutorial or teaching tool, or anything else that genuinely belongs to their profession.",
            "The session is spent on definition first: stating what the project is, what it is for, "
            "what it will produce, and how it will be judged as finished. Once the definition "
            "holds, participants begin building. The work continues outside class, and the session "
            "exists to make sure every project starts from a specification rather than from an "
            "impulse.",
            "The point of ownership is worth stating plainly here. The project may be built "
            "entirely by AI, and that is acceptable. What is not delegated is responsibility: the "
            "participant owns the result, answers for it, and must be able to explain, defend and "
            "correct every part of it. That distinction is the subject of the course, and the "
            "project is where it is tested.",
        ],
        "fields": [
            ("Goal", "TBD"),
            ("Topics", "TBD"),
            ("Hands-on", "Defining the personal project and beginning implementation."),
            ("Deliverable", "A written project definition, and the beginning of a working "
                            "implementation under version control."),
        ],
    },
    {
        "num": 12,
        "slug": "lesson-12",
        "title": "Project presentations",
        "kind": "Presentations",
        "tagline": "Each participant presents and demonstrates their project to the class. Sessions "
                   "12 and 13.",
        "body": [
            "The final two sessions are given to presentations. Each participant presents the "
            "personal project defined in lesson 11 and demonstrates it live to the rest of the "
            "class. The presentation covers what the project does, how it was built, which of the "
            "course methods were used and where they helped or failed, and what the participant "
            "would do differently.",
            "The demonstration is required. A project that cannot be shown running is not finished. "
            "Participants should also expect questions about their own code from the room and from "
            "the staff, since being able to explain and defend the work is part of what is being "
            "assessed.",
        ],
        "fields": [
            ("Format", "Live presentation and working demonstration to the class."),
            ("Deliverable", "The completed project, its repository, and the presentation given in "
                            "class."),
        ],
        "label": "Sessions 12 and 13",
    },
]


def e(text):
    return html.escape(text, quote=False)


def field_value(value):
    if value == "TBD":
        return '<span class="tbd">TBD</span>'
    return e(value)


def page(title, body, depth):
    up = "../" if depth else ""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<link rel="stylesheet" href="{up}assets/style.css">
</head>
<body>
{body}
</body>
</html>
"""


def site_nav(current, depth):
    up = "../" if depth else ""
    home_cls = ' class="active"' if current == "home" else ""
    det_cls = ' class="active"' if current == "details" else ""
    items = [
        f'<a href="{up}index.html"{home_cls}>Course home</a>',
        f'<a href="{up}course-details.html"{det_cls} data-plain="1">Course details</a>',
    ]
    for L in LESSONS:
        label = L.get("label", f"Lesson {L['num']}")
        cls = ' class="active"' if current == L["slug"] else ""
        items.append(
            f'<a href="{up}lessons/{L["slug"]}.html"{cls}>'
            f'<span class="n">{e(label)}</span>'
            f'<span class="t">{e(L["title"])}</span></a>'
        )
    return '<nav class="sidenav">\n' + "\n".join(items) + "\n</nav>"


def masthead(kicker, title, subtitle, meta_items, home_link=False, up_prefix=None):
    up = ("../" if home_link else "") if up_prefix is None else up_prefix
    back = f'<a class="back" href="{up}index.html">Back to course home</a>' if home_link else ""
    metas = "".join(f"<span>{e(m)}</span>" for m in meta_items)
    kick = f'<p class="kicker">{e(kicker)}</p>' if kicker else ""
    sub = f'<p class="sub">{e(subtitle)}</p>' if subtitle else ""
    return f"""<header class="masthead">
  <div class="wrap">
    {back}
    {kick}
    <h1>{e(title)}</h1>
    {sub}
    <div class="meta">{metas}</div>
  </div>
</header>"""


def build_index():
    lede = INTRO[0]

    rows = []
    for L in LESSONS:
        label = L.get("label", f"Lesson {L['num']}")
        rows.append(f"""      <a class="lesson-row" href="lessons/{L['slug']}.html">
        <span class="row-num">{e(label)}</span>
        <span class="row-main">
          <span class="row-title">{e(L['title'])}</span>
          <span class="row-tag">{e(L['tagline'])}</span>
        </span>
        <span class="row-kind">{e(L['kind'])}</span>
      </a>""")
    lesson_rows = "\n".join(rows)

    body = f"""{masthead(
        COURSE["institution"] + ", academic year " + COURSE["year"],
        COURSE["title"],
        COURSE["subtitle"],
        [COURSE["status"], "Last updated " + COURSE["updated"]],
    )}

<div class="layout">
{site_nav("home", 0)}
<main>

  <section id="about">
    <p class="opening">{e(lede)}</p>
    <p class="byline">{e(COURSE["instructors"])}</p>
    <p class="more-link"><a href="course-details.html">Full course details, requirements and grading</a></p>
  </section>

  <section id="lessons">
    <h2>Lessons</h2>
    <div class="lesson-list">
{lesson_rows}
    </div>
  </section>

</main>
</div>

<footer>{e(COURSE['title'])}, {e(COURSE['institution'])}, academic year {e(COURSE['year'])}. Draft under construction.</footer>
"""
    with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
        f.write(page(COURSE["title"] + ": course syllabus", body, depth=0))


def build_details():
    intro = "\n    ".join(f"<p>{e(p)}</p>" for p in INTRO)

    facts = "\n".join(
        f"<tr><td>{e(k)}</td><td>{field_value(v)}</td></tr>" for k, v in FACTS
    )
    grades = "\n".join(
        f"<tr><td>{e(k)}</td><td>{e(v)}</td></tr>" for k, v in GRADING
    )
    staff = "\n".join(
        f'<tr><td>{e(r)}</td><td>{e(n)}</td><td class="tbd">TBD</td>'
        f'<td class="tbd">TBD</td></tr>'
        for r, n in (("Lecturer", "Avi Salmon, Intel Israel"),
                     ("Lecturer", "Yuval Vered, Intel Israel"))
    )

    sched = []
    for L in LESSONS:
        label = L.get("label", str(L["num"]))
        week = label.replace("Lesson ", "").replace("Sessions ", "")
        sched.append(
            f'<tr><td>{e(week)}</td>'
            f'<td><a href="lessons/{L["slug"]}.html">{e(L["title"])}</a></td>'
            f'<td>{e(L["kind"])}</td>'
            f'<td class="tbd">TBD</td></tr>'
        )
    schedule = "\n".join(sched)

    body = f"""{masthead(
        "Course details",
        "AI 10X Engineer",
        "Full syllabus, requirements, schedule and grading",
        [COURSE["institution"], "Academic year " + COURSE["year"],
         COURSE["status"], "Last updated " + COURSE["updated"]],
        home_link=True,
        up_prefix="",
    )}

<div class="layout">
{site_nav("details", 0)}
<main>

  <section id="overview">
    <h2>Course overview</h2>
    {intro}
  </section>

  <section id="facts">
    <h2>Course details</h2>
    <table>
      <thead><tr><th>Field</th><th>Value</th></tr></thead>
      <tbody>
{facts}
      </tbody>
    </table>
  </section>

  <section id="staff">
    <h2>Instructor and staff</h2>
    <table>
      <thead><tr><th>Role</th><th>Name</th><th>Contact</th><th>Office hours</th></tr></thead>
      <tbody>
{staff}
      </tbody>
    </table>
  </section>

  <section id="objectives">
    <h2>Learning objectives</h2>
    <p class="tbd">TBD</p>
  </section>

  <section id="requirements">
    <h2>Prerequisites and what participants need</h2>
    <p>Required: <span class="tbd">TBD</span></p>
    <p>Recommended: <span class="tbd">TBD</span></p>
    <p>{e(REQUIREMENTS)}</p>
  </section>

  <section id="schedule">
    <h2>Schedule</h2>
    <table>
      <thead><tr><th>Week</th><th>Topic</th><th>Kind</th><th>Date</th></tr></thead>
      <tbody>
{schedule}
      </tbody>
    </table>
  </section>

  <section id="grading">
    <h2>Grading</h2>
    <table>
      <thead><tr><th>Component</th><th>Weight</th></tr></thead>
      <tbody>
{grades}
        <tr class="total"><td>Total</td><td>100%</td></tr>
      </tbody>
    </table>
  </section>

  <section id="policies">
    <h2>Policies</h2>
    <p class="tbd">TBD. Attendance, AI usage policy, collaboration, late submissions, academic integrity.</p>
  </section>

  <section id="resources">
    <h2>Resources</h2>
    <p class="tbd">TBD</p>
  </section>

</main>
</div>

<footer>{e(COURSE['title'])}, {e(COURSE['institution'])}, academic year {e(COURSE['year'])}. Draft under construction.</footer>
"""
    with open(os.path.join(ROOT, "course-details.html"), "w", encoding="utf-8") as f:
        f.write(page("Course details: AI 10X Engineer", body, depth=0))


def build_lesson(i, L):
    label = L.get("label", f"Lesson {L['num']}")
    body_html = "\n    ".join(f"<p>{e(p)}</p>" for p in L["body"])
    fields = "\n".join(
        f"      <dt>{e(k)}</dt><dd>{field_value(v)}</dd>" for k, v in L["fields"]
    )

    prev_link = ""
    next_link = ""
    if i > 0:
        p = LESSONS[i - 1]
        prev_link = f'<a class="prev" href="{p["slug"]}.html">Previous: {e(p["title"])}</a>'
    if i < len(LESSONS) - 1:
        n = LESSONS[i + 1]
        next_link = f'<a class="next" href="{n["slug"]}.html">Next: {e(n["title"])}</a>'

    body = f"""{masthead(label, L["title"], L["tagline"], [L["kind"]], home_link=True)}

<div class="layout">
{site_nav(L["slug"], 1)}
<main>

  <section id="recording">
    <h2>Lesson recording</h2>
    <div class="video-placeholder" role="img" aria-label="Recording not yet available">
      <div class="vp-inner">
        <div class="vp-mark"></div>
        <p class="vp-title">Recording not yet available</p>
        <p class="vp-note">The video for this lesson will be published here after the session is recorded.</p>
      </div>
    </div>
  </section>

  <section id="description">
    <h2>Description</h2>
    {body_html}
  </section>

  <section id="at-a-glance">
    <h2>At a glance</h2>
    <dl class="fields">
{fields}
    </dl>
  </section>

  <section id="materials">
    <h2>Materials</h2>
    <p class="tbd">TBD</p>
  </section>

  <nav class="pager">
    {prev_link}
    {next_link}
  </nav>

</main>
</div>

<footer>{e(COURSE['title'])}, {e(COURSE['institution'])}, academic year {e(COURSE['year'])}. Draft under construction.</footer>
"""
    out = os.path.join(LESSON_DIR, L["slug"] + ".html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(page(f"{label}: {L['title']}", body, depth=1))


def main():
    os.makedirs(LESSON_DIR, exist_ok=True)
    build_index()
    build_details()
    for i, L in enumerate(LESSONS):
        build_lesson(i, L)
    print(f"built index.html, course-details.html and {len(LESSONS)} lesson pages")


if __name__ == "__main__":
    main()

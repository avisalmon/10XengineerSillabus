# AI 10X Engineer: course syllabus

Status: draft, under construction
Institution: Technion
Academic year: 2027
Last updated: 2026-08-25

---

## 1. Course overview

This course is a full semester of hands-on practice in using AI at an engineering level, the way
working engineers and practical professionals actually use it. AI here is not a replacement for the
engineer, and this is not vibe coding. AI is an agentic tool that magnifies engineering capability.
The participant becomes, in effect, a first-line manager of AI agents: learning to delegate, direct,
review and hold them accountable, while remaining the responsible engineer behind the result.

Over the semester we cover the methods, workflows and techniques that make this work in practice,
together with a short grounding in AI theory, from classical machine learning through to
transformers, so that the tools are used with understanding rather than by imitation.

The course is project based. Each topic opens with a short lecture on how the thing is done, and is
followed immediately by hands-on practice. At the end of the semester every participant presents a
working project in their own professional field, built on the methodology, skills and techniques
taught in this syllabus.

| Field | Value |
|---|---|
| Course name | AI 10X Engineer |
| Course number | TBD |
| Semester | TBD |
| Credit points | TBD |
| Language | TBD |
| Format | TBD |
| Weekly hours | TBD |

---

## 2. Instructor and staff

| Role | Name | Contact | Office hours |
|---|---|---|---|
| Lecturer | TBD | TBD | TBD |
| TA | TBD | TBD | TBD |

---

## 3. Learning objectives

By the end of this course, participants will be able to:

1. TBD
2. TBD
3. TBD

---

## 4. Prerequisites

Required: TBD

Recommended: TBD

Tooling and accounts needed: a personal laptop, available to the participant throughout the course.
A paid AI coding assistant subscription at the level of roughly twenty dollars per month for the
duration of the semester, for example Claude Code or an equivalent service that supplies a working
token budget. An integrated development environment installed and working, for example Visual Studio
Code, Cursor or an equivalent, so that the participant can work with AI inside a real project rather
than through a browser chat window.

---

## 5. Course structure

TBD. How the semester is organized: modules, weekly rhythm, labs, project milestones.

---

## 6. Weekly schedule

| Week | Topic | Training or lab | Video | Materials | Assignment |
|---|---|---|---|---|---|
| 1 | TBD | TBD | TBD | TBD | TBD |
| 2 | TBD | TBD | TBD | TBD | TBD |
| 3 | TBD | TBD | TBD | TBD | TBD |
| 4 | TBD | TBD | TBD | TBD | TBD |
| 5 | TBD | TBD | TBD | TBD | TBD |
| 6 | TBD | TBD | TBD | TBD | TBD |
| 7 | TBD | TBD | TBD | TBD | TBD |
| 8 | TBD | TBD | TBD | TBD | TBD |
| 9 | TBD | TBD | TBD | TBD | TBD |
| 10 | TBD | TBD | TBD | TBD | TBD |
| 11 | TBD | TBD | TBD | TBD | TBD |
| 12 | TBD | TBD | TBD | TBD | TBD |
| 13 | TBD | TBD | TBD | TBD | TBD |

---

## 7. Modules in detail

### Lecture 1: Introduction to the 10X engineer

The opening lecture sets the frame for the whole semester. It presents the three levels of AI
knowledge and where a practicing engineer needs to sit on that scale. Level one is the user level:
working with AI products as they are given, through a chat window or a built-in feature. Level two
is the practical level: building with AI, directing agents, wiring tools and models into a working
process, and judging the output as an engineer rather than accepting it. Level three is the deep
level: understanding how the models themselves work, from classical machine learning through to
transformers, enough to reason about what the system can and cannot do. The course is aimed at
level two, with as much of level three as is needed to work at level two responsibly.

The lecture then turns to the engineer. We discuss the skills and capabilities the new engineer is
expected to have in the AI era, and specifically the capabilities that sit above engineering
knowledge itself: framing a problem clearly enough to hand it off, delegating work to agents and
verifying what comes back, judging quality and correctness under uncertainty, and taking
responsibility for a result produced with tools the engineer did not write. These are the abilities
an engineer has to maintain in order to stay relevant in the industry as it is now, and they are the
abilities the rest of the course trains.

Goal: TBD

Topics: TBD

Hands-on: TBD

Deliverable: TBD

### Lecture 2: Level one, the user level

The second lecture covers level one in full, so that it can then be set aside. We go through the
usable tricks and working methods that anyone can apply on the AI tools available today, both the
free tiers and the paid ones. We run deep research properly, and we use NotebookLM to turn source
material into podcasts and visual summaries. We build a personal static website and host it on
GitHub for free. Time permitting, we also look at generating music, images and video, and other
things of that kind.

The point of the lecture is deliberately double. Everyone can do a great deal at this level, and
they should: these tools are genuinely useful and worth knowing. But none of it is engineering. The
lecture therefore also addresses the illusion of knowledge that level one produces, the confidence
that comes from vibe coding and from output that looks finished, and the sense of expertise that
follows from it. Participants should leave understanding that this level is a game, enjoyable and
useful, and that it is not the standard expected from an experienced engineer working with AI.

Goal: TBD

Topics: TBD

Hands-on: TBD

Home assignment: build a personal website and host it for free on GitHub.

Deliverable: a live URL to the participant's personal site, plus the repository it is served from.

### Lecture 3: Introduction to level two, the practical level

The third lecture is where the course proper begins. Level two is the practical level, and its
defining property is ownership: we are responsible for the result, whoever or whatever produced it.
Participants start writing Python scripts and small Python GUI applications inside a real
development environment, whether VS Code, Cursor or another IDE, so that there is an actual project
in front of them rather than a chat window. We set up a virtual environment, work with git, make
commits, and track versions of the work as it changes.

Alongside the mechanics, the lecture puts the question of ownership on the table directly. If AI
wrote the code, who is answerable for it, and what does an engineer have to do before signing off on
it. The lecture is largely hands-on: participants write and run Python throughout the session rather
than only watching.

Goal: TBD

Topics: TBD

Hands-on: writing Python scripts and a simple Python GUI, creating and using a virtual environment,
initializing a repository and committing work in tracked steps.

Deliverable: TBD

### Lecture 4: Skills, APIs, MCP and project memory

The fourth lecture builds the layer that turns a chat assistant into a working tool. We start with
skills: packaged, reusable instructions that give an agent a defined competence it can apply
repeatedly rather than being re-explained each time. We then work with APIs directly, calling
external services from our own code and understanding what the agent can and cannot reach on its
own. From there we cover MCP, what the protocol is for, what it actually does, and why a standard
interface between models and tools matters once more than one tool is involved.

The lecture then widens to the harness around the model: the surrounding tooling that decides what
the model sees, what it is allowed to do, and how its output is captured and checked. A significant
part of the session is devoted to project memory, meaning where information about a project is kept
so that it survives beyond a single conversation. We distinguish between the different approaches,
memory that belongs to the project and lives in files and repositories under our control, and memory
that belongs to the AI system and is managed for us, and we discuss when each is appropriate and
what each one costs.

The practice for this lecture is to build a working application on top of free APIs.

Goal: TBD

Topics: TBD

Hands-on: building a small application that consumes one or more free public APIs.

Deliverable: TBD

### Lecture 5: Formal process, specs and the virtual AI team

The fifth lecture moves from single tasks to real projects. A larger project cannot be held in one
prompt or one conversation, so it needs a formal process around it. We work with specifications,
backlogs and agile practice, and we borrow directly from the world of software engineering and
engineering team process, because these methods were designed for exactly the problem we now have:
coordinating work across several actors toward a result none of them holds in full.

On top of that process we build a virtual AI team. The participant stops acting as a single operator
and starts acting as the manager of that team: deciding what work exists, who takes which part, in
what order, and what counts as done. The lecture treats this management side seriously, because it
is the skill that determines whether the process holds together.

The second focus is formal documentation. We use markdown files as the working substrate of the
project, holding the specification, the backlog, the decisions and the state of the work, so that
the process is stable, inspectable and reproducible rather than living in a chat history. Throughout,
the human stays in the loop as the point where the work is reviewed and approved.

Goal: TBD

Topics: TBD

Hands-on: TBD

Deliverable: TBD

### Lecture 6: Learning a new technology with AI as teacher and mediator

The sixth lecture is pure practice, and its subject is the situation an engineer meets constantly:
an unfamiliar technology, a deadline, and no time to become an expert first. Here AI acts as teacher
and as mediator between the participant and the hardware, and the exercise is to find out how well
that works and where it fails.

Each participant receives an ESP32 kit with no tutorial, no guided instructions and no prepared
example to copy. The task is to reach the point of controlling the device. Everything needed,
identifying the board, setting up the toolchain, understanding the pins, writing and flashing
firmware, and debugging what comes back, has to be worked out through the AI, the documentation it
points to, and the participant's own judgment about which of its answers to trust.

The lesson being taught is transferable and is not specific to the ESP32. What matters is the
method: how to interrogate an unfamiliar domain through AI, how to tell a confident wrong answer
from a correct one before you know the field well enough to see it, and how to converge on working
hardware without a tutorial.

Goal: TBD

Topics: TBD

Hands-on: bring up an ESP32 board from nothing and control it, working without tutorials.

Deliverable: TBD

### Lecture 7: ESP32 hackathon

The seventh session is a hackathon built on the ESP32 kit handed out in lecture 6. Participants have
had a week with the hardware, and whatever they know about it they learned through AI rather than
from a course on embedded systems. This session tests what that week was worth.

The format is a timed competition among the participants. Tasks are handed out at the start of the
session and are not published in advance, so nobody can prepare a solution beforehand. Each
participant works for two hours and completes as many tasks as they can. Grading is based on the
time taken to complete each task, which makes speed the measured quantity rather than elegance.

The purpose is to put the claim of the course under real conditions. The participants hold only
shallow knowledge of the technology, acquired in a week, and are asked to produce working results
under time pressure on problems they have not seen. What the session demonstrates is how much a
practical engineer can actually deliver at that speed using agentic AI tools, and where the limits
of the approach show up.

Format: two hours, individual competition, tasks revealed at the start.

Grading: based on time to complete each task.

Deliverable: working solutions to as many of the assigned tasks as possible, demonstrated on the
participant's own hardware.

### Lecture 8: Classical AI, from statistics to the eve of the transformer

The eighth lecture is theory. It covers artificial intelligence as it existed before large language
models: statistical methods and classical machine learning, and the line of technologies that led up
to, but does not include, the transformer era.

The emphasis is on terminology and on the methods themselves. Participants should come out able to
read the vocabulary of the field and know what the standard techniques do: supervised and
unsupervised learning, regression and classification, clustering, feature engineering, evaluation
and the reasons models fail on data they have not seen. This matters partly because the current
generation of systems is built on these foundations and its own vocabulary is inherited from them.

The lecture also makes a practical argument. Not every problem needs a large language model. Many
tasks are solved better, faster, more cheaply and far more predictably by a classical method, and an
engineer who reaches for the largest available model every time is choosing a cannon for work that
calls for a smaller instrument. We look at cases where the classical approach is the correct
engineering choice, and at how to tell which situation you are in.

Goal: TBD

Topics: TBD

Hands-on: TBD

Deliverable: TBD

### Lecture 9: Large language models and transformers

The ninth lecture continues the theory and picks up where lecture 8 stopped. It follows the
development of large language models and the transformer architecture that made them possible, and
covers both the ideas and the mathematics underneath them: tokenization and embeddings, attention
and why it replaced what came before, the structure of a transformer block, and what training and
inference actually consist of.

The reason for teaching the mathematics is practical rather than academic. Much of what appears
mysterious about working with these systems follows directly from how they operate. Context limits,
the cost of long inputs, sensitivity to how a prompt is phrased, the difference between what a model
knows and what it has been given to read, and the reasons a confident answer can still be wrong, all
become predictable once the mechanism is understood. Participants who know what happens behind the
scene design better agentic flows: they structure context deliberately, decide what to put in front
of the model and what to keep out, and stop expecting behaviour the architecture cannot provide.

Goal: TBD

Topics: TBD

Hands-on: TBD

Deliverable: TBD

### Lecture 10: Physical AI

The tenth lecture is the third and last of the theory sessions, and it turns to physical AI: systems
that perceive and act in the physical world rather than only producing text. This is the direction
the field is moving in now, and it is the point where the course's own hardware work connects to
current research.

The lecture covers the terminology and the problems that define the area. Perception from real
sensors, control under uncertainty, the gap between a model trained in simulation and the same model
running on a real device, latency and safety constraints that do not exist when the output is text,
and what it means for a learned policy to act on the world with consequences that cannot be undone.

The second half presents research being carried out at the Technion in this area, so that
participants see the work as it is actually being done, by whom, and on what problems, rather than
as a survey of the literature.

Goal: TBD

Topics: TBD

Hands-on: TBD

Deliverable: TBD

### Lecture 11: Personal project, definition and start of work

The eleventh session is a working week devoted to the personal project that each participant will
develop and later present. Each participant chooses a subject from their own professional field and
defines a project built at level two, using the tools and methodologies taught in the course. It can
be a simulator, an analysis tool, a tutorial or teaching tool, or anything else that genuinely
belongs to their profession.

The session is spent on definition first: stating what the project is, what it is for, what it will
produce, and how it will be judged as finished. Once the definition holds, participants begin
building. The work continues outside class, and the session exists to make sure every project starts
from a specification rather than from an impulse.

The point of ownership is worth stating plainly here. The project may be built entirely by AI, and
that is acceptable. What is not delegated is responsibility: the participant owns the result,
answers for it, and must be able to explain, defend and correct every part of it. That distinction
is the subject of the course, and the project is where it is tested.

Goal: TBD

Topics: TBD

Hands-on: defining the personal project and beginning implementation.

Deliverable: a written project definition, and the beginning of a working implementation under
version control.

### Lectures 12 and 13: Project presentations

The final two sessions are given to presentations. Each participant presents the personal project
defined in lecture 11 and demonstrates it live to the rest of the class. The presentation covers what
the project does, how it was built, which of the course methods were used and where they helped or
failed, and what the participant would do differently.

The demonstration is required. A project that cannot be shown running is not finished. Participants
should also expect questions about their own code from the room and from the staff, since being able
to explain and defend the work is part of what is being assessed.

Format: live presentation and working demonstration to the class.

Deliverable: the completed project, its repository, and the presentation given in class.

---

## 8. Tools and environment

Every participant works on their own laptop for the whole semester. The course assumes a paid AI
coding assistant with a real token budget, on the order of twenty dollars per month, such as Claude
Code or an equivalent service, since the practical sessions depend on running agents rather than
occasional free-tier queries. Participants also install an integrated development environment,
Visual Studio Code, Cursor or an equivalent, and work inside it for the rest of the course. Working
in a real project, with files, a repository and a running program in front of you, is a requirement
of the course rather than a preference.

---

## 9. Assignments and projects

| Number | Title | Type | Weight | Due |
|---|---|---|---|---|
| A1 | TBD | TBD | TBD | TBD |

---

## 10. Grading

| Component | Weight |
|---|---|
| Attendance | 10% |
| Personal static website, assignment from lecture 2 | 10% |
| ESP32 hackathon result, lecture 7 | 20% |
| Personal project specification | 30% |
| Personal project demonstration | 30% |
| Total | 100% |

---

## 11. Resources

### Videos

TBD

### Reading

TBD

### Links and references

TBD

---

## 12. Policies

TBD. Attendance, AI usage policy, collaboration, late submissions, academic integrity.

---

## 13. Frequently asked questions

TBD

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

### Lecture 3: Skills, APIs, MCP and project memory

The third lecture builds the layer that turns a chat assistant into a working tool. We start with
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

### Lecture 4: Formal process, specs and the virtual AI team

The fourth lecture moves from single tasks to real projects. A larger project cannot be held in one
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

### Lecture 5: ESP32 hackathon

The fifth session is a hackathon on hardware. Each participant receives an ESP32 kit in advance,
with no tutorial, no guided instructions and no prepared example to copy. Bringing the board up is
their own problem, and whatever they know about it by the day of the session they learned through AI
rather than from a course on embedded systems.

The format is a timed competition among the participants. Tasks are handed out at the start of the
session and are not published in advance, so nobody can prepare a solution beforehand. Each
participant works for two hours and completes as many tasks as they can. Grading is based on the
time taken to complete each task, which makes speed the measured quantity rather than elegance.

The purpose is to put the claim of the course under real conditions. The participants hold only
shallow knowledge of the technology, acquired on their own in a short time, and are asked to produce
working results under time pressure on problems they have not seen. What the session demonstrates is
how much a practical engineer can actually deliver at that speed using agentic AI tools, and where
the limits of the approach show up.

The subject being taught is transferable and is not specific to the ESP32. What matters is the
method: how to interrogate an unfamiliar domain through AI, how to tell a confident wrong answer
from a correct one before you know the field well enough to see it, and how to converge on working
hardware without a tutorial.

Preparation: the ESP32 kit is distributed ahead of the session. Participants bring the board up on
their own, without tutorials, before they arrive.

Format: two hours, individual competition, tasks revealed at the start.

Grading: based on time to complete each task.

Deliverable: working solutions to as many of the assigned tasks as possible, demonstrated on the
participant's own hardware.

### Lecture 6: AI theory 1: classical AI, from statistics to the eve of the transformer

The sixth lecture is the first of four sessions on AI in depth. It covers artificial intelligence as
it existed before large language models: statistical methods and classical machine learning, and the
line of technologies that led up to, but does not include, the transformer era.

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

### Lecture 7: AI theory 2: large language models and transformers

The seventh lecture is the second of the four in-depth sessions and picks up where lecture 6
stopped. It follows the development of large language models and the transformer architecture that
made them possible, and covers both the ideas and the mathematics underneath them: tokenization and
embeddings, attention and why it replaced what came before, the structure of a transformer block,
and what training and inference actually consist of.

The reason for teaching the mathematics is practical rather than academic. Much of what appears
mysterious about working with these systems follows directly from how they operate. Context limits,
the cost of long inputs, sensitivity to how a prompt is phrased, the difference between what a model
knows and what it has been given to read, and the reasons a confident answer can still be wrong, all
become predictable once the mechanism is understood. Participants who know what happens behind the
scene design better agentic flows: they structure context deliberately, decide what to put in front
of the model and what to keep out, and stop expecting behaviour the architecture cannot provide.

The session carries a task. Each participant trains a small transformer of their own on the
TinyStories dataset, a corpus of short, simple stories designed so that a model small enough to
train on ordinary hardware can still produce coherent language. The point is not to build something
competitive. It is to run the full loop once, from data to tokenizer to training to generation, and
to see the mechanism from the inside rather than described on a slide.

Goal: TBD

Topics: TBD

Hands-on: train a small transformer on the TinyStories dataset, taking it from raw data through
tokenization and training to generated text.

Deliverable: a trained model, the code that produced it, and a sample of its output.

### Lecture 8: Inside the harness: how an IDE hosts an agent

The eighth lecture is the third of the four in-depth sessions, and it opens the tool that
participants have been using since the start of the course. Visual Studio Code is built from a small
number of clearly separated parts: the editor core, the extension host that runs third party code
out of process, the language server protocol, the debug adapter protocol, the terminal, and the
extension API that binds them together. We go through these parts and see what each one is
responsible for.

The reason for the detour is that an AI harness is built out of exactly these pieces. The harness is
what stands between a model and the work: it decides what the model is shown, which tools it may
call, how a call is executed, what comes back, and what the user is asked to approve. Once the
structure of the editor is clear, the structure of the agent running inside it stops being
mysterious, and the behaviour of any agentic tool becomes something that can be reasoned about
rather than guessed at.

Participants then build a harness of their own. It is small and it does not need to compete with
anything, but it must genuinely work: take a request, assemble context, call a model, execute a
tool, return the result, and keep the human in control of what is allowed to happen. Building one is
the fastest way to understand every harness the participant will use afterwards.

Goal: TBD

Topics: TBD

Hands-on: build a working AI harness: context assembly, a model call, tool execution, and a human
approval step.

Deliverable: a running harness, with its source, that completes at least one task end to end.

### Lecture 9: The 10X engineer on the exponential slope

The ninth lecture is the last of the four in-depth sessions, and it steps back from the tools to the
position of the engineer who uses them. The technology is changing on an exponential slope:
capabilities that justified a job title arrive as a product feature within a year, methods taught at
the start of a semester are dated by the end of it, and the useful life of a specific skill is now
shorter than the time it takes to acquire it properly.

The lecture examines what that means for a working engineer. It covers what remains stable when the
tools do not: judgment, the ability to specify a problem, responsibility for a result, and the
capacity to learn a new domain quickly, which is the ability the ESP32 session was designed to
exercise. It covers what it costs to stay current, how to distinguish a genuine shift from noise,
and why the ability to discard a hard-won method without regret is now part of the job.

The cultural side is treated as seriously as the technical one. The expectations placed on
engineers, the way teams are organized, what counts as competent work and who is credited with it
are all moving, and an engineer who tracks only the technology will be surprised by the rest. The
session closes the theory block by putting the course itself in that context: what it teaches will
age, and the point is to leave with a way of working rather than with a set of current answers.

Goal: TBD

Topics: TBD

Hands-on: TBD

Deliverable: TBD

### Lecture 10: Physical AI

The tenth lecture closes the theoretical part of the course and turns to physical AI: systems
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
| ESP32 hackathon result, lecture 5 | 20% |
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

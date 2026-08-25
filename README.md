# 10X Engineer Syllabus

Syllabus and course materials for the AI 10X Engineer semester course at the Technion,
academic year 2027.

## Contents

| Path | Purpose |
|---|---|
| `SYLLABUS.md` | Source of truth for the course content |
| `index.html` | Course home page: overview and lesson list |
| `course-details.html` | Requirements, schedule, grading and policies |
| `lessons/` | One page per lesson, with a slot for the lesson recording |
| `assets/style.css` | Site stylesheet |
| `tools/build_site.py` | Generates the site pages |
| `tools/transcribe.py` | Transcribes lecture audio |

## Building the site

```
python tools/build_site.py
```

This regenerates `index.html`, `course-details.html` and every page under `lessons/`.
Edit the content in `tools/build_site.py` and in `SYLLABUS.md` together, then rebuild.

## Status

Draft, under construction. Lesson recordings are not yet available and each lesson page
carries a placeholder until its video is published.

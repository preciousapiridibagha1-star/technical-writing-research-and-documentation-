# Portfolio Structure and Build Plan

**Owner:** Precious Apiri Dibagha  
**Working branch:** `portfolio/structure-and-cleanup`  
**Status:** Active build; existing material is being reviewed and moved carefully.

## Portfolio positioning

**Precious Apiri Dibagha — Technical Writer & Researcher**

Primary focus: **AI systems and software documentation**  
Additional focus: **technical research, cloud infrastructure, open source, digital labour and global mobility**

The portfolio will show real examples of technical writing, research and system design. It will be honest about what is complete, in progress, conceptual, tested or deployed.

## Agreed repository structure

This is the structure we will follow:

```text
/
├── README.md
├── projects/
│   ├── vantage-automata/
│   │   ├── README.md
│   │   ├── architecture/
│   │   ├── requirements/
│   │   ├── workflows/
│   │   ├── implementation/
│   │   ├── testing/
│   │   └── user-guide/
│   ├── jarvis-ai/
│   │   ├── README.md
│   │   ├── architecture/
│   │   ├── agent-documentation/
│   │   ├── system-workflows/
│   │   └── technical-specifications/
│   └── cloud-infrastructure-and-open-source/
│       ├── README.md
│       ├── project-overviews/
│       └── technical-documentation/
├── research/
│   ├── talent-paradox/
│   ├── ai-job-search-platforms/
│   └── research-methodology/
├── technical-guides/
│   ├── README-guides/
│   ├── FAQs/
│   ├── user-guides/
│   └── documentation-examples/
├── contributions/
│   └── open-source/
└── learning-and-development/
    └── technical-skills/
```

Folders will be added when there is real content for them. Git does not track empty folders, so we will use short README or index files where a folder needs an explanation before its first full document is ready.

## What belongs where

- **Vantage Automata:** the main practical MVP. Its documentation will cover requirements, architecture, workflow, implementation notes, tests and a user guide. The first demonstrable slice is: instruction → AI interpretation → proposed action → human approval or rejection → safe test action → result and audit log.
- **Jarvis AI:** the broader multi-agent business-system concept. We will document the diagrams, agent roles, system workflows and technical specifications. We will not describe integrations or deployment as working until they have been implemented and tested.
- **Cloud infrastructure and open source:** project overviews and technical material connected to the existing cloud infrastructure/open-source work.
- **Research:** The Talent Paradox, the AI Job Search Platforms research and a transparent account of research methods and source checking.
- **Technical guides:** the existing software overview, FAQ, user-guide and documentation examples. These are early samples and will be revised for accuracy, scope and usefulness.
- **Contributions:** actual open-source contributions and documentation reviews. Planned contributions will not be presented as completed.
- **Learning and development:** practical technical learning tied to work shown in the repository, not a padded list of courses.

## Existing material to preserve and reorganise

The repository already contains a main README, four cloud-AI documentation samples, a documentation review report, The Talent Paradox report, and earlier cloud infrastructure/open-source research material. The current documentation samples are generic rather than documentation for a named, verified product. We will label that scope clearly unless we later choose and research a specific product.

Some existing filenames contain accidental trailing newline characters. We will correct those paths while preserving the file contents and updating links.

## Build order

1. Establish this agreed structure and replace the root README with a useful portfolio landing page.
2. Create the Vantage Automata project home and define its first MVP slice.
3. Create the Jarvis AI project home and record the current system concept without inventing implementation details.
4. Move and improve the existing documentation samples and cloud/open-source material.
5. Review and strengthen The Talent Paradox and the AI Job Search Platforms research.
6. Add learning records and genuine open-source contributions as they happen.
7. Review all links, claims and project-status labels before merging the working branch into `main`.

## Quality rules

- Use clear, natural language. Explain technical ideas fully without dressing them up in unnecessary jargon.
- Separate facts, decisions, assumptions and recommendations.
- Cite sources for external factual claims and record when important sources were checked.
- Label work as **concept**, **specified**, **in progress**, **prototyped**, **tested** or **deployed**, as appropriate.
- Do not claim that a workflow works until it has been run and tested.
- Use mock data and safe test actions before connecting real accounts or taking consequential actions.
- Do not claim an open-source contribution until there is a real contribution link.
- Keep the work on this branch until it has been reviewed. The default branch remains untouched.

This is the working structure and build plan, not a claim that every listed folder or project is already complete.

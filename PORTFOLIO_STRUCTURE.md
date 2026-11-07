# Portfolio Structure and Cleanup Plan

**Owner:** Precious Apiri Dibagha  
**Working branch:** `portfolio/structure-and-cleanup`  
**Status:** Proposed structure; existing work is being preserved while it is reviewed.

## Portfolio positioning

**Precious Apiri Dibagha — Technical Writer & Researcher**

Primary focus: **AI systems and software documentation**  
Additional areas: **technical research, open source, digital labour and global mobility**

This portfolio will bring together evidence of clear technical communication, careful research, practical system documentation and learning through real projects. It will distinguish completed work from concepts, work in progress and proposed contributions.

## Proposed repository structure

```text
/
├── README.md
├── PORTFOLIO_STRUCTURE.md
├── technical-documentation/
│   ├── cloud-ai-assistants/
│   │   ├── README.md
│   │   ├── product-overview.md
│   │   ├── faq.md
│   │   └── user-guide.md
│   └── documentation-quality/
│       └── documentation-review.md
├── systems/
│   ├── vantage-automata/
│   │   ├── README.md
│   │   ├── requirements/
│   │   ├── architecture/
│   │   ├── workflows/
│   │   ├── implementation/
│   │   └── testing/
│   └── jarvis-ai/
│       ├── README.md
│       ├── architecture/
│       ├── agent-specifications/
│       └── workflows/
├── research/
│   ├── talent-paradox/
│   │   ├── README.md
│   │   └── report.md
│   ├── cloud-ai-assistants/
│   │   └── research-brief.md
│   └── ai-job-search-platforms/
│       └── README.md
├── open-source/
│   ├── contributions/
│   └── documentation-reviews/
└── learning/
    └── technical-development/
```

## Why these sections exist

- **Technical documentation:** groups the product overview, FAQ, user guide and documentation audit as one coherent sample set. The current samples describe a general cloud AI assistant rather than a named, verified product; that limitation will be made clear and the examples will be improved.
- **Systems:** gives Vantage Automata and Jarvis AI separate project spaces. Vantage Automata remains the practical MVP priority in the governing Master Portfolio, Learning & Fellowship Plan. Jarvis AI is documented as a related system vision and MVP concept, not presented as a deployed product unless implementation evidence supports that claim.
- **Research:** separates policy research from technical research. The Talent Paradox will receive a source and argument review before it is presented as a fellowship-quality policy paper.
- **Open source:** records real contributions and reviews only. Planned contributions will not be described as completed.
- **Learning:** records relevant technical learning and evidence of applied practice without turning the portfolio into a list of courses.

## Existing files found at the repository root

The current default branch contains:

- `README.md`
- `project-1-software-overview.md` — the actual GitHub path currently ends with a newline character.
- `project-2-faq-document.md`
- `project-3-user-guide.md` — the actual GitHub path currently ends with a newline character.
- `project-4-research-brief.md` — the actual GitHub path currently ends with a newline character.
- `project-5-documentation-review-report.md`
- `the-talent-paradox-report.md` — the actual GitHub path currently ends with a newline character.

The newline characters in four filenames are accidental path issues and should be corrected during the migration. Their contents must be preserved.

## Review findings to address

1. The main README currently mixes the portfolio introduction with a long description of The Talent Paradox. It should become a concise landing page with clear links to projects and research.
2. The current documentation samples are useful starting points, but they are generic and make broad technical claims. They need clearer scope, more precise explanations, sources where factual claims require them, and explicit limitations.
3. The documentation review currently awards every item a Grade A and says the repository is fully verified. Those conclusions are not supported by the review evidence and must be replaced with specific, traceable findings.
4. The Talent Paradox needs stronger sourcing, careful distinction between migration and remote digital work, and a more balanced policy analysis. Its current wording sometimes makes broad claims without evidence.
5. The repository should clearly label each item as a completed sample, work in progress, concept, or planned contribution.

## Migration principles

- Preserve the existing files and their contents before changing paths.
- Correct the four filenames that contain trailing newline characters.
- Move documents into the structure above and update all internal links.
- Do not create empty folders just to make the tree look complete; add project folders as their content is ready.
- Do not claim that Vantage Automata or Jarvis AI is deployed, integrated or production-ready without evidence.
- Do not claim an open-source contribution has been made until a real contribution is linked.
- Keep this portfolio as one evidence base for the eight fellowships in the Master Portfolio, Learning & Fellowship Plan. Tailor application materials separately to each opportunity.

## Immediate work sequence

1. Finish the inventory and quality review of all existing repository files.
2. Migrate and rename the existing files on this working branch, preserving their content.
3. Rewrite the root README as the portfolio landing page and add project-level introductions.
4. Improve the technical documentation samples and replace unsupported audit grades with a transparent review.
5. Review and strengthen The Talent Paradox before featuring it prominently.
6. Add Vantage Automata documentation in line with the Master Portfolio, Learning & Fellowship Plan, keeping the practical MVP as the priority.
7. Document Jarvis AI separately and accurately as a system concept until implementation evidence exists.
8. Review the branch changes before merging them into `main`.

## Scope note

This file is a working organisation plan, not a claim that all listed projects or folders already exist. The working branch keeps these initial changes separate from the current default branch while the repository is improved.

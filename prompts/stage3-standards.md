# Stage 3: standards, in one run

Run after docs/toc.md is frozen and voice/sample.md exists.

```
Read voice/sample.md, docs/buyer.md, docs/toc.md, and CLAUDE.md.

1. docs/chapter-template.md
   Sections: opening scene, the business problem, core explanation, worked
   example, what this looks like inside a real organization, the misconception
   people hold, the callback (which earlier concept this chapter reuses), the
   summary, one question the reader should ask at work on Monday.
   Word budget per section, totalling 3,800 to 4,200. Mark optional sections.

2. docs/terminology.md
   Every term the frozen TOC forces us to use: chosen spelling, capitalization,
   vendor naming convention, and one approved short definition per term so no
   two chapters define it differently.

3. docs/concept-registry.md
   Table: concept | first introduced | revisited in | approved one-line
   definition. Prefill from the TOC with the chapter each concept belongs to.

4. docs/case-study-registry.md
   Table: company | industry | concept illustrated | chapters | source URL |
   fact-checked date | borrowed or first-hand. Prefill the borrowed candidates
   and leave the first-hand rows empty for the author.

5. .vale.ini and .vale/styles/Book/
   Translate the CLAUDE.md voice rules and prohibited language into Vale rules.
   At minimum: em dashes, adverbs ending in -ly, the "not X, it's Y" pattern,
   corporate jargon list, vendor evangelism list, exam-prep phrasing. Use
   existence and substitution rule types. Set severity to warning, not error.

6. setup.sh
   Install and verify Vale and Pandoc. Leave Graphviz, the Python diagrams
   library, and mermaid-cli commented out with a note that they are needed at
   the diagram stage. Run the script and report what failed.

Update CLAUDE.md's voice section with three concrete rules you extracted from
voice/sample.md that are not already listed. Quote the sentence each rule comes
from. Do not write chapter content.
```

Edit docs/terminology.md yourself after this runs.

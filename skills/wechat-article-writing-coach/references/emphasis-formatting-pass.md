# Emphasis Formatting Pass

Run this pass only after the article's claims, evidence, structure, compression, reader flow, voice, and AI-flavor review are stable. Its purpose is to help a mobile reader see the article's reasoning path. It is not a sentence-polishing or gold-quote generation stage.

## Core Decision

Treat bold as navigation, not decoration.

A sentence earns bold only when it performs at least one necessary structural function:

- states the article's central judgment after the reader has enough context;
- names the mechanism that explains the opening problem;
- marks a real turn from diagnosis to method, consequence, or decision;
- gives the reader the key action or question the article has earned;
- closes the article by resolving its central question without merely repeating the title.

No sentence is bold by default. A valid pass may return zero bold placements.

## Selection Tests

For every candidate, ask:

1. Does it add information, or only announce that the surrounding material is important?
2. Is it supported by a concrete scene, action, source, or prior reasoning within the nearby paragraphs?
3. Does it perform a different function from the other bold sentences?
4. If a mobile reader scans only the bold sentences in order, can they recover the article's main progression rather than a pile of interchangeable slogans?
5. Would the sentence still deserve to exist if the bold formatting were removed?

Reject the candidate when any of the following is true:

- it is a generic bridge such as `这值得我们深思` or `真正重要的是` without new content;
- it relies on symmetry, contrast, repetition, or `不是 A，而是 B` to sound sharp but lacks nearby evidence;
- it paraphrases a heading or repeats another bold sentence;
- it is generic encouragement that could be moved unchanged into another article;
- it turns a cautious source claim into a stronger conclusion;
- it is included only because the previous several paragraphs contain no bold text.

Apply `ai-flavor-concreteness-gate.md` again to every retained candidate. An abstract screenshot-ready sentence does not become acceptable merely because it is visually emphasized.

## Density Guidance

Use density as a ceiling and review prompt, never as a quota:

- under 1,200 Chinese characters: usually 2-3 placements;
- 1,200-2,200 characters: usually 3-5 placements;
- 2,200-3,500 characters: usually 4-7 placements;
- longer articles: increase only when a new section introduces a genuinely new reasoning step.

Prefer fewer placements when images, subheadings, lists, or short standalone paragraphs already provide visual rhythm. Avoid bold in consecutive paragraphs unless the two sentences form one deliberate contrast that the article has fully supported.

## Formatting Rules

- Bold the smallest complete sentence or clause that carries the function; do not bold an entire long paragraph.
- Do not bold headings merely to increase visual weight.
- Do not automatically bold research names, book titles, statistics, or source attributions. Emphasize evidence only when that exact fact is necessary for the reader's decision.
- Split a candidate into a standalone paragraph only when doing so also improves rhythm and comprehension, not solely to make it look quotable.
- Preserve the user's spoken cadence. Do not rewrite a plain, accurate sentence into a balanced slogan just to create emphasis.

## Final Read

After applying Markdown bold:

1. read the full article once without looking only at the bold text;
2. scan only headings, images, and bold sentences as a mobile reader would;
3. remove any bold placement that interrupts the emotional scene, overstates the evidence, duplicates another point, or makes the article resemble a quote-card collection;
4. return the fully formatted article, not a separate `金句合集`, unless the user explicitly requests one.

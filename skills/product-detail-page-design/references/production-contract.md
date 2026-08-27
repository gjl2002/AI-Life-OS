# Production Contract

## Source of truth

Keep all visible copy in one structured content object or Markdown document before image generation. Reuse that source for prompts, image edits, overlays, and revisions.

## Default production output

Create a width-consistent, height-flexible ordered image set. The default deliverable is finished PNG/JPG images, not HTML/CSS.

Requirements:

- one planned source of truth for copy, hierarchy, and visual direction per image
- one locked list of allowed visible copy before generation
- choose width from the delivery channel; use 1080px when no platform constraint is supplied
- calculate height from content rather than forcing one aspect ratio
- typical heights may range from 1350px to 2400px, but these are guidance rather than limits
- allow adjacent images to use different heights when their persuasion jobs require different density
- shared visual system across all images
- accurate Chinese text, either generated correctly or repaired/composited afterward
- no unsupported extra claims, numbers, badges, prices, discounts, proof, or benefits added by the image model
- no external dependency unless already available or explicitly chosen
- meaningful alt text
- no overflow or clipped content

Production modes:

- `full-raster image`: generate/design the full high-fidelity commercial image, then inspect and iterate.
- `image edit / repair`: edit the generated image to fix text, composition, spacing, or detail problems.
- `hybrid composite`: generate the visual scene, background, or system object first; add exact Chinese copy as a separate layer only when text repair is necessary.
- `deterministic layout`: use HTML/CSS, SVG, Canvas, Figma, slides, or similar methods only when the user explicitly requests HTML, editable source, web components, or deterministic layout.

Do not use deterministic layout as the default merely because it is easier to control text. The user's default expectation is finished images.

## Image-set export

For marketplace or social delivery:

1. Produce each numbered image at the target width and its content-driven height.
2. Inspect every image at mobile scale.
3. Export numbered files such as `01-hero.png`, `02-conflict.png`.
4. Create a contact sheet for sequence review.
5. Keep the art direction, prompts, or revision notes used to create each image.

Do not accept garbled generated Chinese copy.
Do not accept generated images that invent unconfirmed commercial information.
Do not concatenate the set into one long image unless the user explicitly requests an additional stitched preview.

## Visual-role mapping

- hero: dominant outcome and product identity
- cognitive conflict: contrast or before/after logic
- failed path: diagnostic cards
- mechanism: flow or flywheel diagram
- proof: evidence-led metrics, artifacts, or quotes
- audience: self-selection cards
- outcomes: deliverable or transformation cards
- blueprint: system map
- curriculum: timeline or staged path
- bundle: stacked value inventory
- price: clean decision panel

## Quality gate

Reject the artifact if:

- the hero could describe many unrelated AI courses
- tools replace the product mechanism
- curriculum appears before the buyer understands the need
- claims exceed the supplied evidence
- generated art contains garbled critical text that has not been repaired
- generated art invents student counts, tool counts, module counts, SOP counts, prices, discounts, bonuses, scarcity, proof, or guarantees
- images repeat information without advancing the argument
- any individual image requires zooming
- one image tries to explain several unrelated ideas
- the delivered result is only one long image
- CTA lacks an explicit next action
- CTA looks like a generic cheap gradient button, low-end app UI, sale sticker, or decorative pill rather than a premium conversion control
- the visual result is technically readable but clearly weaker than the supplied benchmark references

# Visual Production Modes

Use this file to choose the production path. The default output is finished raster images. The goal is not merely readable layout; the output must feel like a high-value commercial product-detail image set.

## Default mode: visual-first raster production

For promotional covers, hero pages, mechanism pages, proof pages, and normal product-detail pages, default to image-first production:

1. Write the page copy and hierarchy first.
2. Define the visual shot: composition, focal object, lighting, material, background, perspective, and negative space.
3. Create a locked copy list: exact text that may appear in the image.
4. Generate or design the page as a high-fidelity raster poster/image.
5. Inspect the result for commercial impact, legibility, brand fit, text accuracy, and unsupported extra claims.
6. Use image editing or text repair only if needed.
7. Iterate visually before calling the page done.

Use this mode when the user provides strong visual references or says the output should match a benchmark, poster, sales page, cinematic look, commercial design, or “高级感.”

## Text strategy

Chinese text accuracy matters, but do not let text precision force a flat HTML look.

Before generation, define:

- `allowed copy`: exact headline, subtitle, labels, CTA, and confirmed facts that may appear
- `forbidden copy`: unconfirmed numbers, prices, discounts, student counts, bonuses, testimonials, guarantees, scarcity, module counts, tool counts, SOP counts, or invented labels

If a generated image adds unsupported copy, numbers, badges, prices, benefits, or modules, reject or edit it. Do not explain it away as “visual placeholder.”

Choose one of three text strategies:

- `full-raster`: Default. Use an image model to render the whole page, including text. Inspect and repair if the Chinese is wrong.
- `hybrid-composite`: Generate the visual background, objects, atmosphere, and composition first; then add exact Chinese text as a separate layer using a design/compositing method.
- `deterministic-layout`: Use HTML/CSS, SVG, Canvas, Figma, slides, or another deterministic layout method only when the user explicitly asks for HTML, editable source, web components, or exact deterministic layout.

Default for high-impact hero pages: `full-raster image generation`, followed by image edit/repair if necessary.

## HTML/CSS is opt-in only

Do not use plain HTML/CSS unless the user explicitly asks for it. Especially avoid it when:

- the user is benchmarking cinematic, poster-like, or high-end commercial visuals
- the page needs dramatic lighting, atmosphere, 3D depth, metallic/glass typography, or realistic product imagery
- the first draft would look like a web mockup rather than a finished promotional image
- the reference image relies on photographic/cinematic texture that CSS cannot reproduce well

HTML/CSS can be used only as an explicitly requested source format or emergency text-compositing aid. It should never be the default production path.

## High-impact hero recipe

For first-screen result pages, use a bold commercial composition:

- one monumental headline or product identity
- one dominant cinematic visual field, product object, system metaphor, or atmospheric scene
- strong depth: foreground title, midground system/product object, background environment
- controlled lens flare, rim light, glow, reflection, particles, or glass/metal material
- a small number of sharp proof/benefit blocks
- minimal explanatory copy; push dense explanation to later images
- clear CTA or next-step panel only if it does not weaken the hero
- CTA should feel like a premium interface control, not a cheap gradient sticker: restrained size, elegant border/light, strong spacing, and one clear action.

The hero should be sellable as a standalone poster, not merely a readable information card.

## Visual quality gate

Reject or iterate if:

- the page looks like a generic web section, slide, or dashboard instead of a finished commercial image
- the typography has no mass, depth, contrast, or focal hierarchy
- the background feels like decorative gradient rather than a designed scene
- the composition lacks a single dominant visual moment
- text is clear but the page has weak desirability
- the result is less visually compelling than the supplied benchmark references
- the image invents numbers, rights, modules, prices, guarantees, discounts, or proof not present in the locked copy
- the CTA looks like a generic template button, cheap capsule, sale sticker, or low-end app UI

## Output contract

For visual-first work, deliver:

- the final numbered PNG/JPG image
- the prompt or art direction used to create it
- a short inspection note listing what was checked and what still needs iteration

For full product-detail sets, keep the image sequence consistent even if individual pages use different production modes.

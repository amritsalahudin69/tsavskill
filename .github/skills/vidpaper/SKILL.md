---
name: vidpaper
description: >
  Paper Cutout visual guidance for user-defined scenes and animations.
  Use when a user requests layered, tactile cut-paper presentation.
---

# Paper Cutout

## Identity and status

- Stable VSkills skill ID: `style.paper-cutout`
- AI agent project skill name and directory: `vidpaper`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidpaper` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual language

Apply a coherent cut-paper treatment to the user's chosen content:

- Build forms from distinct overlapping paper pieces with readable silhouettes, cut edges, and layer boundaries. Avoid reducing the style to unlayered flat vector shapes.
- Suggest paper with subtle grain, fibers, edge variation, folds, or handmade irregularity. Keep texture restrained enough that important shapes and details remain clear.
- Use soft, local shadows between offset layers to establish tactile depth and separation. Keep shadow direction and strength consistent with the scene lighting.
- Choose a limited but expressive palette for the user's scene; do not prescribe fixed colors.
- Construct characters from separable paper components. Use clear pivots or visible joints when parts articulate, and keep overlaps and contact readable through motion.
- Treat environments as layered collage: order background, midground, subjects, and foreground deliberately, with occlusion that agrees with the chosen view.
- Keep perspective and scale consistent across characters, props, paths, and scenery. A paper construction does not excuse incompatible viewpoints or unsupported movement.
- Use deliberate cutout timing, held poses, or measured increments when they suit the request. Slight hand-worked variation is optional; do not require jitter, random deformation, strings, or a particular animation cadence.

No character, environment, action, story, palette, duration, aspect ratio, loop, camera, or output format is a style default.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character/source inputs, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Apply Paper Cutout presentation without replacing or narrowing scene content. Do not copy example-specific characters, events, props, framing, or timing.

Preserve canonical source identity and required detail when supplied. If a paper simplification would erase required identity or function, retain that information and adapt the cut-paper treatment around it.

## Renderer and production integration

Paper Cutout is a visual style, not a renderer requirement. Canvas 2D is suitable for layered drawn puppets and collage when it meets the scene requirements; use Three.js when genuine volumetric geometry is required. A style request does not override an explicitly selected renderer.

Compose this style with `cap.scene-production` when HTML implementation is requested. Keep scene content, production capability, renderer, and visual style distinct. The capability provides implementation guidance, not automatic generation.

## Validation

Assess evidence independently:

- **Source/build:** HTML and JavaScript syntax, renderer-appropriate structure, declared dependencies, local assets, and run instructions.
- **Structure:** distinct paper layers, edge and shadow treatment, composition, depth ordering, articulated components, and spatial relationships match the requested scene.
- **Runtime:** load the artifact in a real browser and confirm the selected rendering context initializes without critical errors.
- **Visual:** inspect paper texture, cut edges, layer separation, palette, silhouette readability, perspective, and preservation of requested content.
- **Motion:** observe requested actions at distinct times and verify articulation, contact, occlusion, timing, and endpoint/loop behavior.
- **Delivery:** confirm paths, renderer, dependencies, and limitations.

Static validation does not prove browser rendering, visual appearance, or observed motion. Report unobserved checks as `NOT_TESTED`.

`TSA_VIDPAPER_DISCOVERY_MARKER: VIDPAPER_CHILD_2E_4`

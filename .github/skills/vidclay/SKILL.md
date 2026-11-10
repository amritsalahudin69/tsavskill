---
name: vidclay
description: >
  Claymation visual guidance for user-defined scenes and animations.
  Use when a user requests handmade sculpted-clay presentation.
---

# Claymation

## Identity and status

- Stable VSkills skill ID: `style.claymation`
- Copilot project skill name and directory: `vidclay`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidclay` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual direction

Apply a coherent handmade clay-animation treatment to the user's chosen content:

- Use soft, rounded, volumetric forms with slightly irregular sculpted silhouettes. Preserve recognizable proportions and required object function.
- Favor clay-like materials with restrained gloss and tactile surface variation. Subtle fingerprints, seams, or tool marks may be used where appropriate; keep them intentional and legible.
- Use warm, controlled lighting and soft highlights to describe form without making surfaces look like smooth plastic toys.
- Construct characters from readable forms and preserve facial features. Give articulated limbs believable pivots and contact; keep the character's identity and action clear.
- Maintain coherent scale, camera perspective, ground contact, and spatial interaction among characters, props, and supports.
- Use deliberate stop-motion-inspired pose timing or held poses when compatible with the request. Timing may feel handcrafted without mechanical jerkiness; do not add mandatory frame jitter or uncontrolled frame-to-frame deformation.
- Keep any irregular geometry deterministic and subtle. Avoid excessive random deformation, flicker, or surface changes that undermine continuity.

No character, environment, story, palette, duration, aspect ratio, loop, or output format is a style default.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character/source inputs, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Apply Claymation presentation without replacing or narrowing scene content. Do not copy example-specific characters, events, or props. Preserve canonical source identity and required detail when supplied.

## Renderer and production integration

Claymation is a visual style, not a renderer requirement. Use Three.js when the requested scene needs genuine volume, articulated 3D geometry, or a spatial camera. Do not use flat 2D substitutes for required 3D forms, and do not imitate smooth plastic-toy construction when a handmade clay surface is requested. Honor an explicitly selected renderer when it can meet the scene requirements.

Compose this style with `cap.scene-production` when HTML implementation is requested. Keep scene content, production capability, renderer, and visual style distinct. The capability provides implementation guidance, not automatic generation.

## Validation

Assess evidence independently:

- **Source/build:** HTML and JavaScript syntax, renderer-appropriate structure, declared dependencies, local assets, and run instructions.
- **Structure:** volumetric forms, character construction, articulation pivots, support/contact, scale, and spatial relationships match the requested scene.
- **Runtime:** load the artifact in a real browser and confirm the selected rendering context initializes without critical errors.
- **Visual:** inspect handmade form, clay material response, surface detail, facial readability, composition, and preservation of requested content.
- **Motion:** observe requested actions at distinct times and verify articulated contact, held-pose timing, continuity, and endpoint/loop behavior.
- **Delivery:** confirm paths, renderer, dependencies, and limitations.

Static validation does not prove browser rendering, visual appearance, or observed motion. Report unobserved checks as `NOT_TESTED`.

`TSA_VIDCLAY_DISCOVERY_MARKER: VIDCLAY_CHILD_2E_3`

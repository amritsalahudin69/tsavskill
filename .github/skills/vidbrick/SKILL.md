---
name: vidbrick
description: >
  Toy Brick visual guidance for user-defined scenes and animations.
  Use when a user requests modular, glossy plastic-brick presentation.
---

# Toy Brick

## Identity and status

- Stable VSkills skill ID: `style.toy-brick`
- Copilot project skill name and directory: `vidbrick`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidbrick` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual direction

Apply a coherent toy-brick construction treatment to the user's chosen content:

- Build compatible forms from modular interlocking-brick geometry, with visible studs, seams, and consistent module proportions where appropriate.
- Use a consistent dimensional system for brick bodies, stud spacing, and stack heights. Keep joints and connections visually plausible; do not scatter studs onto unrelated surfaces without reason.
- Favor molded plastic materials with clear, controlled highlights and reflections. Avoid metallic or mirror-like response unless explicitly requested.
- Use toy-scale proportions and readable silhouettes while preserving the identity and function of required subjects.
- Extend the construction language to environments and props when suitable; maintain clear paths, support, contact, and spatial relationships.
- Keep articulation legible by separating moving components at meaningful pivots. Derive movement from the requested action and timeline; stop-motion-like stepping or stiffness is optional, not a default.
- Use a camera and lighting that reveal the brick-built structure without sacrificing scene readability. Composition, depth, and object placement must remain coherent.

No particular brick brand, character, story, environment, palette, duration, aspect ratio, loop, or output format is a style default.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character/source inputs, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Apply toy-brick presentation without replacing or narrowing scene content. Do not copy proprietary toy sets, branded logos, or commercial models. Preserve canonical source identity and required detail when supplied.

## Renderer and production integration

Toy Brick is a visual style, not a renderer requirement. Use Three.js when the requested scene needs genuine volume, articulated 3D geometry, or a spatial camera; use Canvas 2D only when it satisfies the actual scene requirements. A style request does not override an explicitly selected renderer.

Compose this style with `cap.scene-production` when HTML implementation is requested. Keep scene content, production capability, renderer, and visual style distinct. The capability provides implementation guidance, not automatic generation.

## Validation

Assess evidence independently:

- **Source/build:** HTML and JavaScript syntax, renderer-appropriate structure, declared dependencies, local assets, and run instructions.
- **Structure:** brick modules, studs/seams, consistent scale, pivots, articulation, contact, and spatial relationships match the requested scene.
- **Runtime:** load the artifact in a real browser and confirm the selected rendering context initializes without critical errors.
- **Visual:** inspect material response, brick construction, silhouette readability, composition, and preservation of requested content.
- **Motion:** observe requested actions at distinct times and verify articulation, contact, timing, and endpoint/loop behavior.
- **Delivery:** confirm paths, renderer, dependencies, and limitations.

Static validation does not prove browser rendering, visual appearance, or observed motion. Report unobserved checks as `NOT_TESTED`.

`TSA_VIDBRICK_DISCOVERY_MARKER: VIDBRICK_CHILD_2E_2`

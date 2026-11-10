---
name: vidanime
description: >
  Retro Anime visual guidance for user-defined scenes and animations.
  Use when a user requests classic hand-drawn cel-animation presentation.
---

# Retro Anime

## Identity and status

- Stable VSkills skill ID: `style.retro-anime`
- Copilot project skill name and directory: `vidanime`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidanime` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual language

Apply a coherent hand-drawn cel-animation treatment to the user's chosen content:

- Use clean, expressive ink outlines with deliberate line-weight variation and readable silhouettes.
- Favor flat color fields and a small number of controlled shadow shapes. Keep cel-shading tones distinct and consistent with the lighting; avoid unnecessary gradients on characters.
- Give environments a painted-background sensibility through considered color transitions, atmospheric depth, and layered scenery, while keeping important subjects legible.
- Use warm, cinematic color treatment when suitable for the scene, not as a fixed palette.
- Construct characters with consistent anatomy, recognizable facial features, and a view convention suited to the camera. Preserve facial readability through turns and pose changes.
- Plan animation with clear key poses, holds, and controlled transitions. Add secondary motion to hair, clothing, or accessories when it supports the action and remains attached to the character.
- Layer background, subjects, and foreground deliberately. Maintain consistent perspective, scale, contact, and occlusion across the composition.
- Optional subtle film grain, restrained softness, or period-inspired presentation may support the intended mood. Avoid excessive jitter, random flicker, or effects that reduce clarity.

No decade, character, environment, story, palette, duration, aspect ratio, frame rate, camera, loop, or output format is a style default. Do not imitate a specific copyrighted franchise or reproduce proprietary characters.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character/source inputs, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Apply Retro Anime presentation without replacing or narrowing scene content. Do not copy example-specific characters, events, props, framing, or timing.

Preserve canonical source identity and required detail when supplied. If a stylized simplification would erase identity, function, or required facial detail, retain that information and adapt the style around it.

## Renderer and production integration

Retro Anime is a visual style, not a renderer requirement. Canvas 2D is suitable for drawn cel animation and painted backgrounds when it meets the scene requirements; use Three.js when genuine volumetric geometry is required. A style request does not override an explicitly selected renderer.

Compose this style with `cap.scene-production` when HTML implementation is requested. Keep scene content, production capability, renderer, and visual style distinct. The capability provides implementation guidance, not automatic generation.

## Validation

Assess evidence independently:

- **Source/build:** HTML and JavaScript syntax, renderer-appropriate structure, declared dependencies, local assets, and run instructions.
- **Structure:** character construction, facial readability, key poses, secondary-motion attachment, perspective, and layer ordering match the requested scene.
- **Runtime:** load the artifact in a real browser and confirm the selected rendering context initializes without critical errors.
- **Visual:** inspect ink work, cel-shadow regions, painted-background treatment, composition, anatomy, and preservation of requested content.
- **Motion:** observe requested actions at distinct times and verify pose transitions, contact, secondary motion, head/face continuity, and endpoint/loop behavior.
- **Delivery:** confirm paths, renderer, dependencies, and limitations.

Static validation does not prove browser rendering, visual appearance, or observed motion. Report unobserved checks as `NOT_TESTED`.

`TSA_VIDANIME_DISCOVERY_MARKER: VIDANIME_CHILD_2E_5`

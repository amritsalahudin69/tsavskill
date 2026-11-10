---
name: vidcomic
description: >
  Comic Book visual guidance for user-defined scenes and animations.
  Use when a user requests expressive inked, graphic-novel presentation.
---

# Comic Book

## Identity and status

- Stable VSkills skill ID: `style.comic-book`
- Copilot project skill name and directory: `vidcomic`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidcomic` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual language

Apply a coherent comic-book treatment to the user's chosen content:

- Use bold, ink-like contours with purposeful line-weight variation to define silhouettes, overlaps, and focal details.
- Favor a compact, expressive palette and clear value grouping. Use flat graphic fills or restrained cel shading where suitable; do not impose fixed colors.
- Use halftone, Ben-Day-style dot fields, print grain, or limited offset-color effects selectively to suggest printed texture without obscuring important forms.
- Keep silhouettes and action readable at the intended size. Use contrast, simplified shapes, and graphic shadow blocks to preserve recognition and depth.
- Compose with deliberate diagonals, foreground framing, or panel-like divisions when they support the requested camera and action. Panels and borders are optional.
- Keep graphic simplification, overlaps, and motion cues consistent with the user's chosen viewpoint and spatial relationships. Use intentional perspective distortion only when it supports the requested composition and remains readable; Comic Book presentation does not prescribe a camera angle.
- Use speed lines, motion accents, or impact emphasis only when they clarify requested movement or an existing event. Do not invent an impact, event, or action to justify an effect.
- Speech bubbles, captions, sound effects, HUD elements, and text overlays are not defaults; use them only when requested or clearly useful and compatible with the user's constraints.
- For animation, use elapsed time and make stylized timing or held poses serve the requested action without making playback frame-rate dependent.

No character, story, environment, palette, line style, panel layout, duration, aspect ratio, or action is a style default.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character/source inputs, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Apply comic-book presentation without replacing or narrowing scene content. Do not add characters, props, events, dialogue, sound effects, or captions merely because they occur in a reference example.

Preserve canonical source identity and compatible runtime conventions when supplied. If a graphic simplification would erase required identity or source detail, keep that detail legible and adapt the style around it.

## Renderer and production integration

Comic Book is a visual style, not a renderer requirement. Use Canvas 2D for naturally two-dimensional scenes when appropriate; use Three.js when the user's scene requires genuine 3D. A style request does not override an explicitly selected renderer or justify replacing required 3D characters with flat approximations.

Compose this style with `cap.scene-production` for a requested HTML animation, keeping production capability, renderer, and visual style distinct. The capability provides guidance for Three.js and Canvas 2D; it does not automatically generate a scene. Its Python validator performs static structural checks only and does not prove browser rendering, visual appearance, or motion.

## Validation

Assess evidence independently:

- **Source/build:** HTML and JavaScript syntax, renderer-appropriate structure, declared dependencies, local assets, and run instructions.
- **Runtime:** load the artifact in a real browser and confirm the selected rendering context initializes without critical errors.
- **Visual:** inspect ink contours, palette and shading, halftone/print treatment, silhouette clarity, composition, and preservation of requested content.
- **Motion:** observe requested actions at distinct times and verify timing, readability, and endpoint/loop behavior.
- **Delivery:** confirm paths, renderer, dependencies, and limitations.

Static source checks do not prove browser rendering, visual quality, or observed motion. Report unobserved checks as `NOT_TESTED`; report an unsupported production or validation path as `BLOCKED` or `NOT_IMPLEMENTED`.

`TSA_VIDCOMIC_DISCOVERY_MARKER: VIDCOMIC_CHILD_2E_1`

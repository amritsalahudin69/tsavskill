---
name: vidpixel
description: >
  Pixel Art visual guidance for user-defined scenes and animations.
  Use when a user requests crisp, grid-based pixel-art presentation.
---

# Pixel Art

## Identity and status

- Stable VSkills skill ID: `style.pixel-art`
- Copilot project skill name and directory: `vidpixel`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidpixel` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested; its renderer guidance supports Three.js and Canvas 2D.

This skill provides visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual language

Apply a deliberate pixel-art treatment to the user's chosen content:

- Build recognizable silhouettes from crisp, intentional pixel clusters. Use hard edges and purposeful detail; avoid accidental blur, anti-aliasing, soft gradients, or noisy single-pixel decoration that weakens readability.
- Choose a logical pixel grid and canvas resolution appropriate to the requested output. Align shapes and movement to that grid where practical; avoid fractional coordinates that create inconsistent edge softness.
- Select a compact palette that supports the scene's lighting, depth, and readability. Palette size and colors are scene-specific, not fixed defaults.
- Render at the logical resolution, then enlarge with nearest-neighbor sampling. Disable canvas smoothing for scaled draws and use browser pixelated rendering for a CSS-scaled canvas. Prefer integer display scaling when the requested viewport permits it.
- Use clear value separation and restrained outlines or shading to distinguish important forms without changing their identity or adding unrequested content.
- Layer backgrounds and foregrounds to establish depth. Use parallax only when it supports the requested camera and action; keep relative movement subtle and consistent with scene perspective.
- For sprite animation, author explicit frames or sprite-sheet regions. Select frames from elapsed time or a requested animation clock, not from the number of render callbacks. Keep frame cadence readable and motion aligned to the pixel grid.
- Use elapsed-time-based motion for object travel and other continuous actions. Snap positions to the chosen grid when that supports the look; do not make behavior frame-rate dependent.

No character, environment, palette, pixel resolution, camera, duration, aspect ratio, HUD, or action is a style default.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character/source inputs, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Apply pixel-art presentation without replacing or narrowing scene content. Do not invent characters, stories, objects, text, interface elements, or actions merely because they occur in a reference example.

Preserve canonical source identity and compatible runtime conventions when supplied. If a requested element cannot be expressed faithfully with a pixel-art treatment, explain the limitation rather than silently removing or substituting it.

## Renderer and production integration

Pixel Art is a visual style, not a renderer requirement. For naturally two-dimensional scenes, Canvas 2D may be more appropriate than Three.js; use Three.js only when the scene calls for genuine 3D.

Compose this style with `cap.scene-production` for a requested HTML animation, while keeping production capability and visual style distinct. The capability provides renderer guidance for both Three.js and Canvas 2D; use the renderer appropriate to the scene and user requirements. Its Python validator performs renderer-specific static structural checks, not automatic scene generation or browser verification. A validator PASS does not prove Canvas rendering, visual quality, or motion.

## Validation

Assess evidence independently:

- **Source/build:** HTML structure, JavaScript syntax, Canvas 2D context creation, logical dimensions, palette and grid discipline, nearest-neighbor scaling, elapsed-time animation, and local dependencies.
- **Runtime:** load the artifact in a real browser and confirm the 2D context initializes without console errors.
- **Visual:** inspect crisp pixel boundaries, palette coherence, silhouette readability, layering, composition, and preservation of requested content.
- **Motion:** observe the requested actions at distinct times, including sprite cadence, elapsed-time behavior, and final/loop state.
- **Delivery:** confirm paths, run instructions, external dependencies, and renderer-specific validator support.

Static source checks do not prove browser rendering, visual quality, or observed motion. Report unobserved checks as `NOT_TESTED`; report an unsupported production or validation path as `BLOCKED` or `NOT_IMPLEMENTED` rather than claiming success.

`TSA_VIDPIXEL_DISCOVERY_MARKER: VIDPIXEL_CHILD_2D_3`

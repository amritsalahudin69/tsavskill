---
name: vidriso
description: >
  Risograph print-style visual guidance for user-defined scenes and animations.
  Use for layered, paper-based, spot-ink illustration with print texture and controlled misregistration.
---

# Risograph

## Identity and status

- Stable VSkills skill ID: `style.risograph`
- Copilot project skill name and directory: `vidriso`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidriso` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, global renderer, or print-production engine. The user's scene, subject matter, timing, camera, and output constraints remain authoritative.

## Visual language

Apply a coherent Risograph treatment to the user's chosen content:

- Use limited spot-ink palettes with readable separation and layered print construction.
- Favor paper-colored backgrounds, soft tonal variation, and intentional ink density rather than glossy modern vector styling.
- Build layered ink passes to create strong silhouettes, background hierarchy, and controlled overprinting.
- Use halftone or stipple treatment where it supports form, shadow, or texture without destroying readability.
- Keep the paper stock, grain, and ink behavior consistent across the scene.
- Allow small deterministic registration offsets between ink layers so the print has tactile separation without flicker or random drift.
- Preserve clear foreground/background relationships and coherent object silhouettes.
- Keep motion stylized and print-aware: dynamic elements should feel like printed forms moving under the same ink logic, not like floating digital overlays.
- Use scene-appropriate palette choices and keep the illustration readable at a distance.

Avoid: ordinary vector art with a global noise filter; random per-frame registration jitter; excessive glossy shading; hidden or arbitrary color layering; unnecessary textures; or a style-default scene that overrides the user's story.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, characters, camera framing, duration, aspect ratio, and loop behavior. Apply Risograph treatment without replacing or narrowing the scene. Do not copy example-specific characters, objects, or framing unless the user explicitly provides them.

Preserve canonical source identity and required details when supplied. If a stylized simplification would erase identity, function, or required form, retain that information and adapt the style around it.

## Renderer and production integration

Risograph is a visual style, not a renderer requirement. Canvas 2D is appropriate for a layered print treatment and procedural ink textures. Three.js is not required unless the user explicitly asks for a 3D scene. A style request does not override an explicitly selected renderer.

Compose this style with `cap.scene-production` when HTML implementation is requested. Keep scene content, production capability, renderer, and visual style distinct. The capability provides implementation guidance, not automatic generation.

## Validation

Assess evidence independently:

- Source/build: HTML and JavaScript syntax, chosen renderer, dependency usage, local assets, and local HTTP instructions.
- Structure: separate ink layers, halftone/stipple treatment, paper grain, print registration offsets, layered overprint behavior, and coherent scene hierarchy.
- Motion: confirm that dynamic objects move smoothly, that the beacon/sailboat or other animation remains anchored to the scene, and that the print texture does not flicker unpredictably.
- Delivery: confirm paths, renderer, dependencies, and limitations.

Static validation does not prove browser rendering, visual appearance, or observed motion. Report unobserved checks as `NOT_TESTED`.

`TSA_VIDRISO_DISCOVERY_MARKER: VIDRISO_CHILD_2E_7`

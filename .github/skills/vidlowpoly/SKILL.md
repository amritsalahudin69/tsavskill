---
name: vidlowpoly
description: >
  Low-Poly 3D visual guidance for user-defined scenes and animations.
  Use when a user requests stylized faceted 3D presentation.
---

# Low-Poly 3D

## Identity and status

- Stable VSkills skill ID: `style.low-poly-3d`
- Copilot project skill name and directory: `vidlowpoly`
- Logical parent: `vskills`
- Category: `visual_style`
- User-facing prompt alias: `/vidlowpoly` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when implementation is requested.

This is visual-style guidance, not a scene generator, model bank, renderer, or export system. The user's scene and constraints remain authoritative.

## Visual language

Apply a coherent low-poly 3D treatment to the user's chosen content:

- Use genuine volumetric 3D geometry rather than 2D facsimiles or smooth high-poly surfaces disguised as low-poly.
- Keep polygon counts intentionally low, with readable planar facets and distinct silhouette shapes.
- Favor flat shading or faceted normals so each form reads clearly from a distance.
- Use simple stylized materials with limited variation and clear color separation.
- Design architecture, terrain, props, and characters with coherent proportions and recognizable mass.
- Treat lighting as a deliberate story device: directional sun, controlled shadows, and readable depth not noise or excessive gradients.
- Preserve clear support, contact, and occlusion between objects. Floating elements or unsupported props are not acceptable unless the user's scene explicitly requires them.
- Keep the camera and object scale consistent within a single world coordinate system.
- Use a scene-appropriate palette, but do not impose a mandatory set of colors or an exact environment.

Avoid: smooth high-poly modeling disguised as low-poly; unnecessary texture complexity; excessively dense geometry; floating objects without supports; non-meaningful shapes; scene content unrelated to the user request; or style-default scenes, durations, or aspect ratios.

## Scene authority and boundaries

Accept the user's subjects, environment, actions, character and source inputs, camera, duration, aspect ratio, loop behavior, output format, lighting, and other constraints. Apply Low-Poly 3D presentation without replacing or narrowing scene content. Do not copy example-specific characters, objects, framing, or timing.

Preserve canonical source identity and required detail when supplied. If a stylized simplification would erase identity, function, or required form, retain that information and adapt the style around it.

## Renderer and production integration

Low-Poly 3D is a visual style, not a renderer requirement. Three.js is appropriate for genuine volumetric 3D scenes and faceted silhouettes. Canvas 2D is not a substitute for true low-poly 3D. A style request does not override an explicitly selected renderer.

Compose this style with `cap.scene-production` when HTML implementation is requested. Keep scene content, production capability, renderer, and visual style distinct. The capability provides implementation guidance, not automatic generation.

## Validation

Assess evidence independently:

- Source/build: HTML and JavaScript syntax, chosen renderer, dependency version, local assets, and local HTTP instructions.
- Structure: volumetric geometry, faceted shading, support and contact, scene depth, terrain/architecture coherence, object silhouettes, and one consistent world coordinate system.
- Runtime: confirm the selected rendering context initializes without critical errors in a real browser.
- Visual: inspect silhouette clarity, faceting, lighting, shadow behavior, depth, and composition.
- Motion: observe requested actions at distinct times and verify support, path coherence, object separation, and endpoint behavior.
- Delivery: confirm paths, renderer, dependencies, and limitations.

Static validation does not prove browser rendering, visual appearance, or observed motion. Report unobserved checks as `NOT_TESTED`.

`TSA_VIDLOWPOLY_DISCOVERY_MARKER: VIDLOWPOLY_CHILD_2E_6`

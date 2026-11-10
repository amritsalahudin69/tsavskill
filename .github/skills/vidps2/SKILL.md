---
name: vidps2
description: >
  Retro PS2 visual guidance for user-defined scenes and animations.
  Use when a user requests an early-2000s console-game 3D presentation.
---

# Retro PS2

## Identity and status

- Stable VSkills skill ID: `style.retro-ps2`
- Copilot skill name and directory: `vidps2`
- Logical parent: `vskills`
- Category: `visual_style`
- Descriptive name: Retro PS2
- User-facing prompt alias: `/vidps2` (not a verified native slash command)
- Production capability: compose with `cap.scene-production` when HTML/Three.js implementation is requested.

This is visual-style guidance, not a scene generator, renderer, or video-export capability. The user's scene and constraints remain authoritative.

## Visual direction

Apply an early-2000s console-game-inspired 3D presentation to the user's chosen content. The style should read as a deliberate, cohesive real-time game scene rather than merely a modern scene with reduced resolution.

- Use low-to-moderate polygon density with clear silhouettes, faceted transitions, and detail concentrated where it reads at the intended camera distance. Preserve important identity and functional shapes.
- Prefer period-appropriate material response: compact palettes, simple specular highlights, restrained gloss, vertex-color accents, and authored textures when useful. Do not make every surface shiny or impose a fixed palette.
- Keep texture maps deliberately limited in resolution when that supports the look. Nearest-neighbor sampling, visible texel structure, or simple tiled textures may be appropriate; retain enough resolution and contrast for required details.
- Shape lighting with readable key and fill sources, purposeful shadow contrast, and restrained color accents. Hard or stylized shadows and distance fog are options, not universal requirements.
- Use a camera treatment suited to the requested scene: stable game-like coverage, a motivated follow camera, or a cinematic cutscene move. A 4:3 frame, fixed camera, or dramatic lens effect is optional and must not override user constraints.
- Construct environments from clear, reusable forms and layered spatial landmarks. Use geometry, materials, and lighting together to establish depth; avoid flat substitutes when the user requests volumetric 3D.
- Keep animation readable and time-based. Apply stepped or deliberately coarse motion only when it suits the requested action; do not make motion choppy by default.

## Scene authority and inputs

Accept the user's subjects, environment, events, characters, actions, camera, duration, aspect ratio, loop behavior, output format, and other constraints. Do not supply default characters, settings, stories, HUD elements, text, props, or durations. Ask only when missing information materially changes the requested result.

The style changes presentation, not scene content. Do not replace a supplied canonical character, asset, or runtime with a lookalike. Avoid external game assets, copied game models, logos, or distinctive material from a particular commercial title unless the user supplies authorized source material and asks to preserve it.

## Composition with scene production

Keep the three dimensions distinct:

- `mode.*` determines the requested output type.
- `cap.scene-production` owns HTML/Three.js construction, animation, packaging, and execution validation.
- `style.retro-ps2` informs compatible appearance choices only.

When implementation is requested, select `cap.scene-production`, read its workflow, and load this skill for presentation guidance. Use Three.js when genuine 3D is required; this style does not require Three.js by itself. Preserve user-selected dependencies and disclose any external assets or network requirements. Do not claim that selecting or loading the skill generated or rendered a scene.

## Visual validation

Assess the actual rendered result when a browser is available. Report these separately from source checks:

- The user's scene remains recognizable and complete, with its requested subjects and actions intact.
- Low-to-moderate polygon treatment is visible in suitable forms without damaging important silhouettes or identity.
- Materials and texture resolution support the intended era-inspired appearance; texture softness or pixelation alone is not sufficient.
- Lighting, shadows, fog, and color are coherent and keep important action readable.
- Camera framing and movement honor the user's aspect ratio, viewpoint, and motion constraints.
- Environmental depth comes from visible spatial forms and relationships, not only a filter or low-resolution output.
- Motion is observed at distinct times; state static-source and browser evidence separately.

If actual browser output is unavailable, mark runtime, visual, and motion checks `NOT_TESTED` or `BLOCKED` as appropriate. Never treat static checks as proof of visual fidelity.

## Limitations

This skill contains portable instructions only. It does not provide an automatic router, universal scene generator, browser runtime, game engine, or MP4 exporter. Native `/vidps2` registration is host-specific and unverified; use the skill name in a prompt if the host does not recognize the alias.

`TSA_VIDPS2_DISCOVERY_MARKER: VIDPS2_CHILD_2D_1`

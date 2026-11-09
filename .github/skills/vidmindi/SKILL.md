---
name: vidmindi
description: >
  Miniature Diorama visual guidance for user-defined scenes.
  Use when a user requests miniature-scale, tabletop-inspired
  presentation or wants to plan a scene in this visual style.
---

# Miniature Diorama

## Identity and status

- Stable VSkills skill ID: `style.miniature-diorama`
- Copilot skill name and directory: `vidmindi`
- Logical parent: `vskills`
- Category: `visual_style`
- Descriptive name: Miniature Diorama
- Prompt-based invocation phrase: `Use the /vidmindi skill`
- `/vidmindi` is not a registered native slash command.

This is an instruction-only visual-style skill. Its discovery and invocation must be verified by the host; the file's presence alone is not evidence. It does not provide a scene generator, renderer, or video-generation engine. Video and HTML generation are not implemented.

## Source and design basis

The original `sub skill.txt` source is not available in this repository snapshot, and the available TSA references identify the style without specifying its visual techniques. The techniques below follow the approved Phase 2B requirements; they are not claimed as a verified extraction from the missing source.

## Purpose and visual techniques

Apply Miniature Diorama presentation to the user's scene without changing its subjects, environment, actions, or story. Choose techniques that suit the requested scene and constraints:

- Suggest miniature scale and toy-like spatial proportions where compatible with the user's design; do not turn a subject into a toy unless requested.
- Use a physical-model or tabletop appearance only when appropriate to the scene.
- Use tilt-shift-inspired depth of field and controlled selective focus where they support the requested framing; do not obscure important action or detail.
- Choose miniature-compatible materials and textures without imposing a fixed palette or material on the user's scene.
- Use scale cues that fit the scene; do not add props or objects solely to signal scale.
- Light the scene to communicate miniature form while preserving the requested mood and readability.
- Use cinematic camera movement that follows the user's camera and motion constraints; do not assume an orbit or a default shot.
- Use Three.js when the requested scene requires true 3D. Select another suitable renderer when the technical requirements do not call for Three.js.

No particular character, model town, teacup, forest, action, or storyline is required.

## Inputs

Accept the user's scene description and any supplied subjects, environment, actions, duration, aspect ratio, camera requirements, optional canonical character HTML, and additional constraints. Ask for missing information only when it materially affects the requested result.

## Guidance output

For a planning or style request:

1. Restate the user's scene intent without replacing or narrowing it.
2. Identify the Miniature Diorama treatment appropriate to that scene.
3. Describe applicable scale, focus, material, lighting, and camera choices.
4. Identify the production capability needed for any requested implementation.
5. State what is and is not executable in the current environment.

## Execution ownership and source authority

A visual style selects presentation techniques; it does not automatically provide a scene-production capability. Keep production mode, operation capability, and visual style distinct. If a requested implementation requires an unavailable generator, renderer, or runtime, report it as `BLOCKED` or `NOT_IMPLEMENTED`; do not claim that a scene was rendered or a video generated.

The user's scene requirements take precedence over style convenience. When canonical character HTML is supplied, inspect and preserve its character implementation and compatible runtime conventions; do not replace it with a visual approximation. Apply style treatment only where compatible with the source authority. Image-based character creation is a separate capability, and the user-provided image remains the appearance authority for that task.

## Validation and reporting

Report evidence and limits separately:

- **Discovery:** Copilot CLI lists `vidmindi` as an available project skill.
- **Metadata:** the host accepts `name: vidmindi` and the skill description.
- **Instruction loading:** an explicit prompt invokes the skill and returns the diagnostic marker.
- **Style identification:** the response applies Miniature Diorama guidance without conflating it with a production capability.
- **Scene independence:** the user's subjects, environment, and actions remain authoritative; no example scene is substituted.
- **Limitations:** no video or HTML generation is claimed unless a real execution capability is separately available and tested.

The marker is diagnostic only and is not proof of discovery or invocation merely because it appears in this file:

`TSA_VIDMINDI_DISCOVERY_MARKER: VIDMINDI_CHILD_2B`

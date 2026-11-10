---
name: vskills
description: >
  TSA VSkills parent capability for discovering
  video visual styles, character workflows,
  scene production modes, and usage guidance.
  Use when users request TSA video skills,
  skill discovery, or capability selection.
---

# TSA VSkills Parent

`vskills` is the TSA orchestration entry point (`vskills.parent`). It guides selection and composition of production modes, operation capabilities, and visual presentation while preserving the user's scene and constraints. It is instruction guidance, not an automatic universal router, renderer, or generator.

## Production modes and operations

- **Standalone Animation** produces one autonomous animation; duration is user-defined.
- **Modular Film** organizes scenes for assembly; the complete film has a 15-minute maximum, not each scene.
- **Character Asset** produces or prepares a reusable character asset.

Production mode determines output type. Operation capabilities determine the work (scene production, video breakdown, character creation, canonical character integration, or scene assembly). Visual style determines presentation techniques. These are separate dimensions: compose only the needed operation capability with zero or one primary style. A style alone does not provide an execution engine.

## Installed skills and scene inputs

<<<<<<< Updated upstream
Visual styles describe presentation techniques, not required characters, stories, actions, or environments. Scene content is always user-defined; never substitute an illustrative example for missing scene input. The initial design permits at most one primary style.

### Installed style child: Miniature Diorama

- **Stable ID:** `style.miniature-diorama`
- **User-facing alias:** `/vidmindi` (not a registered native slash command)
- **Installed instructions:** `.github/skills/vidmindi/SKILL.md`
- **Status:** installed as an instruction-only project skill; `copilot skill list` listed it in Copilot CLI 1.0.108.
- **Scope:** visual-style guidance for a user-defined scene; it is not video generation.

When a user requests Miniature Diorama, select and guide the host toward the installed `vidmindi` child skill so its instructions can be loaded. Preserve the user's subjects, environment, actions, story, and constraints; use the child for visual presentation guidance only. Do not claim a scene or video was generated.

Other visual styles, including Retro PS2, remain unimplemented; do not claim an installed child for them.

### Installed production capability: Scene Production

- **Stable ID:** `cap.scene-production`
- **Project skill name:** `scene-production`
- **Installed instructions:** `.github/skills/scene-production/SKILL.md`
- **Status:** installed instruction-only project skill; `copilot skill list` listed it in Copilot CLI 1.0.108.
- **Scope:** user-defined browser scenes, including HTML/Three.js construction, animation, packaging, and validation guidance.
- **Invocation:** select/load the project skill by its name or read its instructions manually. It is not a native `/scene-production` shell command.

The capability owns implementation workflow; it does not supply scene content, choose a style, or provide executable scene-generation software. Its railway fixture passed static and local HTTP checks, but browser runtime, visual fidelity, and rendered motion were not tested. Do not infer arbitrary-scene reliability from the fixture.

## Scene composition flow

For a scene-production request, preserve the user's subject, environment, actions, source authority, and explicit output constraints, then follow:

**user scene → choose the needed production capability → choose zero or one primary visual style → execute the selected scene workflow → validate the delivered output**

Use `cap.scene-production` when the requested operation is to implement a browser scene, including HTML/Three.js when the user requests or the technical requirements need genuine 3D. Select `style.miniature-diorama` only when Miniature Diorama is requested or clearly intended, and load `vidmindi` for presentation guidance. The production capability creates the user's scene; the style may affect compatible materials, scale cues, lighting, focus, and composition, but never substitutes characters, objects, environment, or actions. If the user asks only for style guidance, do not imply scene execution.

### Composition example

For “Create a standalone Miniature Diorama HTML/Three.js animation of a small delivery truck crossing a wooden bridge in a mountain village”:

- Select `mode.standalone-animation`, `cap.scene-production`, and `style.miniature-diorama`.
- Load `.github/skills/scene-production/SKILL.md` for the HTML/Three.js workflow and `.github/skills/vidmindi/SKILL.md` for style guidance.
- Preserve the delivery truck, wooden bridge, mountain village, and crossing action. Do not replace them with Lunar Outpost or railway-fixture content; do not invent duration, aspect ratio, or looping constraints as universal defaults.
- Produce an HTML artifact only when implementation is requested and available; follow the production skill's run instructions and six validation gates. Report browser, visual, or motion checks as untested unless observed.
=======
Visual style describes presentation techniques, not required characters, stories, actions, or environments. Scene content is always user-defined; never substitute an illustrative example for missing scene input. The initial design permits at most one primary style.

### Installed visual-style child

- **Miniature Diorama**
  - Stable skill ID: `style.miniature-diorama`
  - User-facing prompt alias: `/vidmindi`
  - Copilot skill location: `.github/skills/vidmindi/SKILL.md`
  - Status: implemented and tested as a discoverable Copilot project skill.
  - Scope: visual-style guidance for user-defined scenes only; it does not provide video generation, HTML generation, or a renderer.

When Miniature Diorama is requested, select the `vidmindi` child and direct the host to load its instructions using the prompt-based phrase `Use the /vidmindi skill`. Use the child's instructions for style guidance. If the host cannot load them, report that limitation rather than presenting the child marker or its detailed guidance as loaded. `/vidmindi` is not a registered native slash command.

Retro PS2 and other visual-style children remain unimplemented. Do not present them as installed capabilities.
>>>>>>> Stashed changes

## Character source authority

When integrating canonical character HTML, inspect and preserve its identity, geometry, hierarchy, pivots, materials, and compatible runtime conventions; do not substitute a lookalike. For image-based character creation, the user's image defines appearance; canonical HTML is optional implementation guidance.

## Intended hybrid routing

- With no arguments, explain available capabilities and their implementation status.
<<<<<<< Updated upstream
- With an explicit recognized skill, select that capability.
- With a sufficiently clear task, select a compatible production mode and operation; compose a visual style only when requested or unambiguous.
=======
- With an explicit recognized skill, select that capability. For Miniature Diorama, select the installed `vidmindi` child and use its instructions as described above.
- With a sufficiently clear task, select a compatible production mode and operation.
>>>>>>> Stashed changes
- With material ambiguity, ask for clarification.
- Never silently override explicit requirements or character/source authority.

## Implementation status and fallback

<<<<<<< Updated upstream
Copilot CLI 1.0.108 listed `vskills`, `vidmindi`, and `scene-production` as project skills. This verifies project-skill discovery in that CLI version only; listing or selecting instructions does not prove automatic parent routing, scene execution, browser/WebGL runtime, visual fidelity, or motion. `scene-production` is an instruction capability, not a generator; video export and other visual-style children remain unimplemented. `/vidmindi` is not a registered native slash command, and no native `/scene-production` command is established.
=======
The `vidmindi` visual-style child is implemented and tested as discoverable; its stable ID is `style.miniature-diorama`. Other visual-style child skills, native slash-command registration, automated routing, and video/character production execution are not implemented. Do not claim a capability ran merely because its instructions were read; report limitations and checks honestly.
>>>>>>> Stashed changes

If the host does not automatically load a project skill, use these instructions manually: identify the user's requested outcome, scene and source inputs, mode, operation, and optional style; load the selected skill files; follow applicable source-authority constraints; and report unsupported execution or unrun validation honestly. Do not claim execution merely because a skill was discovered or its instructions were read.

TSA_VSKILLS_DISCOVERY_MARKER: VSKILLS_PARENT_2B_R

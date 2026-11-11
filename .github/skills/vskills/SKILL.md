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

Visual styles describe presentation techniques, not required characters, stories, actions, or environments. Scene content is always user-defined; never substitute an illustrative example for missing scene input. The initial design permits at most one primary style.

### Active visual-style catalog

The active catalog contains nine implemented style children. Each is instruction guidance for user-defined scenes, not a generator, renderer, or video-export capability. The user reports all nine as **USER-OBSERVED MANUAL PASS**.

| Style | Stable ID | Project skill | Prompt alias |
| --- | --- | --- | --- |
| Miniature Diorama | `style.miniature-diorama` | `vidmindi` | `/vidmindi` |
| Retro PS2 | `style.retro-ps2` | `vidps2` | `/vidps2` |
| Pixel Art | `style.pixel-art` | `vidpixel` | `/vidpixel` |
| Comic Book | `style.comic-book` | `vidcomic` | `/vidcomic` |
| Toy Brick | `style.toy-brick` | `vidbrick` | `/vidbrick` |
| Claymation | `style.claymation` | `vidclay` | `/vidclay` |
| Paper Cutout | `style.paper-cutout` | `vidpaper` | `/vidpaper` |
| Low-Poly 3D | `style.low-poly-3d` | `vidlowpoly` | `/vidlowpoly` |
| Risograph | `style.risograph` | `vidriso` | `/vidriso` |

Prompt aliases are invocation phrases, not verified native slash commands. Load the selected child skill for its presentation guidance and preserve the user's content and constraints.

### Retired visual style

Retro Anime 2D (`style.retro-anime`, `vidanime`) is **RETIRED / NOT ACCEPTED** and is not part of the active catalog. Its original instructions are archived at `archive/skills/vidanime/SKILL.md`; historical fixtures and asset-contract files are retained unchanged. The prior 2D implementation remains a user-observed visual FAIL with a blocked asset-authoring workflow. Anime-Styled 3D is a future research candidate only, not an implemented or accepted replacement.

### Installed production capability: Scene Production

- **Stable ID:** `cap.scene-production`
- **Project skill name:** `scene-production`
- **Installed instructions:** `.github/skills/scene-production/SKILL.md`
- **Status:** installed instruction-only project skill.
- **Scope:** user-defined browser scenes, including HTML/Three.js construction, animation, packaging, and validation guidance.
- **Invocation:** select/load the project skill by its name or read its instructions manually. It is not a native `/scene-production` shell command.

The capability owns implementation workflow; it does not supply scene content, choose a style, or provide executable scene-generation software. Do not infer arbitrary-scene reliability from a fixture.

## Scene composition flow

For a scene-production request, preserve the user's subject, environment, actions, source authority, and explicit output constraints, then follow:

**user scene → choose the needed production capability → choose zero or one active primary visual style → execute the selected scene workflow → validate the delivered output**

Use `cap.scene-production` when the requested operation is to implement a browser scene, including HTML/Three.js when the user requests or the technical requirements need genuine 3D. Select a visual style only when requested or clearly intended, and load that child's instructions for presentation guidance. The production capability creates the user's scene; a style may affect compatible presentation choices, but never substitutes characters, objects, environment, or actions. If the user asks only for style guidance, do not imply scene execution.

### Composition example

For “Create a standalone Miniature Diorama HTML/Three.js animation of a small delivery truck crossing a wooden bridge in a mountain village”:

- Select `mode.standalone-animation`, `cap.scene-production`, and `style.miniature-diorama`.
- Load `.github/skills/scene-production/SKILL.md` for implementation guidance and `.github/skills/vidmindi/SKILL.md` for style guidance.
- Preserve the delivery truck, wooden bridge, mountain village, and crossing action; do not replace them with fixture content or invent duration, aspect ratio, or looping constraints.
- Report browser, visual, or motion checks as untested unless observed.

## Character source authority

When integrating canonical character HTML, inspect and preserve its identity, geometry, hierarchy, pivots, materials, and compatible runtime conventions; do not substitute a lookalike. For image-based character creation, the user's image defines appearance; canonical HTML is optional implementation guidance.

## Intended hybrid routing

- With no arguments, explain available capabilities and their implementation status.
- With an explicit active skill, select that capability and load its instructions when available.
- With a sufficiently clear task, select a compatible production mode and operation.
- Compose a visual style only when requested or unambiguous, and select only from the active catalog above.
- Treat retired Retro Anime 2D as unavailable; do not route to its archived instructions as an active style or substitute Anime-Styled 3D.
- With material ambiguity, ask for clarification.
- Never silently override explicit requirements or character/source authority.

## Implementation status and fallback

Project-skill discovery is host-specific. Listing or selecting instructions does not prove automatic parent routing, scene execution, browser/WebGL runtime, visual fidelity, or motion. `scene-production` is an instruction capability, not a generator; video export and Anime-Styled 3D are not implemented. Prompt aliases are not established native slash commands.

If the host does not automatically load a project skill, use these instructions manually: identify the user's requested outcome, scene and source inputs, mode, operation, and optional style; load the selected skill files; follow applicable source-authority constraints; and report unsupported execution or unrun validation honestly. Do not claim execution merely because a skill was discovered or its instructions were read.

TSA_VSKILLS_DISCOVERY_MARKER: VSKILLS_PARENT_2B_R

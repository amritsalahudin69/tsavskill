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

TSA VSkills is intended to guide selection of video production modes, operations, and visual presentation. This parent skill provides discovery and routing guidance; it is not a video renderer or production tool.

## Production modes and operations

- **Standalone Animation** produces one autonomous animation; duration is user-defined.
- **Modular Film** organizes scenes for assembly; the complete film has a 15-minute maximum, not each scene.
- **Character Asset** produces or prepares a reusable character asset.

Production mode determines output type. Operation capabilities determine the work (scene production, video breakdown, character creation, canonical character integration, or scene assembly). Visual style determines presentation techniques. These are separate dimensions, and a style alone does not necessarily provide an execution engine.

## Visual styles and scene inputs

Miniature Diorama and Retro PS2 are intended visual styles. They describe presentation techniques, not required characters, stories, actions, or environments. Scene content is always user-defined; never substitute an illustrative example for missing scene input. The initial design permits at most one primary style.

## Character source authority

When integrating canonical character HTML, inspect and preserve its identity, geometry, hierarchy, pivots, materials, and compatible runtime conventions; do not substitute a lookalike. For image-based character creation, the user's image defines appearance; canonical HTML is optional implementation guidance.

## Intended hybrid routing

- With no arguments, explain available capabilities and their implementation status.
- With an explicit recognized skill, select that capability.
- With a sufficiently clear task, select a compatible production mode and operation.
- With material ambiguity, ask for clarification.
- Never silently override explicit requirements or character/source authority.

## Implementation status and fallback

This parent instruction file is the only VSkills skill created in this iteration. Visual-style child skills, aliases as native commands, routing automation, and video/character production execution are not implemented here. Do not claim a capability ran merely because its instructions were read; report limitations and checks honestly.

If no native command or router is available, use these instructions manually: identify the user's requested outcome, scene and source inputs, mode, operation, and optional style; follow applicable source-authority constraints; and explain any unsupported execution or validation.

TSA_VSKILLS_DISCOVERY_MARKER: VSKILLS_PARENT_2A

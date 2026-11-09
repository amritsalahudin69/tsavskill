# TSA VSkills Skill Contract

**Document status:** APPROVED DESIGN; interface and executable behavior are not implemented.  
**Applies to:** Parent and visual-style skill definitions, operation capabilities, and future executable tools/adapters.  
**Date:** 2026-11-09

## Status labels

- **APPROVED DESIGN** — approved contract, not working software.
- **VERIFIED IMPLEMENTATION** — executable behavior actually implemented and tested; none is established here.
- **PROPOSED FUTURE CAPABILITY** — planned but not implemented and tested.
- **UNKNOWN** — unresolved or unverified.

## 1. Contract principles

**APPROVED DESIGN**

- Production mode determines output type; capability determines operation; visual style determines presentation.
- Scene content is user input. A style may not substitute a baked-in scene.
- User-declared source authority and canonical character constraints take precedence over style convenience.
- Hybrid routing follows the approved behavior in §3 and never silently overrides explicit requirements.
- Design approval is never evidence of executable implementation or host support.
- Failures and validation limits are reported explicitly.

**VERIFIED IMPLEMENTATION:** No executable skill or command is established by this contract.

## 2. Identity, IDs, and aliases

Every portable skill definition declares:

| Field | Requirement |
|---|---|
| `skill_id` | Stable identifier distinct from all command aliases. |
| `name` | Descriptive human-readable name. |
| `description` | Purpose and selection guidance. |
| `version` | Version of the skill definition/contract. |
| `parent` | Parent skill ID, or `null` for `/vskills`. |
| `category` | `parent`, `visual_style`, or `operation_capability`. Shared protocols and adapters are not skill categories by default. |
| `status` | `APPROVED_DESIGN`, `PROPOSED_FUTURE_CAPABILITY`, or `UNKNOWN`; this describes design maturity, not execution. |
| `invocation` | Alias list and per-host status (`SUPPORTED`, `UNSUPPORTED`, or `UNVERIFIED`); slash spelling does not imply registration. |
| `purpose_limits` | Explicit non-purpose and constraints. |
| `implementation_status` | `NOT_IMPLEMENTED`, `IMPLEMENTED`, `TESTED`, `BLOCKED`, or `UNKNOWN`, with evidence. |
| `inputs_outputs` | Required/optional inputs and declared outputs. |
| `dependencies` | Required/optional operation capabilities, tools, libraries, and host features. |
| `quality` | Acceptance criteria, validation procedure, and known limitations. |

**APPROVED DESIGN:** Keep identifiers and invocation aliases separate. The following identifiers and aliases are design metadata only; aliases remain unimplemented.

| Skill ID | Descriptive style | Proposed invocation alias |
|---|---|---|
| `style.miniature-diorama` | Miniature Diorama | `/vidmindi` |
| `style.retro-ps2` | Retro PS2 | `/vidps2` |
| `style.pixel-art` | Pixel Art | `/vidpixel` |
| `style.comic-art` | Comic Art | `/vidcomic` |
| `style.brick-toy` | Brick-toy (source label: Lego style) | `/vidlego` |
| `style.claymation` | Claymation | `/vidclay` |
| `style.paper-cutout` | Paper Cutout | `/vidpaper` |
| `style.retro-anime` | Retro Anime | `/vidanime` |
| `style.low-poly-3d` | Low-poly 3D | `/vidlowpoly` |
| `style.risograph` | Risograph | `/vidrisograph` |

The parent skill ID is `vskills.parent`, with proposed invocation alias `/vskills`. IDs are not commands and need not mirror alias spelling. Public names should be descriptive; final naming/licensing review is still pending.

Operation IDs (`cap.scene-production`, `cap.video-breakdown`, `cap.character-creation`, `cap.canonical-character-integration`, and `cap.scene-assembly`) are distinct from `skill_id`. A capability is not automatically an independently invokable skill. Define it as an operation reference unless it has a distinct reusable invocation contract; shared TSA protocols remain references by default, not executable skills.

Allowed ID and alias syntax, normalization, alias lookup, and collision handling are defined in `VSKILLS_INVOCATION_CONTRACT.md`.

## 3. Routing and architectural dimensions

**APPROVED DESIGN — hybrid routing:**

- No arguments: discover and explain available capabilities and their current status.
- Explicit recognized skill alias: select that requested skill/capability.
- Sufficiently clear task: select the appropriate production mode and compatible operation capability.
- Material ambiguity: request clarification.
- Explicit user requirements are never silently overridden.

The request keeps these values distinct:

| Dimension | Identifiers/examples | Determines |
|---|---|---|
| `production_mode` | `mode.standalone-animation`, `mode.modular-film`, `mode.character-asset` | Output type and mode-specific artifact contract. |
| `capabilities` | `cap.scene-production`, `cap.video-breakdown`, `cap.character-creation`, `cap.canonical-character-integration`, `cap.scene-assembly` | Operation(s) performed. |
| `primary_style` | A style skill ID from §2, or none | Presentation techniques; at most one in the initial design. |

`Character Asset` is a production mode, not a capability. It normally composes with Character Creation or Canonical Character Integration. Those capabilities may also be used in Standalone Animation or Modular Film.

**APPROVED DESIGN:** Only one primary visual style is supported initially. Automatic style mixing is not supported. Mixing may be documented as a future capability.

## 4. Inputs

### 4.1 Common request fields

**APPROVED DESIGN:** A request may include:

- `objective` — desired outcome.
- `production_mode` — Standalone Animation, Modular Film, or Character Asset.
- `scene_or_script` — user-defined content, when scene-based.
- `source_media` — source video or other reference, if applicable.
- `capabilities` — requested operation(s).
- `primary_style` — zero or one requested visual style.
- `character_inputs` — images, canonical HTML, descriptions, or animation references.
- `output_constraints` — file format, duration, aspect ratio, runtime, dependencies/offline policy, and destination as specified by the user.
- `validation_expectations` — required checks or acceptance criteria.

Do not silently turn source examples into default scene content, duration, aspect ratio, renderer, or dependency settings.

### 4.2 Mode-specific required inputs

| Mode/capability | Required inputs | Optional inputs |
|---|---|---|
| Parent `/vskills` | User objective or question. | Any explicit mode, capability, style, inputs, and output constraints. |
| Visual-style skill | User scene/context to style, or request for style guidance. | Character, motion, camera, and rendering constraints. |
| Standalone Animation | User-defined scene or explicit request to develop one. | Scene-production capability, one style, character integration, duration/framing/runtime constraints. |
| Modular Film | Script/source/breakdown sufficient for the requested film task, or explicit request to plan/build a modular film. | Video breakdown, scene production, scene assembly, one style, character integration, output constraints. |
| Capability-only Video Breakdown | Source video or request to audit an existing breakdown. | No production mode unless the analysis feeds a requested production output; result is an evidence-based breakdown package. |
| Character Asset + Character Creation | Target character image for image-to-Three.js creation. | Written detail, animation reference, canonical HTML as optional implementation guidance. |
| Character Asset + Canonical Character Integration | Canonical source HTML and intended reuse/construction task. | Image, scene requirements, animation, output constraints. |

If image and canonical HTML are supplied without clear source roles, clarify. User-provided images define appearance for new image-based characters; existing canonical HTML is optional implementation guidance in that workflow.

## 5. Operation capability responsibilities

| Category | Owns | Must not own |
|---|---|---|
| `cap.scene-production` | Scene behavior and implementation in the selected mode. | Selecting a required scene, style, or character without user authorization. |
| `cap.video-breakdown` | Evidence-based source-video audit, coverage, scenes/shots, and handoff. | Treating an analysis/adaptation proposal as observed source fact. |
| `cap.character-creation` | New character from user-provided appearance inputs. | Inventing identity that contradicts supplied references. |
| `cap.canonical-character-integration` | Inspecting and faithfully reusing canonical HTML. | Replacing a canonical character with a lookalike or silently changing source architecture. |
| `cap.scene-assembly` | Modular Film manifest, sequence, lifecycle/handoffs, and assembly. | Defining visual style or splitting every shot into a module by default. |
| Shared TSA protocols | Evidence rules, preservation, scoped execution, validation status, and handoff. | Claiming unverified runtime behavior. |

## 6. Output contracts

All outputs are **APPROVED DESIGN**, not VERIFIED IMPLEMENTATION. Exact filenames and packaging remain request- or project-defined.

### Standalone Animation

- Requested autonomous animation artifact and requested supporting/source files.
- Run/dependency notes, deviations, limitations, and validation report.
- User-defined duration; no mode-wide duration default.

### Modular Film

- Scene/module plan with stable IDs, boundaries, and rationale.
- Per-scene artifacts and local runtime contracts.
- Film manifest/sequence, duration and continuity/handoff data.
- Master assembly artifact when requested.
- Coverage, integration, playback, and visual validation report.
- Complete film duration no greater than 15 minutes; this is not a per-scene limit.

### Character Asset

- Reusable character artifact in the requested format.
- Source audit when canonical source is supplied; dependency record and implementation/deviation report.
- Relevant appearance/source fidelity, geometry/hierarchy, requested animation, and runtime validation statuses.

A generated file alone is not evidence that it runs or meets visual acceptance.

Operation-specific outputs: Video Breakdown produces evidence-labeled analysis/handoff artifacts; Character Creation produces a new character asset; Canonical Character Integration produces a source audit and faithful integration/reuse record; Scene Assembly produces the modular film manifest/assembly. None of these operations changes the selected production mode by itself.

## 7. Rendering and dependencies

**APPROVED DESIGN**

- Select rendering technology from actual scene requirements: Three.js for genuinely 3D scenes; Canvas, CSS, SVG, or another suitable browser technology where appropriate.
- Do not force every style to use Three.js or silently replace a canonical runtime architecture.
- Prefer minimal dependencies; document all required dependencies.
- Do not claim offline support without verification.
- Preserve compatibility with supplied canonical sources when required.

## 8. Error and conflict handling

**APPROVED DESIGN:** On error, the capability must:

1. Name the affected requirement and evidence/source.
2. Report `FAIL`, `BLOCKED`, or `NOT_TESTED` accurately.
3. Preserve canonical inputs and unrelated files.
4. Avoid silent substitution of a scene, character, style, dependency, or output format.
5. Offer only the smallest viable alternatives when a user decision is needed.

Clarify on material ambiguity. Never silently override explicit requirements, downgrade fidelity, alter canonical identity, or omit requested content.

## 9. Validation contract

Every future execution declares applicable checks and evidence:

- Source/input inventory and provenance.
- Contract/schema or static validation.
- Dependency and asset availability.
- Mode-specific unit/contract and integration checks.
- Browser/runtime checks when an executable browser artifact is produced.
- Visual and motion acceptance when rendering/inspection is available.
- Production/export checks when export is part of the request.

Use TSA statuses `PASS`, `FAIL`, `BLOCKED`, and `NOT_TESTED`. A static check does not imply runtime success; a runtime load does not imply visual fidelity. State host limitations and checks not run.

## 10. Portable boundaries and extension

**APPROVED DESIGN:** Keep these concerns separate:

- Vendor-independent skill definitions.
- Skill metadata and contracts defined above.
- Executable tools that perform deterministic work.
- Host-specific agent adapters that translate invocation and tool/file access.

Native slash-command support must be verified separately for each agent.

**PROPOSED FUTURE CAPABILITY:** New style definitions and operation capabilities conform to this contract without changing the meanings of production modes, capabilities, or styles.

**UNKNOWN:** Registry implementation, serialization format, version negotiation, and automated conformance tests are not selected in this documentation-only iteration.

The portable `SKILL.md` content, directory layout, reference resolution, and host-specific metadata boundary are defined in `VSKILLS_SKILL_LAYOUT.md`. A skill must remain manually usable by reading its instructions when no router or native slash adapter exists.

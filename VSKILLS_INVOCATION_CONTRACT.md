# TSA VSkills Invocation Contract

**Document status:** APPROVED DESIGN; resolver and invocation mechanisms are not implemented.  
**Phase:** 1B — Skill Definition & Invocation Contract  
**Date:** 2026-11-09

## Status labels

- **APPROVED DESIGN** — target contract approved for future work; not working software.
- **VERIFIED IMPLEMENTATION** — executable behavior actually implemented and tested; none is established here.
- **PROPOSED FUTURE CAPABILITY** — planned alias, skill, tool, or adapter not yet implemented and tested.
- **UNKNOWN** — unresolved or unverified.

Runtime outcomes use TSA statuses `PASS`, `FAIL`, `BLOCKED`, and `NOT_TESTED`.

## 1. Purpose and boundary

This contract defines how a user request maps to a stable skill or operation, production mode, inputs, references, execution, validation, and report.

**APPROVED DESIGN:** `/vskills` uses hybrid routing. Production Mode determines output type; Operation Capability determines work performed; Visual Style determines presentation. One request may use at most one primary style. No resolver, registry, command, or host adapter is implemented.

Related contracts:

- Skill identity and mode/capability/style fields: `VSKILLS_SKILL_CONTRACT.md`.
- Directory, `SKILL.md`, and progressive-reference behavior: `VSKILLS_SKILL_LAYOUT.md`.
- User-facing examples: `VSKILLS_USAGE_DESIGN.md`.

## 2. Stable identifiers and aliases

### 2.1 Identifier syntax

**APPROVED DESIGN:** Stable skill IDs use lowercase ASCII segments separated by `.` or `-`:

```text
^[a-z][a-z0-9]*(?:[.-][a-z0-9]+)*$
```

Examples: `vskills.parent`, `style.miniature-diorama`, `style.retro-ps2`.

Operation IDs use the same syntax, with the `cap.` namespace, for example `cap.scene-production`. Production mode IDs use `mode.`, for example `mode.modular-film`. IDs are canonical, lowercase, and do not include a slash.

Invocation aliases use a leading slash followed by a lowercase ASCII name:

```text
^/[a-z][a-z0-9-]*$
```

Examples: `/vskills`, `/vidmindi`, `/vidps2`. Aliases are user-facing entry points, not identity values.

### 2.2 Normalization and lookup

**APPROVED DESIGN:**

1. Trim whitespace around the alias token only.
2. Normalize the alias token to lowercase ASCII for lookup.
3. Require the leading `/`; do not infer missing slashes or convert descriptive names to aliases.
4. Preserve all remaining arguments, scene text, filenames, and user content exactly; do not normalize scene content.
5. Resolve only an exact normalized alias-table match to a stable `skill_id`.
6. Treat operation and mode values as their declared canonical IDs or documented names; do not fuzzy-match them.

The initial alias map is listed in `VSKILLS_SKILL_CONTRACT.md`, §2. Alias-table changes must be reviewed as interface changes.

### 2.3 Collision and unknown-alias handling

- Stable IDs must be globally unique within a package.
- Normalized aliases must map to exactly one skill ID. A duplicate/colliding alias blocks package validation; no precedence rule may silently choose a target.
- An unknown alias returns `FAIL` for alias resolution, lists available aliases when possible, and does not invoke a “closest” skill automatically.
- An unknown or malformed internal skill ID or capability ID returns `FAIL` with the unresolved identifier; it must not be reinterpreted as a command alias.
- Retired aliases must not be reassigned to a different skill ID.

## 3. Three invocation layers

### Layer A — Intended user alias

**PROPOSED FUTURE CAPABILITY:** Target aliases are `/vskills`, `/vidmindi`, `/vidps2`, and the other visual aliases listed in the skill contract. All remain unimplemented until separately tested on a host.

- `/vskills` is the parent entry point.
- A style alias selects a visual-style skill, not an execution engine.
- Operation capabilities and production modes may be selected through parent arguments or task interpretation; they are not automatically slash commands.
- A user may instead read and follow the selected skill's `SKILL.md` manually.

### Layer B — Portable skill resolution

**APPROVED DESIGN — hybrid routing:**

| Request form | Resolution |
|---|---|
| `/vskills` with no arguments | Discover and explain available modes, capabilities, styles, and their implementation/host status. |
| Explicit recognized skill alias | Resolve its stable skill ID and select that skill. Explicit mode/capability/scene constraints remain in force. |
| Sufficiently clear task | Select the appropriate mode and compatible operation capability; select a style only if requested or unambiguous. |
| Material ambiguity | Ask a focused question before execution. |

Explicit user requirements always take precedence. An explicit alias does not authorize changing the user's scene, character identity, source authority, or output constraints.

#### Style alias with a clear scene

**APPROVED DESIGN:** When a user invokes a visual-style alias with a clear scene but omits the mode, treat the invocation as a request to create a standalone animation and resolve to:

- `mode.standalone-animation`
- `cap.scene-production`
- the explicitly invoked style as the sole `primary_style`

This is a compatible default, not a hardcoded scene or a duration/format default. If the user explicitly asks only for style guidance, return guidance without selecting an execution mode. If the request clearly implies Modular Film or Character Asset, select that mode instead. Clarify only if mode or intent remains materially ambiguous.

A style alias without a required scene:

- may return style guidance if that is the user's intent;
- must request the user-defined scene when scene production is requested;
- must never fill the gap with a source-prompt example.

#### Mode/capability/style compatibility

| Mode | Required operation | Compatible optional operations |
|---|---|---|
| Standalone Animation | `cap.scene-production` | `cap.character-creation` when creating an asset, `cap.canonical-character-integration` when reusing one, `cap.video-breakdown` for source-based preproduction. |
| Modular Film | `cap.scene-production`; `cap.scene-assembly` when producing the assembled film | `cap.video-breakdown` when source analysis is needed, character creation/integration as required. |
| Character Asset | `cap.character-creation` **or** `cap.canonical-character-integration`, selected from the requested source/task | The other character operation only when the user requests both and their source roles are clear. |

Video Breakdown may also be invoked as a capability-only analysis task, producing its analysis artifacts without selecting a film-production mode. When the breakdown feeds a film, select the mode based on the requested eventual output. A cinematic adaptation is a separate proposal/production step; source reconstruction remains evidence-based.

Only one primary visual style may be selected. If multiple styles are requested, return `BLOCKED` and ask the user to choose one. Do not mix styles automatically.

Conflicting modes or incompatible capabilities return `BLOCKED` with the conflict and smallest choice needed. Do not silently drop a capability.

### Layer C — Host-specific invocation

**APPROVED DESIGN:** A future adapter may map a stable skill ID and declared inputs to one host's native mechanism. It must separately declare and test:

- command/skill registration and argument parsing;
- attachment and file access;
- reference loading and path behavior;
- executable-tool permissions and runtime availability;
- output artifact handling;
- host-specific validation limitations.

Portable instructions do not guarantee native alias support. The adapter may expose only verified features and must not change the portable skill's meaning.

| Mechanism/host | Status in this project |
|---|---|
| Manual instruction-based use by reading the selected `SKILL.md` | **APPROVED DESIGN** fallback; host-specific behavior is not verified. |
| Native slash aliases through the portable core alone | **Unsupported by design:** an alias string does not register a command. This is not a claim about a vendor's capabilities. |
| Codex native skills/commands | **UNKNOWN / unverified**; no adapter tested. |
| Claude Code native skills/commands | **UNKNOWN / unverified**; no adapter tested. |
| Gemini CLI native skills/commands | **UNKNOWN / unverified**; no adapter tested. |
| Other agents | **UNKNOWN / unverified** until individually tested. |

## 4. Execution flow and ownership

| Stage | Owner | Required behavior |
|---|---|---|
| User request | User / parent | Capture objective, scene/source, explicit constraints, source authority, and desired output. |
| Invocation resolution | Parent or manual reader | Normalize and resolve an exact alias/ID; report unknown or colliding identifiers. |
| Production mode selection | Parent | Use explicit mode first; otherwise select only when intent is sufficiently clear. Video-breakdown-only work may be capability-only. |
| Capability composition | Parent | Select only required, compatible operations from the contract matrix. |
| Style selection | User / parent | Apply zero or one primary style; style affects presentation only. |
| Input validation | Selected capability | Check required scene/source/assets, constraints, and source authority before execution. |
| TSA reference loading | Skill instructions | Load only the references required for this operation, following `VSKILLS_SKILL_LAYOUT.md`. |
| Execution | Declared capability and available tool/agent | Follow the mode/capability contract; never claim execution if only instructions were read. |
| Validation | Executing capability | Run applicable checks; report evidence and `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED`. |
| User report | Parent or manual executor | State selected mode/capability/style, artifacts actually produced, checks, limitations, and unresolved issues. |

## 5. Source authority and composition

- **User scene:** remains user-defined. A style may not prescribe scene characters, environment, action, or story.
- **Canonical HTML character:** inspect the actual source; preserve identity, geometry, hierarchy, pivots, materials, and compatible runtime conventions. Do not substitute a lookalike.
- **Image-to-Three.js character creation:** the target image defines appearance; canonical HTML may guide implementation but is optional.
- **Style with canonical character:** style may affect compatible lighting, staging, environment, camera, or presentation, but may not silently change authoritative character identity or geometry.
- **Renderer/runtime conflict:** preserve required canonical runtime conventions. If the requested style cannot be achieved compatibly, report the conflict and request approval; do not silently replace the renderer or runtime.
- **Video breakdown and cinematic adaptation:** preserve source evidence and label uncertainty; do not apply a requested style to source reconstruction. If adaptation is requested, produce a separately labeled adaptation proposal, then use `cap.scene-production` to implement only an approved adaptation in the selected mode. Apply the style to that adaptation, not to source facts.
- **Modular Film:** use `cap.scene-assembly`; retain the 15-minute limit for the complete film, not per scene.

If a selected style conflicts with canonical geometry or runtime, first determine whether presentation-only treatment can satisfy the style. If not, report `BLOCKED` and request authorization for a change; canonical source remains unchanged.

## 6. Error and validation contract

| Condition | Required response |
|---|---|
| Unknown skill ID or alias | `FAIL` resolution; identify the value and show known choices when available. No fuzzy fallback. |
| Missing scene for requested scene production | `BLOCKED`; request a user-defined scene. Never substitute an example. Style-guidance-only requests may proceed without a scene. |
| Missing canonical source for canonical integration | `BLOCKED`; request the source. Do not rebuild a lookalike. An alternative is offered only as a user decision. |
| Invalid/missing required reference path | `BLOCKED`; identify the path and referring instruction. Do not guess or silently skip a required reference. |
| Unsupported operation | `BLOCKED`; name the unsupported operation and available supported options. |
| Unsupported/unverified host feature | `BLOCKED` for that host-dependent action, or use the manual fallback if the user can proceed; report the limitation. |
| Multiple/conflicting primary styles | `BLOCKED`; ask the user to select one. No automatic mixing. |
| Missing tool, runtime, or dependency | `BLOCKED`; report the missing prerequisite and do not silently switch technology. |
| Validation failure | `FAIL`; report failed criteria and evidence. Do not report success. |
| Validation not run | `NOT_TESTED`; state why. |

An alias resolving successfully proves only selection, not execution. Reading instructions is not execution evidence. Report only artifacts actually produced and checks actually run.

## 7. User-facing report

Every execution report includes:

- resolved `skill_id`/capability IDs, production mode (if applicable), and primary style (if any);
- whether selection was explicit, inferred by hybrid routing, or manually selected;
- input/source authority and references loaded;
- exact artifact paths only for files actually produced;
- required dependencies and host/runtime limitations;
- applicable checks with `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED` and concise evidence;
- deviations, unresolved conflicts, and user decisions needed.

**VERIFIED IMPLEMENTATION:** No resolver, native command, adapter, or end-to-end execution has been implemented or tested by this documentation.

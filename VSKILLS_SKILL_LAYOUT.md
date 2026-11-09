# TSA VSkills Skill Layout Contract

**Document status:** APPROVED DESIGN; no skill package or `SKILL.md` is created in this phase.  
**Phase:** 1B — Skill Definition & Invocation Contract  
**Date:** 2026-11-09

## Status labels

- **APPROVED DESIGN** — target package/layout contract, not implemented.
- **VERIFIED IMPLEMENTATION** — actual package behavior implemented and tested; none is established here.
- **PROPOSED FUTURE CAPABILITY** — planned package, tool, or adapter not yet implemented and tested.
- **UNKNOWN** — host support or behavior not established.

## 1. Package layout

**APPROVED DESIGN:** Use stable skill IDs for directory names; aliases are metadata, not directory names.

```text
<package-root>/
  skills/
    vskills.parent/
      SKILL.md
      references/                 # optional, targeted parent references
    style.miniature-diorama/
      SKILL.md
      references/                 # optional style and TSA references
      scripts/                    # optional, inert unless explicitly invoked
      assets/                     # optional static style-support assets
    style.retro-ps2/
      SKILL.md
      references/
      scripts/
      assets/
    <future-skill-id>/
      SKILL.md
      references/
      scripts/
      assets/
  protocols/                      # shared TSA reference documents; not executable skills by default
    <protocol-file>.md
  tools/                          # optional executable tools, distinct from skill instructions
    <tool-id>/
  adapters/                       # optional host-specific mappings and metadata
    <host-id>/
```

All shown directories except `skills/<skill-id>/SKILL.md` are optional when unused. This tree is a design example only; do not create it until separately authorized.

Operation capabilities are stable `capability_id` values. They may be described by a parent/production skill and referenced as operation instructions; an operation becomes an independent skill only if it has a distinct reusable invocation contract. Shared TSA protocols belong under references/protocols and do not need executable-skill registration.

### 1.1 Initial operation representation

**APPROVED DESIGN:** Initial operations are capability definitions/references, not separately registered slash commands. The parent or selected mode invokes them; shared TSA protocols remain reference documents.

| Capability ID | Initial representation | Relevant TSA references (load only when needed) |
|---|---|---|
| `cap.scene-production` | Operation instructions under the selected production mode; not an independent skill alias initially. | Relevant implementation sections of `TSA_HTML_Game_Video_Production_PROTOCOL_v1.0.0.md` when applicable; scene execution contract. |
| `cap.video-breakdown` | Reusable analysis operation; may produce a capability-only breakdown without a production mode. | `TSA protocol/vdideo/TSA_Video_Breakdown_Protocol_v1.0.0/PROTOCOL.md`; selected templates and master analysis prompt as needed. |
| `cap.character-creation` | Operation used by Character Asset; independent skill package may be considered later if it has a distinct invocation contract. | Image-to-Three.js chat prompt or canonical 3D character build prompt, according to input/source authority. |
| `cap.canonical-character-integration` | Reusable operation used in Character Asset, Standalone Animation, or Modular Film; not an independent command by default. | `TSA_Canonical_Character_to_Scene_Integration_Protocol_v1.0.0.md` and the supplied canonical HTML. |
| `cap.scene-assembly` | Modular Film operation; not an independent skill alias initially. | `TSA_HTML_SCENE_MODULARIZATION_AND_ASSEMBLY_PROTOCOL_v1.0.0.md`. |

These are references to audited source documents, not claims that their instructions have been implemented as tools.
Paths in the table identify source locations within the audited archive; a future packaged skill must declare its actual package-relative reference path and may not assume an agent can load a file directly from the ZIP.

## 2. Portable `SKILL.md` contract

### 2.1 File and metadata

**APPROVED DESIGN:** `SKILL.md` is UTF-8 Markdown and is the portable human-readable source of instructions.

Recommended minimal YAML front matter:

```yaml
---
name: Descriptive skill name
description: One-sentence purpose and selection guidance.
---
```

This two-field subset is a compatibility target, not a claim that every host parses it. The authoritative identity contract also appears in a plain Markdown `## TSA Skill Metadata` section so the skill remains manually usable if front matter is ignored.

Required identity fields in that section:

- `skill_id`
- `name`
- `description`
- `version`
- `parent`
- `category`
- `status`
- `invocation`
- `dependencies`

For these fields, use the definitions and status separation in `VSKILLS_SKILL_CONTRACT.md`. Keep stable IDs separate from aliases. The portable core does not select a registry serialization format.

Optional metadata may include contract version, `capability_ids`, input/output schemas, tested host/runtime matrix, supported renderers, compatibility constraints, asset licenses, and deprecation/migration notes.

### 2.2 Required instruction sections

Every future `SKILL.md` contains:

1. **Purpose and boundaries** — intended task and explicit non-goals.
2. **TSA Skill Metadata** — required identity fields and implementation status.
3. **Invocation and routing** — aliases, inputs, mode/capability/style semantics, and manual invocation.
4. **Required and optional inputs** — including source authority and validation.
5. **Execution workflow** — ordered steps and ownership; never imply an unimplemented step works.
6. **Relevant references** — exact relative paths, purpose, and whether required or optional.
7. **Output contract** — artifacts, formats, and runtime expectations.
8. **Errors and conflicts** — explicit status handling and stop conditions.
9. **Validation and reporting** — checks, evidence, and statuses.
10. **Limitations and compatibility** — dependencies, host support, and known unknowns.
11. **Usage examples** — clearly marked PROPOSED until actually supported.

Styles must additionally state that scene content is user-defined, identify one-style-only behavior, and avoid requiring sample scenes or characters.

## 3. Reference directory and progressive loading

### 3.1 Reference behavior

- `references/` contains only focused material relevant to that skill; it is optional.
- Shared TSA protocols may be stored once under package-level `protocols/` and referenced by declared relative paths. Do not copy entire protocols into every skill without need.
- List each reference path and its purpose in `SKILL.md`. Mark it required or optional.
- Load only the selected skill's primary instructions and references needed for the current operation. Do not load all style definitions at once.
- Load canonical character HTML only when the requested capability requires inspecting or integrating it.
- If a required reference is missing, report `BLOCKED`, naming the path and dependency. Do not invent its contents.
- If an optional reference is missing, disclose the omission and continue only if it does not undermine the requested result; otherwise report `BLOCKED`.

### 3.2 Loading order

1. Read skill identity and description to confirm selection.
2. Read the selected `SKILL.md` instructions.
3. Read only the TSA protocol references relevant to the selected mode/capability.
4. Read canonical HTML source when canonical construction/integration requires it.
5. Read a selected visual style's references only; do not load unrelated styles.
6. Load tool instructions/dependencies only for a declared operation that uses them.

## 4. Relative paths and source handling

**APPROVED DESIGN:**

- Resolve a relative reference from the directory containing the referring `SKILL.md`, not from the agent's current working directory.
- Normalize the resolved path and require it to remain within the declared package root. Reject absolute paths or paths escaping that root.
- Use exact, documented path spelling; do not guess alternate filenames or case.
- User-provided scene assets and canonical character sources are inputs, not skill-bundled defaults. Resolve them only through the host's declared file/attachment mechanism.
- If a source is inside an archive, do not assume the host can read it as an ordinary path; require an explicitly supported archive-reading mechanism or report the limitation.

## 5. Scripts and tools

- `scripts/` is optional and contains only scripts owned by that skill. Presence is not permission or instruction to execute.
- Each script/tool must have a declared ID, purpose, inputs, outputs, runtime, dependencies, and validation procedure.
- A skill invokes a script only when the execution contract explicitly requires it, the user request authorizes that operation, and the host supports execution.
- Read/inspect the declared tool instructions before use. Never run arbitrary files merely because they exist in `scripts/`, `tools/`, an archive, or a reference directory.
- Executable tools live separately from portable skill text. Tool failure is reported; do not replace it silently with an unvalidated tool or technology.

## 6. Assets

- `assets/` is optional and contains static, reusable skill-support files only.
- Assets must be described with exact relative paths, purpose, format, dependency, and license/provenance when applicable.
- Do not bundle example characters, story environments, or scenes as mandatory defaults.
- User-supplied scene files and canonical character assets remain user inputs and must not be overwritten by skill assets.
- Missing required assets produce `BLOCKED`; missing optional assets are disclosed and skipped only when safe.

## 7. Versioning and compatibility

**APPROVED DESIGN:**

- Keep `skill_id` stable across compatible releases; a rename does not silently create a new alias target.
- Use `MAJOR.MINOR.PATCH` versions. Major changes may break inputs/outputs or behavior; minor changes add backward-compatible capability; patch changes correct instructions or non-breaking details.
- Declare the VSkills contract version the skill follows and any required protocol versions.
- Declare runtime/rendering/dependency constraints and the host capabilities required.
- Track host support separately as `SUPPORTED` (tested), `UNSUPPORTED` (known not available for that integration), or `UNVERIFIED` (not tested). Include test evidence/version where supported.
- Do not infer native slash-command support from `SKILL.md` presence.
- Put native host metadata, command registration, and host-only configuration under `adapters/<host-id>/`; keep it out of the portable skill definition.

**UNKNOWN:** The final machine-readable metadata schema, registry format, and host-specific manifests are deferred.

## 8. Manual invocation fallback

**APPROVED DESIGN:** If no router or native slash adapter exists, the skill remains usable by:

1. Selecting the skill by its stable ID or descriptive name.
2. Reading its `SKILL.md` manually.
3. Providing the user-defined request and required assets directly to an agent that can follow instructions.
4. Loading only the declared references.
5. Following the same error, validation, and reporting contract.

This fallback is a documentation design. It does not claim that a particular agent can access files, run tools, render a scene, or produce downloadable artifacts.

## 9. Validation and reporting

Before a future skill is released, validate:

- required identity fields and ID/alias uniqueness;
- required instruction sections and all declared relative paths;
- no mandatory illustrative scene or character in a style;
- required dependencies and compatibility claims;
- scripts/tools are documented and never implied to run automatically;
- output and failure contracts;
- examples labeled as proposed unless tested on a named host.

At execution, report `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED` for applicable checks with evidence. Reading `SKILL.md` is not proof of execution. A successful static check is not proof of browser/runtime or visual fidelity.

**VERIFIED IMPLEMENTATION:** No `SKILL.md`, package tree, executable tool, or host adapter has been created or tested in Phase 1B.

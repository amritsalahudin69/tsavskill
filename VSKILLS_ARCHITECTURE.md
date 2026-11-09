# TSA VSkills Architecture

**Document status:** APPROVED DESIGN; no executable implementation is verified.  
**Phase:** 1A-R — Architecture Alignment & Decision Lock  
**Date:** 2026-11-09

## Status labels

- **APPROVED DESIGN** — architecture decisions approved for future implementation; not evidence of working software.
- **VERIFIED IMPLEMENTATION** — executable behavior actually implemented and tested. None is established by this document.
- **PROPOSED FUTURE CAPABILITY** — planned skill, alias, tool, or adapter not yet implemented and tested.
- **UNKNOWN** — unresolved or unverified behavior.

## 1. Purpose and architectural dimensions

**APPROVED DESIGN:** TSA VSkills separates three dimensions:

- **Production mode** determines the output type: Standalone Animation, Modular Film, or Character Asset.
- **Capability** determines the operation: scene production, video breakdown, character creation, canonical character integration, or scene assembly.
- **Visual style** determines presentation techniques, such as Miniature Diorama, Retro PS2, Pixel Art, or another supported style.

These dimensions compose but do not replace one another. A request can select one mode, one or more capabilities as needed, and at most one primary visual style in the initial design.

**VERIFIED IMPLEMENTATION:** None of the VSkills commands, routing, skills, registry, tools, or adapters is implemented and tested in the supplied materials.

## 2. Parent and capability model

```text
User request
    |
    v
/vskills parent (hybrid routing)
    |
    +-- Production mode             output type
    +-- Capability                  operation(s)
    +-- One primary style           presentation techniques (optional)
    +-- Shared TSA protocols        evidence, preservation, validation
    |
    v
Portable skill definition and metadata
    |
    +-- Executable tool(s), when required
    +-- Host-specific agent adapter, when required
    |
    v
Requested artifact and evidence-based report
```

### 2.1 Parent `/vskills` — hybrid routing

**APPROVED DESIGN:** `/vskills` uses hybrid routing:

- With no arguments, discovers and explains available capabilities and their support status.
- With an explicit recognized skill alias, selects that requested capability.
- With a sufficiently clear task, selects the appropriate production mode and compatible capability.
- With material ambiguity, asks for clarification before acting.
- Never silently overrides explicit user requirements.

When a visual-style alias is invoked with a clear scene but no mode, default to Standalone Animation with `cap.scene-production`. A request explicitly limited to style guidance needs no execution mode; an explicit different mode takes precedence.

The parent gathers the objective, mode, operation, scene/source, style, character inputs, and output constraints. It does not own visual techniques, invent a default scene, replace canonical character assets, or claim unsupported invocation behavior.

### 2.2 Capabilities

**APPROVED DESIGN:** Capabilities define operations, not output types or visual presentation. The initial operation set is:

- **Scene production:** create or implement scene content in a selected production mode.
- **Video breakdown:** produce an evidence-based source-video analysis and handoff.
- **Character creation:** create a character asset from user-provided appearance inputs.
- **Canonical character integration:** inspect and reuse supplied canonical character HTML without replacing it with a lookalike.
- **Scene assembly:** assemble justified scene modules for Modular Film.

Capabilities may be selected explicitly or by hybrid routing when the request makes the operation clear. A capability may be implemented by a portable skill definition, an executable tool, or both; those implementation forms must be declared separately.

Operation capabilities have stable `capability_id` values, but are not automatically standalone skills or slash commands. A capability becomes an independent skill only when it has a distinct reusable invocation contract. Otherwise it is described by the parent/mode skill and may refer to a shared TSA protocol. Shared TSA protocols are reference material by default, not executable skills requiring registration.

### 2.3 Visual-style skills

**APPROVED DESIGN:** A visual-style skill defines presentation techniques: visual characteristics, materials, lighting, camera treatment, and appropriate animation behavior. It receives the user's scene requirements and does not provide required story content.

Style specifications must not hardcode example characters, environments, actions, or storylines. User requirements take precedence over illustrative examples. A style must not silently alter canonical character identity.

Only one primary visual style is supported in the initial design. Automatic style mixing is not supported; it may be considered as a future capability.

**VERIFIED FACT:** `sub skill.txt` contains ten style prompt examples. They are source material, not separate executable skills.

**PROPOSED FUTURE CAPABILITY:** Style skill IDs and invocation aliases are separate. Candidate IDs and aliases are documented in `VSKILLS_SKILL_CONTRACT.md`; every slash alias remains proposed until implemented and tested.

### 2.4 Shared TSA protocols

**APPROVED DESIGN:** Shared protocols own cross-cutting evidence handling, source preservation, scoped execution, error reporting, validation status, and handoff. Existing TSA documents remain references; this architecture does not rewrite or supersede them.

## 3. Production modes and output contracts

### 3.1 Standalone Animation

- **APPROVED DESIGN — purpose:** Produce one autonomous animation from a user-defined scene.
- **Inputs:** Scene requirements, selected capability/style, optional character assets, and user-specified output constraints.
- **Output:** Requested standalone animation artifact, execution/dependency record, known limitations, and evidence-based validation statuses.
- **Ownership:** Scene production owns scene behavior and runtime; style owns presentation; character capabilities own character assets.
- **Duration:** User-defined; no global duration is imposed.
- **Validation:** Static/dependency checks, plus browser/runtime and visual checks when available.

Three.js is used for genuinely 3D scenes. Canvas, CSS, SVG, or another suitable browser technology may be used where appropriate. No single output technology or format is forced.

### 3.2 Modular Film

- **APPROVED DESIGN — purpose:** Produce a film using justified, independently testable scene modules and an assembly/handoff contract.
- **Inputs:** User script, source video, or approved breakdown; one primary style at most; character/assets; film and output requirements.
- **Output:** Scene plan and boundaries; scene artifacts; manifest/sequence; assembly/master artifact; continuity/handoff records; validation report.
- **Ownership:** Scene production owns decomposition and local timelines; scene assembly owns sequencing and cross-scene handoff; style remains presentation-only.
- **Duration:** The complete modular film is limited to 15 minutes. This is not a per-scene limit.
- **Validation:** Coverage and timeline integrity, module and assembly contracts, asset/handoff integrity, and full playback/visual checks when available.

Do not split every shot into a separate module by default. Preserve scene continuity and justify module boundaries.

### 3.3 Character Asset

- **APPROVED DESIGN — purpose:** Produce or prepare a reusable character asset independent of a particular film scene or game mechanic.
- **Inputs:** Determined by the selected character capability: an image for image-to-Three.js creation, or canonical source HTML and the user's preservation intent for canonical integration/construction.
- **Output:** Requested reusable asset; applicable source audit; dependency record; implementation/deviation report; evidence-based fidelity, geometry, hierarchy, animation, and runtime statuses.
- **Ownership:** Character creation owns new character construction; canonical character integration owns source inspection and faithful reuse. Scene placement and story-level behavior belong to the selected scene-production capability.
- **Duration:** Not applicable as a production-mode limit.
- **Validation:** Verify only the relevant source/image fidelity, geometry, hierarchy, pivots, requested motion, and runtime. Browser/visual checks are not PASS unless actually performed.

Character Asset is a **production mode (output type)**, not a capability. It normally composes with Character Creation or Canonical Character Integration. Those capabilities may also be used within Standalone Animation or Modular Film.

## 4. Character authority

**APPROVED DESIGN — canonical HTML:** Inspect the actual source and preserve identity, geometry, hierarchy, pivots, materials, and compatible runtime conventions. Do not substitute lookalikes. A style must not silently alter canonical character identity.

**APPROVED DESIGN — image-to-Three.js creation:** User-provided images define appearance. Existing canonical HTML is optional implementation guidance and is not required when absent.

If source authority is ambiguous or inputs conflict, clarify before proceeding. Preserve the user's explicit source-of-truth declaration.

## 5. Composition and precedence

**APPROVED DESIGN:** Compose a request as:

1. User goal, explicit constraints, and source authority.
2. One production mode, selected by the user or hybrid routing.
3. Required operation capability/capabilities.
4. Zero or one primary visual style.
5. Shared TSA protocols and mode/capability validation.
6. Executable tool(s), then a host adapter only when needed and supported.

The mode owns output type; capabilities own operations; style owns presentation. Explicit user requirements take precedence. Surface conflicts; do not silently merge or override them.

## 6. Portable architecture and rendering

**APPROVED DESIGN:** Keep vendor-independent skill definitions, metadata/contracts, executable tools, and host-specific agent adapters separate. Native slash-command support must be verified for each host. An adapter may expose only verified host behavior and must report limitations.

Choose rendering technology according to actual requirements: Three.js for genuinely 3D scenes; Canvas, CSS, SVG, or another suitable browser technology where appropriate. Do not force Three.js on every style or silently replace a canonical runtime architecture.

Prefer minimal dependencies and document all required dependencies. Do not claim offline support without verification. Preserve compatibility with supplied canonical sources when required.

## 7. Extensibility, naming, and remaining unknowns

**APPROVED DESIGN:** Future skill definitions conform to `VSKILLS_SKILL_CONTRACT.md`. Skill IDs are distinct from invocation aliases. Public documentation should prefer descriptive names. “PS2” is a descriptive visual-era reference, not a claim of Sony affiliation or endorsement.

**PROPOSED FUTURE CAPABILITY:** Style definitions and aliases listed in the skill contract, executable tools, host adapters, and native invocations remain unimplemented until separately built and tested.

**UNKNOWN:** Registry serialization/format, host-by-host command support, selected adapters, distribution and licensing checks, and any offline-support claim. No registry or serialization format is selected in this phase.

Resolution and host behavior are specified in `VSKILLS_INVOCATION_CONTRACT.md`; directory and progressive-reference behavior are specified in `VSKILLS_SKILL_LAYOUT.md`. Public naming and licensing review remain pending distribution work.

# TSA VSkills Usage Design

**Document status:** APPROVED usage design; all commands, aliases, routing, and adapters remain unimplemented.  
**Date:** 2026-11-09

## Status labels

- **APPROVED DESIGN** — approved user experience, not working software.
- **VERIFIED IMPLEMENTATION** — executable behavior actually implemented and tested; none is established here.
- **PROPOSED FUTURE CAPABILITY** — planned command, skill, tool, or adapter not yet implemented and tested.
- **UNKNOWN** — unresolved or unverified behavior.

## 1. Design goals

**APPROVED DESIGN**

- Keep production mode (output type), capability (operation), and visual style (presentation) separate.
- Let the user define arbitrary scene content independently from a style.
- Use hybrid routing through `/vskills`.
- Preserve canonical character sources and distinguish image-based creation from canonical reuse.
- Report host support and validation limits honestly.

**VERIFIED FACT:** `sub skill.txt` contains fixed scene examples and repeated format constraints. They are illustrative source material, not VSkills defaults.

## 2. Hybrid routing and proposed aliases

**APPROVED DESIGN:** `/vskills` follows hybrid routing:

- No arguments: discover and explain available capabilities.
- Explicit recognized skill alias: select that requested skill.
- Sufficiently clear task: select the appropriate production mode and compatible capability.
- Material ambiguity: request clarification.
- Explicit user requirements are never silently overridden.
- If an explicit visual-style alias includes a clear scene but omits a mode, default to Standalone Animation with `cap.scene-production`. If the user explicitly asks only for style guidance, return guidance without selecting an execution mode. An explicit different mode takes precedence.

**PROPOSED FUTURE CAPABILITY:** Every slash-form below is an unimplemented alias, not a claim of native support.

| Skill ID | Descriptive style | Proposed alias |
|---|---|---|
| `vskills.parent` | TSA VSkills | `/vskills` |
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

Skill IDs identify definitions and are distinct from aliases. The remaining style names come from `sub skill.txt`; public naming/licensing review is pending. “PS2” is a descriptive visual-era reference, not a claim of Sony affiliation or endorsement.

### Proposed usage examples — not implemented

All examples are documentation only. The alias syntax, hybrid routing, and execution behavior below are not implemented or tested.

Discover capabilities:

```text
/vskills
```

Select a requested style and produce a user-defined animation:

```text
/vidmindi "<freely defined user scene>"
```

With a clear user-provided scene, the direct style alias defaults to Standalone Animation and `cap.scene-production`; a production mode need not be restated unless the user explicitly requests guidance only or another mode.

Apply Retro PS2 presentation while reusing a canonical character:

```text
/vidps2 scene="<user-defined scene>" character_html="<canonical character HTML>"
```

Use the parent for a sufficiently clear task; it selects a mode and operation:

```text
/vskills "Create an autonomous animation of <user-defined scene> using a pixel-art treatment."
```

Create a new Three.js character from an image:

```text
/vskills mode=character-asset capability=character-creation image="<user-provided character image>" output="Three.js character asset"
```

Break down and assemble a source-based film:

```text
/vskills mode=modular-film capabilities=video-breakdown,scene-production,scene-assembly source="<user-provided source>" style=/vidps2
```

These examples show distinct dimensions: `mode` determines output type, `capability`/`capabilities` determine operations, and a style alias determines presentation.

Further resolution, error, and host-layer rules are in `VSKILLS_INVOCATION_CONTRACT.md`. Portable skill directories and manual invocation are specified in `VSKILLS_SKILL_LAYOUT.md`.

## 3. Input and source behavior

**APPROVED DESIGN**

- The user may provide any setting, story, action, cast, or environment; no sample scene is preselected.
- Scene content is independent from style instructions. Do not hardcode example characters, environments, actions, or storylines in a style.
- User requirements take precedence over illustrative examples and style convenience.
- Existing canonical HTML must be inspected and preserved when selected as the source of truth; image-based creation uses the user image to define appearance, with existing HTML optional.
- If an absent input prevents a meaningful choice—or source authority conflicts—ask a focused clarifying question.
- Reuse an adequate existing breakdown after auditing it rather than automatically repeating analysis.
- A host-specific adapter explains supported file/attachment input; no universal attachment API is assumed.

## 4. Mode contracts and rendering

All contracts are **APPROVED DESIGN**, not VERIFIED IMPLEMENTATION.

| Production mode | Expected result |
|---|---|
| Standalone Animation | Requested autonomous animation artifact, supporting files, run/dependency notes, and validation status. Scene and duration remain user-defined. |
| Modular Film | Scene plan/modules, manifest, handoffs, requested master assembly, and coverage/integration/playback status. Complete film duration is at most 15 minutes; this is not a per-scene limit. |
| Character Asset | Reusable asset, applicable source audit, dependency/deviation record, and fidelity/geometry/runtime status. No mandatory film scene. |

Choose a renderer according to actual requirements: Three.js for genuinely 3D scenes; Canvas, CSS, SVG, or another suitable browser technology where appropriate. Do not force Three.js on every style or silently replace a canonical runtime architecture. Prefer minimal dependencies, document required dependencies, and do not claim offline support without verification.

## 5. Capability composition

**APPROVED DESIGN**

1. Select one production mode (output type).
2. Select the operation capability/capabilities.
3. Apply zero or one primary visual style.
4. Apply shared TSA rules and mode/capability validation.
5. Use executable tools and host adapters only when available and declared.

Character Asset is a mode, not a capability: it composes with Character Creation or Canonical Character Integration. Those operations may also be used within other modes. Video Breakdown can produce source analysis for Modular Film; Scene Assembly owns module sequencing. Only one primary visual style is supported initially; automatic style mixing is not supported.

## 6. Status and failure response

The design requires future invocations to report:

- Selected mode, operations, and primary style, each with design/implementation and host-support status.
- Missing inputs or assumptions that affect the outcome.
- Files actually produced and their exact paths, if file output is supported.
- Checks run with `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED` and concise evidence.
- Unsupported host features, unavailable dependencies, or unresolved conflicts.

**VERIFIED IMPLEMENTATION:** None of the proposed commands or routing behavior is implemented or tested.  
**UNKNOWN:** Native slash-command support, attachment syntax, output-link behavior, and host-specific parsing must be verified separately for each agent.

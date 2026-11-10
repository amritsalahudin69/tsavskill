# TSA VSkills — Verified Knowledge and Decision Ledger

**Status:** RECOVERED / RECONSTRUCTED — not a byte-for-byte recovery of the original missing document  
**Recovery date:** 2026-11-10  
**Evidence hierarchy:** (1) current supplied `tsavskill.tar` file contents; (2) earlier user-provided command output and agent reports; (3) approved architectural proposals. Label each separately.

## 1. Snapshot-grounded facts (VERIFIED FROM TAR)

- The root contains `.github/skills/vskills/SKILL.md` and `.github/skills/vidmindi/SKILL.md`, alongside `README.md`, `.gitignore`, and five design documents (`VSKILLS_ARCHITECTURE.md`, `VSKILLS_SKILL_CONTRACT.md`, `VSKILLS_INVOCATION_CONTRACT.md`, `VSKILLS_SKILL_LAYOUT.md`, `VSKILLS_USAGE_DESIGN.md`).
- The root also contains `sub skill.txt`, the two canonical character prompts, and `video TSA skill/` source protocols and video-breakdown templates. The source directory is present as extracted files.
- `VSKILLS_TSA_STATE.md` and `VSKILLS_TSA_KNOWLEDGE.md` were absent in the archive before reconstruction.
- `.gitignore` contains exact root-anchored ignores `/VSKILLS_TSA_STATE.md` and `/VSKILLS_TSA_KNOWLEDGE.md`. It also excludes unreviewed original source materials and common secrets/caches. Ignore rules do not automatically synchronize files between PCs or delete files.
- Both SKILL.md files use YAML frontmatter with `name` and `description`.
- The parent discovery marker is `TSA_VSKILLS_DISCOVERY_MARKER: VSKILLS_PARENT_2A`.
- The child discovery marker is `TSA_VIDMINDI_DISCOVERY_MARKER: VIDMINDI_CHILD_2B`.
- The child declares `style.miniature-diorama` as stable VSkills ID, `vidmindi` as Copilot skill name, and `vskills` as logical parent. These are documented declarations, not evidence of an automated registry.
- At the snapshot point before Phase 2B-R, the parent SKILL.md still said no visual-style child had been created, despite the child file being present.
- The README and child SKILL.md say the original `sub skill.txt` is absent, but it is present in this snapshot. This is stale provenance wording.
- The README documents two *proposed installation methods*: GitHub CLI `gh skill` and manual copying to `.github/skills/`. Its remote install commands and cross-project installation are described as not tested.

## 2. Evidence from earlier user/agent reports (REPORTED, NOT RE-RUN)

- Phase 2A: GitHub Copilot CLI 1.0.107 reportedly listed `vskills` and a separate prompt-mode invocation returned its marker and three production modes.
- Phase 2B: GitHub Copilot CLI 1.0.107 reportedly listed both `vskills` and `vidmindi`; a separate child prompt reportedly returned the child marker and miniature-diorama techniques while preserving the user's RC-excavator scene.
- Parent-first invocation in Phase 2B reportedly identified the installed child's name but not its stable ID; reliable parent-to-child routing remained BLOCKED.
- Interactive `/skills reload`, `/skills list`, `/skills info` were not proven by those earlier tests.
- Earlier Git logs showed local/remote histories merged at `cf3114c` and pushed to `origin/main`. No claim is made about the present office Git state or later commits.
- The user reports that the files were developed at home and were missing after moving to the office machine; the ignore rules explain why Git did not transfer those untracked records.

## Current live-checkout evidence (2026-11-10)

- Commit at the start of Phase 2B-R: `d32bdafd21a3ce9ed0daab37b961379810e3a735` (`pahse2a-r`).
- The live Git audit found no staged paths. Existing unstaged changes were preserved; no files outside the 2B-R allowlist were edited.
- The updated parent identifies `style.miniature-diorama`, alias `/vidmindi`, at `.github/skills/vidmindi/SKILL.md`.
- The parent was aligned in Phase 2B-R to distinguish visual-style guidance from video generation and to leave other visual styles unimplemented.
- The host skill loader successfully loaded `vidmindi`; the loaded instructions contain `TSA_VIDMINDI_DISCOVERY_MARKER: VIDMINDI_CHILD_2B`.
- A parent-first manual instruction test established selection and child loading only. It does not prove a native `/vidmindi` command, automated router, scene renderer, or video-generation runtime.
- The state documents are untracked but not ignored. No scene/video files were generated; no staging, commit, push, `.gitignore` edit, or automatic cross-PC sync was performed.

## 3. Approved design — not proven execution

### 3.1 Core dimensions

- **Production modes:** Standalone Animation, Modular Film, Character Asset. Character Asset is a **mode**, not the character-generation operation itself.
- **Operation capabilities:** scene production, video breakdown, character creation, canonical character integration, scene assembly.
- **Visual style:** presentation technique; Miniature Diorama (`style.miniature-diorama`) is one style, not a fixed script or environment.
- Each request has at most one primary style in the initial design; mixing styles is deferred.
- `/vskills` is designed for hybrid routing (discover, explicitly select, infer a clear capability, or clarify material ambiguity). Native slash command registration is not established.

### 3.2 Scene and source authority

- User-supplied scene/characters/actions/environment are not replaced by the scenes in example prompts.
- For supplied canonical HTML, inspect and preserve actual geometry, proportions, hierarchy, pivots, materials, facial identity, and compatible runtime. No screenshot-based approximation is a substitute when canonical source is available.
- For creating a new character from a user image, the image supplies appearance identity; prior TSA character HTML is optional implementation guidance unless the task explicitly requires canonical reuse.
- When source and style conflict, report the conflict and use the smallest compatible and reversible approach.

### 3.3 Output modes and limits

- Standalone Animation: one autonomous artifact; duration/aspect ratio defined by user or task, not forced to eight seconds or 9:16.
- Modular Film: scene modules and assembly handoffs; maximum complete film duration is **15 minutes**, not 15 minutes per scene.
- Character Asset: reusable HTML/Three.js character when requested, with source, fidelity and runtime validation.
- Three.js is appropriate for genuine 3D; avoid mandating it for inherently 2D visual techniques.
- Style instruction alone is not a scene generator or renderer. Never mark HTML/video execution PASS on the basis of guidance or a marker.

### 3.4 Invocation and skill layout

- Logical parent `vskills`; physical Copilot project skill directories are siblings: `.github/skills/vskills/` and `.github/skills/vidmindi/`.
- Stable IDs are distinct from skill directory names and intended user aliases `/vskills` and `/vidmindi`.
- Portability goal: core instructions and manual fallback must remain usable without a Python router; host-specific adapters are independent and require host-by-host testing.
- Skill loading should be progressive: selected skill instructions and only relevant reference files; do not indiscriminately ingest all protocols.

## 4. Key original source materials and their roles

| Source in snapshot | Role | Publication status |
| --- | --- | --- |
| `sub skill.txt` | Ten visual-style prompt examples, including Miniature Diorama and Retro PS2; examples are not mandatory scene content | Rights/attribution review pending |
| `TSA_Master agent CANONICAL_3D_CHARACTER_BUILD_PROMPT_v1.0.0.md` | Canonical HTML-based character-build baseline | Rights/attribution review pending |
| `TSA_Mater web CANONICAL_3D_CHARACTER_CHAT_PROMPT_v1.0.1.md` | Image-to-Three.js character creation | Rights/attribution review pending |
| `video TSA skill/TSA_Canonical_Character_to_Scene_Integration_Protocol_v1.0.0.md` | Canonical source integration and preservation | Rights/attribution review pending |
| `video TSA skill/TSA_HTML_Game_Video_Production_PROTOCOL_v1.0.0.md` | HTML/game/video development protocol | Rights/attribution review pending |
| `video TSA skill/TSA_HTML_SCENE_MODULARIZATION_AND_ASSEMBLY_PROTOCOL_v1.0.0.md` | Modular scene and assembly specification | Rights/attribution review pending |
| `video TSA skill/video/TSA_Video_Breakdown_Protocol_v1.0.0/` | Source-video analysis, templates, and handoff | Rights/attribution review pending |

The archive contains these source materials, but this does not establish that they may all be redistributed publicly. Preserve them locally until provenance is resolved.

## 5. Proven vs. unproven capability matrix

| Capability | Evidence | Status |
| --- | --- | --- |
| Parent skill file exists and identifies the installed child | Updated parent instructions, inspected in live checkout | VERIFIED INSTRUCTIONS |
| Child `vidmindi` skill file exists | Tar inspection | VERIFIED FILE |
| Parent and child skill discovery | Successful host skill-loader responses | PASS for instruction discovery |
| Parent-to-child stable-ID selection | Updated parent guidance and parent-first manual test | PASS for instruction-level selection |
| Child instruction loading | Host loaded child and returned its diagnostic marker | PASS |
| Standalone native `/vidmindi` command | No test/evidence | NOT IMPLEMENTED / NOT VERIFIED |
| GitHub remote-install workflow | README documents but no end-to-end test | NOT_TESTED |
| Skills on Codex/Claude/Gemini | No adapter tests | NOT_TESTED |
| HTML scene/video renderer | Not present in scoped skill files | NOT IMPLEMENTED |
| Character generator / Python router | Not present in scoped skill files | NOT IMPLEMENTED |

## 6. Known inconsistencies and risks

1. **Cross-PC knowledge loss:** ignoring state/knowledge caused their omission from ordinary Git synchronization. A deliberate transfer policy is needed.
2. **Resolved:** parent now describes Miniature Diorama child identity, installed path, host selection, and capability boundary.
3. **Stale source statement:** current README and child say `sub skill.txt` absent, although it is in the snapshot. Correction requires an authorized scope change; do not silently alter child in 2B-R.
4. **Privacy:** private machine paths and unreviewed source materials should not be committed by default. These reconstructed files deliberately omit exact local user paths.
5. **Live Git state:** the Phase 2B-R audit found no staged changes and recorded the starting commit; unrelated existing unstaged work was preserved. This does not establish remote synchronization.
6. **Host portability:** GitHub Copilot discovery does not imply support for all agents.
7. **TSA discipline:** all edits must be small, auditable and reversible; tests cannot be inferred from source structure alone.

## 7. Repository continuity policy — pending decision

**Option A — Recommended for cross-PC Git workflow:** Treat state/knowledge as sanitized, shareable engineering ledgers; remove their two entries from `.gitignore` in an approved scoped patch, audit for paths/secrets/third-party content, and explicitly track them. Future agents can read/update them on each machine. This decision is **not yet implemented**.

**Option B — Private local ledgers:** Retain ignore rules and use an explicit private transfer mechanism or reconstruct state from tracked, public documentation and actual tests at each location. Never assume ignored files come from `git pull`.

## 8. Rules for the next agent turn

1. Phase 2B-R is complete. Preserve child `vidmindi/SKILL.md`, README, `.gitignore`, all canonical sources, Git index, and history.
2. Report parent-to-child selection separately from actual child instruction loading and runtime execution.
3. Do not infer native slash-command registration, automated routing, or video/HTML execution from a successful skill load.
4. Do not start Phase 2C, stage, commit, push, or automatically sync local records without separate authorization.

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

## Phase 2B-R live-checkout evidence (2026-11-10)

- Commit at the start of Phase 2B-R: `d32bdafd21a3ce9ed0daab37b961379810e3a735` (`pahse2a-r`).
- The live Git audit found no staged paths. Existing unstaged changes were preserved; no files outside the 2B-R allowlist were edited.
- The updated parent identifies `style.miniature-diorama`, alias `/vidmindi`, at `.github/skills/vidmindi/SKILL.md`.
- The parent was aligned in Phase 2B-R to distinguish visual-style guidance from video generation and to leave other visual styles unimplemented.
- The host skill loader successfully loaded `vidmindi`; the loaded instructions contain `TSA_VIDMINDI_DISCOVERY_MARKER: VIDMINDI_CHILD_2B`.
- A parent-first manual instruction test established selection and child loading only. It does not prove a native `/vidmindi` command, automated router, scene renderer, or video-generation runtime.
- The state documents are untracked but not ignored. No scene/video files were generated; no staging, commit, push, `.gitignore` edit, or automatic cross-PC sync was performed.

## Phase 2C-1 live-checkout evidence (2026-11-10)

- Repository root was confirmed with `git rev-parse --show-toplevel`; branch `main`; starting commit `6aff20f9291cd9fd5c0160c45300172a927bb993`.
- Starting index had no staged paths and `git status` had no untracked paths. Nine pre-existing tracked worktree modifications were present: both skill files, `.gitignore`, `README.md`, and the five existing VSKills design documents. They were preserved.
- `VSKILLS_HTML_EXECUTION_CONTRACT.md` and `VSKILLS_RUNTIME_VALIDATION_CONTRACT.md` did not exist before this phase. The state and knowledge files had no starting worktree modifications.
- Located and inspected relevant sections of `video TSA skill/TSA_HTML_Game_Video_Production_PROTOCOL_v1.0.0.md`, `video TSA skill/TSA_Canonical_Character_to_Scene_Integration_Protocol_v1.0.0.md`, and `video TSA skill/TSA_HTML_SCENE_MODULARIZATION_AND_ASSEMBLY_PROTOCOL_v1.0.0.md`.
- Read only the Miniature Diorama entry in `sub skill.txt`. It evidences one example's tabletop/model treatment, tilt-shift, lighting, scale prop, and camera motion; those example-specific scene, cast, props, format, duration, and loop are not universal style requirements.
- Created the two proposed contract documents and updated only this ledger and `VSKILLS_TSA_STATE.md`. No engine, parser, HTML, scene, screenshot, animation, or browser runtime was created or run.
- This checkout contains `sub skill.txt`, despite older README/child wording that described it as absent. The child and README were kept unchanged as required.

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
| Parent and child skill discovery | Copilot CLI 1.0.108 `copilot skill list` lists `vskills` and `vidmindi` as project skills; both instruction files loaded in this session | PASS for discovery/loading evidence; not execution |
| Parent-to-child stable-ID selection | Updated parent guidance and parent-first manual test | PASS for instruction-level selection |
| Child instruction loading | Host loaded child and returned its diagnostic marker | PASS |
| HTML/Three.js execution contract | Phase 2C-1 contract documents | PROPOSED DESIGN; not implemented |
| Runtime/visual validation gates | Phase 2C-1 validation contract | PROPOSED DESIGN; no infrastructure tested |
| Standalone native `/vidmindi` command | No test/evidence | NOT IMPLEMENTED / NOT VERIFIED |
| GitHub remote-install workflow | README documents but no end-to-end test | NOT_TESTED |
| Skills on Codex/Claude/Gemini | No adapter tests | NOT_TESTED |
| Reusable HTML/Three.js scene-production instructions | `.github/skills/scene-production/SKILL.md` plus one independent railway fixture; static parse, CDN endpoint, and local HTTP passed | IMPLEMENTED INSTRUCTIONS; browser/runtime/visual/motion not tested; arbitrary-scene reliability unproven |
| Scene-production skill discovery | Copilot CLI 1.0.108 `copilot skill list` lists `scene-production`; the separate session `functions.skill` loader did not find it | PASS for native CLI project discovery; tool-adapter behavior differs; no execution implied |
| Parent composition of production capability and style | Updated parent and manual delivery-truck/bridge/village request test | PASS for guidance and user-scene preservation; no artifact or automatic routing tested |
| Automatic HTML/video generator or export engine | No generator or MP4 exporter was created; scene instructions require manual implementation | NOT_IMPLEMENTED |
| Character generator / Python router | Not present in scoped skill files | NOT IMPLEMENTED |
| Miniature Diorama HTML fixture | `tests/fixtures/vidmindi-lunar-outpost/index.html`; static and local HTTP checks passed; user manually confirmed browser rendering and motion | IMPLEMENTATION COMPLETE; USER-OBSERVED MANUAL PASS; agent automation incomplete |

## 6. Known inconsistencies and risks

1. **Cross-PC knowledge loss:** ignoring state/knowledge caused their omission from ordinary Git synchronization. A deliberate transfer policy is needed.
2. **Resolved:** parent now describes Miniature Diorama child identity, installed path, host selection, and capability boundary.
3. **Source-note discrepancy:** this checkout contains `sub skill.txt`, and its Miniature Diorama entry was inspected for Phase 2C-1. README and child source-note text still reflects an earlier snapshot; they were not modified because they are outside this phase's scope.
4. **Privacy:** private machine paths and unreviewed source materials should not be committed by default. These reconstructed files deliberately omit exact local user paths.
5. **Live Git state:** Phase 2C-1 began at `6aff20f9291cd9fd5c0160c45300172a927bb993` on `main`, with no staged/untracked paths and nine existing unstaged changes. Those changes were preserved. This does not establish remote synchronization.
6. **Host portability:** GitHub Copilot discovery does not imply support for all agents.
7. **TSA discipline:** all edits must be small, auditable and reversible; tests cannot be inferred from source structure alone.

## 7. Repository continuity policy — pending decision

**Option A — Recommended for cross-PC Git workflow:** Treat state/knowledge as sanitized, shareable engineering ledgers; remove their two entries from `.gitignore` in an approved scoped patch, audit for paths/secrets/third-party content, and explicitly track them. Future agents can read/update them on each machine. This decision is **not yet implemented**.

**Option B — Private local ledgers:** Retain ignore rules and use an explicit private transfer mechanism or reconstruct state from tracked, public documentation and actual tests at each location. Never assume ignored files come from `git pull`.

## 8. Rules for the next agent turn

1. Preserve existing skill files, README, `.gitignore`, architecture/contracts, canonical sources, Git index, and unrelated worktree changes unless later explicitly authorized.
2. Phase 2C-2 is one Lunar Outpost implementation proof with user-observed manual browser validation; agent automation remains incomplete.
3. Phase 2C-3 added instruction-only `cap.scene-production` and one independent railway fixture. Static and local HTTP checks passed; railway browser runtime, visual fidelity, and motion were not tested.
4. Copilot CLI 1.0.108 `copilot skill list` verified `vskills`, `vidmindi`, and `scene-production` as project skills. This does not establish automatic parent routing or execution; the separate session skill tool did not find `scene-production`.
5. Phase 2C-4 updated parent composition guidance and manually tested scene preservation without creating an artifact. Do not start Phase 2D or add a generator, style, or execution infrastructure without explicit authorization.

## 9. Phase 2C-2 live-checkout evidence (2026-11-10)

- Baseline recorded before implementation: repository root confirmed, branch `main`, starting commit `6aff20f9291cd9fd5c0160c45300172a927bb993`; the prior audit recorded no staged or untracked paths and nine pre-existing unstaged tracked changes. Those changes were preserved. The final audit shows the two Phase 2C-1 contract files as untracked; they were not edited in this phase, and when they appeared relative to the baseline is unverified. No files outside the authorized paths were edited.
- The `vskills` parent and `vidmindi` child instructions were already loaded in the active host context and used. The child identifies as stable ID `style.miniature-diorama`, skill name `vidmindi`, intended alias `/vidmindi`, at `.github/skills/vidmindi/SKILL.md`. No fresh skill-loader event occurred during this phase; context use does not prove native slash-command registration or automated routing.
- Copilot CLI version: **1.0.108**. Node.js **v24.15.0** and npm **11.12.1** were available. No Linux browser was found on `PATH`; subsequent Windows inspection found Chrome **154.0.8037.93** and Edge **157.0.4341.42**.
- Created `tests/fixtures/vidmindi-lunar-outpost/index.html`; modified this ledger and `VSKILLS_TSA_STATE.md`. No fixture runtime support files were created; the three PNGs listed below are validation captures only.
- The fixture declares a network ES-module dependency on Three.js **0.187.0**, sourced from `https://cdn.jsdelivr.net/npm/three@0.187.0/build/three.module.js`. The exact endpoint returned HTTP 200, `application/javascript`, and `Access-Control-Allow-Origin: *`. Offline availability and direct `file://` loading were not tested.
- The standalone HTML uses real procedural Three.js geometry: relief terrain and a circular display base, a volumetric habitat, articulated six-wheel rover with tread detail, rocks/craters/tracks, Earth, and a tracking dish. A 4:3 landscape camera and physical-model material/light treatment target a miniature-diorama appearance. No external assets, build system, or extra package dependency is used.
- Animation is a six-second, elapsed-time-driven deterministic one-shot. The rover travels a curved route; wheel rotation follows its travel; the camera arcs slightly; the dish tracks a subtly moving Earth target. Earth drift is an explicit minimal assumption to make tracking observable. User-observed manual validation confirmed the rendered style and rover/wheel motion; agent automation did not independently verify them.
- Static validation: the embedded module passed `node --check --input-type=module`. Local HTTP validation previously returned HTTP 200. Windows also reached the WSL-served fixture at `http://127.0.0.1:18765/` with HTTP 200.
- **USER-OBSERVED MANUAL PASS:** the user confirmed that the scene rendered in a browser; rover and habitat were visible; objects had real 3D volume; Miniature Diorama appearance was recognizable; the rover changed position; its wheels rotated; and no critical errors appeared in the DevTools Console. The user did not report browser/version, viewport, or screenshot paths.
- Agent automation was incomplete. Headless Windows Chrome **154.0.8037.93** produced three captures at `tests/fixtures/vidmindi-lunar-outpost/phase-2c-2r-t0.png`, `phase-2c-2r-t3.png`, and `phase-2c-2r-t5p8.png` (each 1280x960). The CLI virtual-time budgets did not independently verify animation timestamps; do not treat these images as automated motion evidence or automated visual PASS. A subsequent CDP-based motion-capture attempt was interrupted by the user.
- Agent Chrome output logged the non-critical Three.js warning `PCFSoftShadowMap has been removed. Using PCFShadowMap instead.` The page rendered; the user separately reported no critical DevTools Console errors. A Chrome-managed web-app install error was unrelated browser-process noise.
- Fixture HTML was unchanged during closeout. Its closeout SHA-256 is `6f77064df0036ff28da564b6d22837383edbfb1d648820fff79be3cb673f3412`. No reusable universal generator or additional sub-skill was implemented or created.

### Phase 2C-2 validation status

| Gate | Status | Evidence / limitation |
| --- | --- | --- |
| 1 — Source | PASS | Lunar-outpost fixture and approved scene requirements followed; one minimal tracking-target assumption documented |
| 2 — Build | PASS | JavaScript syntax check and version-pinned CDN endpoint passed; user-observed browser rendering corroborates successful import |
| 3 — Runtime | PASS — USER-OBSERVED MANUAL | User confirmed the scene rendered with rover and habitat visible; browser/version not reported |
| 4 — Visual | PASS — USER-OBSERVED MANUAL | User confirmed volumetric objects and recognizable Miniature Diorama style |
| 5 — Motion | PASS — USER-OBSERVED MANUAL | User confirmed rover position changed and wheels rotated |
| Critical DevTools errors | PASS — USER-OBSERVED MANUAL | User reported none; agent automation did not complete a structured console audit |
| Agent browser/motion automation | BLOCKED / INCOMPLETE | Captures exist, but exact timestamps were not confirmed; CDP motion capture was interrupted |
| 6 — Delivery | PASS | Fixture exists, local run command is documented and HTTP-tested, dependency is declared, and outcomes are recorded |
| Full Phase 2C-2 acceptance | PASS — USER-OBSERVED MANUAL | Required runtime, visual, and motion outcomes were confirmed by the user; no automated visual/motion PASS is claimed |

## 10. Phase 2C-3 live-checkout evidence (2026-11-10)

- Phase 2C-3 began at the repository root (machine-specific path omitted), branch `main`, HEAD `6aff20f9291cd9fd5c0160c45300172a927bb993`. There were no staged paths. Pre-existing worktree changes—including both style/parent skills, README, `.gitignore`, design documents, both TSA ledgers, untracked execution/runtime contracts, Lunar Outpost fixture, and three earlier PNG captures—were preserved.
- Created `.github/skills/scene-production/SKILL.md`, `.github/skills/scene-production/references/html-threejs-workflow.md`, and `tests/fixtures/vidmindi-miniature-railway/index.html`; updated only this knowledge ledger and `VSKILLS_TSA_STATE.md`. The new target paths were absent beforehand. No parent/child skill, contract, Lunar fixture, README, or unrelated path was changed by this phase.
- The new capability is `cap.scene-production`, an operation skill separate from parent `vskills` and style `style.miniature-diorama`. It owns HTML/Three.js scene construction, time-based animation, packaging, runtime instructions, and six validation gates. The user owns scene content; visual style supplies presentation guidance. The skill is portable instructions, not executable scene-generation software.
- The active session skill loader returned “not found” for `scene-production` and omitted it from its available list. Manual reading of the skill and reference was used instead. `vskills` and `vidmindi` instructions were available, and their composition with the production capability was manual; no automated parent routing or native slash command was demonstrated.
- The railway fixture independently defines mountain terrain, a curved railway, a small train with independently rotating wheels, bridge, stream, trees, and rocks. It contains no Lunar Outpost terrain, rover, habitat, or lunar objects. Duration of 8 seconds, 4:3 aspect ratio, and play-once behavior are explicitly fixture assumptions, not capability defaults.
- The embedded module pins Three.js `0.187.0` from `https://cdn.jsdelivr.net/npm/three@0.187.0/build/three.module.js`; the exact endpoint returned HTTP 200. No package manifest or new package dependency was introduced. The embedded module passed `node --input-type=module --check`, and static checks confirmed the required objects/animation and absence of Lunar-specific terms.
- An isolated local HTTP server on port 18765 served the new fixture with HTTP 200 and expected content, then was stopped. An attempted use of port 8765 found it already occupied; that pre-existing service was left untouched and is not part of the validation evidence. Run command: `python3 -m http.server 8000 --bind 127.0.0.1 --directory tests/fixtures/vidmindi-miniature-railway`; open `http://127.0.0.1:8000/`. CDN use requires network access; offline and `file://` operation are unverified.
- No browser execution, WebGL observation, screenshot, visual inspection, or motion observation was performed for the railway fixture. The motion formula in source is not proof of rendered movement. All three browser-dependent gates remain NOT_TESTED.
- Reuse boundaries: renderer/canvas setup, resize handling, error reporting, a render lifecycle, and elapsed-time animation are source-proven generic patterns from the Lunar fixture, not a general reliability guarantee. Tabletop presentation, crafted materials, miniature proportions, and soft intentional lighting are style-specific. Lunar terrain, habitat, rover, Earth, dish, and their choreography are fixture-specific. Cross-browser resilience, arbitrary scene generality, WebGL recovery, and low-end performance remain unverified.
- No reusable universal generator, video exporter, additional style, or additional sub-skill was created. No staging, commit, or push occurred.

## 11. Phase 2C-4 parent-composition evidence (2026-11-10)

- Baseline: repository root (machine-specific path omitted), branch `main`, HEAD `6aff20f9291cd9fd5c0160c45300172a927bb993`; no staged paths. Pre-existing worktree changes and untracked Phase 2C-3 skills, contracts, fixtures, and captures were preserved.
- Modified only `.github/skills/vskills/SKILL.md`, `VSKILLS_TSA_STATE.md`, and this ledger. Created no files; did not change `vidmindi/SKILL.md`, `scene-production/SKILL.md`, either fixture, README, `.gitignore`, contracts, or original source material.
- The Phase 2C-4 starting status listed the fixtures as untracked. During final audit `.gitignore` contained `/tests`, causing Git to report both fixture directories as ignored. This was outside scope and was left untouched; no fixture content was modified.

## 12. Phase 2C-4R Git hygiene and portability audit

- Baseline was branch `main` at HEAD `6aff20f9291cd9fd5c0160c45300172a927bb993`, with no staged paths. Existing tracked modifications and untracked source/evidence files were preserved.
- The user had removed the broad `/tests` ignore rule before this phase. The `.gitignore` diff shows that removal; both fixture directories are now untracked and not ignored. The rule was not deleted or otherwise changed during this audit.
- Both TSA ledgers and all skill/contract/fixture paths pass `git check-ignore` (no matching rule). The ledgers are tracked in the index. The invocation contract is tracked; the HTML execution and runtime validation contracts are currently untracked but eligible for Git.
- Ignore protections continue to match original `video TSA skill/` files, `sub skill.txt`, `.env` and `.env.*` (except `.env.example`), PEM/key files, and `id_rsa`/`id_ed25519` names. No blanket PNG/JPG rule exists or was added.
- Publication classification: skills, references, contracts, docs, and fixture HTML are source candidates. Three prior PNG captures are evidence with unverified timing and are not required source; omit them from a minimal commit unless separately reviewed. No disposable server log/cache was found in the fixture directories. Original prompt/protocol materials remain private/restricted because redistribution rights are unresolved.
- The state/knowledge records contained the machine-specific WSL repository path; those occurrences were replaced with a repository-root description. The skill instructions and fixture run guidance use repository-relative paths. `README.md` remains unchanged and is stale: it describes two skills, old Copilot CLI 1.0.107 tests, and omits `scene-production`; its manual copy examples likewise omit the production skill.
- The fixture run commands are portable in concept from a fresh clone when run from the documented fixture/output directory; Three.js is pinned to 0.187.0 from jsDelivr and requires network access. No browser was launched. No project `LICENSE` is selected, and source-material redistribution rights remain unresolved, so Git eligibility is not public-release authorization.
- No `.gitattributes` file or `core.autocrlf`/`core.eol` setting is configured. Relevant text files have mixed LF and CRLF endings. `git diff --check` reports CRLF bytes as trailing whitespace in CRLF files; LF ledger checks pass. No files were normalized and no line-ending policy was added.
- This phase changed only the two TSA ledgers to sanitize local paths and record the audit. `.gitignore`, README, skills, references, fixtures, contracts, and evidence files were not edited; nothing was staged, committed, pushed, or deleted.

### Proposed minimal publication set

Subject to README correction and license/provenance approval, explicitly consider:

- `.gitignore`
- `.github/skills/vskills/SKILL.md`
- `.github/skills/vidmindi/SKILL.md`
- `.github/skills/scene-production/SKILL.md`
- `.github/skills/scene-production/references/html-threejs-workflow.md`
- `VSKILLS_INVOCATION_CONTRACT.md`
- `VSKILLS_HTML_EXECUTION_CONTRACT.md`
- `VSKILLS_RUNTIME_VALIDATION_CONTRACT.md`
- `VSKILLS_TSA_STATE.md`
- `VSKILLS_TSA_KNOWLEDGE.md`
- `tests/fixtures/vidmindi-lunar-outpost/index.html`
- `tests/fixtures/vidmindi-miniature-railway/index.html`

Hold `README.md` until its installed-skill claims and instructions are updated. Exclude the three PNG captures and all ignored original prompt/protocol material from a minimal publication commit. This is a proposed manifest only; no staging was performed.
- Copilot CLI **1.0.108** `copilot skill list` returned three project skills: `scene-production`, `vidmindi`, and `vskills`. This is direct project-skill discovery evidence for that CLI version. `copilot skill list` does not prove that the parent automatically selects children or that any selected instructions execute a scene. The separate session `functions.skill` tool did not find `scene-production`; record this as a tool-specific discrepancy rather than overriding the native CLI list result.
- Updated parent model: `vskills` orchestrates; `cap.scene-production` owns browser-scene implementation workflow; `style.miniature-diorama` via `vidmindi` owns presentation guidance. Keep the user scene authoritative and compose only the needed production operation with zero or one primary style.
- Manual test request: “Create a standalone Miniature Diorama HTML/Three.js animation of a small delivery truck crossing a wooden bridge in a mountain village.” Selected `mode.standalone-animation`, `cap.scene-production`, and `style.miniature-diorama`. The scene and crossing action were preserved; no Lunar Outpost or railway fixture content was substituted.
- The expected flow is user scene → production capability → visual style → scene workflow → validation. The production skill supplies implementation/run guidance; the style child adjusts presentation only. The six validation gates remain required for an actual implementation, and runtime, visual, or motion success must not be claimed without evidence.
- This was a composition-only test. No HTML, scene, video, or other artifact was created. No generator, native `/scene-production` command, registered native `/vidmindi` command, automatic universal router, browser execution, or arbitrary-scene reliability was demonstrated. Wait for authorization before Phase 2D.

## 13. Phase 2C-4S README alignment (2026-11-10)

- From the repository root, GitHub Copilot CLI 1.0.108 reported exactly three project skills with `copilot skill list`: `vskills`, `vidmindi`, and `scene-production`. The observed version documents the test environment only; no minimum version is specified.
- The README now distinguishes `vskills` as parent/orchestration guidance, `vidmindi` as the Miniature Diorama style, and `scene-production` as the HTML/Three.js implementation capability. The parent composition model keeps the user-defined scene authoritative and treats style selection as optional.
- The README hold recorded in the Phase 2C-4R proposed manifest is resolved by this alignment. Public release remains blocked on the separate license and provenance questions.
- Parent composition evidence is manual, not proof of a universal automatic router. Native `/vidmindi` and `/scene-production` slash-command registration remains unverified. Remote `gh skill` installation examples and manual cross-project copying are explicitly unverified.
- Lunar Outpost browser results are recorded as USER-OBSERVED MANUAL PASS: rendering, rover/habitat visibility, 3D volume, recognizable Miniature Diorama appearance, rover movement, wheel rotation, and no critical DevTools Console errors. They are not agent-automated results; browser automation and automated motion capture remain incomplete.
- Miniature Railway static checks and local HTTP smoke testing passed. Browser runtime, visual fidelity, and rendered motion remain unverified. Do not equate its smoke test with browser execution.
- Both fixtures use Three.js 0.187.0 from jsDelivr and require network access. The fixtures demonstrate bounded workflow evidence, not arbitrary-scene reliability.
- `scene-production` remains an instruction capability, not a generic scene generator; no MP4 exporter is implemented. No new style or skill was added.
- The README documents that no confirmed project license is present and original source-material redistribution rights remain unresolved. No license or source protocol was added or reproduced.
- This phase changed only `README.md`, `VSKILLS_TSA_STATE.md`, and this ledger. README's existing CRLF line endings were preserved; ledger files remain LF. No staging, commit, push, fixture change, or skill implementation change occurred.

## 14. Phase 2C-5R provenance and safe checkpoint preparation (2026-11-10)

- Verified baseline: branch `main`, HEAD `6aff20f9291cd9fd5c0160c45300172a927bb993`; public `origin/main` has the same SHA. The index is empty. GitHub reports the repository as PUBLIC and has no recognized license; no local LICENSE file exists.
- The ignored `sub skill.txt` exists in the development checkout and is not included in the `vidmindi` skill directory or Git. Corrected the child’s inaccurate “source unavailable” sentence to say the source is excluded and not required for installation/use. The skill remains self-contained; its stable ID and guidance are unchanged. Public HEAD still has the old sentence until a later authorized commit/push.
- The ignored original protocol package and canonical prompts have uncertain authorship/rights. Targeted public-history queries for the inspected source paths returned no commits; local history queries also found none. Existing design documents do refer to those source filenames, but they do not require the files to load the installed skills.
- Provenance classifications: README and ignore rules are PROJECT-AUTHORED; parent/style/production guidance and execution contracts are ADAPTED or AI-assisted project work; fixture HTML is project-created/AI-assisted with procedural geometry; original prompts/protocols remain UNCERTAIN; Three.js is THIRD-PARTY. No source license/attribution grant was identified in the targeted notice review. These classifications are evidence labels, not legal clearance.
- A selected-source exact 12-word-window scan and fixture long-line comparison found no substantial exact textual/code matches. This does not resolve distinctive paraphrase, AI-generated similarity, ownership, or redistribution rights. The `vidmindi` source note and the execution contract’s source references must remain explicit in future provenance review.
- Both HTML fixtures import only `three@0.187.0` from jsDelivr among external resources checked; no images, models, textures, fonts, or other imports were found. Three.js r187’s official license is MIT; it is not vendored.
- MIT is the recommended candidate for owner consideration because its notice burden is lighter for reusable cross-agent skills. Apache-2.0 is an alternative when an express contributor patent grant is important and the owner accepts additional notice/change obligations. Owner approval is pending; neither candidate can grant rights to unowned or uncleared source material.
- EOL facts: worktree Markdown/HTML mixes LF and CRLF; `core.autocrlf`/`core.eol` are unset and no `.gitattributes` exists. Parent, child, and README CRLF worktree content differs from LF HEAD blobs; several other tracked status changes are line-ending-only. No normalization was performed. Any future LF policy and migration require a separate authorization.
- Local checkpoint manifest: semantic README/parent/child/ledger changes, new production skill/reference and execution/runtime contracts, and the two fixture HTML files. Do not stage the PNG captures, ignored original materials, or line-ending-only diffs. The `.gitignore` worktree difference is blank-line-only.
- Public manifest remains conditional on rights and owner license choice. Hold the TSA ledgers from public distribution unless their embedded user-request and environment history is explicitly approved. Public HEAD content remains public regardless of future staging exclusions.
- Cross-PC recommendation: after an explicitly authorized local commit, use an offline Git bundle and verify its checksum. A private remote is viable only after privacy and access controls are verified. The current public `origin` must not be used as private synchronization.
- No files were staged, committed, pushed, bundled, or licensed. This phase only corrects the child’s factual source note and updates the state/knowledge records.

## 15. Phase 2D-1 Retro PS2 implementation (2026-11-10)

- The local ignored `sub skill.txt` contains a Retro PS2 style section. Its general visual direction informed the new guidance, but its specific scene example was not copied into the skill or fixture.
- `.github/skills/vidps2/SKILL.md` declares `style.retro-ps2`, name `vidps2`, and prompt alias `/vidps2`. Copilot CLI 1.0.108 listed it alongside `vskills`, `vidmindi`, and `scene-production`; this proves project-skill discovery in that environment, not native slash-command registration or automatic routing.
- The new style skill describes compatible low-to-moderate polygon density, era-inspired textures/materials, limited texture resolution, stylized lighting/shadows, camera/environment treatment, scene authority, visual criteria, and use with `cap.scene-production`. It has no default story or scene and provides no executable renderer.
- `tests/fixtures/vidps2-retro-garage/index.html` builds a garage, stylized sports car, tool cabinets, work lights, and ventilation fan from Three.js geometry. The car drives inward and the fan rotates. A follow-up in Phase 2D-1R added radial wheel-face details because the symmetric tire/rim surfaces made the original rotation visually indiscernible. It uses a generated 64x64 nearest-filter floor texture and only the Three.js 0.187.0 jsDelivr import. No external game assets or framework were introduced.
- `.github/skills/scene-production/scripts/validate_scene.py` uses only Python's standard library. It checks readable HTML, scene and camera construction, WebGL renderer initialization, render invocation, and an animation-loop indicator. It reports static structural findings only and exits nonzero when required patterns are absent.
- Verified checks: validator PASS for Lunar Outpost, Miniature Railway, and Retro Garage; negative validator case returned nonzero; Node.js syntax checks PASS for all three inline modules; local HTTP smoke request returned 200; Copilot CLI 1.0.108 listed all four project skills.
- Browser runtime, actual visual fidelity, and motion observation are NOT_TESTED because no browser executable was found. The local HTTP response does not imply browser or WebGL success. Manual verification remains required.
- No existing skill implementation, prior fixture, execution contract, README, or `.gitignore` was changed. Only `vidps2/SKILL.md`, the Retro Garage fixture, the generic validator, and the two TSA ledgers were changed for this phase. No staging, commit, or push occurred.

## 16. Phase 2D-1R Retro Garage wheel rotation repair (2026-11-10)

- Wheel geometry orientation was confirmed from source: `CylinderGeometry` begins with its axis on local Y; the tire and rim are each rotated 90 degrees around Z, so the wheel axle is X. Each wheel assembly remains a child of the car group at the original coordinates.
- The prior wheel angle used `distance / wheelRadius` around X, synchronized to the same eased traveled distance used for car translation. Smooth rotationally symmetric cylinders made the correct motion visually hard to perceive.
- Added three small radial spoke markers on each side of each rim, parented to the same wheel spinner as the tire/rim. No wheel positions, proportions, car geometry, car motion, camera, lighting, fan, or dependency version changed.
- The wheel angle remains distance-derived. The eased travel clamps at the drive endpoint, so wheel orientation stops changing when car translation stops.
- Checks: existing structural validator PASS; JavaScript syntax PASS; formula check PASS for initial rest, distance/angle relationship, car synchronization, and stationary angle after stopping. Browser-observed rotation remains NOT_TESTED.
- Only the Retro Garage fixture and the two TSA ledgers changed in this repair. No staging, commit, or push occurred.

## 17. Phase 2D-2 Cross-Style Production Test (2026-11-10)

- Added two independent HTML fixtures for the identical Mountain Bridge Delivery test scene: `tests/fixtures/cross-style-mountain-bridge/miniature-diorama/index.html` and `tests/fixtures/cross-style-mountain-bridge/retro-ps2/index.html`. Both import Three.js 0.187.0 from jsDelivr and construct their scenes with volumetric Three.js geometry.
- Scene-content parity: each includes one delivery truck, four articulated wheels, curved mountain road, wooden bridge, narrow stream below the bridge, roadside warehouse, mountain terrain, and limited vegetation. Both implement the same 8-second timeline, 16:9 framing, play-once behavior, and sequence of approaching, crossing the bridge, then stopping beside the warehouse. No HUD, subtitles, extra characters, or additional story events were introduced.
- Motion parity: both fixtures use identical Catmull-Rom route control points, bridge interval, drive duration, eased travel progress, and wheel radius. Truck position follows the route; visible wheel-face details rotate from traveled distance divided by wheel radius and remain stationary after truck motion ends.
- Miniature Diorama uses an orthographic camera, tabletop base, handmade terrain/environment treatment, textured road and bridge, warm light, and atmospheric/selective-focus presentation. Retro PS2 uses a perspective camera, low-poly terrain and angular forms, limited-resolution nearest-filter texture, stylized directional and fill light, and distance fog. The scene semantics and actions are held constant while visual implementations differ.
- Checks: the existing Python structural validator PASS for both fixtures; JavaScript module syntax PASS for both; basic required-object/action and framing checks PASS for both; cross-fixture route and test-constant parity PASS; local HTTP smoke tests PASS with HTTP 200 at both fixture paths.
- Static source validation does not establish that the camera actually frames every object well, nor prove rendering or motion. `BROWSER_RUNTIME: NOT_TESTED`, `VISUAL: NOT_TESTED`, and `MOTION: NOT_TESTED`; browser/WebGL appearance and animation still require manual inspection.
- Manual smoke test from repository root: run `python3 -m http.server 8000 --directory tests/fixtures/cross-style-mountain-bridge`, then visit `http://localhost:8000/miniature-diorama/` and `http://localhost:8000/retro-ps2/`. Check console/errors, complete scene visibility, the 8-second route, visible wheel rotation while moving, and stationary wheels after stopping.
- Only the two requested fixture files and these two TSA ledgers changed for this phase. Pre-existing unrelated modifications and untracked files were preserved; no staging, commit, or push occurred.

## 18. Phase 2D-3 Pixel Art visual skill (2026-11-10)

- Added `.github/skills/vidpixel/SKILL.md` (`style.pixel-art`, project skill name `vidpixel`, prompt alias `/vidpixel`). It treats style separately from execution and specifies crisp pixel clusters, a scene-appropriate logical grid and compact palette, nearest-neighbor scaling, time-selected sprite frames, optional parallax, Canvas 2D for suitable 2D scenes, user scene authority, and static/runtime/visual/motion validation. No scene, palette, duration, or aspect ratio is prescribed as a general default.
- Read the Pixel Art section in `sub skill.txt`. Its general pixel-grid, limited-palette, nearest-neighbor, sprite-frame, and layered-parallax principles informed the skill. The section's specific characters, falling scene, HUD, fixed resolution, duration, and aspect ratio were not used.
- Added `tests/fixtures/vidpixel-river-crossing/index.html`. The fixture uses a 320x180 Canvas 2D logical canvas, `image-rendering: pixelated`, disabled context smoothing, and hand-drawn hard-edged pixel clusters. It includes a river with elapsed-time-driven water details, a small delivery boat, wooden dock, distant shoreline, and limited vegetation. The boat moves toward the dock using elapsed milliseconds and clamps at its destination. Its 8-second duration and 16:9 ratio are fixture-only choices.
- Checks: Canvas element/context, 2D scene layers, logical dimensions, nearest-neighbor scaling, and elapsed-time loop source checks PASS; Node JavaScript syntax PASS; animation-state checks PASS for start, intermediate travel, destination, stop/clamp, and negative elapsed input; local HTTP smoke test returned `200`.
- Renderer limitation: current `cap.scene-production` and `VSKILLS_HTML_EXECUTION_CONTRACT.md` describe HTML/Three.js. The unchanged `validate_scene.py` checks Three.js scene/camera/WebGL/render patterns and does not validate Canvas 2D. It was not reported as passing this fixture. Renderer-neutral production instructions plus a renderer-aware validator are a proposed next iteration, not implemented in this phase.
- `BROWSER_RUNTIME: NOT_TESTED`, `VISUAL: NOT_TESTED`, `MOTION: NOT_TESTED`. No browser rendering or motion was observed; static checks and HTTP response are not visual/runtime evidence.
- Manual smoke test from repository root: run `python3 -m http.server 8000 --directory tests/fixtures/vidpixel-river-crossing` and open `http://localhost:8000/`. Inspect browser console, pixel edge crispness, complete scene visibility, water animation, and boat arrival.
- Only the two requested new artifacts and the TSA ledgers changed for this phase. Pre-existing unrelated worktree changes were preserved; no staging, commit, or push occurred.

## 19. Phase 2D-4 Renderer-aware scene production and validation (2026-11-10)

- Updated `.github/skills/scene-production/SKILL.md`: use Three.js for genuine volumetric 3D and Canvas 2D for appropriate native 2D rendering. Preserve explicit renderer requests, user requirements, and canonical sources; styles do not select or override renderers. Canvas 2D must not flatten required 3D geometry or canonical 3D characters.
- Added `.github/skills/scene-production/references/html-canvas2d-workflow.md`, documenting Canvas context initialization, logical/backing/display dimensions, coordinate and pixel-ratio policies, optional Pixel Art nearest-neighbor treatment, elapsed-time animation, frame clearing/redraw, resize handling, visible errors, local HTTP, and validation limits. `.github/skills/scene-production/references/html-threejs-workflow.md` was retained unchanged.
- Updated `.github/skills/scene-production/scripts/validate_scene.py` to require `--renderer threejs PATH` or `--renderer canvas2d PATH`. Three.js structural checks were retained. Canvas validation checks the element, `2d` context, drawing calls, animation-loop indicator, and backing dimensions when CSS/JS resize or scaling is declared. It does not impose Pixel Art properties on generic Canvas scenes. Automatic renderer detection was not implemented, so ambiguous detection is not applicable.
- Python AST syntax check PASS. Three.js structural validation PASS for all five requested inputs: Lunar Outpost, Miniature Railway, Retro Garage, Cross-style Miniature Diorama, and Cross-style Retro PS2. Canvas 2D validation PASS for Pixel Art River Crossing.
- Negative/CLI tests: missing file returned 1; Canvas missing a drawing operation returned 1; declared scaling without backing dimensions returned 1; incomplete Three.js returned 1; invalid renderer was rejected with exit 2. A minimal generic Canvas fixture without pixel-art styling or declared resizing returned 0.
- Static structural checks explicitly do not establish browser runtime, visual appearance, or observed motion. Browser testing was not required. The validator uses Python standard-library modules only; no runtime dependency was introduced.
- The HTML execution and runtime validation contracts were not modified and remain scoped to their existing HTML/Three.js design. The added Canvas reference supplements the production instructions.
- At the close of Phase 2D-4, `.github/skills/vidpixel/SKILL.md` still stated that Canvas 2D support was proposed. Phase 2D-4R corrects this mismatch.
- Only the requested scene-production skill, validator, two TSA ledgers, and new Canvas reference were changed/created. The five Three.js fixtures, Pixel Art fixture, existing Three.js reference, visual styles, parent skill, contracts, README, and `.gitignore` remained unchanged; no staging, commit, or push occurred.

### Phase 2D-4 stop condition

Renderer-selection guidance, Canvas 2D workflow reference, renderer-specific validator, requested regression and negative checks, and TSA ledger updates are complete. Stop here; browser validation or further renderer work requires separate authorization.

## 20. Phase 2D-4R Pixel Art capability alignment (2026-11-10)

- Corrected the production integration text in `.github/skills/vidpixel/SKILL.md` to state that `cap.scene-production` now provides Three.js and Canvas 2D renderer guidance, without conflating visual style and renderer responsibilities.
- Clarified that renderer-specific Python validation is static structure checking, not automatic generation or browser verification; a validator PASS is not proof of Canvas rendering, visual quality, or motion.
- Preserved the skill metadata and identity (`vidpixel`, `style.pixel-art`), discovery marker, and all existing visual-style, scene-authority, and validation guidance.
- Validation: metadata and identity checks PASS; targeted search confirms no unsupported-Canvas claim remains in `vidpixel/SKILL.md`; the correction touched only the renderer/production integration statements.
- Only `.github/skills/vidpixel/SKILL.md` and both TSA ledgers were modified. No fixtures, validator, scene-production files, contracts, staging, commit, or push changes occurred.

### Phase 2D-4R stop condition

The stale Canvas support statement is corrected and the requested checks are complete. Stop here.

## 21. Phase 2E-1 Comic Book visual skill and fixture (2026-11-10)

- Added `.github/skills/vidcomic/SKILL.md` (`style.comic-book`, project skill name `vidcomic`, prompt alias `/vidcomic`). It guides expressive ink contours, compact scene-specific colors, flat/cel shading, selective halftone/print texture, readable silhouettes, dynamic composition, optional panels and motion effects, user scene authority, renderer choice, and visual/runtime validation without prescribing content or format defaults.
- Read the Comic Book section of `sub skill.txt`. Its general graphic style principles informed the skill; no character, plot, slogan, speech effect, or format from the illustrative source scene was carried over.
- Added `tests/fixtures/vidcomic-city-delivery/index.html`, a self-contained Canvas 2D scene with a bicycle courier who rides along the city street, turns onto the side street, and stops beside the storefront. City buildings, storefront, travel path, outlined courier/bicycle, turning wheels, halftone, and motion lines are represented. It contains no subtitles, speech bubbles, or HUD and uses no external dependency.
- The fixture uses an elapsed-time timeline. Wheel angle is derived from traveled distance divided by wheel radius; the static logic check found wheel angle unchanged after the courier stops.
- Checks: skill metadata and source structure PASS; `validate_scene.py --renderer canvas2d` PASS; JavaScript syntax PASS; required-scene static checks PASS; elapsed-time route and wheel-stop logic checks PASS; local HTTP returned `200`.
- Browser runtime, actual visual appearance, and observed motion are **NOT_TESTED**. The validator and source checks are structural only.
- Only the new `vidcomic` skill, its fixture, and the two TSA ledgers were changed/created. No existing skill or fixture was edited; no staging, commit, or push occurred.

### Phase 2E-1 stop condition

The Comic Book skill and fixture are implemented and available checks are complete. Stop here; browser validation or any further scene work requires separate authorization.

## 22. Phase 2E-1R Comic Book scene layout and path repair (2026-11-10)

- Root cause in `tests/fixtures/vidcomic-city-delivery/index.html`: frontal building/storefront facades and a separate narrow vertical road rectangle implied a screen-depth turn without a visibly continuous road connection. The courier and side-view bicycle were rotated in 2D screen space, which did not match that implied perspective.
- Recast the scene consistently as a top-down city layout. Buildings are roof footprints; the main road and northbound side street are one connected L-shaped intersection. Painted lane markings follow the same straight, quarter-circle, and straight segments as the courier's path.
- Reworked the bicycle/courier as a top-down sprite whose forward axis rotates with the path tangent. The courier remains on the road through the turn; wheel-face spokes rotate from traveled distance and remain stationary at the stop.
- Placed a clear access apron, west-facing storefront entry, and awning adjacent to the side street. The courier ends beside the entry with its projected footprint clear of the store wall. Background, road, and storefront draw before the courier.
- Layout checks sampled start, pre-turn, during-turn, post-turn, and stop states; also checked continuous route samples, wheel centers, heading, draw order, entry proximity, and wall clearance. All static checks PASS.
- Validation: Canvas renderer validator PASS; JavaScript syntax PASS; static path/geometry and animation-logic checks PASS; local HTTP returned `200`. Browser runtime, visual perspective, and motion observation are **NOT_TESTED**.
- Only the Comic Book fixture and the two TSA ledgers changed for this repair. No skill, other fixture, validator, contract, README, or `.gitignore` was modified; nothing was staged, committed, or pushed.

### Phase 2E-1R stop condition

The layout/path defect is corrected at source level and available checks are complete. Stop here; visual confirmation requires manual browser inspection.

## 23. Phase 2E-1R2 Top-down bicycle geometry repair (2026-11-10)

- The user-observed mismatch was in the bicycle drawing, not the established scene perspective: `drawWheel` showed circular faces and rotating spokes, even though the road, buildings, and path were top-down.
- Wheel assemblies now use narrow longitudinal tire silhouettes with subtle tread marks whose offset derives from the existing distance-based wheel angle. Tread motion therefore follows travel and freezes when the courier stops; no side-view disc spin is depicted.
- The front and rear wheels are placed along the local forward axis. The frame connects both wheel assemblies and includes the crank/pedal area, saddle, fork, and handlebars perpendicular to travel. The rider remains over the frame with head, torso, arms, and legs, and the existing parent transform rotates the full group with the path tangent.
- Route, timing, road, storefront access, camera, colors, and stop position were retained. Source-level checks cover wheel geometry/alignment, frame and handlebar structure, centerline placement, turn transform, and stationary tread state.
- Canvas structural validator and JavaScript syntax: PASS. Static geometry/animation checks: PASS. Browser runtime, visual appearance, and observed motion: **NOT_TESTED**.
- Only the Comic Book fixture and the two TSA ledgers were modified. No staging, commit, or push occurred.

### Phase 2E-1R2 stop condition

The requested bicycle geometry correction and available static checks are complete. Manual browser review is still required to establish the rendered perspective and tread motion.

## 24. Phase 2E-1K Perspective and spatial consistency knowledge propagation (2026-11-10)

### Verified Comic Book fixture behavior

- The user identified two perspective defects: the initial scene combined frontal building facades and a disconnected narrow road with a screen-depth turn; after the overhead layout repair, the bicycle still showed circular side-view wheel faces and spokes.
- Source corrections established roof-footprint buildings, one connected L-shaped road and matching route, a storefront access apron, and a top-down courier/bicycle group aligned with the path tangent. The subsequent bicycle correction replaced circular wheel faces with narrow longitudinal tire silhouettes and distance-driven tread cues, connected the wheel assemblies with a frame, and aligned the handlebars perpendicular to travel.
- The recorded source evidence is static: Canvas structural validation, JavaScript syntax, geometry/path checks, and route-state checks passed. The user subsequently confirmed “ok pass” after the Phase 2E-1R2 perspective correction. Record **USER-OBSERVED MANUAL PASS** based on that confirmation; browser/version, detailed inspection steps, and screenshot evidence were not supplied. Automated browser validation remains **NOT_TESTED**.

### Generalized design rules

- Select and document a camera/view convention before constructing the environment and subjects. Keep support geometry, subject shape, movement direction, path, and occlusion compatible with that convention.
- Derive moving-object heading from the path tangent; use local axes and view-appropriate geometry. Align visible paths with traversable space and validate contact, clearance, clipping, layer/depth order, and start/turn/stop states.
- Mixed perspective is acceptable when intentional and justified by source or design; it must preserve readable spatial relationships.
- Canvas guidance addresses screen-space coordinates, transforms, draw order, and view-dependent depictions. Three.js guidance addresses camera projection, world coordinates, object orientation, support-surface alignment, and depth/clipping. These are complementary, not interchangeable renderer instructions.

### Limits and transfer status

- The Comic Book manual PASS is user-reported, not an automated browser result. Automated browser validation and independently recorded visual/motion evidence remain **NOT_TESTED**.
- These rules are reusable design guidance, but their effectiveness across other styles, scenes, camera types, or renderers remains **UNVERIFIED**. No fixture was modified in Phase 2E-1K.

## 25. Phase 2E-2 Toy Brick visual skill and construction-yard fixture (2026-11-10)

### Implementation

- Read the Toy Brick source section in `sub skill.txt`. Its generic glossy-plastic brick construction and stop-motion-like presentation informed the skill; the example's people, dog, skydiving story, framing, and timing were not transferred.
- Created `.github/skills/vidbrick/SKILL.md`: `style.toy-brick`, `vidbrick`, `/vidbrick`. Guidance covers modular interlocking forms, visible studs and seams, consistent dimensions, plastic highlights, toy-scale proportion, readable articulation, brick-built environments, projection, scene authority, and evidence-based validation. It sets no brand, character, story, duration, or format default.
- Created `tests/fixtures/vidbrick-construction-yard/index.html`, using Three.js 0.187.0, procedural volumetric geometry, and no model/texture assets or build system. A studded platform and loading pad support a brick pile, brick-built excavator, and brick-built dump truck.
- The excavator arm is a parented two-link assembly with boom, stick, and bucket pivots. Inverse kinematics targets the pile and truck bed; a small brick is carried by the bucket and released into the bed. The truck then translates forward, with visible wheel spokes rotating by distance divided by tire radius.
- The fixture uses an elapsed-time, 10-second play-once timeline and a responsive 16:10 viewport; these are fixture decisions, not skill defaults.

### Validation and evidence

- Skill metadata and stable ID: PASS.
- `python3 .github/skills/scene-production/scripts/validate_scene.py --renderer threejs tests/fixtures/vidbrick-construction-yard/index.html`: PASS for scene, camera, WebGL renderer, render call, and animation loop structure.
- Embedded JavaScript module syntax: PASS.
- Static checks for required objects, brick/stud construction, pivots, inverse-kinematics targets, action sequence, and distance-derived truck wheel rotation: PASS. Static calculations placed rest, pile, and bed targets within the arm's reachable distance.
- Local HTTP smoke test: HTTP 200.
- Browser runtime, actual visual appearance, and observed motion: **NOT_TESTED**. The CDN dependency requires network access. Structural checks and calculated reach do not establish rendered contact, successful bucket loading, or observed wheel movement.

### Applicability limits

- The Comic Book perspective guidance is recorded as implemented reusable instructions. The user confirmed “ok pass” for the specific Phase 2E-1R2 Comic Book bicycle perspective correction, which is a **USER-OBSERVED MANUAL PASS**; automated browser validation remains **NOT_TESTED**.
- That confirmation applies to the repaired Comic Book fixture only. It does not prove generalized perspective rules for every scene, style, or renderer.

## 26. Phase 2E-3 Claymation visual skill and garden-delivery fixture (2026-11-10)

### Implementation

- Read the Claymation section in `sub skill.txt`. Its handmade, squishy forms, clay-like surfaces, and stop-motion influence informed the style guidance. The example's falling people, dog, sky, camera move, fixed duration/framing, and per-frame random wobble were not copied.
- Created `.github/skills/vidclay/SKILL.md` with stable ID `style.claymation`, skill name `vidclay`, and user-facing alias `/vidclay`. It describes rounded volumetric forms, subtle deterministic irregularity, restrained clay gloss, optional tool/fingerprint marks, warm lighting, recognizable faces, articulated pivots, spatial coherence, and controlled stop-motion-inspired timing. It does not require frame jitter or set scene/format defaults.
- Created `tests/fixtures/vidclay-garden-delivery/index.html` using Three.js 0.187.0, procedural geometry, and no external models or textures. It includes a sculpted character with eyes and a mouth, articulated arms/legs, a clay pot and plant, a wooden worktable, wooden display shelf, and simple garden surroundings.
- Shoulder/elbow and hip/knee groups provide articulated limbs. A hand anchor holds the flowerpot during carry. The pot transitions through explicit `table`, `carried`, and `placed` states; `carryAnchor.attach(pot)` and `scene.attach(pot)` preserve world transforms at pickup and release. A deterministic 12-pose-per-second sample cadence gives held-pose timing without random flicker.
- The character approaches the table, reaches and lifts the pot, carries it while walking to the shelf, lowers/releases it onto the shelf, and returns arms/legs to neutral. Pot and hand-anchor coordinates coincide at pickup; the final pot location coincides with the shelf support height.

### Validation and evidence

- Skill metadata, stable ID, alias, and marker: PASS.
- `python3 .github/skills/scene-production/scripts/validate_scene.py --renderer threejs tests/fixtures/vidclay-garden-delivery/index.html`: PASS for scene, camera, WebGL renderer, render call, and animation loop structure.
- Embedded JavaScript module syntax: PASS.
- Static checks for required objects, facial features, volume, pivots, state transitions, and transform-preserving attachment: PASS.
- Calculated pickup continuity and shelf placement: PASS; table/shelf support heights match the pot bottom. Local HTTP smoke test: HTTP 200.
- Browser runtime, visual appearance, and observed motion: **NOT_TESTED**. Source checks cannot establish that the scene renders, that hands visually grip the pot, or that the motion reads clearly.

### Scope and limits

- The 9-second play-once timeline, 16:10 composition, and 12-pose-per-second cadence belong only to this fixture. The CDN dependency requires network access.
- The Comic Book Phase 2E-1R2 perspective correction is recorded as **USER-OBSERVED MANUAL PASS** based on the user's “ok pass” confirmation. Automated browser validation remains **NOT_TESTED**. Its generalized perspective guidance remains implemented instruction, not a guarantee for future scenes.

## 27. Phase 2E-4 Paper Cutout visual skill and forest-crossing fixture (2026-11-10)

### Implementation

- Read the Paper Cutout section of `sub skill.txt`. Its layered paper scenery, visible grain, inter-layer shadows, and articulated paper-puppet ideas informed reusable style guidance. The example's falling people and dog, strings, vertical framing, fixed timing, and per-frame wobble were not transferred.
- Created `.github/skills/vidpaper/SKILL.md` with stable ID `style.paper-cutout`, project skill name `vidpaper`, and user-facing alias `/vidpaper`. The style keeps paper layering and tactile depth central while leaving user content, renderer, palette, timing, framing, and output choices unconstrained.
- Created `tests/fixtures/vidpaper-forest-crossing/index.html` as a standalone Canvas 2D forest scene. It uses generated paper-grain texture, outlined cut edges, soft shadows, stacked tree and vegetation shapes, a blue cut-paper stream, a wood-plank bridge, and a flower. No external assets or dependencies are used.
- The scene uses a lateral storybook view: the fox travels left-to-right along a visible bank-to-bank route, climbs a shallow approach, crosses the level bridge deck above the stream, and descends to the far bank. `routeY` defines both deck/plank height and fox support height; the fox turns with the route slope. Segmented limbs and knee joints articulate with the elapsed-time walk. Background, stream, banks, trees, trail, bridge, fox, and foreground leaves are layered in draw order; the stop pose leaves visible space between the fox silhouette and flower.

### Validation and evidence

- Skill metadata, stable ID, alias, and discovery marker: PASS.
- `python3 .github/skills/scene-production/scripts/validate_scene.py --renderer canvas2d tests/fixtures/vidpaper-forest-crossing/index.html`: PASS for Canvas element, 2D context, drawing operation, animation-loop indicator, and backing dimensions with resize handling.
- JavaScript syntax: PASS. Static checks for required scene objects, paper treatment, layer order, route/deck alignment, leg articulation, timing, and final flower clearance: PASS.
- Local HTTP smoke test returned `200`.
- Browser runtime, actual visual appearance, and observed motion: **NOT_TESTED**. Static route calculations do not establish browser-rendered foot contact, composition quality, or motion readability.

### Scope and limits

- The 11-second play-once fixture timeline, 9-second walk, 960×600 logical canvas, and landscape framing are fixture-specific, not style defaults.
- This fixture demonstrates one paper-cutout scene only; it does not establish a generator or prove the guidance across other scenes. No browser observation was performed.

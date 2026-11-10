# TSA VSkills — Project State

**Status:** RECOVERED / RECONSTRUCTED, not an exact copy of the missing home-machine file  
**Recovery date:** 2026-11-10  
**Evidence:** `tsavskill.tar` snapshot supplied by the user; previously supplied TSA phase and agent-test reports.  
**Active phase:** Phase 2B-R — Parent–Child Routing Alignment (COMPLETED 2026-11-10)  
**Next authorization:** None in this phase. Phase 2C is not authorized.

## 1. Goal and invariant baseline

TSA VSkills is a portable, incremental skill framework with parent `vskills`, visual-style children, production capabilities, character capabilities, and shared TSA protocols. Design constraints:

- User scene is authoritative; style guidance never hardcodes an example scene.
- Production mode, operation capability, and visual style are separate dimensions.
- Initially allow at most one primary visual style per request.
- Parent hybrid routing: discovery without arguments; select an explicit skill; infer a clear mode/capability; clarify material ambiguities.
- Canonical HTML character source is authoritative when supplied; image reference is authoritative for new image-to-Three.js character appearance.
- Modular Film baseline is 15 minutes **for the complete film**, not for each scene.
- Preserve original sources, keep changes scoped and reversible, and report PASS/FAIL/BLOCKED/NOT_TESTED with evidence.
- Never equate agent skill discovery with video rendering, native slash command registration, or portable cross-host functionality.

## 2. Progress ledger

| Phase | Recorded outcome | Evidence strength / limitation |
| --- | --- | --- |
| Phase 0 — Source audit | Inventory and classification of TSA protocols, prompts, 10 style examples, and source conflicts | Earlier agent report; root snapshot includes relevant extracted sources |
| Phase 1A — Architecture | Five architecture/contract/state documents created | Earlier agent report; present architecture documents are inspectable |
| Phase 1A-R — Alignment | Hybrid routing, mode/capability/style separation, canonical preservation, one-style limit, 15-minute film ceiling approved | Earlier agent report and current design documents |
| Phase 1B — Skill contract | Invocation and skill-layout contracts created | Files present in snapshot |
| Phase 2A — Parent discovery | `.github/skills/vskills/SKILL.md` implemented; Copilot CLI 1.0.107 reportedly discovered and used it | Earlier agent test report; cannot rerun Copilot in this recovery |
| Phase 2A-G1 — Publication audit | Public/private/license-risk files classified | Earlier audit report |
| Phase 2A-G2 — Repo preparation | README and `.gitignore` created/updated; source and internal development records excluded from ordinary Git staging | README and `.gitignore` present |
| Phase 2B — First child discovery | `.github/skills/vidmindi/SKILL.md` created; Copilot CLI 1.0.107 reportedly listed both skills and used child guidance | Child file present; test output supplied by user, not rerun here |
| Phase 2B-R — Parent–child alignment | Updated parent child-routing guidance; loaded child through the skill host and confirmed its stable ID and marker | **COMPLETED** for instruction discovery and selection; native alias and video-generation runtime remain unimplemented |

## 3. Current filesystem snapshot (office tar)

**Verified directly from supplied `tsavskill.tar`:**

- Present: `.github/skills/vskills/SKILL.md`, `.github/skills/vidmindi/SKILL.md`, `.gitignore`, `README.md`, `VSKILLS_ARCHITECTURE.md`, `VSKILLS_SKILL_CONTRACT.md`, `VSKILLS_INVOCATION_CONTRACT.md`, `VSKILLS_SKILL_LAYOUT.md`, `VSKILLS_USAGE_DESIGN.md`.
- Present: `sub skill.txt`, two canonical-character prompt documents, and `video TSA skill/` source protocols/templates.
- **Absent:** `VSKILLS_TSA_STATE.md` and `VSKILLS_TSA_KNOWLEDGE.md` prior to this reconstruction.
- The tar contains `.git/`, but no live `git status`, index reconciliation, remote synchronization, or host tests were performed as part of recovery. Do not infer clean/staged/pushed status.
- Earlier reports indicate GitHub remote `https://github.com/amritsalahudin69/tsavskill.git`, branch `main`. Reverify in the active working directory.

## 4. Verified inconsistencies and open blockers

1. **Resolved in Phase 2B-R:** the parent now identifies the installed Miniature Diorama child and distinguishes its style guidance from video generation.
2. `README.md` and the `vidmindi/SKILL.md` source note claim `sub skill.txt` is absent; **the supplied tar actually contains it**. Do not silently rewrite the source attribution; inspect provenance and permissions before a future scoped change.
3. `.gitignore` explicitly ignores `/VSKILLS_TSA_STATE.md` and `/VSKILLS_TSA_KNOWLEDGE.md`. Those files therefore did not travel via ordinary Git commits and clone/pull. Git ignores do not delete existing local files.
4. Rights/attribution for source protocols and external style examples remain unresolved. Do not publish them by default.
5. **Partially resolved in Phase 2B-R:** parent guidance identifies the child ID and location, and the host loaded the child instructions. This verifies instruction-level selection/loading only; no native slash alias, registry, or automated router is established.
6. No HTML/video generator, Python router, native standalone `/vidmindi` command, or multi-host adapter has been implemented/tested.
7. Prior Phase 2B report mentioned unexpected staged content and trailing whitespace in previously staged docs. **Resolved for this checkout:** the current index has no staged paths; existing unstaged work was preserved.

## 5. Phase 2B-R execution record

- This task changed only `.github/skills/vskills/SKILL.md`, this state record, and `VSKILLS_TSA_KNOWLEDGE.md`.
- The initial live Git audit found no staged changes. Existing unstaged changes were preserved; no files outside the authorized set were edited.
- The parent-first instruction test selected `style.miniature-diorama` and directed the host to `.github/skills/vidmindi/SKILL.md`. The host then loaded the child and returned its diagnostic marker.
- No scene, video, or other generated file was produced. No native slash command or execution runtime was invoked.
- Cross-PC synchronization policy remains unresolved. Do not modify `.gitignore`, force-add files, or sync local records automatically.

The live repository commit at the start of this phase was `d32bdafd21a3ce9ed0daab37b961379810e3a735` (`pahse2a-r`).

## 6. Validation ledger for this recovery

| Item | Status | Basis |
| --- | --- | --- |
| Snapshot inventory | PASS | Tar member listing examined without extraction/execution |
| Missing state/knowledge diagnosis | PASS | Neither file exists in tar; both excluded by .gitignore |
| Present parent/child skill files | PASS | Both SKILL.md files found in tar |
| Parent metadata validity | PASS | Parent skill loaded successfully earlier in the session; its unchanged frontmatter declares `name: vskills` and `description` |
| Parent discovery | PASS | Host loaded `vskills` earlier in the session; the updated file was reviewed directly, not reloaded by the host |
| Child discovery | PASS | Host skill loader found and loaded `vidmindi` |
| Parent-to-child instruction selection | PASS | Updated parent instructions selected the installed child and stable ID in a manual parent-first test |
| Actual child instruction loading | PASS | Host returned the child instructions containing `TSA_VIDMINDI_DISCOVERY_MARKER: VIDMINDI_CHILD_2B` |
| Native `/vidmindi` alias / automated routing | NOT_TESTED | No native command or router was implemented or invoked |
| Git safety | PASS | No staged paths; pre-existing unstaged changes preserved; no files outside the allowlist changed |
| Current commit | PASS | `d32bdafd21a3ce9ed0daab37b961379810e3a735` at phase start |
| Original home-state exact reconstruction | BLOCKED | Original ignored files not available |
| Runtime execution | NOT_TESTED | No scene/video runtime was invoked; no output was generated |
| Video/HTML execution | NOT_IMPLEMENTED | No generator was found/verified |

## 7. Stop condition

Phase 2B-R alignment, available instruction-loading tests, and these documentation updates are complete. Stop here. Phase 2C, staging, committing, pushing, and cross-PC synchronization are not authorized.

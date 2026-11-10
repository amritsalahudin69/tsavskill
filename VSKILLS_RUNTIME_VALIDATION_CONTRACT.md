# TSA VSkills Runtime and Visual Validation Contract

**Status:** PROPOSED IMPLEMENTATION — Phase 2C-1 contract design only
**Applies to:** Future HTML/Three.js `cap.scene-production` output, including optional Miniature Diorama styling
**Not implemented:** No browser harness, validator, runtime adapter, or scene exists as a result of this contract.

## 1. Purpose and evidence rules

This contract defines observable evidence for source, build, browser/runtime, visual, animation, and delivery validation. It complements `VSKILLS_HTML_EXECUTION_CONTRACT.md`; it does not claim that a test environment or implementation is available.

Use only TSA outcomes:

- **PASS** — the specific criterion was executed and passed; identify evidence.
- **FAIL** — it was executed and failed; identify observed failure.
- **BLOCKED** — a necessary check could not be completed because a stated prerequisite or decision is missing.
- **NOT_TESTED** — the check was not attempted; give the reason.

Do not merge checks into a blanket “works” claim. A generated file is not runtime evidence; a successful parse is not browser evidence; a screenshot is not proof of animation; browser rendering is not proof of Miniature Diorama fidelity. Report partial results gate by gate. If any required gate is `FAIL`, the overall deliverable cannot be reported as fully accepted.

Evidence record should include artifact path and content identity where practical, command or manual procedure, browser/runtime and version, viewport, dependency source/revision, date, observed output, and exact gate status. Do not record private paths or credentials in shareable evidence.

## 2. Gate 1 — Source and input

**Purpose:** Prove that implementation inputs and authority were understood before editing or generation.

**Checks and evidence:**

- Required scene description and intended subject/event are present; record the normalized task interpretation alongside exact constraints.
- Optional actions, environment, camera, duration, aspect ratio, resolution, looping, lighting, and delivery requirements are inventoried; assumptions are explicit.
- Each supplied asset exists at the exact case-sensitive path and its role/license/provenance is known or reported unknown.
- If canonical HTML is supplied, record the source entry point, runtime/renderer/imports, geometry, proportions, distinctive details, materials, hierarchy/pivots, animation support, and dependencies from actual source inspection.
- Confirm intended source files remain unchanged unless the user explicitly authorizes a source edit.

**PASS evidence:** concise input/source audit and constraint-to-plan mapping.
**FAIL:** contradictory interpretation or unauthorized source replacement/edit.
**BLOCKED:** required source, scene, or authority decision is missing.
**NOT_TESTED:** source/input audit was not performed; do not begin implementation while a critical source issue is unresolved.

## 3. Gate 2 — Build and dependency integrity

**Purpose:** Prove the delivered source structure and dependencies can be resolved before browser claims.

**Checks and evidence:**

- HTML and JavaScript parse under the selected toolchain; identify the exact check used.
- Declared Three.js core/add-on imports resolve to the same tested version. Record exact dependency source and version; do not pin or imply a version that was not exercised.
- All required local assets resolve with exact path/case. No required asset silently falls back.
- External network requirements, license/provenance, and `file://` limitations are stated. Verify the proposed local HTTP run command against the actual artifact.
- Any supporting source modules and relative paths match the delivered package.

**PASS evidence:** command output or equivalent reproducible dependency/path checks.
**FAIL:** parse/build error or missing required dependency/asset.
**BLOCKED:** required browser/tool/dependency source unavailable or violates user constraints.
**NOT_TESTED:** no static/build/dependency check was run.

A structural check does not prove browser initialization, WebGL, visual fidelity, or animation.

## 4. Gate 3 — Browser/runtime

**Purpose:** Prove that the actual artifact initializes and renders in the declared target environment.

**Checks and evidence:**

- Serve the delivered package using the documented supported local HTTP method; do not assume `file://` behavior.
- Record browser name/version, operating system when material, viewport, dependency/network state, and exact launch procedure.
- Confirm HTML, modules, dependencies, and required assets load; renderer/context initializes without critical console errors.
- Confirm a visible canvas and the expected 3D scene appear; wait for required assets before judging readiness.
- Exercise resize and any requested controls/interactions; observe context/init failure handling where practical.
- Identify runtime errors and warnings separately; a non-critical warning is not silently described as clean.

**PASS evidence:** actual browser observation, console/runtime record, and screenshot or equivalent capture proving visible output.
**FAIL:** reproducible initialization, asset, WebGL, or critical runtime failure.
**BLOCKED:** no compatible browser/WebGL or local-serving capability is available.
**NOT_TESTED:** browser execution was not attempted. Static tests, HTTP status, and screenshots supplied without runtime evidence cannot earn this gate a PASS.

## 5. Gate 4 — Visual acceptance

**Purpose:** Inspect the rendered result against the user scene, camera, composition, and selected style.

**Checks and evidence:**

- Capture the actual browser render at the requested viewport/ratio; record its dimensions.
- Confirm the intended subject/event is visible and readable in opening, action, and ending states.
- Inspect framing, perspective, clipping, occlusion, silhouettes, spatial relationships, contact, and unintended floating.
- Confirm genuine volumetric geometry for scene elements that require 3D.
- For Miniature Diorama, identify at least two complementary visual cues (for example: coherent model-scale proportions, crafted material treatment, and intentional model-like lighting/composition). Small size or blur alone is insufficient.
- Verify that optional blur, shadows, props, and effects do not hide the requested action or introduce unrequested content.
- Compare canonical character identity/materials/proportions against the audited source when applicable.

**PASS evidence:** human inspection of actual browser captures for the required view(s), tied to the criteria.
**FAIL:** a required subject is missing/unreadable, severe clipping/occlusion occurs, true 3D was required but absent, style is not recognizable, or canonical fidelity is lost.
**BLOCKED:** no browser capture or required reference/source is available.
**NOT_TESTED:** no visual inspection occurred.

A source-code review or generated screenshot placeholder is not visual evidence.

## 6. Gate 5 — Animation and camera behavior

**Purpose:** Prove requested motion, timeline, interactions, and camera behavior at runtime.

**Checks and evidence:**

- Play the animation in the target browser; record observed start/end and whether play-once/loop behavior matches input.
- Verify every requested action and interaction visibly occurs in the right order and timeframe.
- Check contact, direction, pivots, object relationships, and camera targeting; root-only movement is not sufficient when the requested action implies articulated motion or interaction.
- Confirm the camera does not lose the intended subject, clip important geometry, or introduce unintended movement.
- If seek/reset/determinism is part of the output contract, test at least two timestamps, repeat the same timestamp/reset, and compare the resulting scene state.
- If looping was requested, inspect the wrap boundary for visible position/pose/camera discontinuity.
- If a fixed duration or export frame rate was requested, verify measured playback/export timing and actual frame count separately; preview playback alone is not exact export evidence.

**PASS evidence:** recorded browser playback observations and timestamp/reset/loop checks applicable to the request.
**FAIL:** required action is absent, materially mistimed, discontinuous, or camera behavior contradicts constraints.
**BLOCKED:** runtime cannot play or a required interaction/asset is unavailable.
**NOT_TESTED:** motion was not observed in the executing runtime. A static image never passes this gate.

## 7. Gate 6 — Delivery

**Purpose:** Prove the promised artifact and instructions are present and usable.

**Checks and evidence:**

- List exact delivered file paths; confirm the primary HTML and required support files exist.
- Follow the delivered run instructions from the stated working directory and environment.
- Confirm all required assets/dependencies are included or their external/network requirements are explicit.
- Include selected mode, operation, style, input interpretation, assumptions, dependency versions/sources, gate results, limitations, and unverified claims.
- Confirm canonical source materials were not overwritten or unintentionally packaged.

**PASS evidence:** file inventory plus successful follow-through of the run instructions in the declared environment.
**FAIL:** a promised artifact/support file is missing, paths are incorrect, or run instructions fail.
**BLOCKED:** output destination, dependency policy, or necessary delivery permission is unavailable.
**NOT_TESTED:** files/instructions were not checked.

## 8. Partial validation and overall report

Report each applicable gate separately. State the reason for every `BLOCKED` or `NOT_TESTED`; include a concise failure and evidence for each `FAIL`. Do not promote one gate's evidence to another gate.

Examples:

- Static checks pass but the browser is unavailable: Gates 1–2 may be `PASS`; Gate 3 is `BLOCKED` if the required browser could not be run, and Gates 4–5 are `NOT_TESTED` or `BLOCKED` according to whether the check was attempted and what prevented it.
- Browser renders a still image but motion was not exercised: Gate 3 can be `PASS`; Gates 4–5 remain separately assessed, and Gate 5 is not `PASS`.
- A screenshot appears correct but source and dependency checks were not run: visual evidence cannot make Gates 1–3 pass.
- A delivered artifact was generated but never opened: runtime, visual, and animation are not `PASS`.

The overall report should state `PASS` only when all required gates pass. Otherwise report **PARTIAL** with the individual TSA statuses; `PARTIAL` is a summary, not a replacement status.

## 9. Phase 2C-2 evidence plan

Use the proposed lunar-outpost fixture from `VSKILLS_HTML_EXECUTION_CONTRACT.md` only after Phase 2C-2 is explicitly authorized. Do not create it during Phase 2C-1.

| Acceptance claim | Required evidence |
|---|---|
| Child/style selected | Parent-first request resolution plus actual child instruction loading evidence. |
| Scene requirements preserved | Input-to-implementation comparison for subjects, motion, 6-second duration, 4:3 ratio, no text, and non-loop behavior. |
| Actual HTML generated | Exact delivered `index.html` path and source inspection. |
| Volumetric objects | Source geometry inspection plus browser view showing volume, silhouette, and spatial relationships. |
| Requested animation runs | Actual browser playback showing rover turn and dish tracking; no static-only substitute. |
| Camera frames subject | Browser captures/inspection during opening, movement, and ending. |
| Miniature style evident | Actual rendered capture with named complementary model-scale/material/light/composition cues. |
| No critical runtime errors | Browser console/runtime record for the tested run. |
| Evidence-based outcome | Completed per-gate status table with evidence and limitations. |
| Canonical sources unchanged | Git/source comparison showing canonical source materials were not modified. |

## 10. Validation infrastructure status

**VERIFIED SOURCE FACT:** The repository contains TSA written protocols for HTML/Three.js production, canonical character integration, and modular scene assembly. These are reference documents, not proof of an installed browser, runtime, renderer, test harness, or generator.

**UNVERIFIED:** Browser automation, browser versions, WebGL availability, screenshot capture, a supported local HTTP server, and any offline dependency cache. Phase 2C-2 must inspect the actual host environment and report unavailable checks instead of installing packages or claiming success.

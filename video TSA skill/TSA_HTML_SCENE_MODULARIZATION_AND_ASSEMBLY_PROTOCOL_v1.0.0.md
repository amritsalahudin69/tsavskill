# TSA HTML SCENE MODULARIZATION AND ASSEMBLY PROTOCOL

**Document ID:** TSA-HTML-SCENE-MODULARIZATION-AND-ASSEMBLY  
**Version:** 1.0.0  
**Status:** Proposed baseline for TSA review  
**Maximum assembled film duration:** 15 minutes  
**Production model:** Independently executable scene HTML modules assembled by a Master HTML Engine.

## 1. Purpose

This protocol defines how a local agent decomposes an approved cinematic breakdown into scene modules, implements each module as a testable HTML/Three.js deliverable, and assembles the modules into one continuous film.

It distinguishes three levels:
1. **Film:** the complete viewing experience, maximum 15 minutes.
2. **Scene module:** a coherent narrative/spatial/production unit, implemented as an independently testable HTML file.
3. **Shot:** a camera/editing unit inside a scene. A shot change does not automatically require another HTML file.

The objective is not to maximize file count. It is to preserve cinematic continuity while keeping production units testable and maintainable.

## 2. Relationship to other TSA protocols

| Document | Responsibility |
|---|---|
| `TSA_Video_Breakdown_PROTOCOL_v1.0.0.md` | Source analysis: story, screenplay, dialogue, scenes, shots, camera, motion, sound, evidence status |
| `TSA_Canonical_Character_to_Scene_Integration_PROTOCOL_v1.0.0` | Canonical character and asset identity, reuse, binding, and integration constraints |
| `TSA_HTML_Game_Video_Production_PROTOCOL_v1.0.0` | HTML/Three.js implementation and production workflow |
| **This protocol** | Scene boundaries, scene HTML contract, Master Engine assembly, handoff, and validation |

### 2.1 Is the Video Breakdown Protocol still needed?

**Yes, as a reusable analysis method; no, it does not have to be rerun when an acceptable breakdown already exists.**

- If Gemini is used to inspect a YouTube source, use the Video Breakdown Protocol to guide that analysis and obtain its Markdown package.
- If the video is uploaded and successfully analyzed in the current ChatGPT or local-agent environment, produce the same required breakdown artifacts there. Do not rerun Gemini merely to satisfy the protocol name.
- If the user supplies an existing breakdown, audit its coverage, evidence labels, and completeness. Reuse valid work and request only missing analysis.
- If only transcript or metadata is available, mark visual/audio gaps explicitly. Never fabricate evidence.

The protocol is not Gemini-only. Gemini is one possible analysis environment. The required analysis structure and output quality remain platform-independent.

### 2.2 Analysis is not canonical asset authority

The breakdown describes what the source shows. It does not authorize rebuilding supplied canonical characters. The canonical integration protocol governs character and asset reuse.

## 3. Architecture

```text
SOURCE VIDEO / USER SCRIPT
          |
          v
SOURCE BREAKDOWN PACKAGE
          |
          v
CANONICAL ASSET AUDIT
          |
          v
SCENE DECOMPOSITION PLAN
          |
     +----+----+
     |    |    |
     v    v    v
   SC01  SC02  SC-N
   HTML  HTML  HTML
     |    |    |
     +----+----+
          |
          v
     MASTER HTML ENGINE
 sequence / audio / transitions /
 timeline / continuity / lifecycle
          |
          v
     FINAL HTML FILM (<= 15:00)
```

Each scene HTML must be independently launchable for development and validation. The Master Engine sequences scene documents using a defined manifest and lifecycle/message contract.

**Default integration approach:** same-origin scene documents loaded into a controlled scene viewport (for example, one active iframe). The Master Engine owns film playback, global audio, scene order, and inter-scene transitions. A different architecture is allowed only if the agent documents how it preserves isolation, deterministic timing, asset reuse, and testability.

Do not create multiple simultaneously active WebGL contexts by default. Preloading or overlapping scenes requires performance evidence.

## 4. Film-level rules

1. Maximum assembled film duration is 15:00. This is a ceiling, not a target.
2. Duration comes from the approved source/script requirement.
3. Scene durations must reconcile with the film timeline. Any transition overlap must be explicit.
4. Every scene declares local duration and global film start/end.
5. Do not silently omit dialogue, action, pauses, or transitions to fit the limit.
6. If the source exceeds 15 minutes, divide it into multiple film parts or production units; do not silently shorten it.

## 5. Scene decomposition rules

### 5.1 A scene module may be justified by

- A meaningful location/environment change.
- A meaningful time jump or story-phase change.
- A new narrative objective, conflict, or event sequence.
- A materially different asset/environment dependency.
- A production boundary that reduces implementation or validation risk.
- A deliberate editorial boundary that can be independently tested.

### 5.2 These do not automatically create a new HTML

- Camera cut or angle change.
- Wide-to-close-up change.
- Pan, tilt, dolly, tracking, zoom, orbit, or POV change.
- Character animation start/end.
- Prop entering or leaving frame.
- Dialogue line beginning/ending.
- Short reaction shot in the same continuous situation.

These normally remain inside one scene's timeline.

### 5.3 Keep continuous actions together

Keep a continuous action in one module when splitting would complicate character movement, prop trajectory/physics, camera movement, collision/fall/recovery, dialogue exchange, spatial continuity, or persistent visual effects.

### 5.4 Split when it reduces actual risk

Consider a new module when location/time/story state resets, asset dependencies change substantially, a separate narrative unit can be tested independently, or runtime/memory constraints make the existing module unreliable.

### 5.5 No fixed scene-duration quota

There is no mandatory 30-second, 1-minute, or 2-minute scene length. A short complex action may deserve its own module; a longer continuous sequence may remain one module. The agent must justify boundaries using narrative continuity, dependencies, runtime, and testability—not arbitrary duration targets.

## 6. Required decomposition deliverable

Before implementation, create `SCENE_DECOMPOSITION.md` containing:

- Film title and target duration.
- Source breakdown reference/version.
- Canonical asset audit reference.
- Scene count and rationale.
- Scene ID/title.
- Source time range and global film time range.
- Duration and location/environment.
- Characters, props, and asset dependencies.
- Shot IDs contained in each scene.
- Camera setups and required actions.
- Dialogue/audio range.
- Entry state and exit/handoff state.
- Cross-scene continuity dependencies.
- Evidence gaps and uncertainty labels.
- Per-scene validation criteria.

Example table (format only, not source evidence):

| Scene | Source range | Film range | Duration | Location | Boundary rationale |
|---|---|---|---|---|---|
| SC01 | 00:00–01:25 | 00:00–01:25 | 01:25 | Kitchen | Coherent kitchen action |
| SC02 | 01:25–03:10 | 01:25–03:10 | 01:45 | Garden | New location and asset group |

## 7. Scene HTML contract

Every scene HTML must:

- Have a stable ID such as `SC01`.
- Declare title, local duration, global film range, assets, audio cues, entry requirements, and exit/handoff data.
- Open directly in the supported local browser/runtime.
- Initialize a deterministic start state.
- Use canonical assets and approved paths.
- Run its own local timeline and camera choreography.
- Support playback from its beginning and report completion.
- Keep debug controls separate from final cinematic output.
- Show clear development errors for missing assets or failed initialization.
- Contain no production HUD, timer, card, or unrelated UI in the final output unless explicitly requested.

### 7.1 Deterministic timeline

- Drive animation using scene-local elapsed time or an equivalent deterministic timeline.
- Do not use arbitrary chains of `setTimeout` for core choreography.
- Camera, character, prop, dialogue, and sound events must share a timebase.
- Restart/seek must restore a known state.
- Frame-rate variation must not alter intended action duration.
- Completion is based on the declared timeline, not an unverified callback delay.

### 7.2 Lifecycle contract

The implementation must provide equivalent lifecycle operations:

- `initialize(context)`
- `start(startContext)`
- `update(localTimeMs, deltaMs)`
- `pause()`
- `resume()`
- `stop()`
- `dispose()`
- `getHandoffState()`

These are semantic operations; an adapter may expose different names. `dispose()` must release scene-owned listeners, animation loops, audio nodes, render resources, and other resources not intended to survive.

### 7.3 Input and output

The Master Engine may provide film/scene ID, local start time, global film time, playback rate, audio policy, prior handoff state, and shared resources where supported.

The scene reports `ready`, `started`, `paused/resumed`, `error`, `completed`, and handoff state. Do not assume arbitrary JavaScript objects cross isolated documents; serialize and validate cross-document state.

## 8. Master HTML Engine contract

The Master Engine owns:

- Manifest loading and validation.
- Scene order and global film timeline.
- Play, pause, resume, seek, stop, and restart.
- Global music/audio and subtitle synchronization.
- Scene loading/unloading.
- Inter-scene transitions.
- Validated handoff state.
- Missing-file and initialization error handling.
- Playback diagnostics and final duration validation.

Each scene owns:

- Character choreography.
- Prop interaction and movement.
- Local camera choreography and shot changes.
- Environment animation.
- Scene lighting and effects.
- Internal visual continuity.

Do not move every camera cut into the Master Engine. The Master Engine sequences scenes; each scene controls its own shots.

### 8.1 Audio ownership

Default policy:

- Film-level music and continuous soundtrack belong to the Master Engine.
- Scene-specific sound effects may belong to the scene if they are correctly timed and disposed.
- Dialogue/subtitles follow the approved screenplay/audio timeline.
- Never play the same audio source twice across a scene boundary.
- Declare audio ownership and cross-boundary behavior.

### 8.2 Transition ownership

The Master Engine owns transitions between scene documents. Each scene owns internal cuts/transitions.

Declare transition type, duration, outgoing/incoming visibility, initialization timing, audio crossfade policy, and handoff timing. Do not preload multiple WebGL scenes by default.

## 9. Cross-scene continuity and handoff

When a character or prop continues into the next scene, provide a validated handoff record.

Example schema only:

```json
{
  "filmId": "FILM_001",
  "fromScene": "SC01",
  "toScene": "SC02",
  "characters": {
    "BING": {
      "worldPosition": [0, 0, 0],
      "facing": 1.57,
      "costumeVariant": "canonical_default",
      "posePolicy": "reinitialize"
    }
  },
  "props": {
    "PROP_01": {
      "state": "held",
      "holder": "BING"
    }
  },
  "continuityNotes": ["The same prop continues into SC02."]
}
```

Rules:

- Use stable character/prop IDs.
- Do not invent rig node or animation clip names.
- Transfer only state supported by the canonical asset and scene implementation.
- Declare intentional resets.
- Preserve prop identity/state when required by the story.
- Validate handoff data before use.
- Missing critical state must produce a warning or block, not a silent guess.

## 10. Film manifest

Use one authoritative `film.manifest.json`.

Example:

```json
{
  "filmId": "FILM_001",
  "title": "Example Film",
  "version": "1.0.0",
  "durationMs": 900000,
  "aspectRatio": "16:9",
  "scenes": [
    {
      "sceneId": "SC01",
      "title": "Opening",
      "html": "scenes/scene_01.html",
      "filmStartMs": 0,
      "durationMs": 85000,
      "transitionIn": {"type": "cut", "durationMs": 0},
      "transitionOut": {"type": "crossfade", "durationMs": 700},
      "audioGroup": "AUDIO_MAIN",
      "entryState": {},
      "handoffToNext": true
    }
  ]
}
```

Values are illustrative only. Validate unique IDs, valid paths, positive durations, ordered starts, explained gaps/overlaps, transition accounting, asset/audio resolution, and total duration.

## 11. Suggested project structure

```text
film-project/
├── README.md
├── SCENE_DECOMPOSITION.md
├── film.manifest.json
├── index.html
├── engine/
│   ├── master-engine.js
│   ├── scene-loader.js
│   ├── timeline-controller.js
│   ├── transition-controller.js
│   ├── audio-controller.js
│   └── continuity-state.js
├── scenes/
│   ├── scene_01.html
│   ├── scene_02.html
│   └── scene_N.html
├── shared/
│   ├── scene-contract.js
│   └── runtime-config.js
├── assets/
│   ├── characters/
│   ├── environments/
│   ├── props/
│   ├── audio/
│   └── textures/
├── evidence/
│   ├── source-breakdown/
│   └── asset-audit/
└── validation/
    ├── scene-test-report.md
    ├── assembly-test-report.md
    └── continuity-test-report.md
```

This is a reference structure. Preserve the existing repository layout where possible. Do not reorganize an existing repo without audit and a reason.

## 12. Agent execution workflow

### Phase 0 — Read and audit

1. Read this protocol and available referenced TSA documents.
2. Read source breakdown and screenplay.
3. Inspect only the repository areas needed.
4. Audit canonical character HTML, GLB, textures, animation capabilities, props, and environment assets.
5. Record missing evidence/assets.
6. Do not begin implementation if critical asset identity or requirements are unresolved.

### Phase 1 — Decompose

1. Derive scene candidates from narrative and continuity.
2. Map every shot to a scene, unless a deliberate cross-scene transition is documented.
3. Group shots belonging to the same continuous action/environment.
4. Identify entry/exit state and dependencies.
5. Create `SCENE_DECOMPOSITION.md`.
6. Reconcile scene durations with target film duration.
7. Stop for review if the split breaks a continuous action or lacks rationale.

### Phase 2 — Contract and skeleton

1. Create/adapt the manifest.
2. Define lifecycle and message contract.
3. Define audio ownership and transition policy.
4. Create Master Engine skeleton.
5. Create one scene HTML skeleton.
6. Validate standalone launch and Master Engine loading before implementing every scene.

### Phase 3 — Implement scenes incrementally

For each scene:

1. Load canonical assets; do not rebuild without explicit approval.
2. Implement environment and props.
3. Implement character choreography.
4. Implement internal camera/shot timeline.
5. Implement dialogue, subtitles, and sound.
6. Implement deterministic local timeline and lifecycle.
7. Run standalone validation.
8. Record evidence before proceeding.

Do not implement all scenes in parallel while asset, camera, or continuity decisions remain unresolved.

### Phase 4 — Assemble

1. Load validated scene files through Master Engine.
2. Verify order and duration.
3. Verify transitions.
4. Verify audio and subtitle synchronization.
5. Verify character/prop handoff.
6. Verify pause/resume/seek/restart.
7. Verify unload/disposal.
8. Verify total film duration.

### Phase 5 — Deliver and validate

Produce:

- `SCENE_DECOMPOSITION.md`
- `film.manifest.json`
- Scene HTML files.
- Master Engine files.
- `scene-test-report.md`
- `assembly-test-report.md`
- `continuity-test-report.md`
- `FINAL_ACCEPTANCE_REPORT.md`

Reports must distinguish `PASS`, `FAIL`, `BLOCKED`, and `NOT_TESTED`. Never report PASS without execution evidence.

## 13. Acceptance gates

### Gate A — Decomposition

- [ ] Every narrative scene has a module decision.
- [ ] Shot changes are not treated as automatic HTML boundaries.
- [ ] Every shot maps to a scene.
- [ ] Boundaries have written rationale.
- [ ] Scene durations reconcile with the film timeline.
- [ ] Continuous actions are not broken without documented handoff.

### Gate B — Individual scene

- [ ] HTML opens independently.
- [ ] Canonical assets load correctly.
- [ ] Deterministic initial state.
- [ ] Camera and character choreography share a timeline.
- [ ] Dialogue/audio/subtitles follow approved timing.
- [ ] Restart/seek is deterministic.
- [ ] Completion is reported.
- [ ] Owned resources are disposed.

### Gate C — Master Engine

- [ ] Manifest validates.
- [ ] Scene order is correct.
- [ ] Scene documents load/unload.
- [ ] Playback controls work.
- [ ] Transitions work as declared.
- [ ] Audio is not duplicated or lost at boundaries.
- [ ] Handoff preserves required continuity.
- [ ] Missing scene errors are visible.

### Gate D — Final film

- [ ] Complete narrative coverage.
- [ ] Correct total duration, maximum 15 minutes.
- [ ] No unexplained timeline gaps/overlaps.
- [ ] Canonical character identity preserved.
- [ ] No unexpected visual style changes.
- [ ] No unrequested HUD/timer/debug cards.
- [ ] No unresolved critical runtime errors.
- [ ] Full playback tested.

## 14. Failure handling

Stop and report `BLOCKED` when a required canonical asset is unidentified, a critical action/boundary is unsupported, a continuous action cannot be handed off safely, the Master Engine cannot load a scene, audio ownership is ambiguous, duration cannot be reconciled, or runtime/WebGL limits make the architecture unreliable.

Do not hide failures by rebuilding canonical characters without approval, replacing complex motion with static poses, omitting action/dialogue, merging all scenes into one giant HTML without approval, splitting every shot into a separate HTML, or claiming untested continuity.

## 15. Change control

- Source-analysis changes belong in the Video Breakdown Protocol.
- Canonical asset changes belong in the canonical integration protocol.
- Three.js implementation standards belong in the HTML Game/Video Production Protocol.
- Scene lifecycle, manifest, and assembly changes belong here.
- Read and audit existing files before updating them.
- Preserve existing repository behavior with small, reversible patches.

## 16. Final operating rule

The agent must not guess the number of HTML files before understanding the story and auditing assets.

**One scene HTML may contain many shots. Multiple scene HTML files may form one film. The Master Engine assembles those modules into one continuous film of no more than 15 minutes.**

The goal is cinematic continuity, independent testability, maintainability, and reliable assembly—not maximum file count.

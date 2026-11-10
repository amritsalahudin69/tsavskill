# TSA PROTOCOL — HTML Game Systems, Visual Runtime & Series-Video Continuity

**Version:** 1.0.0  
**Date:** 2026-11-06  
**Status:** Evidence-derived protocol baseline  
**Primary references audited:** TABRAKAN, LOMBALARI, RACEBALL uploaded builds  
**Companion standard:** `TSA_Canonical_Character_to_Scene_Integration_Protocol_v1.0.0.md`

---

## 0. Purpose and relationship to CANONICAL.md

This document captures reusable engineering and production knowledge from three existing TSA HTML/Three.js game builds:

- **TABRAKAN** — character presentation, arena sessions, physics, background modes, camera framing, HUD and visual validation.
- **LOMBALARI** — staged obstacle-race architecture, character state, AI decisions, platform support, dynamic obstacles, camera tracking, lifecycle and multi-seed validation.
- **RACEBALL** — modular track generation, deterministic seeded layouts/obstacles, track patterns, physics, AI, character visuals and regression testing.

It extends the character-preservation standard in CANONICAL.md.

The two documents have different responsibilities:

| Document | Authority |
|---|---|
| `CANONICAL.md` | How to preserve and integrate the user's existing character HTML/source implementation |
| `PROTOCOL.md` (this document) | How to build the surrounding HTML/Three.js world, game/video runtime, camera, movement, physics, timeline, continuity and validation |

For a video or game using supplied characters, **both standards apply**.

This document is not a claim that every feature in the three projects is interchangeable or universally proven. It distinguishes source-observed architecture, project-specific evidence, reusable engineering principles, and recommendations that still require validation in a new project.

---

# PART I — TSA EXECUTION MODEL

## 1. Goal-first production

Before implementation, translate the user's request into an explicit outcome.

Record:

- Output: HTML game, standalone film scene, continuous video, or a series of scenes.
- Theme/story/gameplay.
- Characters and their canonical source files.
- Environment and world rules.
- Actions, interactions, obstacles and reactions.
- Camera position, movement, lens/FOV and framing.
- Duration, aspect ratio and output resolution.
- Whether the runtime must be playable, autonomous, deterministic, or exportable.
- Required delivery format and whether external dependencies are permitted.

Do not start by choosing a technology or writing a renderer. Start with the requested experience.

## 2. Inspect before reuse

Read the actual project/source files before implementing. Existing builds are evidence, not vague inspiration.

Minimum inspection:
1. Project state and knowledge files (`TSA_STATE.md`, `TSA_KNOWLEDGE.md`, current pipeline docs).
2. Entry point and module graph.
3. Config/state ownership.
4. Character implementation and assets.
5. Physics and movement.
6. AI or timeline orchestration.
7. Arena/world and obstacle implementation.
8. Camera and visual presentation.
9. Tests, fixtures, screenshots and known blockers.

Do not claim an old pattern is currently available in a new repo until its actual source and dependencies have been inspected.

## 3. Evidence labels

Keep facts, inference and hypotheses separate.

- **SOURCE FACT:** Directly supported by source code or project documentation.
- **TEST EVIDENCE:** Supported by a named test or reproducible run.
- **RUNTIME EVIDENCE:** Observed in the actual browser/runtime.
- **INFERENCE:** A reusable conclusion derived from evidence, not itself directly tested.
- **HYPOTHESIS:** A proposed design that still needs testing.

Use statuses accurately:

- `PASS` — the named acceptance criterion was tested and passed.
- `FAIL` — it was tested and failed.
- `BLOCKED` — testing could not be completed because of a stated blocker.
- `NOT_RUN` — no test was performed.

A passing Node test is not a browser visual pass. An HTTP 200 is not proof that WebGL rendered correctly. A generated HTML file is not proof that the scene looks good.

---

# PART II — PROVEN REUSABLE SYSTEM PRINCIPLES

## 4. Separate authoritative state from presentation

A robust interactive 3D project separates:

1. **Configuration** — tunable values, stage definitions, participant definitions.
2. **Authoritative state** — positions, velocities, grounded/support state, lifecycle, obstacle state, AI state.
3. **Simulation** — physics, collision, AI decisions, obstacle updates and lifecycle transitions.
4. **Presentation** — Three.js meshes, animation pose, camera, lighting, particles, HUD and background.
5. **Orchestration** — session/stage transitions and update ordering.

The visual mesh must not become the only source of truth for gameplay physics.

Likewise, the physics system must not use visual-only scaling or camera effects as collision dimensions unless that relationship is explicitly designed and tested.

### Evidence from the builds

- TABRAKAN has distinct modules for physics, AI, arena, character, effects, HUD, participants and game orchestration.
- LOMBALARI's `Arena` owns platform/support geometry and obstacle runtime; AI selects actions against arena support data; physics owns character movement and landing.
- RACEBALL separates track generation/layout, obstacle patterns/placement, physics, character visuals and game orchestration.

### Reusable rule

Use one authoritative owner for each kind of state. Do not create competing movement systems, duplicate timers, or separate obstacle states that can disagree.

## 5. Fixed-step simulation for gameplay

For physics-driven games, prefer a fixed simulation timestep with an accumulator:

```js
accumulator += clampedFrameDelta;

while (accumulator >= fixedStep) {
  updateSimulation(fixedStep);
  accumulator -= fixedStep;
}

const alpha = accumulator / fixedStep;
renderInterpolated(alpha);
```

The exact timestep and clamping policy must come from the project's requirements and validated configuration.

Why:
- physics becomes less dependent on monitor refresh rate,
- collision and landing behavior become more reproducible,
- AI decisions can be evaluated against consistent simulation time,
- deterministic replay becomes practical when randomness and update ordering are controlled.

TABRAKAN's documented contract uses a 1/60-second accumulator and clamps frame delta. RACEBALL and LOMBALARI also use fixed-step physics patterns in their tested gameplay systems.

Do not confuse a fixed-step game simulation with a film timeline. They solve different problems.

## 6. Deterministic randomness and replay

Use seeded randomness for generated layouts, participant variation and repeatable obstacle patterns.

A seed should be explicit and traceable:
- input seed,
- derived stream or sub-seed,
- participant count/configuration,
- selected layout/pattern,
- generated layout fingerprint,
- generated obstacle fingerprint.

Do not use unrelated calls to `Math.random()` throughout gameplay if reproducibility is required.

Where multiple procedural systems exist, derive separate deterministic streams from the master seed. This prevents adding an obstacle random draw from silently changing the already-approved track layout.

### Evidence from the builds

- TABRAKAN documents Xorshift32 seeded per session (`seed + sessionIdx * 1000`).
- RACEBALL R4/R5 separates deterministic track and obstacle streams; the R5 obstacle stream does not change the R4 track generation.
- RACEBALL's current state records seeded layout/obstacle behavior and same-seed regression suites.
- LOMBALARI uses seeded participant/AI simulations and repeated multi-seed competitions to inspect natural outcomes.

### Reusable rule

The same seed + same configuration + same code version should produce the same procedural world and simulation result, within the determinism limits of the runtime.

Record the seed and configuration with every accepted capture or replay.

## 7. Character state and lifecycle

Keep explicit state machines rather than inferring everything from visual pose.

Common gameplay states seen in these projects include:
- `READY`
- `ACTIVE`
- `FALLING`
- `ELIMINATED`
- `FINISHED`

AI sub-states may include:
- `RUN`
- `EVALUATE_PATH`
- `CHANGE_LANE`
- `AVOID_OPPONENT`
- `JUMP`
- `AIRBORNE`
- `LAND`
- `FALL`

The exact state set is project-specific.

Lifecycle requirements:
- transitions must be explicit,
- terminal events must not fire repeatedly,
- eliminated characters must not revive unless the user explicitly requests a respawn mechanic,
- stage advancement must use validated survivor/finisher data,
- resets must clear the correct state without changing character identity,
- simultaneous events need deterministic tie handling.

LOMBALARI's race lifecycle explicitly validates finish crossing against the actual finish support and carries only valid finishers to the next stage. TABRAKAN's session transitions use a pending guard and do not revive eliminated participants.

## 8. Physics and collision must agree with the world

The visible world and the collision world must describe the same geometry.

Examples from the projects:
- platform support top must equal the visible grass/top surface,
- actual gaps must be unsupported gaps,
- moving platform mesh displacement and collision/support displacement must agree,
- conveyor surface velocity must be represented in the physics model,
- rotating obstacle collision must use the same pivot, radius, angle and contact height as its visual arm,
- bridge support must be removed at the same lifecycle transition as the visual/physical collapse contract.

Do not create visual-only obstacles that gameplay ignores, or invisible collision surfaces that contradict the rendered scene, unless explicitly intended.

### Jumping

A real jump should be a trajectory integrated through velocity/gravity, not a teleport from one platform to another.

The AI may predict a landing target, but physics must decide whether the actual trajectory lands on valid support.

Track useful diagnostic categories where evidence supports them:
- undershoot,
- overshoot,
- lane mismatch,
- missed takeoff,
- support removed,
- collision-interrupted jump.

Do not classify a failure from guesswork; use position, velocity, support and crossing evidence.

## 9. Arena and obstacle ownership

A useful pattern from LOMBALARI is to keep arena geometry and obstacle runtime under one `Arena` authority.

An obstacle definition should declare, as needed:
- unique ID,
- type,
- stage and zone,
- anchor/support platform,
- geometry,
- motion or surface parameters,
- timing/state transitions.

Validate definitions before constructing the world:
- IDs are unique,
- references point to existing platforms/zones,
- dimensions and speeds are finite and bounded,
- obstacles do not occupy forbidden spawn/finish supports,
- motion amplitude stays within physical bounds,
- unsupported or unknown obstacle types are rejected.

Do not scatter obstacle state across unrelated modules.

### Reusable obstacle patterns evidenced by LOMBALARI

| Type | Core behavior | Important contract |
|---|---|---|
| Moving platform | Periodic X/Z movement | Visual mesh, support bounds and carrier motion agree |
| Collapsing bridge | Tile lifecycle | Support remains during warning, then is disabled at the defined transition |
| Rotating sweeper | Rotating beam around pivot | Swept collision, vertical separation and visual arm use the same geometry |
| Conveyor floor | Surface velocity | Grounded movement/AI reach prediction accounts for belt velocity |

These are reusable patterns, not a requirement to put every obstacle into every project.

## 10. AI should reason from physical reachability

Avoid AI that chooses a random lane or jump without considering the actual world.

A more robust decision process:
1. Identify current support.
2. Identify next candidate supports/routes.
3. Check lane and platform bounds.
4. Estimate takeoff runway.
5. Estimate reachable horizontal/lateral displacement.
6. Account for height differences and moving-support velocity.
7. Account for obstacle timing/state.
8. Include character-specific reaction/avoidance attributes where desired.
9. Select a target that is physically reachable.
10. Queue a jump or lane change; let physics execute it.

AI must not guarantee a successful jump merely because it selected a target.

LOMBALARI's documented AI evaluates platform elevation, runway, jump lead, maximum gap, safety margins, moving-platform carrier velocity, conveyor velocity, warning bridge support time and sweeper timing.

## 11. Camera is a separate presentation system

Do not let camera behavior corrupt physics or character scale.

Separate:
- world/character scale,
- camera lens/FOV,
- camera position,
- camera target,
- camera safe frame,
- HUD exclusion areas,
- tracking smoothing and maximum tracking speed.

### Camera principles evidenced by TABRAKAN and LOMBALARI

- Calculate framing from actual world bounds and perspective projection.
- Include platform thickness and the standing character silhouette where relevant.
- Use actual viewport aspect/FOV.
- Account for measured HUD geometry, not arbitrary hardcoded space.
- Keep a stable framing envelope when platforms disappear or obstacles move, avoiding camera jitter.
- Track an active cluster or median focus rather than fitting the entire long course into a tiny view.
- Smooth camera movement using elapsed time and a bounded tracking speed.
- Separate camera framing from visual character scaling.
- Validate multiple viewport sizes and aspect ratios.

TABRAKAN's V1.2 records a specific camera-fit recovery: theoretical jump apex was removed from the permanent standing fit, symmetric margins were used, and event-feed space was reserved only when it actually overlapped the arena. Its camera interpolation was tested for equal one-second displacement at 30, 60 and 120 fps.

LOMBALARI F3 records an active-cluster median camera with lookahead, local view bounds and smoothing. Its camera was designed not to zoom out to fit the entire long stage.

### Camera acceptance

At minimum inspect:
- opening/start composition,
- active movement,
- jump/obstacle moment,
- clustered and spread-out participants,
- finish/result composition,
- portrait and landscape viewports if both are required.

A mathematically projected frame is useful test evidence, but it is not a substitute for a real browser screenshot.

## 12. Visual scale is not physical scale

TABRAKAN documents a separate sprite visual scale multiplier that does not affect physics, AI, collision, jumping or support detection.

Reuse this separation:
- physical collider dimensions belong to simulation,
- character art/model scale belongs to presentation,
- camera fit may consider the visual silhouette,
- physics must not silently change when the art is enlarged.

Preserve source image/model aspect ratio. Do not stretch character assets to fit a layout.

## 13. Background and visual layers

TABRAKAN has a background configuration with `IMAGE`, `SOLID` and `CHROMA` modes. Its `BackgroundManager` is the sole writer of scene background, fog and renderer clear color. The documented implementation handles image fit/crop, sRGB, resize, failure fallback and disposal.

Reusable rule:
- one owner for background/clear/fog state,
- environment/background must not accidentally overwrite character or arena lighting,
- background modes must be explicit,
- loading failure must have a known fallback,
- texture lifecycle must dispose stale resources,
- chroma mode should avoid fog/clouds that contaminate the key color.

For film/video, environment can be more layered and animated:
- far background,
- midground structures,
- foreground objects,
- parallax,
- weather,
- moving lights,
- particles,
- ambient animation.

But these presentation layers must remain separate from authoritative gameplay collision unless they are actual interactive world objects.

---

# PART III — VIDEO AND SERIAL CONTINUITY

## 14. Game runtime and film runtime are not the same

A game uses input and live state as the primary driver.

A film uses a timeline and authored action as the primary driver.

| Concern | Game | Film/video |
|---|---|---|
| Primary driver | Input + game state | Master timeline |
| Character action | Player/AI + physics | Authored action/animation timeline |
| Camera | Gameplay tracking/intent | Cinematic shot plan |
| Physics | Interactive simulation | Can be simulated, baked or timeline-driven |
| Randomness | Seeded procedural behavior | Prefer precomputed/seeded repeatability |
| Duration | Session/gameplay lifecycle | Exact target duration |
| Export | Optional | Often deterministic frame render + mux |
| UI | Gameplay HUD as requested | Usually clean cinematic output unless requested |

Do not turn a film into a game HUD. Do not turn a game into a pre-rendered film when interactivity is required.

## 15. Series continuity: maintain a shared production bible

When a user plans multiple connected videos/scenes, create a persistent series continuity record.

Recommended file:

`SERIES_CONTINUITY.md`

It should include:

### A. Character continuity
- canonical source file and version/hash,
- character scale and proportions,
- costume/material/palette,
- allowed animation capabilities,
- recurring character-specific motion/behavior,
- known source limitations.

Use CANONICAL.md for the detailed source-preservation contract.

### B. World continuity
- world/environment identity,
- geography and spatial layout,
- recurring props and obstacle design,
- material and color language,
- lighting/time/weather rules,
- background layers and recurring visual landmarks.

### C. Camera continuity
- aspect ratio and output resolution,
- lens/FOV or focal length,
- camera height and distance,
- subject scale in frame,
- tracking behavior and smoothing,
- recurring shot grammar,
- rules for intentional shot changes.

Do not assume the same FOV means identical framing if camera distance, viewport aspect, target or subject scale changes.

### D. Motion continuity
- walk/run cycle style,
- acceleration/deceleration behavior,
- jump/landing language,
- interaction timing,
- animation phase/pose continuity across cuts,
- physical constraints and contact behavior.

### E. Visual continuity
- renderer and Three.js revision,
- tone mapping and exposure,
- color management,
- lighting setup,
- shadow settings,
- texture filtering and pixel ratio,
- fog and post-processing,
- background and particle rules.

### F. Narrative continuity
- previous scene ending state,
- next scene opening state,
- character positions/orientations,
- carried props,
- time/weather,
- unresolved action,
- state transitions and cause/effect.

### G. Technical continuity
- project baseline/version,
- assets and checksums,
- deterministic seeds,
- scene duration/frame rate,
- timeline API,
- render/export settings,
- known validation gaps.

## 16. Scene handoff contract for connected videos

Every scene should produce a handoff record:

```json
{
  "seriesId": "SERIES_ID",
  "sceneId": "SCENE_02",
  "continuityIn": {
    "previousScene": "SCENE_01",
    "timeOfDay": "late afternoon",
    "weather": "overcast",
    "characterStates": [],
    "worldState": {},
    "props": []
  },
  "continuityOut": {
    "timeOfDay": "late afternoon",
    "weather": "overcast",
    "characterStates": [],
    "worldState": {},
    "props": [],
    "nextSceneHook": ""
  },
  "visualContract": {
    "aspectRatio": "16:9",
    "renderer": "Three.js",
    "camera": {},
    "lighting": {},
    "colorPipeline": {}
  },
  "canonicalCharacters": [],
  "validation": {}
}
```

This is a template, not a filled story fact. Populate it from the actual scene brief and previous accepted scene.

The next scene must read the prior accepted handoff rather than inventing a new starting state.

## 17. Deterministic film timeline

For HTML video, use a single authoritative timeline.

A robust contract exposes absolute-time seeking:

```js
window.TSA_VIDEO = {
  duration: 60,
  fps: 30,
  setTime(seconds) {
    // Derive all animated state from this absolute time.
    // Camera, characters, environment, effects and dialogue
    // must be set consistently for the same input time.
  }
};
```

Do not depend on how many animation frames have elapsed to determine scene state.

Avoid unseeded randomness in:
- particle positions,
- crowd animation,
- weather,
- camera shake,
- procedural background movement.

If randomness is required, use a fixed seed or precomputed event stream.

For exact-duration output:
- define duration and FPS,
- define frame count,
- ensure the final frame maps to the intended end time,
- render at exact timestamps,
- mux audio/video with explicit timing,
- verify output duration and frame count.

A `requestAnimationFrame` preview loop is useful for browser playback, but alone it does not guarantee deterministic offline rendering.

## 18. Continuous scene integration

For a series built from standalone scene HTML files:
- keep each scene independently runnable,
- keep character source identity consistent,
- keep shared visual parameters in a reusable continuity config,
- record each scene's in/out state,
- ensure the next scene begins from the prior accepted end state,
- avoid duplicating and drifting shared character implementations.

Possible structure:

```text
series/
├── SERIES_CONTINUITY.md
├── shared/
│   ├── characters/
│   ├── visual-config.js
│   ├── camera-presets.js
│   └── environment-assets/
├── scenes/
│   ├── scene-01/
│   │   ├── scene.html
│   │   └── handoff.json
│   ├── scene-02/
│   │   ├── scene.html
│   │   └── handoff.json
│   └── scene-03/
│       ├── scene.html
│       └── handoff.json
└── export/
```

This is a recommended organization. Adopt only the pieces that fit the user's workflow; do not force a large framework for a small project.

---

# PART IV — VISUAL AND ASSET PIPELINE

## 19. Character asset types are not interchangeable

The projects demonstrate different character presentation strategies:

- TABRAKAN uses PNG character artwork as camera-facing Three.js billboard sprites.
- RACEBALL restores and uses a set of original character PNGs, while separating character visuals from physics/game state.
- LOMBALARI uses its own character/participant presentation layer and a visual contract based on the supplied PNG art.

Choose based on the actual supplied asset:
- PNG/sprite: preserve aspect ratio, alpha and source image identity.
- GLB/GLTF: inspect mesh hierarchy, materials, skeleton, animation clips and transforms.
- Character HTML: inspect actual embedded geometry, materials, hierarchy, pivots and runtime.
- Procedural character: preserve the accepted generator/configuration and distinctive silhouette.

Do not convert an asset to another representation unless there is a concrete need and a validation plan.

## 20. Visual references need a hierarchy

When the user supplies reference images or a visual blueprint, define:
1. Primary reference — composition and visual language.
2. Secondary reference — mechanical or detail guidance.
3. Explicit written constraints.
4. Inferences that need approval or validation.

Do not treat every visible detail in a reference as authorization to invent new mechanics.

LOMBALARI's `VISUAL_CONTRACT.md` explicitly separates observed reference facts from design inferences and unverified details. This is a reusable practice.

## 21. Pixel sharpness and resolution

TABRAKAN's V1.3 evidence shows that:
- canvas CSS size, backing element and WebGL drawing buffer should be checked independently,
- DPR changes must update the drawing buffer on resize,
- loaded source image dimensions constrain recoverable detail,
- a low-resolution source asset cannot be made truly high-detail by renderer settings alone,
- label textures may need higher-resolution source canvases,
- visual sharpness claims should be based on actual screenshots.

For pixel-art:
- use nearest-neighbor sampling where appropriate,
- preserve source pixel dimensions and aspect ratio,
- avoid accidental CSS resampling or fractional scaling,
- keep pixel-art character rendering distinct from richer 3D environments if that is the approved art direction.

For smooth 3D:
- choose renderer antialiasing, DPR and texture filtering based on actual runtime performance and screenshots.

Do not apply one global rendering policy to all assets.

---

# PART V — VALIDATION AND REGRESSION

## 22. Required validation layers

### Gate A — Static/source
- syntax checks,
- module graph,
- dependency availability,
- exact-case asset paths,
- config/schema validation,
- no unintended source replacement.

### Gate B — Unit/contract
- physics calculations,
- collision/support boundaries,
- state transitions,
- obstacle lifecycle,
- AI reachability calculations,
- seeded generation and fingerprints,
- camera projection/framing calculations.

### Gate C — Integration simulation
- full stage/round lifecycle,
- many participants,
- multiple seeds,
- terminal-state completion,
- no stuck entities,
- no duplicate events,
- no non-finite state,
- reset/replay behavior,
- same-seed replay equality.

### Gate D — Browser/runtime
- actual page starts,
- modules/assets load,
- WebGL renders,
- console/runtime errors,
- interactions/gameplay occur,
- scene transitions work,
- resize and aspect ratios work.

### Gate E — Visual acceptance
- screenshots at required viewport sizes,
- character scale and identity,
- camera composition,
- HUD overlap,
- environment depth,
- motion readability,
- obstacle visibility,
- visual reference comparison.

### Gate F — Production/export
- deterministic seeking,
- exact frame count/duration,
- repeatable rendering,
- audio/video mux,
- final file playback and metadata.

A project can pass Gates A–C and still be PARTIAL because Gates D–F were not run.

## 23. Seeded simulation is evidence, not a substitute for playability

Use multiple seeds and full competition runs to find:
- softlocks,
- stuck racers,
- unreachable routes,
- balance outliers,
- invalid terminal states,
- nondeterministic event duplication.

Record:
- seed range,
- entrant count,
- finishers/OUT,
- stage duration,
- route selection/entry/merge,
- obstacle contacts and falls,
- stuck timeouts,
- replay comparison.

Do not tune difficulty with arbitrary elimination quotas. Prefer physical causes, AI reachability and evidence-based calibration.

## 24. Camera validation must be measured and visually checked

Projection tests can verify that expected world bounds fit mathematically.

Also capture actual screenshots:
- start,
- active gameplay,
- jumps,
- obstacles,
- stage transitions,
- finish/results,
- each target viewport/aspect ratio.

Record pixel measurements where useful:
- projected character height,
- arena bounds,
- clipping,
- HUD overlap,
- safe-frame occupancy.

Label theoretical measurements as theoretical. Label actual browser screenshot measurements as runtime evidence.

## 25. Regression discipline

For every patch:
1. State the baseline and authorized scope.
2. Identify existing passing tests.
3. Add focused tests for the changed behavior.
4. Run targeted tests first.
5. Run relevant regression suites.
6. Run browser/runtime validation when available.
7. Compare against prior accepted behavior.
8. Report untouched systems and known limitations.

Do not change physics, camera, character art, background and HUD together unless the objective requires it. Isolate causes so regressions can be attributed.

---

# PART VI — EVIDENCE FROM THE THREE REFERENCE BUILDS

This section records what the uploaded archives actually support. It is not a claim that every project is at the same validation level.

## 26. TABRAKAN — reusable evidence

### Source-observed architecture
- Three.js 0.160.0 is stored locally as `vendor/three.module.js`.
- No bundler/transpiler; bare `three` import is resolved through an import map.
- Modular entry flow: `main.js` → `game.js` → physics, AI, arena, character, effects, HUD and participants.
- Characters use `THREE.PlaneGeometry` with `MeshBasicMaterial` and camera-facing quaternion updates.
- Fixed-step physics accumulator: 1/60 second with frame-delta clamp.
- Seeded Xorshift32 RNG per session.
- Tile geometry is grouped, with top mesh and bevel edge.
- Particle systems use preallocated pools.

### Source-observed game contracts
- Gravity is integrated through velocity.
- Horizontal collision uses circle-circle logic in XZ, overlap separation and mass-weighted impulse.
- Jump trajectory is integrated, not teleported.
- Session progression is explicit.
- Eliminated participants do not revive.
- Session transition uses a pending guard.
- Collapsing tile lifecycle is explicit and removes support at a defined state.

### Camera/background/visual evidence
- Camera fit considers perspective FOV/aspect and projected layout geometry.
- Framing is HUD-aware.
- Camera fit bounds are retained when tiles disappear to avoid collapse-driven jitter.
- Sprite visual scaling is separate from physics.
- Background modes include IMAGE, SOLID and CHROMA with one background manager.
- V1.2 includes deterministic camera projection comparisons and frame-rate-independent camera interpolation tests.
- V1.3 records actual headless Chrome captures for selected UI/canvas/resizing checks, including 1920×1080, 1280×720 and DPR-2 resize.

### Limitations in the supplied knowledge
- Full game progression, collisions, jumping, falling, collapse and all background modes were not all proven end-to-end in the cited V1.3 record.
- Audio/SFX are not implemented in the recorded knowledge.
- Source PNG resolutions vary; the renderer cannot restore missing source detail.

## 27. LOMBALARI — reusable evidence

### Source-observed architecture
- Three.js project with modular `config`, `main`, `game`, `arena`, `character`, `participants`, `physics`, `AI`, `camera`, `effects`, `background`, `HUD`, `obstacles` and `race-lifecycle`.
- `Arena` owns platform geometry, support bounds, zones, dynamic obstacle instances and obstacle events.
- Physics owns authoritative character position/velocity/support/fall state.
- AI reasons about physical supports, lanes, jump reachability and obstacle state.
- Camera tracks the active racer cluster locally rather than fitting the entire course.
- Stage lifecycle explicitly validates finishers and resets only eligible survivors.

### Geometry and world contracts
- Stage definitions contain ordered spawn, intermediate and finish platforms.
- Platform dimensions and coordinates are validated.
- Real gaps and distinct support elevations are required.
- Zones must reference actual platform IDs.
- Obstacle IDs and references are validated.
- Dynamic obstacle movement is bounded by platform geometry and maximum configured speed.

### Obstacle systems evidenced
- Moving platforms on X/Z axes with bounded periodic motion.
- Collapsing bridge tiles with `SOLID → WARNING → COLLAPSING → FALLING → REMOVED`.
- Rotating sweeper with pivot, beam, swept collision and vertical separation.
- Conveyor floor with surface velocity, visual belt and AI/physics adaptation.
- Effects use a bounded particle pool.
- Mesh disposal/recreation on stage reset is tested for leak-free behavior.

### AI and balance evidence
- AI evaluates next-platform candidates using height, runway, jump lead, max gap and safety margins.
- Moving platform carrier velocity and conveyor surface velocity are included in reach calculations.
- AI can wait for a moving platform or obstacle timing within bounded timeout logic.
- Bridge warning time and support removal are synchronized with physics.
- Multiple 20-seed and 40-seed competition simulations are documented.
- Same-seed full competition replay was recorded as bit-identical in the P4 evidence.
- No stuck racers were recorded in the cited 120 stage executions.

### Camera evidence
- Three-stage arena is divided into ordered zones.
- Camera uses the densest active-racer cluster/median focus, lookahead, local view and smoothing.
- Finished/eliminated racers are excluded from active focus.
- Camera does not zoom out to fit the entire long course.
- Camera projection checks were recorded for 1920×1080 and 1280×720.

### Critical validation caveat
The supplied LOMBALARI state repeatedly records browser visual/gameplay validation as `NOT_RUN` for multiple iterations because a browser runtime was unavailable at those times. Production-module tests and seeded simulations passed, but those results do not prove the browser-rendered obstacle behavior or visual quality. Overall status in those records is `PARTIAL`.

## 28. RACEBALL — reusable evidence

### Source-observed architecture
- Three.js 0.160.0 is stored locally.
- Modular track generation/layout, obstacle patterns/placement, physics, character visuals and game orchestration.
- Fixed-step race loop.
- Track layouts include modular Track L and Track S, plus seeded RANDOM and PATTERN pathways.
- Obstacle pattern selection is represented as shared state consumed by renderer, animation, AI and collision.
- Original 30 character PNGs and 3 arena sprites were restored; source checksums were verified in the project timeline.

### Procedural generation evidence
- R4 constrained seeded random track generation.
- R5 uses a separate deterministic obstacle stream without changing R4 layouts.
- Pattern engine separates pattern library/connector from pattern layout and placement.
- PATTERN mode reuses the fixed-step race loop.
- Ramps and turns include surface-height grounding/landing, 3D segment heights, elevation-aware rails/shadows and smoothed vertical camera framing.
- Existing Track L, Track S, RANDOM and AI behavior were regression-tested after pattern work.
- Tests include P1/P2/P3, AI, forward perspective, Track L, modular track, seeded random and seeded obstacles.

### Critical validation caveat
The supplied `current-state.md` explicitly records Node test suites as passing while browser smoke/visual acceptance was unavailable. The correct state is therefore code/test evidence with browser visual acceptance still pending, not a blanket runtime/visual PASS.

---

# PART VII — MASTER EXECUTION PROMPT

Use this prompt with any coding agent. Attach the relevant canonical character HTML/assets, the user's theme/story prompt, and this protocol.

```text
You are an implementation agent operating under TSA.

Read:
1. CANONICAL.md (character source-preservation standard).
2. PROTOCOL.md (this game/video/runtime standard).
3. Project TSA_STATE.md and TSA_KNOWLEDGE.md, if supplied.
4. The actual source files and assets relevant to this task.

OBJECTIVE
[Describe the requested HTML game, film, video, or connected scene.]

CANONICAL CHARACTER INPUTS
[Attach/list exact character HTML/assets.]

THEME / STORY / GAMEPLAY
[Insert the user's creative prompt. Preserve the user's intended story and requirements.]

SOURCE AUDIT FIRST
Inspect actual character source, asset dimensions/checksums where relevant,
module architecture, renderer, camera, hierarchy, animation, physics and dependencies.
Do not rebuild a supplied canonical character from memory or screenshot.

ARCHITECTURE DECISION
Choose the smallest architecture that satisfies the objective:
- film: master timeline drives authored scene actions;
- game: input and authoritative game state drive gameplay;
- mixed: gameplay state owns play, timeline owns cutscenes only.

IMPLEMENTATION RULES
- Preserve canonical character geometry, materials, proportions, silhouette and details.
- Separate character identity from theme-dependent presentation.
- Keep one authoritative owner for each state.
- Use fixed-step simulation for physics-driven gameplay.
- Use seeded randomness for repeatable procedural output.
- Keep render meshes and physics/collision state consistent.
- Validate world/obstacle geometry and all references.
- Keep camera separate from physics and character scale.
- Build scene/world/camera/lighting/action according to the user theme.
- Implement every required beat/action/reaction, not just dialogue or idle loops.
- For connected videos, read and update SERIES_CONTINUITY.md and scene handoff records.
- Avoid unrelated refactors and unnecessary dependencies.
- Preserve unrelated working-tree changes.

VALIDATION
Run the most relevant static, unit, integration, seeded simulation, browser,
visual, and production/export checks available.
Report each gate as PASS, FAIL, BLOCKED or NOT_RUN.
Never claim browser visual/runtime success from source inspection or Node tests alone.

DELIVER
Provide the requested artifact, exact verified path, concise change summary,
source reuse/adaptation record, tests run, visual/runtime status, and remaining gaps.
Update TSA_STATE.md and TSA_KNOWLEDGE.md only with evidence-backed durable findings.
```

---

# PART VIII — PROJECT KNOWLEDGE MAINTENANCE

## 29. Required durable files

For a project intended to continue across sessions or agents, maintain:

```text
project/
├── CANONICAL.md
├── PROTOCOL.md
├── TSA_STATE.md
├── TSA_KNOWLEDGE.md
├── SERIES_CONTINUITY.md     # if connected film/video series
├── CHANGELOG.md
├── assets/
├── scenes/
├── js/
└── tests/
```

Use:
- `CANONICAL.md` for character-source preservation.
- `PROTOCOL.md` for reusable engineering and production method.
- `TSA_STATE.md` for current stage, current baseline, blockers and next authorized action.
- `TSA_KNOWLEDGE.md` for facts proven in this specific repository.
- `SERIES_CONTINUITY.md` for cross-scene/video continuity.
- `CHANGELOG.md` for dated changes.

Do not copy all project-specific facts into the general protocol. Keep general principles here and evidence/state in the relevant project knowledge files.

## 30. Update protocol without knowledge rot

When new work is completed:
1. Identify whether the result is a general reusable principle or only project-specific.
2. Record the source/test/runtime evidence.
3. Record limitations and untested behavior.
4. Update this protocol only for durable general knowledge.
5. Update project `TSA_KNOWLEDGE.md` for project-specific proven facts.
6. Update `TSA_STATE.md` for the current implementation status.
7. Add a dated entry to `CHANGELOG.md`.
8. Preserve the previous accepted baseline and record migrations.

Never convert a hypothesis into a fact merely because an agent proposed it.

---

# FINAL TSA LOCK

The combined production method is:

**CANONICAL CHARACTER SOURCE**
→ **SOURCE AUDIT**
→ **TSA WORLD / GAME / FILM ARCHITECTURE**
→ **THEME-DRIVEN EXECUTION**
→ **CAMERA + MOTION + PHYSICS / TIMELINE**
→ **VALIDATION**
→ **CONTINUITY HANDOFF**
→ **NEXT SCENE / VIDEO**

The character source defines who the character is.

The user's prompt defines what happens.

The protocol defines how the agent must implement it without destroying the baseline.

For connected videos, accepted scene state, character identity, world rules, camera language and rendering settings must carry forward through explicit continuity records.

**Do not guess what already exists. Inspect it. Reuse what is proven. Change only what the objective requires. Validate what the audience will actually see.**

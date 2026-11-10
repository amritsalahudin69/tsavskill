# TSA VIDEO BREAKDOWN PROTOCOL
## Source Video → Verified Cinematic Breakdown → HTML/Three.js Execution Specification

**Protocol ID:** TSA-VBP  
**Version:** 1.0.0  
**Status:** Initial baseline  
**Decision profile:** Both fidelity layers · Animation and gameplay sources · Modular Markdown output  
**Primary analysis platform:** Gemini or another agent with reliable access to the supplied YouTube video  
**Execution platform:** Any coding agent capable of inspecting the canonical assets and building HTML/Three.js  
**Companion standards:** `CANONICAL.md` and the TSA HTML Game/Video Production Protocol

---

# 0. PURPOSE AND NON-NEGOTIABLE PRINCIPLES

This protocol defines how to transform a YouTube video—animation, gameplay, or game cinematic—into a detailed, evidence-grounded production breakdown that can be executed as an HTML/Three.js film.

The goal is not merely to summarize a video. The goal is to create a production document that preserves the source's meaningful content and can guide a separate implementation agent without requiring it to guess essential details.

The protocol produces **two distinct fidelity layers**:

1. **SOURCE RECONSTRUCTION:** what is actually visible or audible in the source.
2. **CINEMATIC ADAPTATION:** optional, clearly separated improvements or implementation adaptations for the planned HTML film.

Never mix observed facts with creative recommendations.

## 0.1 Core rules

- The source video is the evidence authority for what happened in the video.
- A transcript is evidence for spoken words, but not automatically for visual action, camera framing, or exact speaker identity.
- A generated summary is not a complete timeline.
- A scene is not the same thing as a shot.
- A camera label such as "dynamic tracking" is not an executable camera specification.
- A character action must be described as a sequence of observable movement phases, not just a verb such as "runs" or "falls".
- Environment must be described as spatial geography and dynamic behavior, not only as a background color or theme.
- Source duration and timeline coverage must be accounted for from first frame to last frame.
- If evidence is unavailable, mark it as unknown or unverified. Never invent a value to make the document look complete.
- HTML execution must follow the actual capabilities of canonical character assets and the runtime.
- Do not add timers, cards, HUD, labels, or decorative UI to the film unless present in the source or explicitly requested. Subtitles are allowed only for actual dialogue/narration or explicit user direction.

## 0.2 The two-layer fidelity decision

| Layer | Purpose | Permitted changes |
|---|---|---|
| A. Source Reconstruction | Accurately document source events, dialogue, visuals, timing, and editing | No invented events or dialogue; uncertainty must be labelled |
| B. Cinematic Adaptation | Propose how to reproduce or improve the source for HTML/Three.js | May adapt shots, staging, effects, or motion when required, but must preserve the agreed story/events unless user authorizes narrative changes |

Every adaptation recommendation must point back to a source event or a stated production constraint.

---

# 1. SCOPE: SUPPORTED SOURCE TYPES

The protocol supports three source categories. Classify the source before analysis.

## 1.1 Animation (2D or 3D)

Analyze:
- character design, silhouette, proportions, costume and visual style;
- staging and screen direction;
- pose changes, anticipation, action, contact, follow-through and recovery;
- facial expression and body language;
- background/environment animation;
- shot composition, camera movement and editing;
- dialogue, sound effects and music when audible.

Do not assume that 2D animation has a physically moving camera. Distinguish camera movement from background/character movement and multiplane/parallax effects.

## 1.2 Gameplay recording

Analyze:
- game genre and visible game mode, only as far as observable;
- player-controlled character or vehicle;
- visible AI/opponent behavior;
- world geometry and traversable routes;
- gameplay camera type and behavior;
- movement, physics-like behavior, collisions, jumps, attacks, pickups and state changes;
- UI/HUD only as source evidence;
- objective, progress, failure/success states, and event sequence;
- whether a camera movement is player-controlled, game-system-controlled, or edited into the recording, if this can be determined.

Do not mistake camera shake, frame drops, motion blur, animation, or scripted events for physics evidence without sufficient support.

## 1.3 Game cinematic / mixed source

Separate:
- real-time gameplay,
- scripted in-engine cutscene,
- pre-rendered cinematic,
- editorial footage,
- overlays added by the video creator.

If the source type changes during the video, record the transition and classify each relevant segment.

---

# 2. REQUIRED EVIDENCE LABELS

Every important claim should be traceable to the source and carry an evidence label.

| Label | Meaning | Example |
|---|---|---|
| `OBSERVED` | Directly visible in the video | Character enters from frame-left |
| `AUDIO_VERIFIED` | Directly audible | A voice says a specific sentence |
| `TRANSCRIPT_ONLY` | Present in supplied transcript but not independently checked against audio | Dialogue text supplied by transcript |
| `MEASURED` | Read from reliable source metadata or measured from frames | Video duration reported by player metadata |
| `ESTIMATED` | Approximation from visual evidence | Camera appears low and approximately waist-height |
| `INFERRED` | Reasoned interpretation from multiple observations | Character likely reacts to an off-screen sound |
| `ADAPTATION_PROPOSAL` | New production recommendation, not a source fact | Use a short dolly-in to emphasize the reaction |
| `UNVERIFIED` | Cannot currently be established | Exact lens focal length unavailable |

Use these labels in tables or concise annotations. Do not label every sentence mechanically if that makes the document unreadable, but all technical values and uncertain claims must be traceable.

## 2.1 Confidence

When useful, add confidence:
- High: clearly visible/audible or metadata-backed.
- Medium: reasonable estimate with some ambiguity.
- Low: weak visual evidence or incomplete access.

Confidence does not turn an inference into a fact.

## 2.2 Source references

For each scene/shot, include:
- source time range (`HH:MM:SS.mmm` where practical);
- frame or playback timestamp inspected, if available;
- transcript reference if dialogue is involved;
- notes about skipped, obscured, or inaccessible footage.

Do not claim frame-accurate inspection if only sampled playback frames were examined.

---

# 3. INPUT CONTRACT

The user or requesting agent should provide:

**Required**
- YouTube URL or source video file.
- Requested output goal: faithful reconstruction, cinematic adaptation, or both (default: both).
- Whether source dialogue should be retained.
- Target HTML output type: standalone scene, multiple scenes, or full film.

**Useful**
- Transcript with timestamps.
- Existing story/script.
- Canonical character HTML/GLB/GLTF/PNG assets.
- Existing world/environment assets.
- Target duration, aspect ratio and FPS, if different from source.
- Technical constraints (offline, local Three.js, no libraries, browser target, etc.).

If the user has already supplied an item, do not ask for it again.

---

# 4. ANALYSIS PIPELINE

The analysis must be performed in stages. Long videos must not be treated as one uninterrupted summarization task.

## Stage 01 — Source Audit

Create `01_SOURCE_AUDIT.md`.

Record:
- source URL/title;
- source category: animation / gameplay / game cinematic / mixed;
- actual duration and source of duration evidence;
- aspect ratio, resolution and FPS only when known;
- language and transcript availability;
- analysis access method and limitations;
- broad narrative/gameplay structure;
- known gaps or inaccessible intervals;
- initial character and location inventory.

Do not infer unavailable metadata.

## Stage 02 — Coverage Ledger

Create `02_COVERAGE_LEDGER.md`.

Divide the entire source duration into consecutive intervals. Every interval must have one status:

- `ANALYZED`
- `PARTIALLY_ANALYZED`
- `NOT_ANALYZED`
- `INACCESSIBLE`
- `NO_SIGNIFICANT_VISUAL_CHANGE` (only when actually inspected)

The ledger must:
- begin at the source start;
- end at the source end;
- contain no unexplained time gaps;
- contain no accidental overlaps;
- identify intervals requiring a second pass.

For long videos, choose analysis chunk sizes according to event density, not a fixed arbitrary duration. Action-heavy sequences may need shorter chunks; slow dialogue scenes may permit longer chunks.

**Coverage calculation:**

`Coverage % = analyzed source duration / total source duration × 100`

Report partial, inaccessible and unverified durations separately. A 100% timeline partition does not mean 100% visual understanding; it only means all source time has been accounted for.

## Stage 03 — Narrative and Scene Breakdown

Create `03_NARRATIVE_SCENE_BREAKDOWN.md`.

Identify:
- narrative acts or gameplay phases;
- scene boundaries;
- location changes;
- time jumps;
- objective/conflict changes;
- entrances and exits;
- scene transitions;
- opening and ending state.

A scene is a continuous dramatic or gameplay unit in a location/context. A shot is a continuous camera view. One scene can contain many shots.

For gameplay:
- use gameplay phase/encounter/round/level when "scene" is not a natural unit;
- retain the term scene as a production grouping, not as a claim that the game itself has cinematic cuts.

Every scene needs:
- Scene ID;
- start/end time;
- duration;
- location/context;
- characters/participants;
- purpose or gameplay function;
- source events;
- in-state and out-state;
- evidence/uncertainty notes.

## Stage 04 — Cinematic Shot Breakdown

Create `04_SHOT_BREAKDOWN.md`.

Every meaningful camera setup or editorial cut should receive a shot ID.

For each shot, document:

### A. Shot identity
- Shot ID and parent Scene ID.
- Source start/end time and duration.
- Cut/transition type.
- Source evidence label.

### B. Framing and composition
- Shot size: EWS, WS, FS, MLS, MS, MCU, CU, ECU, insert, POV, OTS, or descriptive equivalent.
- Camera angle: eye-level, low, high, bird's-eye, worm's-eye, Dutch, etc.
- Subject placement: center, thirds, left/right, foreground/background.
- Headroom, lead room, look room, negative space.
- Foreground/midground/background layering.
- Screen direction and visible spatial relationships.

### C. Camera specification
- Camera type: static, pan, tilt, dolly, truck, pedestal, crane, orbit, handheld, tracking, follow, chase, gameplay camera, or mixed.
- Start position relative to subject/world.
- End position relative to subject/world.
- Camera height and distance, if measurable/estimable.
- Target/look-at point.
- Movement direction and path.
- Movement speed profile: constant, accelerating, decelerating, ease-in/out, handheld variation.
- Lens/FOV only if known or responsibly estimated.
- Focus target and depth-of-field behavior if observable.
- Stabilization or shake behavior.

Do not fabricate exact focal length, camera coordinates, or speed from an ordinary video frame. If not measurable, describe relative behavior and mark numeric values as `UNVERIFIED`.

### D. Shot purpose
- What information does the shot reveal?
- What emotion or gameplay information does it communicate?
- Why does the shot begin/end here?
- What must remain visible for the audience to understand the action?

## Stage 05 — Character and Motion Breakdown

Create `05_CHARACTER_MOTION.md`.

### Character Bible
For every recurring character/participant:
- stable ID and source name/label;
- observable appearance and silhouette;
- proportions and costume;
- dominant colors and material appearance;
- distinctive features;
- apparent size relative to environment/other characters;
- role in the story/gameplay;
- source limitations (occlusion, low resolution, off-screen intervals).

Do not identify a real person from an image unless the source itself names them and the task is about that named public/source character; do not guess identity.

### Motion Event Record
Every important action receives an Action ID and includes:

1. Start/end time.
2. Character ID.
3. Initial position, orientation and pose.
4. Trigger/cause if observable.
5. Anticipation.
6. Main action.
7. Contact/interaction.
8. Follow-through.
9. Recovery/resulting pose.
10. Movement direction and path.
11. Speed/tempo (qualitative unless measurable).
12. Body parts visibly involved.
13. Interaction with ground/props/other characters.
14. Camera relationship.
15. Evidence and uncertainty.

Not every action visibly contains all animation principles. Mark phases `NOT_OBSERVED` rather than inventing them.

### Gameplay-specific motion
Also record:
- input-like movement only if inferable from the visible action, not assumed;
- jump/landing;
- acceleration/braking;
- collision and knockback;
- vehicle/weapon/tool state;
- route choice;
- AI response;
- game-state transitions.

Separate visible result from inferred internal game logic.

## Stage 06 — Environment and Spatial Bible

Create `06_ENVIRONMENT_SPATIAL_BIBLE.md`.

For each location/level/arena:

### Spatial layout
- world orientation and main axes if inferable;
- entry/exit points;
- routes and traversable areas;
- walls, floors, ceilings, platforms, doors, windows, landmarks;
- relative dimensions and distances;
- elevation changes;
- obstacles and interaction points;
- character-to-environment spatial relationships.

### Layering
- foreground;
- action/midground;
- background;
- distant background/skybox;
- occlusion and parallax.

### Materials and condition
- ground, wall, foliage, water, glass, metal, fabric, stone, asphalt, etc.;
- roughness/reflection/transparency appearance;
- damage, wetness, dirt, wear, deformation.

### Dynamic environment
- wind, rain, water, smoke, fog, dust, moving lights, vegetation, moving props;
- cause and timing of changes;
- interaction with characters or gameplay.

### Continuity map
Maintain a consistent location map. A door, platform, staircase, landmark, or prop must not jump to another location between shots without a justified camera/world transition.

If the source does not reveal a complete layout, record only the visible portion and mark unseen geography as unknown.

## Stage 07 — Lighting and Color Bible

Create `07_LIGHTING_COLOR_BIBLE.md`.

Record:
- time of day, if observable;
- key/fill/rim/backlight roles;
- direction and softness;
- ambient illumination;
- practical lights;
- shadow direction/length/softness;
- reflections and specular response;
- fog, haze, dust and atmospheric perspective;
- dominant and accent colors;
- contrast, saturation and color-temperature relationships;
- changes over time.

Do not prescribe PBR/HDRI/SSAO/Bloom/SSR/DoF universally. Select rendering techniques later based on source style, canonical assets, performance and browser support.

## Stage 08 — Dialogue, Subtitle and Sound

Create `08_DIALOGUE_SOUND.md`.

For each dialogue event:
- Dialogue ID;
- speaker ID/name, or `UNKNOWN_SPEAKER`;
- exact wording in source language;
- start/end timestamp;
- overlap/interruption;
- emotion and delivery only when audible/observable;
- transcript/audio evidence label;
- subtitle text and timing.

Rules:
- Preserve exact source wording when the source audio/transcript supports it.
- Mark uncertain words as `[unclear]`; do not silently repair or paraphrase.
- Do not assign a line to a character solely because the character is on screen.
- Narration, lyrics, dialogue and sound effects must be distinguished.
- Subtitle policy is explicit: only render dialogue/narration requested by the user; do not add explanatory cards or UI.
- For lyrics, preserve only what is necessary and permitted by the user's task; do not invent missing lyrics.

Sound design:
- dialogue;
- narration;
- music;
- ambience;
- action SFX;
- UI/game SFX (if source has them);
- silence and dynamic changes.

## Stage 09 — Editing and Continuity

Create `09_EDITING_CONTINUITY.md`.

Record:
- cut points and transition types;
- screen direction;
- 180-degree axis where applicable;
- eyeline relationships;
- shot-reverse-shot logic;
- match-on-action;
- spatial continuity;
- time continuity;
- character/prop continuity;
- action state at cut;
- intentional discontinuities.

For gameplay recordings, distinguish in-game camera transitions from video-editor cuts.

## Stage 10 — Cinematic Adaptation

Create `10_CINEMATIC_ADAPTATION.md`.

This is the second fidelity layer. It must never overwrite the source reconstruction.

For each proposed change, include:
- linked source Scene/Shot/Action IDs;
- source limitation or opportunity;
- proposed change;
- reason (clarity, pacing, framing, asset limitation, performance, emotional emphasis);
- impact on story/event order;
- impact on duration;
- impact on camera/continuity;
- implementation complexity;
- whether user approval is required.

Adaptation may:
- adjust shot size or camera path;
- simplify physically impossible source motion to fit canonical character rigs;
- add environmental depth or secondary motion;
- improve visual readability;
- redistribute shot durations only if total duration and key event timing remain within the user's approved constraints.

Adaptation must not silently:
- remove a meaningful event;
- change who wins/loses;
- alter dialogue meaning;
- change character identity;
- invent a new location or prop as if it existed in the source;
- alter ending state.

## Stage 11 — HTML/Three.js Execution Specification

Create `11_HTML_EXECUTION_SPEC.md`.

This document translates accepted source reconstruction/adaptation into implementation instructions.

It must reference `CANONICAL.md` and the HTML Game/Video Production Protocol.

Include:

### A. Runtime contract
- single scene or multiple standalone scene files;
- renderer/library version;
- aspect ratio and target resolution;
- duration and FPS;
- timeline API for film;
- input/state API for gameplay;
- local/offline dependency requirements;
- audio/subtitle handling;
- export requirements.

### B. Asset mapping
For each character/prop/environment:
- source file;
- canonical status;
- actual available geometry/rig/animation;
- reuse method;
- required adaptation;
- unsupported motions or missing assets.

Do not assume an asset exists. Do not rebuild canonical characters without authorization.

### C. Scene implementation
- scene graph;
- environment layers;
- props;
- lighting;
- materials;
- particles;
- camera rig;
- action timeline;
- transitions;
- dialogue/subtitle events.

### D. Motion implementation
Map each Action ID to:
- actual rig/group/pivot capability;
- animation method;
- timeline interval or game-state trigger;
- contact/collision requirement;
- fallback if source rig cannot perform it.

### E. Camera implementation
Translate each shot into:
- camera start/end transform or relative path;
- look-at target;
- FOV/focal length setting when justified;
- interpolation/easing;
- tracking subject;
- constraints and safe frame.

### F. Acceptance tests
- total duration;
- timeline coverage;
- shot timing;
- dialogue timing;
- character source fidelity;
- environment spatial consistency;
- camera framing;
- action readability;
- no unintended UI;
- runtime and visual tests.

---

# 5. SCENE AND SHOT GRANULARITY

Do not use a fixed number of scenes or shots per minute.

Create a new scene when there is a meaningful change in:
- location;
- time;
- dramatic/gameplay objective;
- participant group;
- world state;
- continuous action context.

Create a new shot when:
- camera setup changes;
- editorial cut occurs;
- framing/angle changes materially;
- POV changes;
- a distinct camera movement begins;
- gameplay camera mode changes.

Within one continuous gameplay camera recording, do not fabricate editorial cuts. Use shot/event segments only when there is an observable camera setup or meaningful change in framing/behavior.

Action-heavy material should be described more granularly than static dialogue. The required detail is determined by changes in observable action and camera behavior.

---

# 6. TIME AND DURATION INTEGRITY

## 6.1 Timecode standard

Use `HH:MM:SS.mmm` internally where the source permits. If only whole-second timestamps are available, state that precision limit.

For each scene and shot:
- start time is inclusive;
- end time is exclusive, except the final source endpoint;
- duration = end - start.

Use one consistent convention throughout the project.

## 6.2 Timeline checks

The source timeline must:
- begin at zero or the true first content frame;
- end at the source's actual content endpoint;
- account for all intervals;
- avoid unexplained gaps and overlaps;
- identify black frames, loading screens, menus, pauses or static intervals if they exist.

The sum of scene durations must equal the covered source duration under the chosen timecode convention.

The sum of shot durations within each scene must account for that scene's duration. If continuous footage has no cuts, one continuous shot segment may cover the interval.

Do not force scene boundaries to round minute marks.

## 6.3 Duration adaptation

Default: preserve the source duration exactly.

If a target duration is different:
- record the requested target separately;
- identify which content will be shortened/expanded;
- preserve key event order;
- obtain user approval for meaningful story compression or expansion.

---

# 7. CAMERA AND CINEMATOGRAPHY RULES

## 7.1 Camera vocabulary

Use correct distinctions:
- Pan: rotation around vertical axis.
- Tilt: rotation around horizontal axis.
- Dolly: camera physically moves forward/backward.
- Truck: camera moves laterally.
- Pedestal: camera moves vertically.
- Crane/jib: camera follows an elevated arc/path.
- Orbit: camera moves around a subject/target.
- Zoom: focal length changes; camera position may remain fixed.
- Tracking/follow: camera movement maintains a relationship to a moving subject.
- Handheld: irregular camera motion, not simply random shake.
- POV: a viewpoint tied to a character/player's visual perspective; specify first-person/subjective or other meaning.

## 7.2 Executable camera description

A camera instruction is incomplete if it only says "cinematic camera", "dynamic tracking" or "orbit".

Describe:
- reference subject;
- relative starting position;
- relative ending position;
- camera height;
- distance;
- target;
- movement path/direction;
- movement duration;
- speed/easing;
- lens/FOV if known or estimated;
- stabilization/shake;
- composition and safe frame.

Use qualitative values when exact numeric values cannot be recovered. Do not invent exact coordinates from a video unless they are measured or are explicitly adaptation values.

## 7.3 Continuity

Track:
- screen direction;
- camera axis;
- subject look direction;
- relative positions;
- entrance/exit direction;
- action state at cut.

180-degree continuity is a useful default for dialogue and spatially coherent action, not an absolute prohibition. Intentional axis crossing must be identified as an artistic choice.

---

# 8. CHARACTER MOTION RULES

Describe motion in observable phases:
- initial pose/state;
- anticipation (if visible);
- initiation;
- main action;
- contact/interaction;
- follow-through;
- recovery/result.

Use `NOT_OBSERVED` when a phase is not visible or cannot be determined.

For a running action, when visible, include:
- direction and path;
- body lean;
- arm/leg cycle;
- stride and cadence;
- foot-ground contact;
- acceleration/deceleration;
- head orientation;
- interaction with terrain;
- changes in speed or balance.

For a fall, when visible:
- cause/trigger;
- loss of balance;
- body rotation;
- contact point;
- impact/rebound;
- final resting pose;
- reaction or recovery.

Do not force every animation principle into every movement. The breakdown describes evidence; the adaptation layer decides how to implement it.

---

# 9. VISUAL FIDELITY AND ADAPTIVE RENDERING

Rendering requirements must follow the source's art direction and supplied assets.

Examples:
- pixel art: preserve pixel scale, palette, nearest-neighbor behavior and silhouette;
- voxel/Roblox/Minecraft-like: preserve block proportions, material simplicity and characteristic lighting;
- stylized 3D: preserve shape language, palette and controlled material response;
- realistic 3D: PBR materials, appropriate texture maps, physically plausible lighting and shadows may be useful;
- 2D animation: preserve line, shape, color and compositing language; do not force 3D realism.

Potential techniques—HDRI, MeshStandardMaterial, MeshPhysicalMaterial, normal maps, displacement, SSAO, Bloom, SSR, volumetric effects and Depth of Field—are options, not universal requirements.

Choose only when:
- the source style calls for it;
- the asset supports it;
- the browser/runtime supports it;
- performance is acceptable;
- visual inspection confirms improvement.

---

# 10. COVERAGE, QUALITY AND ACCEPTANCE GATES

A breakdown is not accepted merely because all requested headings are filled.

## Gate A — Source integrity
- Source identity and duration are supported.
- Source category is classified.
- Transcript/audio provenance is clear.
- Unknown values remain unknown.

## Gate B — Coverage integrity
- Coverage ledger spans the complete source.
- No unexplained gaps or overlaps.
- Inaccessible intervals are explicitly marked.
- Coverage percentage is calculated.

## Gate C — Narrative integrity
- All meaningful events are represented.
- Event order matches the source.
- Scene boundaries are justified.
- Ending state matches the source.

## Gate D — Cinematic integrity
- Significant shots are individually described.
- Camera movement is distinguishable and sufficiently specified.
- Screen direction and spatial relationships are tracked.
- Character motion is described at action level.

## Gate E — Audio integrity
- Dialogue is not invented.
- Speaker attribution is supported.
- Timecodes and overlaps are recorded.
- Subtitle policy is explicit.

## Gate F — Adaptation integrity
- Source reconstruction remains unchanged.
- Recommendations are separately labelled.
- Adaptation preserves required narrative events.
- Asset/runtime limitations are documented.

## Gate G — Execution readiness
- Canonical asset mapping exists.
- Missing capabilities/assets are identified.
- Scene, shot, action and dialogue IDs are stable.
- Three.js instructions are implementable.
- Duration and output constraints are explicit.

Use:
- `PASS`
- `FAIL`
- `BLOCKED`
- `NOT_RUN`

A coverage ledger can pass while visual understanding remains partial. Report both separately.

---

# 11. MODULAR OUTPUT PACKAGE

The default deliverable is a folder of Markdown files, not one oversized response.

```text
TSA_VIDEO_PROJECT/
├── README.md
├── PROTOCOL_VERSION.md
├── SOURCE/
│   ├── source_metadata.md
│   └── transcript_reference.md
├── BREAKDOWN/
│   ├── 01_SOURCE_AUDIT.md
│   ├── 02_COVERAGE_LEDGER.md
│   ├── 03_NARRATIVE_SCENE_BREAKDOWN.md
│   ├── 04_SHOT_BREAKDOWN.md
│   ├── 05_CHARACTER_MOTION.md
│   ├── 06_ENVIRONMENT_SPATIAL_BIBLE.md
│   ├── 07_LIGHTING_COLOR_BIBLE.md
│   ├── 08_DIALOGUE_SOUND.md
│   ├── 09_EDITING_CONTINUITY.md
│   └── 10_CINEMATIC_ADAPTATION.md
└── EXECUTION/
    ├── 11_HTML_EXECUTION_SPEC.md
    ├── ASSET_MAPPING.md
    └── ACCEPTANCE_CHECKLIST.md
```

For short videos, files may be combined when the content is small. Do not omit required information merely to preserve a fixed file count.

`README.md` must link to all modules and summarize status.

---

# 12. MASTER PROMPT FOR GEMINI / VIDEO-READING AGENTS

Use the companion file `MASTER_GEMINI_VIDEO_ANALYSIS_PROMPT.md`.

The agent must:
1. inspect the source video;
2. create source audit and coverage ledger;
3. analyze the full duration in chunks appropriate to event density;
4. create source reconstruction;
5. create a separate cinematic adaptation;
6. produce the modular Markdown package;
7. report inaccessible intervals and validation gaps.

Do not claim full video inspection if the platform only supplied a transcript or sampled frames.

---

# 13. AGENT HANDOFF TO HTML EXECUTION

The breakdown agent and coding agent may be different systems.

The handoff must contain:
- source video identity and duration;
- accepted scene/shot/action IDs;
- source reconstruction;
- approved adaptation choices;
- canonical character assets;
- environment/prop asset inventory;
- camera and lighting bible;
- dialogue/subtitle timing;
- scene continuity in/out states;
- exact target output constraints;
- unresolved questions and blocked items.

The coding agent must read:
1. this protocol;
2. `CANONICAL.md`;
3. TSA HTML Game/Video Production Protocol;
4. the modular breakdown files;
5. actual canonical asset source files.

The coding agent must not treat an adaptation proposal as an accepted requirement until it is approved or explicitly authorized by the user.

---

# 14. KNOWLEDGE MAINTENANCE

To prevent knowledge rot:
- keep this protocol versioned;
- keep project-specific facts in project files, not only in chat;
- record evidence and validation status;
- update the changelog when rules change;
- do not promote untested assumptions into protocol facts;
- preserve prior accepted breakdowns as immutable references;
- when a new source reveals a limitation, update the relevant rule and record the reason.

Recommended project files:
- `PROTOCOL.md`: reusable method.
- `TSA_STATE.md`: current task/baseline/blockers.
- `TSA_KNOWLEDGE.md`: proven project-specific facts.
- `SERIES_CONTINUITY.md`: continuity across connected videos.
- `CHANGELOG.md`: version history.

---

# 15. FINAL TSA LOCK

**The source reconstruction records what happened. The cinematic adaptation proposes how to reproduce or improve it. The execution specification tells the coding agent how to build it.**

Never collapse these three responsibilities into one vague prompt.

The final production chain is:

`SOURCE VIDEO`
→ `SOURCE AUDIT`
→ `COVERAGE LEDGER`
→ `SOURCE RECONSTRUCTION`
→ `CINEMATIC ADAPTATION`
→ `CANONICAL ASSET MAPPING`
→ `HTML/THREE.JS EXECUTION`
→ `RUNTIME + VISUAL VALIDATION`
→ `CONTINUITY HANDOFF`

The standard is not "a detailed-looking document".

The standard is: **complete source coverage, evidence-labelled observations, faithful event reconstruction, executable cinematic instructions, and explicit validation.**

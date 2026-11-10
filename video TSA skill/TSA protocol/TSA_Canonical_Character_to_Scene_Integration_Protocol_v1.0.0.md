# TSA Canonical Character-to-Scene Integration Protocol
## Portable Knowledge Standard for HTML Video, Film, and Games

**Document type:** TSA execution knowledge / reusable agent protocol  
**Version:** 1.0.0  
**Status:** Baseline protocol  
**Applies to:** Any AI agent, coding agent, model, or platform used to build HTML-based films, YouTube videos, animations, or games from user-supplied canonical character HTML.

---

## 1. Purpose

This document defines a repeatable, portable method for creating HTML video/film or HTML games using character implementations that the user has already built and approved.

The central problem this protocol prevents is **character reinvention**: an agent receives an existing character HTML file, looks at its appearance, then creates a new character that is merely similar. That is not acceptable when the supplied HTML is the approved baseline.

The intended workflow is:

1. The user supplies one or more character HTML files.
2. The agent inspects the actual source implementation.
3. The agent identifies what must remain unchanged and what can be adapted.
4. The agent builds a new scene or game around those characters according to the user's theme and prompt.
5. The agent validates source fidelity, behavior, runtime, and visual quality separately.

The character source defines the character. The user's prompt defines the new world, story, activity, and presentation.

> **Core rule:** Preserve the character from its supplied source. Adapt the world and execution to the user's requested theme. Do not silently replace the character with an approximation.

---

## 2. Foundational Principle

### 2.1 Canonical source of truth

A user-supplied character HTML file is the **canonical source of truth** for that character, unless the user explicitly says otherwise.

The agent must inspect and use the actual implementation, not rely only on:
- a screenshot,
- a visual description,
- a filename,
- a previous conversation summary,
- the agent's memory of the character,
- or a newly invented interpretation.

The source may contain important implementation details that are not obvious from a screenshot.

### 2.2 What character identity includes

Inspect and preserve, as applicable:

- Geometry and mesh construction.
- Body proportions and silhouette.
- Object hierarchy and group structure.
- Transform origins and pivots.
- Materials, textures, and material parameters.
- Color palette.
- Face, hair, costume, armor, accessories, and signature details.
- Scale and relative dimensions.
- Existing rig, skeleton, joints, or articulated groups.
- Existing animation logic and motion constraints.
- Character orientation and coordinate conventions.

Not every source has all these features. **Never claim a rig, pivot, texture, or animation capability exists unless it is present in the source or has been implemented and verified.**

### 2.3 Similarity is not source preservation

These are different outcomes:

| Approach | Meaning | Acceptable when source is canonical? |
|---|---|---|
| Rebuild from visual reference | Create a new model that looks similar | No, unless explicitly authorized |
| Recreate from memory | Guess geometry, colors, and proportions | No |
| Screenshot imitation | Copy the visible appearance only | No |
| Source-preserving integration | Reuse/adapt the actual character implementation | Yes |
| Isolated embedding | Run the original character HTML in an isolated frame/context | Sometimes; assess integration limits |

An agent must not say a character is “locked” merely because its prompt says so. Locking requires evidence.

---

## 3. TSA Operating Principles

All work must follow the TSA approach:

1. **Goal-first:** Establish the requested outcome before editing.
2. **Evidence-driven:** Inspect actual files and runtime behavior. Do not assume.
3. **Incremental and reversible:** Make scoped changes that can be reviewed or reverted.
4. **Preserve baseline:** Keep approved character implementation intact.
5. **Minimal scoped diff:** Change only what the requested scene/game requires.
6. **No unnecessary rebuild:** Do not refactor or replace working character code without a demonstrated need.
7. **Proportional validation:** Test the aspects affected by the change.
8. **Honest status:** Distinguish PASS, FAIL, BLOCKED, and NOT_RUN.
9. **Stop at objective:** Do not expand scope or add systems without a reason.

Preserve unrelated user changes and files. Do not reset, overwrite, or clean unrelated work.

---

## 4. Required Workflow

### Phase 0 — Intake and objective lock

Record:

- User's requested output: film, YouTube video, animation, or game.
- Theme and story/activity.
- Character HTML files supplied.
- Required duration and aspect ratio, if specified.
- Required camera behavior.
- Required actions, interactions, beats, or gameplay.
- Output format and delivery expectations.
- Explicit constraints (offline, libraries allowed/forbidden, no UI, etc.).

Ask only for missing information that materially blocks execution. Do not ask the user to repeat details already supplied.

### Phase 1 — Source audit

Inspect every supplied character HTML file.

At minimum, identify:

| Audit area | Questions |
|---|---|
| Runtime | Is it standalone HTML? Which libraries or module imports does it use? |
| Renderer | Canvas 2D, Three.js, CSS, WebGL, or another approach? |
| Geometry | How is the character constructed? |
| Hierarchy | Which groups/meshes make up the body? |
| Materials | Which materials, textures, colors, and parameters are used? |
| Dimensions | What is the character's scale and proportion? |
| Pivots | Are arms, legs, head, torso independently transformable? |
| Animation | Does an animation loop or rig already exist? |
| Camera | Is the camera part of the character presentation or only a studio preview? |
| Dependencies | Which external assets or libraries are required? |
| Constraints | What can be reused directly and what needs adaptation? |

Produce a concise source audit before major integration.

**Important:** If source files are large, use targeted inspection after establishing the relevant structure. Do not perform an unnecessary broad rewrite.

### Phase 2 — Reuse and adaptation plan

Divide implementation into three categories.

#### A. Preserve

Character-specific elements that must remain faithful:
- geometry,
- silhouette and proportions,
- materials and palette,
- costume and signature details,
- hierarchy where required for identity,
- existing rig/animation where applicable.

#### B. Adapt carefully

Elements that may need controlled changes for integration:
- root transform,
- scale in the new world,
- orientation,
- parent group,
- animation timing,
- pivot/hierarchy additions needed for a requested movement,
- render order or shadow settings.

Every meaningful adaptation must be documented. Do not imply the source is byte-identical if it has been ported or modified.

#### C. Replace around the character

Theme-dependent presentation systems may be replaced or newly created:
- environment/background,
- lighting,
- camera,
- staging,
- scene timeline,
- UI or subtitles,
- sound,
- physics/world interactions,
- weather and particles,
- game rules and level design.

Do not replace character-specific code merely because a new scene needs a different presentation.

### Phase 3 — Choose integration architecture

Select based on the source and requested result.

#### Option A: Direct source integration

Port or embed the actual character construction and required animation logic into a shared scene/runtime.

Best when:
- the character must share a camera and lighting system with the world,
- it must interact with other characters or objects,
- the film/game needs one coordinated render loop.

Requirements:
- preserve the source geometry and material definitions,
- preserve meaningful hierarchy and pivots,
- document any code adapted or omitted,
- avoid silently substituting geometry.

#### Option B: Isolated HTML embedding

Run the original character HTML in an iframe or isolated rendering context.

Potential advantages:
- strong separation from the source implementation,
- reduced risk of accidentally changing the original character code.

Potential limitations:
- shared 3D camera may not be possible,
- lighting and shadows may not integrate naturally,
- transparency/compositing may be constrained,
- synchronizing animation and timing may require an explicit interface,
- cross-context communication may be needed.

Use only if those limitations are acceptable for the requested scene.

#### Option C: Reusable character module extracted from source

If the source structure permits it, extract the character implementation into a module while preserving the original definitions and behavior.

This can improve reuse across scenes, but extraction itself must be scoped and tested. Do not turn a simple request into an unnecessary architecture refactor.

### Phase 4 — Theme-driven scene/game execution

The user's requested theme controls the new experience.

Theme determines:
- environment,
- story or gameplay,
- actions and reactions,
- character blocking,
- camera staging,
- lighting,
- atmosphere,
- pacing,
- effects,
- interactions,
- scene transitions.

Theme does **not** authorize changing the character's identity.

#### For HTML film/video

The timeline drives the film:
- scene time,
- beats,
- character actions,
- facial/body reactions,
- camera movement,
- environment animation,
- lighting changes,
- effects,
- dialogue/subtitles,
- transitions.

Use one authoritative master clock where practical. For deterministic rendering, provide a seekable time interface such as:

```js
window.TSA_VIDEO = {
  duration: 60,
  setTime(seconds) {
    // Set every animated property from absolute time.
    // Do not depend on the number of frames already rendered.
  }
};
```

The example is a contract pattern, not proof that an implementation already supports deterministic seeking.

Prefer absolute-time animation functions for offline rendering. Avoid uncontrolled randomness; use seeded randomness or precomputed event data when repeatable output is required.

A film scene must execute the actual actions, reactions, and visual beats in the brief. It must not collapse into a dialogue timer with static characters.

#### For HTML games

Input and game state drive gameplay:
- player controls,
- AI behavior,
- physics,
- collisions,
- objectives,
- progression,
- scoring,
- win/loss conditions.

Do not use a film timeline as the sole gameplay authority. A game may use timelines for cutscenes, but gameplay must respond to input and authoritative runtime state.

Maintain one clear owner for movement/state. Avoid competing stores, timers, or update loops.

### Phase 5 — Character motion

Before adding motion, inspect what the source actually supports.

If independent pivots exist:
- use them for articulated movement,
- preserve their original placement and proportions,
- coordinate limb movement with body movement.

If the source is a single rigid mesh or has no suitable pivots:
- state that limitation,
- consider a minimal reversible hierarchy/pivot addition,
- do not claim full skeletal animation,
- do not rebuild the model unless explicitly authorized.

Motion should match the requested activity and character:
- running: alternating leg/arm cycles, body bounce, forward lean, foot contact;
- walking: slower stride, weight transfer, restrained body motion;
- jumping: anticipation, takeoff, airborne pose, landing and recovery;
- interaction: reach, contact, response, release;
- reaction: head/body orientation, pause, recoil, gesture.

A visible moving model is not automatically a convincing animation. Validate contact, timing, direction, and continuity.

### Phase 6 — Camera and visual staging

The camera is part of the requested theme and must be designed intentionally.

Specify:
- shot size and composition,
- camera position relative to characters,
- focal length/FOV,
- target/look-at point,
- movement path,
- tracking behavior,
- lens consistency,
- subject framing,
- transitions.

Do not allow accidental zoom or framing changes when the user requests a consistent lens. Separate:
- camera movement,
- camera lens/FOV,
- character scale,
- camera target.

For a tracking shot, verify the distance and subject framing throughout the action, not only at the opening frame.

### Phase 7 — Build and validation

Validate separately.

| Gate | What it proves |
|---|---|
| Source audit | The supplied source was inspected |
| Structural integration | The intended source implementation is reused |
| File/build | The artifact was generated and parses/builds |
| Runtime | It actually executes in the target browser/runtime |
| Character fidelity | Geometry, palette, proportions, and details remain faithful |
| Motion | Required movement and interactions work |
| Camera | Framing, lens, and tracking behave as requested |
| Visual quality | Rendered result meets the agreed visual target |
| Production | Duration, frame count, export, and assembly work as required |

Use only these statuses:

- **PASS:** The specific criterion was actually tested and passed.
- **FAIL:** The specific criterion was tested and failed.
- **BLOCKED:** Testing could not be completed because of a stated blocker.
- **NOT_RUN:** It has not been tested.

A generated file is not proof of runtime success. A successful build is not proof of visual fidelity. A static screenshot is not proof of animation quality.

For visual comparison, where practical:
1. Render the source character and integrated character under comparable camera, scale, and lighting conditions.
2. Compare silhouette, proportions, materials, palette, and signature details.
3. Inspect multiple angles and animation poses.
4. Record differences and whether each is intentional.

### Phase 8 — Lock and preserve knowledge

After acceptance:
- record the source file identity/version or checksum where practical,
- record which source components were reused,
- record adaptations and known limitations,
- record validation evidence,
- identify the accepted output as a baseline,
- keep the source character file unchanged unless the user authorizes changes.

Do not rely only on conversational memory. Store durable project knowledge in versioned Markdown files in the relevant project/repository.

---

## 5. Required Agent Behavior

Every agent executing this protocol must follow these rules.

### MUST

- Read the supplied character HTML source before implementation.
- Treat it as canonical unless the user says otherwise.
- Use actual source implementation rather than reconstructing from appearance.
- Identify reusable code and theme-dependent code.
- Explain any source limitation that affects the requested result.
- Preserve character identity during integration.
- Implement the requested actions and scene beats, not just dialogue.
- Validate runtime and visuals where tools permit.
- Report what was actually tested.
- Deliver the requested artifact and exact verified file path.

### MUST NOT

- Rebuild a character from memory when source code is available.
- Replace source geometry with generic primitives.
- change costume/palette/proportions without authorization.
- Claim a character is locked without comparison evidence.
- Claim a rig or animation exists without source/runtime evidence.
- Hide source changes behind a claim of “reuse.”
- Substitute a static mockup for the requested animated scene.
- Claim browser/runtime/visual PASS when not tested.
- Refactor unrelated code or add dependencies without a clear need.
- Overwrite the canonical source file during scene integration.

### If blocked

Stop and report:
1. What source capability is missing.
2. Which requested behavior depends on it.
3. What minimal options exist.
4. What can be completed without violating the baseline.

Do not silently invent a replacement.

---

## 6. Reusable TSA Execution Prompt

Copy this prompt into any AI coding agent or platform. Attach the canonical character HTML files and provide the theme/prompt.

```text
You are executing the TSA Canonical Character-to-Scene Integration Protocol.

OBJECTIVE
Create the requested HTML film/video/game using the character HTML files I attach.

CANONICAL SOURCE RULE
The attached character HTML files are the canonical source of truth.
Inspect their actual source code before implementation.
Do not recreate, approximate, redesign, or replace the characters from screenshots,
memory, filenames, or visual descriptions.

FIRST: SOURCE AUDIT
For each character, inspect and report:
- geometry and construction,
- proportions and silhouette,
- object hierarchy and pivots,
- materials, colors, textures,
- costume and signature details,
- scale and orientation,
- existing rig and animation capabilities,
- dependencies and runtime requirements.

Then classify source components:
A. Preserve exactly or faithfully.
B. Adapt only when required, with changes documented.
C. Replace around the character because it belongs to the old presentation,
   such as the old studio camera, background, pedestal, or UI.

INTEGRATION
Reuse the actual character implementation.
Preserve geometry, proportions, material identity, palette, costume, and details.
Do not silently substitute a new model.
If direct integration is not possible, explain why before using another approach.
Do not claim byte-identical reuse if code has been ported or adapted.

USER THEME / CREATIVE BRIEF
[INSERT THE USER'S THEME, STORY, ACTION, GAMEPLAY, DURATION, CAMERA,
ENVIRONMENT, ASPECT RATIO, AND OTHER REQUIREMENTS HERE.]

EXECUTION
Build the new environment and experience around the canonical characters.
Implement all requested actions, reactions, movement, camera staging,
lighting, atmosphere, effects, and transitions.
Do not reduce a film scene to dialogue timers or static character poses.
For a game, make gameplay input/state-driven.
For a film, make the master timeline drive the complete scene.

TSA CONSTRAINTS
- Goal-first and evidence-driven.
- Preserve the supplied baseline.
- Minimal scoped and reversible changes.
- No unrelated refactor or unnecessary dependencies.
- Inspect before editing.
- Do not claim untested behavior as PASS.
- Preserve unrelated user changes.
- Stop when the objective is met.

VALIDATION
Report separately:
1. Source audit.
2. Structural source reuse.
3. Build/file validity.
4. Browser/runtime execution.
5. Character visual fidelity.
6. Animation/action quality.
7. Camera/framing.
8. Production/export behavior, if requested.

Use PASS / FAIL / BLOCKED / NOT_RUN accurately.
A file being generated does not prove runtime or visual success.

DELIVERABLE
Create the requested standalone HTML or project artifact.
Provide the exact verified output path.
Include a concise implementation report, source adaptations, limitations,
and validation status.
```

---

## 7. Scene-Level Execution Record

For each generated scene, maintain a small record:

```yaml
project:
  title: ""
  scene_id: ""
  output_file: ""

sources:
  characters:
    - source_file: ""
      canonical: true
      source_version_or_hash: ""
      reused_components: []
      adapted_components: []
      known_limitations: []

execution:
  output_type: "film | game"
  renderer: "Canvas2D | Three.js | other"
  duration_seconds: null
  aspect_ratio: ""
  master_timeline_or_game_state: ""

validation:
  source_audit: "NOT_RUN"
  structural_integration: "NOT_RUN"
  build: "NOT_RUN"
  runtime: "NOT_RUN"
  character_fidelity: "NOT_RUN"
  motion: "NOT_RUN"
  camera: "NOT_RUN"
  visual_quality: "NOT_RUN"
  production_export: "NOT_RUN"

notes:
  - ""
```

---

## 8. Knowledge Maintenance — Preventing Knowledge Rot

This protocol must be maintained as an operational standard, not left as an isolated chat response.

Recommended project files:

```text
TSA/
└── knowledge/
    └── html-character-scene-integration/
        ├── README.md
        ├── TSA_CHARACTER_SCENE_PROTOCOL.md
        ├── EXECUTION_PROMPT.md
        ├── VALIDATION_CHECKLIST.md
        └── CHANGELOG.md
```

For an individual repository, keep a project-specific state file as well:

- `TSA_STATE.md`: current baseline, active task, known blockers, latest validation.
- `TSA_KNOWLEDGE.md`: proven reusable knowledge and architectural decisions.
- `CHANGELOG.md`: dated changes to this protocol or implementation.

### Update rules

Update the knowledge when:
- a new source integration pattern is proven,
- a character hierarchy or animation limitation is discovered,
- a camera or rendering method is validated,
- a runtime/export workflow is proven,
- a previous assumption is disproved,
- a regression or failure reveals a new constraint.

Do not promote a hypothesis or untested implementation into proven knowledge.

Each knowledge update should state:
- date/version,
- evidence or test performed,
- what changed,
- status,
- affected baseline,
- known limitations.

At the start of a new agent session:
1. Read this protocol.
2. Read the project `TSA_STATE.md` and `TSA_KNOWLEDGE.md`, if present.
3. Inspect the actual source files for the current task.
4. Confirm the current baseline before editing.

At the end:
1. Record implementation and validation evidence.
2. Update state/knowledge if new durable facts were learned.
3. Preserve the source baseline.
4. Report remaining NOT_RUN/BLOCKED items.

---

## 9. Important Distinctions and Limitations

This protocol guarantees a disciplined method, not automatic visual perfection.

- Porting source code into a new scene can preserve its implementation logic, but may not be byte-for-byte identical.
- Different lighting, camera, renderer settings, and scale can make the same geometry look different.
- A model built from separate box meshes may have transformable groups but not a true skeletal rig.
- A model that looks correct in a static render may fail during movement.
- A character's original studio HTML may include controls or a render loop that must be separated from the new scene.
- External libraries/CDNs may prevent offline execution unless bundled or replaced.
- Deterministic video rendering requires explicit time control and repeatable effects; `requestAnimationFrame` alone does not guarantee deterministic export.
- Browser testing, visual inspection, and production rendering remain separate acceptance gates.

When a requested result exceeds the source's capabilities, explain the gap and propose the smallest controlled adaptation.

---

## 10. Final Lock

The TSA method is:

**Canonical character source + user-directed theme + source-preserving integration + validated execution.**

The character is not a suggestion to the AI. It is an existing asset and implementation baseline.

The theme is not a reason to redesign the character. It is the instruction for building the world, action, story, camera, and experience around that character.

The agent's responsibility is to integrate and execute faithfully, disclose limitations, and prove the result through validation.

**Do not guess what already exists in the source. Inspect it, reuse it, adapt only what is necessary, and validate the result.**

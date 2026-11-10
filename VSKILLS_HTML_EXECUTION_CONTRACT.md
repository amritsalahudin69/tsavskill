# TSA VSkills HTML/Three.js Execution Contract

**Status:** PROPOSED IMPLEMENTATION — Phase 2C-1 contract design only
**Scope:** Standalone Animation + `cap.scene-production` + optional `style.miniature-diorama`
**Not implemented:** No parser, generator, renderer, browser adapter, or scene artifact is created by this document.

## 1. Purpose and boundaries

This contract describes how a future scene-production capability may create and validate a user-requested HTML/Three.js animation. It does not turn a visual-style skill into an execution engine.

- `vskills` discovers skills, resolves intent, selects a production mode and operation, preserves constraints, and reports unsupported work.
- `vidmindi` (`style.miniature-diorama`) provides presentation guidance only.
- `cap.scene-production` owns scene construction, runtime, animation, packaging, and execution evidence.
- The production mode owns the output contract. This document covers Standalone Animation only. Modular Film retains its separate module, lifecycle, manifest, and assembly contract; Character Asset remains a distinct mode.
- Use Three.js only when the user's scene requires genuine 3D. A style does not select a renderer by itself.

The source prompt in `sub skill.txt`, section 10, is a **VERIFIED SOURCE FACT**: it demonstrates a tabletop model town, miniature-compatible appearance, tilt-shift blur, warm lighting, and camera movement. Its people, dog, town, cup, actions, vertical format, duration, and loop are example-specific, not reusable defaults. The user's scene and the current `vidmindi/SKILL.md` remain authoritative for scope and scene freedom.

Status labels in this contract:

- **VERIFIED SOURCE FACT** — directly present in a located source or installed instruction.
- **APPROVED DESIGN** — a constraint approved by the VSkills contracts or task.
- **PROPOSED IMPLEMENTATION** — a future behavior specified here, not tested or implemented.
- **UNVERIFIED** — dependent on a host, browser, runtime, or decision not yet tested.

## 2. Responsibilities

| Owner | Owns | Does not own |
|---|---|---|
| Parent `vskills` | Discover installed capabilities; identify mode, operation, and at most one primary style; preserve user intent and source authority; report unsupported execution. | Rendering, inventing scene content, or claiming that a child selection produced an artifact. |
| Visual-style skill (`vidmindi`) | Describe style appearance, compatible surface treatment, scale cues, lighting, camera treatment, and style-specific visual criteria. | Scene content, production mode, Three.js implementation, asset generation, or runtime validation. |
| `cap.scene-production` | Build actual objects and environment; own Three.js initialization, assets, geometry, materials, lights, camera, animation, packaging, and runtime validation. | Replacing the user's scene, silently changing canonical characters, or overriding explicit format/runtime constraints. |
| Shared TSA protocols | Source preservation, evidence discipline, applicable production constraints, validation and handoff rules. | Claims that an untested runtime, visual result, or export works. |

Style, mode, and operation remain separate fields throughout planning, implementation, and reporting.

## 3. Scene input contract

The following is a **PROPOSED IMPLEMENTATION** data shape for planning. It is not a machine-validated schema; no parser or validator is implemented in Phase 2C-1.

```yaml
scene:
  description: required
  intended_subject_or_event: required
  environment: optional
  characters_and_objects: optional
  actions_and_interactions: optional
  camera_direction: optional
  duration: optional
  aspect_ratio: optional
  resolution: optional
  looping: optional
  lighting_preference: optional
  existing_html_sources: optional
  other_constraints: optional
```

### Field meanings and validation

| Field | Requirement and meaning |
|---|---|
| `description` | Required concise statement of the requested scene and its important constraints. Preserve the supplied meaning; do not replace it with a style example. |
| `intended_subject_or_event` | Required focus of the animation. It may be an object, place, process, or event; character assets are not required. |
| `environment` | Optional setting, spatial context, and background. Infer only neutral details that do not materially change the scene. |
| `characters_and_objects` | Optional user-specified entities, references, or source assets. Do not invent a character when none is requested. |
| `actions_and_interactions` | Optional action sequence, contact, timing, and relationships. Record any inferred action beats that affect meaning. |
| `camera_direction` | Optional framing, viewpoint, lens/perspective, movement, target, or motion constraints. Do not assume orbit, push-in, or tracking. |
| `duration` | Optional target duration. No fixed 8-second default. If a finite duration is needed but omitted, choose a scene-appropriate value only when immaterial and disclose the assumption; otherwise clarify. |
| `aspect_ratio` | Optional framing ratio. Do not force 9:16. A responsive preview may follow the viewport when no fixed output ratio is requested. |
| `resolution` | Optional export dimensions or quality target. Do not equate browser viewport size with export resolution. Ask if a fixed export is required but materially underspecified. |
| `looping` | Optional repeat behavior. Do not force a loop. A finite authored action may play once by default if that does not contradict intent; disclose the default. |
| `lighting_preference` | Optional mood, time, direction, softness, or intensity preference. Preserve explicit preferences even when they are not miniature-styled. |
| `existing_html_sources` | Optional canonical character or scene HTML. Inspect actual source and runtime before reuse; preserve source files. |
| `other_constraints` | Optional requirements including no text/HUD, libraries, offline/network, browser, accessibility, input, or delivery constraints. |

**Precedence:** explicit user requirements and declared source authority take priority; canonical source facts constrain compatible implementation; the requested scene determines content; the selected style affects presentation only; implementation defaults apply last. If requirements conflict, identify the conflict and request the smallest decision needed. Record material assumptions. Do not infer missing inputs from the original source prompt.

## 4. Miniature Diorama style application

### Required style characteristics — APPROVED DESIGN

For a request selecting Miniature Diorama, the rendered work must communicate a coherent miniature/model presentation rather than merely scaling all objects down:

- Readable, coherent object proportions and spatial relationships at a plausible miniature scale.
- A physically understandable scene with model-like construction or finish where compatible with the user's subject.
- Environment and prop scale that agrees with the primary subject; do not distort identity or function to imply scale.
- Materials and surface detail that support a crafted miniature appearance while retaining scene-specific color, material, and mood requirements.
- Intentional lighting and strong, readable composition that reveal the modeled forms.
- Camera framing and movement that support the requested subject and action.
- Preserve the user's characters, objects, environment, event, and camera constraints.

### Optional effects — PROPOSED IMPLEMENTATION

Tilt-shift-inspired depth of field, selective focus, tabletop backgrounds, explicit scale-reference objects, miniature construction seams, post-processing, and exaggerated proportions may be used only when they help the requested scene and remain compatible with its constraints. Keep focus effects subtle enough not to hide important action or source details. Avoid advanced post-processing unless its benefit justifies the dependency and it can be validated.

### Forbidden assumptions — APPROVED DESIGN

Do not require a town, teacup, person, dog, landing sequence, cotton clouds, fixed palette, fixed action, HUD, on-screen text, orbiting camera, duration, aspect ratio, or loop. Do not add a scale prop solely because it appeared in an example. Do not shrink every model uniformly or apply toy proportions that alter user-defined identity.

### Style acceptance

Visual inspection must be able to identify a deliberate model-scale treatment from the scene's form, materials, composition, and lighting together. A single blur effect or tiny object scale is insufficient. Report the specific visible cues and any requested style element that could not be applied.

## 5. Proposed HTML/Three.js runtime

All items in this section are **PROPOSED IMPLEMENTATION** and require Phase 2C-2 validation.

### HTML entry point and initialization

The primary standalone artifact is a runnable HTML entry point, normally `index.html`. It owns or imports the minimum code needed to:

1. Load declared dependencies and required assets.
2. Create the scene, renderer, camera, lights, scene graph, and animation controller.
3. Report initialization or asset failures visibly and with actionable detail.
4. Start the requested preview only after required resources are ready.
5. Handle viewport resize without changing the requested world scale or subject identity.
6. Release event listeners, animation loops, and disposable GPU/asset resources when stopped or replaced.

Prefer a small native-ES-module structure over an unnecessary framework. Keep one animation/render loop per scene. Separate reusable setup from scene-specific content only when doing so improves clarity or required reuse. No full Master HTML Engine is required for a standalone animation.

### Three.js loading and dependencies

- Declare each direct dependency, its exact version/revision, source (CDN or local package), purpose, and network/offline requirements in the delivery report.
- Resolve and test a compatible Three.js version during implementation; **no version is selected or pinned by this design**. Keep core and add-on imports on the same tested revision.
- Do not add a framework or post-processing library without a material requirement.
- A CDN dependency requires network access. Do not describe that artifact as offline.
- ES modules and relative assets may be blocked or behave differently under `file://`. Provide and verify a local HTTP serving method for the delivered structure; do not promise direct file-open compatibility.
- If an offline requirement cannot be met with an approved, tested dependency source, report `BLOCKED` and ask for an acceptable source. Do not silently download, vendor, or change dependency policy.

### Renderer and asset lifecycle

Initialize a WebGL renderer with an explicit canvas, size, pixel ratio/performance policy, color/output settings, and shadow policy selected for the target. Check for renderer/context initialization errors. Resize the drawing buffer and camera projection together. Explain WebGL/context loss or unsupported-browser behavior.

Track asset loads. Required assets must finish loading before the animation is declared ready; a missing required file is an error, not a silent fallback. Optional asset failures may be skipped only if the result remains faithful and the omission is reported. Use exact, case-correct relative paths. Dispose resources and listeners owned by the scene.

## 6. Geometry, materials, camera, and lighting

### Geometry and scene graph

- Build true volumetric 3D forms where the requested scene requires 3D; flat cards do not satisfy a volume requirement unless the user requested a 2D/billboard treatment.
- Establish and document a consistent world scale sufficient to keep object proportions and interactions understandable. Do not claim physical real-world dimensions unless they are defined.
- Use silhouettes and detail appropriate to the view distance; important forms must remain readable in the delivered camera.
- Use groups and local pivots for independently animated parts. Keep transforms in the intended hierarchy; root-group motion alone is not adequate when the requested action requires parts, contact, or interaction.
- Keep interaction/contact geometry aligned with the visible forms where collision or touching is represented.

### Materials

Use scene-appropriate Three.js materials and color management, with deliberate color, roughness, metalness/reflectivity, opacity, and texture choices. Miniature treatment may suggest painted, molded, paper, wood, fabric, clay, or other crafted surfaces when compatible; there is no mandatory palette or material. Avoid defaulting every object to glossy plastic. Declare external textures and their licensing/provenance when applicable.

### Camera

Choose perspective or orthographic projection according to user intent and the scene. Frame the main subject with measured world bounds and actual viewport aspect; keep requested negative space, camera direction, and motion. Verify clipping, occlusion, target stability, and all important action beats. Camera movement should be time-based and constrained; do not use movement or depth of field that makes the scene unreadable. A tilt-shift look is optional, not a camera or lens mandate.

### Lighting

Use ambient/environment and directional/key illumination as needed to make volume, material, and action legible. Keep shadow direction coherent with lights. Shadow maps, fill/rim lights, fog, and ambient-occlusion/post effects are optional and performance-dependent. Do not add effects that obscure the subject or override requested mood.

## 7. Camera and animation contract

The animation controller must define an authoritative finite duration when the output is a finite authored animation. If exact repeatability, seeking, or frame validation is needed, expose equivalent semantics to:

```js
animation = {
  durationSeconds,
  setTime(seconds),
  reset(),
  play(),
  pause(),
  dispose()
};
```

These are semantic operations, not a requirement to publish a global object or adopt a particular API name.

- Derive animated transforms, camera, lighting changes, and effects from one scene-local timebase. For seekable output, derive state from absolute time rather than frame count.
- Use `requestAnimationFrame` for interactive preview, with elapsed-time handling that does not change action timing at different refresh rates.
- Keep the requested action, interaction, contact, direction, and order. Coordinate object and camera motion on the same timeline.
- Give independently moving parts appropriate pivots/hierarchy; animate meaningful parts and interaction, not only the root group.
- Reset/seek must restore deterministic initial state when those operations are exposed.
- Play once by default only when compatible with the request. Loop only when explicitly requested; if the request implies continuous cycling but is ambiguous, clarify. Test continuity at the wrap boundary when looping is requested.
- Honor user-specified duration. Do not impose 8 seconds, a frame rate, or loop behavior. If a duration or exact frame rate is required for export but absent, clarify rather than fabricate an export contract.
- Camera tracking must follow the requested framing, avoid abrupt unintended jumps, and not simulate object movement by changing scale.

## 8. Canonical character integration

When canonical HTML is supplied, `cap.canonical-character-integration` owns its source audit and reuse. Before implementation, inspect and record:

- HTML entry/runtime, library versions/import method, renderer, dependencies, and asset paths.
- Geometry construction, dimensions/proportions, materials/textures/colors, face/signature features, hierarchy, and pivots.
- Existing animation/rig capabilities and camera assumptions.
- What can be reused directly and any compatibility conflicts.

Preserve the character's identity, geometry, proportions, palette/material identity, distinctive details, and meaningful hierarchy/pivots. Reuse compatible implementation. If new pivots or transforms are necessary, add the smallest documented wrapper/adaptation; do not imply the original source already had those features. Do not overwrite or silently rewrite canonical files.

Select direct integration, isolated embedding, or a source-derived module only after inspecting the source and checking camera, lighting, timing, and interaction needs. Isolated HTML may prevent a shared camera/light/timeline; document and validate that limitation. If the required result cannot preserve source authority or compatible runtime, stop with `BLOCKED` and request a decision. A style must not justify generic replacement geometry.

When only a target PNG/JPG is provided for a new character, the image is appearance authority; canonical HTML is not required. Character construction is separate from placing a character in a scene.

## 9. Output artifact contract

For a future Standalone Animation proof:

- **Primary artifact:** runnable HTML/Three.js animation at the reported path.
- **Supporting artifacts:** only assets, source modules, dependency/license notices, or run/validation notes needed to reproduce and verify it.
- Include runtime instructions, dependency sources/versions, network/offline requirements, input interpretation, selected mode/capability/style, assumptions, validation statuses/evidence, and limitations.
- Preserve supplied canonical files and report any adapted implementation separately.
- A screenshot, source listing, or generated HTML file alone is not proof of execution or visual quality.
- Do not require a master engine, film manifest, or multiple scene modules for a standalone request.
- Modular Film requests use the distinct scene module and assembly contract in `TSA_HTML_SCENE_MODULARIZATION_AND_ASSEMBLY_PROTOCOL_v1.0.0.md`.

## 10. Failure handling and user flow

Report the smallest affected requirement and use `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED` accurately. Stop or ask when the scene's intent/source authority is materially ambiguous, a required asset is absent, dependencies conflict with user constraints, the target browser lacks required WebGL support, a canonical runtime cannot be preserved, or the requested output cannot be verified. Never substitute an example scene, style, renderer, character, asset, or output format silently.

Proposed flow:

1. User request and explicit constraints.
2. Parent or explicit child selection; resolve mode, operation, and zero/one style.
3. Capture/validate required scene inputs; preserve source authority.
4. Apply selected style guidance without changing content.
5. `cap.scene-production` implements HTML/Three.js only if the real capability and runtime are available.
6. Run applicable source, build, browser, visual, animation, and delivery gates.
7. Deliver the artifact and evidence, including unrun/blocked checks.

Proposed invocation:

> Use the vskills parent and the vidmindi child to create a standalone Miniature Diorama animation from the following scene specification: [user-defined scene and constraints].

The parent/child discovery and guidance are available as instructions. `/vidmindi` is not established as a native executable command. HTML/Three.js scene generation and runtime validation remain **NOT_IMPLEMENTED** until separately implemented and tested.

## 11. Phase 2C-2 minimal acceptance test design

This is a proposed test fixture only, not a default scene or generated artifact.

**Scene:** A hand-crafted miniature lunar research outpost on a small cratered moon base. A cylindrical habitat with an airlock, a three-panel solar array, a dish antenna, a low crater ridge, a six-wheeled rover, and a small visible Earth in the sky are present. Over **6 seconds**, the rover completes one visible turn while the antenna tracks Earth. Use a slow three-quarter camera arc that keeps the rover and habitat in frame. Landscape **4:3**, no characters, no text/HUD, play once, do not loop. The procedural objects and local scene need no external visual assets.

The scene is intentionally distinct from the original Miniature Diorama source example and exists only to test arbitrary user-scene preservation. Style treatment may use coherent model construction, crafted surfaces, intentional light/shadow, and restrained focus; it must not add the source example's town, people, dog, cup, or landing action.

**Acceptance criteria:**

1. Parent selection resolves `vidmindi`, `style.miniature-diorama`, `mode.standalone-animation`, and `cap.scene-production`; child instructions actually load.
2. The generated `index.html` preserves all specified scene entities, camera, 6-second, 4:3, no-text, and non-loop constraints.
3. Scene source contains volumetric habitat, rover, antenna, array, terrain, and coherent spatial scale (not just flat sprites).
4. A real supported browser loads the local HTTP-served artifact; WebGL renderer initializes and all required objects are visible.
5. In browser playback, the rover visibly turns and the dish tracks as requested; camera arc frames the intended subjects for the full duration.
6. Visual inspection identifies a miniature/model treatment from multiple cues, with no severe clipping, unintended floating, or unreadable selective focus.
7. Console/runtime and asset checks have no critical failures; each result has a named browser/version and evidence.
8. The required artifact and working run instructions are delivered. The canonical source directory is unchanged.

Phase 2C-1 does not create, run, screenshot, or validate this scene.

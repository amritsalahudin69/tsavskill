---
name: scene-production
description: >
  A reusable TSA capability for implementing user-defined browser animations with Three.js or Canvas 2D, including runtime initialization, animation, packaging, and validation.
---

# Scene Production

## Purpose and boundaries

Implement a user-defined browser scene as a runnable HTML artifact with a renderer suited to the requested content: Three.js for genuine volumetric 3D, or native Canvas 2D for appropriate two-dimensional rendering. This skill owns scene construction and execution guidance; it does not choose or replace the user's scene, create a visual style, or provide an automatic scene generator.

User requirements and canonical sources take priority in renderer selection. Honor an explicitly requested renderer when it can meet the scene requirements; if it cannot, explain the conflict and resolve it rather than silently switching. Do not force Three.js into Pixel Art or another naturally 2D scene. Do not replace required true 3D geometry or characters with flat Canvas approximations.

The capability works without a style. It can receive presentation instructions from a separately selected style skill, such as `vidmindi` (`style.miniature-diorama`) or `vidpixel` (`style.pixel-art`); apply them only to compatible presentation choices. A visual style never selects or overrides an explicitly requested renderer. Keep scene content, production capability, renderer, and visual style distinct.

## TSA Skill Metadata

- `skill_id`: `cap.scene-production`
- `name`: Scene Production
- `description`: Implement user-defined browser animation scenes with Three.js or Canvas 2D and validate the delivered artifact.
- `version`: `1.0.0`
- `parent`: `vskills.parent`
- `category`: `operation_capability`
- `status`: `IMPLEMENTED` as portable instructions; no automatic generator or router.
- `invocation`: Select manually by skill name or capability ID. No native slash alias is established.
- `dependencies`: A browser and local HTTP serving for runtime checks; Three.js for genuine 3D; native Canvas 2D for appropriate 2D scenes; optional, separately selected style instructions.

## Accepted inputs

Required: a scene description and intended subject or event. Accept optional environment, characters/objects and source files, actions/interactions, camera/framing, duration, aspect ratio, loop behavior, lighting, runtime/dependency constraints, style guidance, and output location. Preserve explicit values. Ask a focused question when missing information materially affects the result; otherwise record minimal assumptions.

When canonical HTML or assets are supplied, inspect their paths, renderer, geometry, hierarchy, materials, animation, and dependencies before reuse. Preserve source files and identity.

## Scene intake procedure

1. Restate the requested scene and action without adding story content.
2. Separate explicit requirements, optional preferences, and assumptions.
3. Inventory sources and verify exact paths; record unavailable or unclear provenance.
4. Record scene entities, spatial relationships, camera, output format, runtime constraints, and validation expectations.
5. Identify the selected production mode and operation. Record a style only when separately requested or selected.
6. Resolve contradictions before implementation; do not silently substitute content, a style, source, or dependency.

## Execution sequence

1. Select the renderer from explicit user requirements, canonical source constraints, and scene dimensionality. Do not infer the renderer from a style name alone.
2. Read `references/html-threejs-workflow.md` for Three.js work or `references/html-canvas2d-workflow.md` for Canvas 2D work.
3. Map each scene requirement to a scene-graph element or Canvas draw layer, action, camera/view behavior, or delivery check.
4. Plan the required spatial or logical coordinate system and keep all requested subjects and actions represented.
5. Initialize the selected renderer, handle sizing and initialization errors, and establish one animation lifecycle.
6. Implement requested actions from a scene-local elapsed-time timeline.
7. Check source, JavaScript syntax, applicable dependencies, renderer-specific structure, and local HTTP serving.
8. Run browser, visual, and motion checks when observable. Report unavailable checks without promoting static evidence to runtime evidence.
9. Deliver only the requested HTML and necessary support files, along with exact run instructions and validation outcomes.

## Projection and spatial consistency gate

Before constructing scene geometry, choose a coherent camera/view convention and coordinate system. Ensure environment, subjects, and object geometry agree with that projection; align moving-object heading to the path tangent and make the path correspond to visible traversable space. Check contact, clearance, clipping, and occlusion, including layer/depth ordering. Validate representative start, turn, and stop states. Mix projections only when explicitly justified by the source or design, and keep the result legible.

## Three.js construction guidance

Use a structured scene graph with named groups for independently placed or animated objects. Prefer procedural primitives or generated geometry when they meet the scene; do not substitute flat artwork for required 3D. Keep geometry, materials, lighting, camera, and behavior scene-specific. Frame all required objects using actual viewport dimensions; avoid clipping and unintended occlusion.

For moving assemblies, separate the vehicle/body from wheels, doors, limbs, or other requested moving parts. Derive position, heading, part rotation, and camera state from the same authoritative timeline. Do not copy fixture-specific models or coordinates into another scene.

## Canvas 2D construction guidance

Use Canvas 2D for native two-dimensional scenes when it satisfies the request. Organize drawing into clear scene layers and reusable draw routines; maintain an explicit coordinate/resolution policy; size the backing store and display area deliberately; and redraw from elapsed-time state. Use pixel-grid snapping and nearest-neighbor enlargement only when requested or compatible with the selected style, not as generic Canvas requirements.

Read `references/html-canvas2d-workflow.md` for initialization, coordinate scaling, animation, resizing, and validation boundaries. Canvas 2D is not a substitute for required volumetric geometry or a canonical 3D character implementation.

## Time-based animation rules

Use `requestAnimationFrame` for preview and elapsed time (for example, `performance.now()`), never frame-count increments. For finite animations, derive state from a normalized timeline and honor the requested duration and loop behavior. Use absolute-time state for repeatable seek/reset when those controls are needed. Coordinate object and view motion; model requested articulation and contact, not just root translation.

Do not impose a universal duration, aspect ratio, loop, camera orbit, HUD, or export frame rate. A fixture may declare test-only assumptions, which must not become skill defaults.

## Dependencies

Keep dependencies minimal, declare exact versions and sources, and use the same tested Three.js revision for all related imports. The Phase 2C-2 fixture used `three@0.187.0` from jsDelivr; prefer that tested version for compatible work unless there is a concrete compatibility reason to change it, and disclose any change. A CDN requires network access. Do not claim offline or direct `file://` support unless verified. Do not add a framework, package-wide manifest, asset pipeline, or post-processing dependency without a demonstrated requirement.

## Output and runtime instructions

Deliver a standalone `index.html` unless the request requires supporting files. State the exact artifact paths, selected capability and optional style, scene interpretation, assumptions, dependency source/version, network requirements, and validation statuses.

From the output directory, a common local run command is:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/` in a browser. This command serves files; it is not a scene generator. Do not claim that direct `file://` loading works without testing it.

## Six TSA validation gates

Report each applicable gate independently as `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED`.

1. **Source:** scene, constraints, source authority, and assumptions are recorded.
2. **Build:** HTML/JavaScript syntax, dependency versions, local assets, and run command are checked.
3. **Runtime:** the actual browser initializes the selected rendering context (WebGL or Canvas 2D); record browser/version, observed errors, and visible output.
4. **Visual:** inspect actual browser output for scene readability, composition, required 3D volume where applicable, and separately selected style cues.
5. **Motion:** observe playback at distinct times; verify requested object/part motion, contact, duration, camera, and loop/endpoint behavior.
6. **Delivery:** verify exact output paths, dependencies, and run instructions.

A source inspection or HTTP 200 does not pass browser, visual, or motion gates. User-observed manual results are valid when attributed to the user. Never label unobserved checks PASS.

## Error handling

Report the specific requirement and evidence. Show import, renderer, asset, or runtime errors visibly and in the console; do not silently skip required assets or create success-shaped fallbacks. Stop with `BLOCKED` when required source, runtime, browser support, or user decisions are missing. Preserve unrelated work and canonical inputs.

## Manual invocation and limitations

Manual use: “Use the `scene-production` capability to implement this scene as an HTML animation with [Three.js / Canvas 2D as appropriate or explicitly requested]; separately apply [style skill] if requested.”

Host discovery, native slash-command registration, and automatic parent routing are host-specific and unverified until tested. This skill contains instructions, not executable scene-generation software. A working fixture demonstrates one workflow instance, not arbitrary-scene reliability, video export, or a universal generator. Modular Film assembly and recording/export are outside this capability's scope.

## Reference loading

Read `references/html-threejs-workflow.md` for Three.js reuse, scene-graph/runtime patterns, and 3D validation. Read `references/html-canvas2d-workflow.md` for Canvas 2D setup and validation. Load the reference that matches the selected renderer; no reference is required for basic skill discovery.

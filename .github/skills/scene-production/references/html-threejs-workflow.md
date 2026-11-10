# HTML/Three.js Scene Production Workflow

This reference supports `.github/skills/scene-production/SKILL.md`. It is implementation guidance, not an executable generator or a guarantee of browser compatibility.

## Reuse audit from the Lunar Outpost fixture

The Phase 2C-2 fixture at `tests/fixtures/vidmindi-lunar-outpost/index.html` is a source and user-observed manual proof. Reuse patterns and scene content are separated below.

| Classification | Evidence and boundary |
|---|---|
| **REUSABLE** | An HTML frame with an explicit canvas; Three.js scene/camera/renderer setup; size and camera-aspect updates; asynchronous import/error reporting; one render loop; and a single elapsed-time animation controller are implementation patterns present in the fixture. The user manually observed that the fixture rendered and that its rover/wheels moved. This does not prove broad browser/device reliability. |
| **STYLE-SPECIFIC** | A physical display base, crafted/model-like material treatment, coherent miniature proportions, clear three-quarter composition, and intentional soft key/fill lighting are suitable Miniature Diorama presentation techniques when compatible with the user's scene. They are not mandatory for all styles. Tilt-shift or depth of field is optional and should not impair readability. |
| **FIXTURE-SPECIFIC** | Lunar radial relief, crater, habitat, solar array, Earth, antenna/dish, rover, wheel layout, rover route, and their relationships or animation belong only to the Lunar Outpost story. Do not copy them into the capability or unrelated scenes. |
| **UNVERIFIED** | General resilience of cleanup/disposal, resize behavior across browsers, WebGL context loss recovery, exact cross-refresh animation determinism, performance on low-end devices, and reliability across arbitrary scene classes were not established by the one fixture. |

Use the audit as a reuse boundary, not a component library. Transfer an implementation pattern only when it fits the new scene and then validate it in that scene.

## Scene-to-scene workflow

1. **Intake:** preserve the user's nouns, actions, spatial relationships, camera, duration, aspect ratio, runtime, and delivery requirements. Record test assumptions separately from skill defaults.
2. **Source audit:** check exact file paths and inspect required canonical HTML/assets before adapting. Do not overwrite them.
3. **Composition:** select `cap.scene-production` for implementation. If one style is requested, load its separate instructions and apply presentation only. The style does not select objects or actions.
4. **Spatial plan:** define a consistent local world scale; place support surfaces, paths, moving objects, and landmarks; determine bounds before final camera framing.
5. **Scene graph:** group logically related objects. Give every requested independently moving part a local pivot. Keep a vehicle or character root separate from wheel/limb/door groups.
6. **Geometry:** use actual 3D geometry for volumetric requirements. Generate paths and repeated details from parametric curves/points rather than copying the previous fixture's narrative geometry.
7. **Appearance:** use scene-appropriate materials, surface detail, and cohesive lighting. Apply separately supplied style guidance without fixing a palette or adding unrequested props.
8. **Runtime:** load declared imports, initialize WebGL once, size renderer and camera together, report failures, and attach/clean up only owned listeners and resources.
9. **Animation:** calculate all transforms from one elapsed-time timeline. For a path-following object, use normalized arc length for movement and derive rolling rotation from traveled distance and wheel radius. Derive heading from the path tangent. Keep camera behavior coordinated with, but not a substitute for, object movement.
10. **Delivery and validation:** check source, syntax/dependencies, local HTTP, browser runtime, visual output, motion, and packaging separately.

## Projection and spatial consistency

- Choose a camera projection and world-coordinate convention that fit the requested view; keep environment and subject geometry in the same world and projection.
- Orient moving roots and articulated parts in their local axes, deriving path-following heading from the path tangent. Keep terrain, roads, tracks, and other support surfaces aligned with the actual route and elevation.
- Check camera framing, near/far clipping, object clearance, ground contact, and depth/occlusion at representative start, turn, and stop states.
- Use mixed projections or deliberately stylized perspective only when justified by the source or design; verify that spatial relationships remain legible.

## Runtime and dependency guidance

- Prefer one standalone HTML entry point with plain JavaScript and native ES modules; add source files only for a clear separation or asset requirement.
- Pin the same Three.js version for the core import and any add-ons. Phase 2C-2 exercised `https://cdn.jsdelivr.net/npm/three@0.187.0/build/three.module.js`; reuse `0.187.0` for this proof unless an actual compatibility issue requires another version.
- The CDN import requires network access. Keep the network requirement visible; do not assert offline or `file://` support.
- Set color management, tone mapping, pixel ratio, shadows, and renderer cost deliberately. The Lunar fixture emitted a Three.js warning because `PCFSoftShadowMap` was removed in 0.187.0; use a supported shadow type such as `PCFShadowMap` when shadows are needed.
- Handle asynchronous import and renderer initialization errors explicitly. A visible error panel is useful, but also preserve console diagnostics.
- Resize using `ResizeObserver` where available or a window-resize fallback. Update camera projection and renderer dimensions together.
- Keep duration and loop behavior request-owned. A test fixture may state its own assumptions; never promote them to skill-wide defaults.
- Do not add GUI controls, recording/export, post-processing, a framework, or a package-wide dependency manifest unless explicitly required.

## Animation controller semantics

For a finite deterministic preview, use a small scene-local controller with equivalent behavior to:

```js
{
  durationSeconds,
  setTime(seconds),
  reset(),
  play(),
  pause(),
  dispose()
}
```

Expose only the controls needed by the artifact. `setTime(t)` should clamp or reject invalid times according to the scene contract and derive state from absolute time. `reset()` restores every animated transform. `play()` uses elapsed time so speed does not depend on frame rate. Stop scheduling frames at the finite endpoint for a play-once animation. Loop only when requested.

For rolling wheels, use the distance actually traveled along the path and the wheel's effective radius; derive wheel angle from distance, not elapsed frame count. Confirm local axle axes after the parent vehicle heading is applied. Test visible motion and contact at multiple times in the browser before marking the motion gate PASS.

## Validation evidence checklist

### Gate 1 — Source

- Record the requested scene, actions, camera, duration/aspect, loop, sources, and constraints.
- Mark assumptions as assumptions; do not let an example scene fill missing content.
- Record a requirement-to-object/action mapping and preserve canonical files.

### Gate 2 — Build

- Parse the embedded module (for example, `node --check --input-type=module` on extracted module text).
- Verify exact dependency URLs/version and asset paths.
- Use the documented local HTTP command; a response code alone does not establish browser runtime.

### Gate 3 — Runtime

- Record browser/version and actual procedure.
- Confirm module load, WebGL renderer/context initialization, visible canvas, and critical console errors.
- Keep warnings distinct from errors. If browser cannot be inspected, mark `BLOCKED` or `NOT_TESTED`, not PASS.

### Gate 4 — Visual

- Inspect actual rendered frames for all required objects, readable geometry, scale relationships, contact, framing, clipping, and visual-style cues.
- For Miniature Diorama, use multiple complementary cues such as model-scale relationships, crafted surface treatment, and intentional model-like lighting/composition. Small size or blur alone is insufficient.

### Gate 5 — Motion

- Observe at least two distinct playback times (and start/end when relevant).
- Verify path progression, heading, wheel/part articulation, contact, camera framing, duration, and endpoint/loop behavior.
- A source formula, static screenshot, or browser load alone is not motion evidence.

### Gate 6 — Delivery

- List exact delivered files and dependencies.
- Follow the run instructions from the stated output directory.
- Record known limitations, unrun checks, and any user-observed manual result with its source.

## Phase 2C-3 railway proof boundary

The second fixture is a mountain railway, independent from the lunar narrative. Its duration, 4:3 layout, and play-once behavior are fixture-only assumptions. Use the same construction workflow, but create new mountain terrain, curved track, bridge, train, wheels, and scenic details. Reuse only generic runtime/geometry/animation patterns. Do not add railway defaults to this capability.

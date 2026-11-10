# HTML/Canvas 2D Scene Production Workflow

This reference covers native Canvas 2D browser scenes. It is renderer guidance, not a generator, framework, or proof of browser compatibility. Select Canvas 2D only when it satisfies the user's scene and source requirements; use Three.js when genuine 3D geometry is required.

## Renderer and scene boundaries

- Preserve the user's explicit renderer choice when it can meet the scene requirements. A visual-style skill does not override that choice.
- Use Canvas 2D for naturally two-dimensional scenes, drawn animation, or pixel-art presentation when compatible. Do not flatten required volumetric geometry or a canonical 3D character into sprites.
- Keep scene content, production capability, renderer, and optional visual style separate. Pixel-grid alignment and nearest-neighbor scaling are Pixel Art options, not rules for every Canvas scene.
- Inspect canonical HTML/assets and preserve their identity and compatible runtime conventions before adapting them.

## Initialization and error handling

1. Provide a standalone HTML entry point with a canvas element and accessible fallback text or description.
2. Obtain the 2D context explicitly with `canvas.getContext("2d")`. If context creation fails, show a clear visible error and preserve useful console diagnostics; do not silently substitute another renderer.
3. Keep drawing setup, scene layers, animation state, and resize handling explicit. Avoid unnecessary dependencies.
4. Choose one coordinate policy before drawing: CSS-pixel coordinates, a fixed logical canvas, or a scene-defined world coordinate space. Document assumptions that materially affect the result.
5. Initialize listeners and the animation loop only after the required canvas/context is available. Clean up owned listeners or scheduled work if the scene can be stopped or replaced.

## Logical and display resolution

The canvas has two distinct sizes:

- **Backing-store resolution:** `canvas.width` and `canvas.height`, in drawing-buffer pixels.
- **Display resolution:** the CSS layout size shown in the page.

Choose the backing-store and display relationship intentionally:

- For CSS-pixel drawing, size the backing store to the displayed dimensions, accounting for device pixel ratio when sharp high-density output is needed. Scale the context so drawing coordinates remain in CSS pixels.
- For a fixed logical coordinate space, retain its logical dimensions and scale the displayed canvas to fit the available area. Map pointer/input coordinates back into that logical space if interaction is required.
- For Pixel Art, draw on a deliberately low-resolution logical canvas and enlarge with nearest-neighbor sampling. Snap pixel-art geometry and movement to the chosen logical grid. Do not impose this treatment on non-pixel styles.
- Preserve a user-requested aspect ratio and avoid stretching content. If letterboxing is needed, use a deliberate background and centered content region.

Use integer display scaling for a uniform pixel size when practical. If responsive layout requires a fractional scale, nearest-neighbor rendering can still keep edges hard, although displayed pixel widths may vary.

## Coordinate systems and pixel ratio

Keep world/logical, backing-store, and CSS/display coordinates distinct. For a canvas whose CSS dimensions are `displayWidth` and `displayHeight`, a common high-density setup is:

```js
const ratio = window.devicePixelRatio || 1;
canvas.width = Math.round(displayWidth * ratio);
canvas.height = Math.round(displayHeight * ratio);
canvas.style.width = `${displayWidth}px`;
canvas.style.height = `${displayHeight}px`;
context.setTransform(ratio, 0, 0, ratio, 0, 0);
```

This is one strategy, not a universal template. For a fixed logical canvas, use a transform or explicit coordinate mapping that preserves its logical dimensions instead of replacing them with device-pixel dimensions. Reapply context state after changing the backing-store dimensions because assigning `canvas.width` or `canvas.height` resets the context state.

## Projection and spatial consistency

Choose a view convention that fits the requested scene; Canvas does not require one universal viewpoint.

- **Top-down:** represent footprints and support surfaces as seen from above; keep routes inside the drawn traversable area and orient the subject along the route.
- **Side view:** show height and ground contact consistently; use side-facing forms when the camera exposes their sides.
- **Isometric:** use a consistent projected axis set and foreshortening for environment and subjects. Do not mix screen-space facade shapes with plan-view movement unless that mix is intentional and readable.
- Draw objects in local coordinates around useful pivots, then use `save()`, `translate()`, `rotate()`, and `restore()` to apply screen-space position and heading. Derive heading from the path tangent and rotate the complete subject group as appropriate.
- Geometry is view-dependent: for example, wheel faces may read as circles from the side, while a top-down view calls for narrow tire footprints aligned with travel. Choose the representation that matches the selected camera, not a fixed style rule.
- Keep draw order explicit. Typically draw background and environment before moving subjects, then add foreground occluders only where the scene requires them; use clipping or deliberate reordering when overlap changes.
- Align the route and any road/path markings with visible traversable space. Check start, turn, and stop positions for support, clearance from obstacles, clipping, and coherent occlusion.

## Image smoothing

When drawing scaled images or canvases, `context.imageSmoothingEnabled = false` requests nearest-neighbor sampling. For a CSS-scaled pixel-art canvas, use `image-rendering: pixelated` where supported. Apply these settings only when appropriate to the requested art style; smooth image interpolation may be correct for other Canvas scenes.

## Animation timing, clearing, and redraw

- Schedule preview frames with `requestAnimationFrame`.
- Compute scene state from elapsed time, such as `performance.now()` or the timestamp passed to the frame callback. Do not advance positions or sprite indices by a fixed amount per callback.
- For finite motion, clamp or otherwise define the timeline endpoint and honor requested duration and loop behavior.
- Select sprite-sheet frames from elapsed time and a declared frame cadence, not callback count. Keep discrete sprite changes separate from continuous object movement.
- Clear the frame with `clearRect` or repaint the complete background before drawing layers, unless persistent trails are explicitly requested.
- Restore transforms, clipping, alpha, compositing, and other mutable context state when drawing routines change them; `save()`/`restore()` can isolate local state.
- Redraw layers in a deliberate order. Use elapsed-time-driven offsets for parallax only when it supports the requested scene and camera treatment.

## Resize behavior

Use `ResizeObserver` or a window-resize listener when the display area can change. Recompute the display/backing-store relationship and any coordinate transforms without changing the user's intended logical scale or aspect ratio. Avoid assigning canvas dimensions on every frame: dimension assignment clears the canvas and resets drawing state. For a fixed logical canvas enlarged by CSS, a resize may require only layout updates, not a change to its backing store.

## Local HTTP delivery

Deliver the standalone HTML and necessary local assets only. State any external dependencies and network requirements. A common local run command from the fixture directory is:

```sh
python3 -m http.server 8000 --bind 127.0.0.1
```

Open `http://127.0.0.1:8000/`. Do not claim direct `file://` compatibility without testing it.

## Validation and evidence limits

Check HTML/JavaScript syntax, canvas element and context initialization, representative drawing calls, animation scheduling, and any declared sizing/scaling strategy. A static validator may report missing structure; it cannot establish that the browser created a working context, that the rendered composition is correct, or that animation was observed.

Report browser runtime, visual appearance, and motion separately. Mark them `NOT_TESTED` unless actually observed. Generic Canvas structural validation must not silently enforce Pixel-Art-only properties such as `imageSmoothingEnabled = false` or `image-rendering: pixelated`.

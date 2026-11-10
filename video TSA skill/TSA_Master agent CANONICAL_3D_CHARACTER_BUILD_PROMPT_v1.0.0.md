# TSA --- CANONICAL 3D CHARACTER BUILD PROMPT

**Document ID:** TSA-CANONICAL-3D-CHARACTER-BUILD-PROMPT\
**Version:** 1.0.0\
**Status:** Reusable baseline prompt\
**Target:** Any AI agent/platform capable of inspecting and editing
HTML/Three.js source\
**Primary deliverable:** A standalone, reusable HTML/Three.js character
asset

------------------------------------------------------------------------

## 1. MASTER PROMPT --- COPY AND EXECUTE

You are a Three.js character artist, technical artist, procedural
modeling engineer, and animation engineer working under the TSA
(Technical Specification and Audit) workflow.

Build a new reusable 3D character using the HTML character files
supplied by the user as the authoritative implementation baseline.

The supplied examples are not merely visual inspiration. Inspect their
actual source code and derive the established construction method,
geometry language, proportions, body hierarchy, pivots, materials,
renderer settings, stage/camera conventions, and animation methods.

**The existing character HTML files define the baseline. Extend that
baseline; do not replace it.**

Do not rebuild a character from visual guesswork when canonical source
code is available. Do not create something that only resembles a
screenshot. Do not silently change the geometry style, hierarchy,
rigging approach, material system, Three.js version, or runtime
architecture.

If a detail cannot be verified from the supplied files, label it
`UNKNOWN` or `PROPOSED`. Never present an assumption as source evidence.

## 2. USER INPUTS

The user may provide:

-   One or more canonical character HTML files.
-   A target character name, image, or description.
-   Required costume, accessories, variants, poses, or expressions.
-   Required animations or actions.
-   Optional stage, aspect ratio, camera, and background requirements.

The canonical HTML examples define implementation conventions. Target
references define the new character's identity and appearance. Keep
these two roles distinct.

If multiple canonical examples are supplied, inspect all of them.
Separate conventions shared by the examples from details unique to one
character.

## 3. TSA WORKFLOW

Use goal-first, evidence-based, incremental, reversible implementation.
Preserve existing behavior and avoid unnecessary repository scans or
over-engineering.

### Phase 0 --- Input inventory

List the supplied files and identify:

-   Canonical character source files.
-   Complete HTML files versus partial snippets.
-   Three.js version and loading method.
-   External models, textures, scripts, fonts, or other dependencies.
-   Missing or inaccessible files.

Do not assume a referenced asset exists until verified.

### Phase 1 --- Canonical source audit

Read the actual HTML/JavaScript source. Inspect relevant sections first,
then expand only as dependencies require.

Audit and record:

1.  HTML structure and runtime initialization.
2.  Three.js version, renderer, scene, camera, and stage dimensions.
3.  Geometry construction method and detail level.
4.  Body-part hierarchy, groups, parent-child relationships, and pivots.
5.  Silhouette, proportions, scale, and orientation.
6.  Face, eyes, mouth, hair/fur/head construction.
7.  Costume layers, accessories, and attachment points.
8.  Material types, colors, roughness, metalness, emissive values, and
    transparency.
9.  Texture loading or procedural texture generation.
10. Lighting, shadows, tone mapping, and color-space settings.
11. Animation loops, keyframes, procedural movement, and interaction
    logic.
12. Naming conventions and reusable helper functions.
13. Known limitations and fragile implementation details.

Do not infer source structure from screenshots when the HTML is
available.

Create `CANONICAL_CHARACTER_AUDIT.md`:

  -----------------------------------------------------------------------
  Area              Observed          Source evidence   Required
                    implementation                      treatment
  ----------------- ----------------- ----------------- -----------------
  Runtime           Actual            File and code     Preserve or
                    version/loading   section           justify change

  Geometry          Actual            File and code     Match baseline
                    construction      section           
                    method                              

  Hierarchy         Actual groups and File and code     Preserve
                    pivots            section           articulation

  Materials         Actual material   File and code     Match visual
                    system            section           response

  Stage/camera      Actual dimensions File and code     Reuse unless
                    and setup         section           justified

  Animation         Actual movement   File and code     Reuse compatible
                    method            section           patterns
  -----------------------------------------------------------------------

Use `UNKNOWN` where evidence is absent.

### Phase 2 --- Define the baseline

Classify findings:

**A. Canonical baseline --- preserve** - Conventions shared across
supplied examples. - Geometry and visual language defining the existing
character family. - Runtime, stage, hierarchy, and animation conventions
required for compatibility.

**B. Character-specific --- may differ** - Identity-specific
proportions. - Face, hair, costume, colors, and accessories. - Unique
geometry and articulation supported by the target.

**C. Unknown or optional** - Details not established by the source
files. - Enhancements that would alter the existing system. - New
dependencies or architectural changes.

Do not promote category C into the canonical baseline without user
approval.

## 4. TARGET CHARACTER SPECIFICATION

Before coding, define:

-   Character identity/name.
-   Recognizable silhouette.
-   Head/body proportions.
-   Face and expression features.
-   Hair, fur, or other head details.
-   Costume layers and colors.
-   Shoes, gloves, and accessories.
-   Distinctive identity markers.
-   Required articulation and animations.
-   Required front, side, and three-quarter appearance.

Label each decision:

-   `REFERENCE_OBSERVED` --- directly supported by target reference.
-   `CANONICAL_DERIVED` --- implementation convention found in supplied
    HTML.
-   `PROPOSED` --- a necessary design decision not established by
    evidence.

If target references conflict with the canonical implementation,
preserve target identity while following canonical construction
conventions wherever technically possible. Report major conflicts before
changing architecture.

## 5. CHARACTER CONSTRUCTION

### Geometry and silhouette

-   Use the geometry approach demonstrated by the canonical examples.
-   Match their visual language and detail level.
-   Build a coherent full-body character, not an arbitrary collection of
    disconnected primitives.
-   Preserve recognizable proportions, silhouette, scale, and
    orientation.
-   Do not label the style voxel, low-poly, high-poly, or another
    category unless the source supports it.

### Hierarchy and pivots

-   Reuse the canonical hierarchy pattern where applicable.
-   Place pivots at appropriate joints and rotation origins.
-   Ensure head, torso, arms, hands, legs, feet, costume, and
    accessories move coherently.
-   Do not rotate a whole limb around an incorrect origin when the
    baseline supports joint-level articulation.
-   If the baseline uses grouped procedural geometry rather than a
    skeletal rig, follow that approach unless migration is approved.
-   Do not invent rig-node or animation-clip names.

### Face and identity

The face is a high-priority identity area.

-   Reproduce recognizable facial structure and expression.
-   Follow the canonical method for eyes, eyebrows, mouth, nose, and
    other features where compatible.
-   Preserve readable front and side views.
-   Avoid facial elements that float, detach, or face the wrong
    direction.
-   Do not simplify distinctive identity features without justification.

### Costume and accessories

-   Inspect how the canonical examples construct and attach clothing.
-   Preserve costume colors, layers, and recognizable details.
-   Attach accessories to the correct group or pivot.
-   Prevent floating, clipping, and unintended intersections.
-   Give independently moving costume elements a suitable hierarchy.

### Materials and rendering

-   Inspect actual canonical materials and renderer color settings.
-   Match color response, roughness, metalness, transparency, and
    emissive behavior.
-   Do not automatically add HDRI, PBR texture maps, bloom, SSAO, SSR,
    or depth of field.
-   Add advanced rendering only when it exists in the baseline or is
    demonstrably required and approved.

## 6. ANIMATION REQUIREMENTS

A character is not accepted merely because it renders.

Use the animation approach supported by the canonical source. When
animation is requested, define:

-   Initial/rest pose.
-   Anticipation.
-   Main action.
-   Contact or interaction.
-   Follow-through.
-   Recovery.
-   Return to idle or transition.

Where supported by the source construction, coordinate head, torso,
hips, shoulders, arms, elbows, wrists, legs, knees, ankles, hands, feet,
hair, clothing, and accessories.

Avoid moving only the whole character when the requested action requires
articulated body movement.

Animation checks:

-   No unintended foot sliding during planted phases.
-   Hands reach intended interaction points.
-   Limbs rotate around correct pivots.
-   No body parts detach or pass through the floor.
-   Anticipation and follow-through are readable.
-   Timing is deterministic.
-   Restart restores the correct initial state.
-   Secondary motion is restrained and consistent with the established
    style.

If the user requests a static model, do not add elaborate animation
without permission.

## 7. STAGE, CAMERA, AND BACKGROUND

-   Reuse canonical stage dimensions and aspect ratio unless instructed
    otherwise.
-   Reuse camera conventions where possible.
-   Keep the entire character visible and correctly framed.
-   Provide a useful default front view.
-   Provide side and three-quarter inspection views if compatible with
    the baseline.
-   Preserve the required background and transparency behavior.
-   Do not add timers, cards, HUD, decorative text, or unrelated UI.

If transparency is requested, implement actual transparent
canvas/renderer output where supported. Do not simulate it with a
checkerboard or solid background and claim it is transparent.

## 8. IMPLEMENTATION RULES

-   Deliver a standalone HTML file when requested.
-   Keep CSS and JavaScript inline if required by the baseline or user.
-   Do not introduce frameworks or dependencies without demonstrated
    need.
-   Do not change Three.js version without justification.
-   Do not add remote dependencies when existing/local implementations
    suffice.
-   Never overwrite or modify supplied canonical reference files.
-   Build the new character as a separate deliverable.
-   Organize code into clear sections: configuration, materials,
    geometry, hierarchy, animation, lighting, camera, and runtime.
-   Keep the character reusable and independent of any particular film
    scene, game mechanic, or camera sequence.

## 9. REQUIRED DELIVERABLES

Unless the user requests otherwise:

1.  `target_character.html` --- standalone character implementation.
2.  `CANONICAL_CHARACTER_AUDIT.md` --- evidence-based source audit.
3.  `CHARACTER_BUILD_REPORT.md` --- implementation summary and
    deviations.
4.  `ASSET_DEPENDENCIES.md` --- external dependencies, or confirmation
    that the HTML is self-contained.

The HTML is the primary deliverable. Documentation does not substitute
for a working character.

## 10. VALIDATION GATES

Report each check as `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED`, with
evidence.

### Source fidelity

-   [ ] All supplied canonical examples inspected.
-   [ ] Canonical conventions documented with source evidence.
-   [ ] Unknowns are not presented as facts.
-   [ ] Original reference files remain unchanged.

### Visual identity

-   [ ] Target silhouette is recognizable.
-   [ ] Key proportions and identity features are present.
-   [ ] Costume and accessories are correctly placed.
-   [ ] Front, side, and three-quarter views have no major defects.
-   [ ] Materials and colors match the baseline.

### Geometry and hierarchy

-   [ ] Body parts follow the intended hierarchy.
-   [ ] Pivots are correctly placed.
-   [ ] No unintended floating or detached geometry.
-   [ ] No severe mesh intersections.
-   [ ] Scale and orientation are correct.

### Animation, when requested

-   [ ] Required actions are present.
-   [ ] Joint movement is coordinated.
-   [ ] Anticipation and follow-through are readable.
-   [ ] No unintended foot sliding or floor penetration.
-   [ ] Timing is deterministic and restart works.

### Runtime

-   [ ] HTML opens in the intended browser/runtime.
-   [ ] Three.js and dependencies load.
-   [ ] No critical console errors.
-   [ ] No missing assets.
-   [ ] Stage dimensions and transparency behave as requested.
-   [ ] Character remains visible at intended size.

Do not mark visual checks `PASS` if the agent could not render and
inspect the result.

## 11. CHANGE CONTROL

If faithful implementation is impossible under the current baseline:

1.  Stop before replacing the baseline.
2.  Identify the exact technical conflict.
3.  Cite the source convention causing it.
4.  Propose the smallest reversible change.
5.  Explain compatibility impact on existing characters.
6.  Obtain user approval before changing canonical architecture.

Do not silently migrate all characters to a new rig, geometry style,
material system, renderer version, or framework.

## 12. REQUIRED AGENT RESPONSE

Before coding, report:

1.  Input inventory.
2.  Canonical findings from actual source.
3.  Baseline rules that will be preserved.
4.  Target character specification.
5.  Unknowns and conflicts.
6.  Minimal execution plan.

Then implement the agreed scope.

After coding, report:

1.  Files created.
2.  Canonical structures/patterns reused.
3.  Character-specific additions.
4.  Deviations from baseline and reasons.
5.  Validation results.
6.  Known limitations.
7.  Exact output paths.

Never claim source reuse unless the implementation was actually derived
from and checked against the supplied HTML.

## 13. SHORT EXECUTION PROMPT

Use this when the full protocol is already available to the agent:

> Read and follow `TSA_CANONICAL_3D_CHARACTER_BUILD_PROMPT_v1.0.0.md`.
> Inspect the attached canonical character HTML files as the
> authoritative implementation baseline. Audit their actual geometry,
> hierarchy, pivots, materials, proportions, stage/camera, renderer
> settings, and animation methods before coding. Build the requested new
> character as a separate standalone HTML asset, preserving the
> established TSA character language and reusing compatible
> implementation patterns. Do not rebuild by visual guesswork, modify
> the supplied references, or introduce a new rig/rendering architecture
> without approval. First report the source audit, baseline rules,
> target specification, unknowns, and minimal plan. Then implement and
> validate the character. Deliver the HTML and evidence-based
> audit/build reports. Mark untested checks honestly.

------------------------------------------------------------------------

## 14. FINAL TSA RULE

**The existing character examples define the baseline. The new character
must extend that baseline, not replace it.**

The agent must inspect, understand, reuse, and carefully extend the
actual implementation---not guess what the original author might have
built.

# TSA --- IMAGE-TO-THREE.JS CHARACTER CREATION PROMPT (CHAT WEB)

1. Gambar referensi adalah sumber utama untuk bentuk, warna, proporsi, dan identitas karakter.
2. Mata dan mulut wajib ada, mengikuti bentuk serta posisinya pada gambar. Tidak boleh hilang atau tertutup geometri.
3. Tubuh benar-benar 3D, memiliki ketebalan dan volume, bukan gepeng.
4. Tangan dan kaki memiliki pivot, siap untuk animasi.
5. HTML Three.js mandiri, dapat diputar untuk inspeksi depan, samping, dan 3/4.
6. Setiap karakter menjadi file HTML terpisah, siap diintegrasikan ke proyek game atau film TSA.
7. Validasi sebelum diserahkan, terutama mencegah layar kosong dan kesalahan dependensi. Pengujian yang belum dilakukan harus dilaporkan.
Aturan tambahan: Karakter berikutnya tidak harus berbentuk kotak. Geometri mengikuti gambar masing-masing, bukan memaksakan bentuk karakter sebelumnya.

# 1. PURPOSE

Use this prompt to create a 3D character in Three.js from a
user-supplied PNG/JPG image.

The image is the **primary visual source of truth** for the new
character. The AI must study the image and construct the character in
HTML/Three.js.

Existing TSA character HTML files are optional implementation
references. They help the AI preserve the established TSA construction
style, but their absence must never prevent character creation.

## The two input types have different jobs

  -----------------------------------------------------------------------
  Input                   Purpose                 Required?
  ----------------------- ----------------------- -----------------------
  Target character        Defines the character's **Yes**
  PNG/JPG                 visual identity and     
                          appearance              

  Existing TSA character  Shows how previous TSA  Optional, strongly
  HTML                    characters were         recommended
                          actually constructed    

  Written description     Clarifies details not   Optional
                          visible in the image    

  Animation reference     Defines requested       Optional
                          movement                
  -----------------------------------------------------------------------

**Important:** Do not confuse the target character image with a
canonical HTML source. The image defines what to build. Existing HTML
examples, when supplied, define how the established TSA characters were
implemented.

If the user supplies only an image, proceed with image-based character
construction. Do not stop or ask for an HTML file.

------------------------------------------------------------------------

# 2. MASTER PROMPT --- COPY AND PASTE

You are a professional Three.js character artist, 3D technical artist,
procedural modeling engineer, and character animation engineer.

Work under the **TSA (Technical Specification and Audit) workflow**.

I am attaching an image of a character. Your primary task is to **build
that character as a 3D Three.js model inside a standalone HTML file**.

Do not merely describe the image. Do not generate another picture. Do
not return only a design proposal. The required output is a working
HTML/Three.js character that I can open in a browser and download.

## CRITICAL INPUT RULE

The attached PNG/JPG is the target character reference and the primary
source of visual truth.

Study the image carefully. Reconstruct the character's visible design in
3D:

-   Overall silhouette and body proportions.
-   Head shape and size.
-   Face, eyes, mouth, nose, and other identity features.
-   Body shape and limb proportions.
-   Costume, armor, clothing, or surface details.
-   Color palette and color distribution.
-   Accessories and distinctive features.
-   Visible asymmetry and design-specific details.

Do not replace the supplied character with a generic character, a
loosely similar design, or an interpretation that ignores distinctive
features.

Do not use image generation as a substitute for building the Three.js
model. The deliverable must be actual HTML/JavaScript/Three.js geometry
and materials.

## BASELINE RULE --- WHEN EXISTING TSA HTML IS ATTACHED

If I also attach one or more existing TSA character HTML files:

1.  Inspect their actual source code.
2.  Identify their Three.js version, geometry construction, hierarchy,
    pivots, materials, renderer, stage, camera, lighting, and animation
    methods.
3.  Reuse compatible construction patterns and code structures.
4.  Preserve the established TSA character visual language and runtime
    conventions.
5.  Build the new character as a separate asset. Do not modify the
    supplied examples.

The supplied HTML files are implementation references. The target image
remains the source of truth for the new character's appearance.

### If no existing HTML is attached

**Continue the task. Do not stop.**

Use the following TSA implementation baseline:

-   Build a standalone HTML document with inline CSS and JavaScript
    where practical.
-   Use Three.js for actual 3D geometry and rendering.
-   Construct the character from organized, named geometry groups and
    meshes.
-   Use meaningful parent-child hierarchy and correctly placed pivots
    for articulating body parts.
-   Use separate geometry/material definitions for body parts, costume,
    face, and accessories.
-   Preserve the image's silhouette, proportions, colors, and
    distinctive details.
-   Keep the character independent of any particular film scene or game
    mechanic.
-   Make the source code readable and suitable for future reuse and
    extension.
-   Avoid unnecessary frameworks, dependencies, and rendering effects.

Do not claim that you inspected or reused an HTML baseline that was not
supplied. State that the implementation follows the TSA construction
requirements available in this prompt, while exact source-level matching
to previous files has not been verified.

------------------------------------------------------------------------

# 3. PHASE 1 --- IMAGE ANALYSIS

Before coding, inspect the attached image.

Describe the character using evidence visible in the image.

### A. Silhouette and proportions

Identify:

-   Character height-to-width impression.
-   Head-to-body ratio.
-   Torso shape.
-   Arm and leg proportions.
-   Hand and foot size.
-   Overall body silhouette.
-   Distinctive outline features.

### B. Face and identity

Identify:

-   Eye count, shape, size, spacing, and placement.
-   Eyebrows, if present.
-   Mouth, teeth, nose, and other facial features.
-   Face orientation and depth.
-   Unique facial or head details.

Do not invent hidden facial details that cannot be seen. For unseen
sides, make the smallest reasonable construction decision and label it
as an assumption.

### C. Costume and surface details

Identify:

-   Main and secondary colors.
-   Clothing or armor components.
-   Color boundaries and patterns.
-   Surface finish: matte, glossy, metallic, fabric-like, etc., only
    where visually supported.
-   Accessories, attachments, and distinctive markings.

### D. Image evidence limitations

Separate observations into:

-   `IMAGE_OBSERVED` --- directly visible in the supplied image.
-   `INFERRED` --- a reasonable 3D interpretation needed to construct
    unseen depth or hidden surfaces.
-   `UNKNOWN` --- cannot be determined from the image.

A single 2D image does not reveal the exact rear design, hidden
geometry, true dimensions, or original 3D topology. Do not claim
otherwise.

If the image is sufficient to build a useful character, proceed without
asking unnecessary questions.

------------------------------------------------------------------------

# 4. PHASE 2 --- BUILD SPECIFICATION

Prepare a concise specification:

1.  Character silhouette and proportions.
2.  Head and face construction.
3.  Torso and limb construction.
4.  Costume and accessories.
5.  Color and material plan.
6.  Geometry hierarchy and pivots.
7.  Default pose.
8.  Requested animation, if any.
9.  Camera and preview stage.
10. Unknowns and assumptions.

If existing TSA HTML files are attached, add a short source audit
explaining which implementation conventions will be reused.

Do not spend the whole response discussing the plan. Once the
specification is clear, proceed to implementation. Ask for approval only
when a major unresolved decision would materially change the requested
character or architecture.

------------------------------------------------------------------------

# 5. PHASE 3 --- THREE.JS CHARACTER CONSTRUCTION

Create an actual 3D model using Three.js.

## A. Geometry

-   Use meshes and geometry appropriate to the character's visible
    design.
-   Reconstruct the silhouette and proportions accurately.
-   Avoid representing a detailed character as a few generic spheres and
    boxes.
-   Add enough geometry to preserve recognizable identity.
-   Keep body parts organized and named.
-   Ensure correct orientation, scale, and attachment.
-   Use custom or combined geometry when primitive shapes alone cannot
    reproduce important features.

Do not arbitrarily classify the character as voxel, low-poly, high-poly,
realistic, or stylized. Follow the supplied image. If TSA HTML
references are attached, also respect their established modeling
language where compatible.

## B. Hierarchy and articulation

Organize the model into logical groups such as:

-   Character root.
-   Hips/pelvis.
-   Torso.
-   Neck/head.
-   Upper and lower arms.
-   Hands.
-   Upper and lower legs.
-   Feet.
-   Costume and accessories.

Adapt this hierarchy to the actual character. These are examples, not
mandatory body parts for every design.

Use correctly placed pivots so the character can be animated later. Do
not make every part an unrelated scene object or rotate limbs around
arbitrary origins.

## C. Face and distinctive details

Prioritize the details that make the supplied character recognizable.

Do not omit a single eye, unusual head shape, emblem, horn, armor
component, or other distinctive feature visible in the image.

Check the face from the front and from an angled view to ensure features
have correct depth and orientation.

## D. Materials and colors

Use Three.js materials appropriate to the reference:

-   `MeshStandardMaterial` for general physically based material
    response where appropriate.
-   `MeshPhysicalMaterial` only when its additional properties are
    useful.
-   Basic materials only when they better match the intended visual
    style.

Match the visible palette and surface appearance. Do not add advanced
textures or post-processing merely to make the implementation look more
complex.

## E. Lighting

Use lighting that makes the character readable and preserves the
reference colors.

Provide sufficient key and fill illumination. Use shadows where they
improve shape readability.

Do not allow dramatic lighting to obscure the character's actual colors
or important details.

------------------------------------------------------------------------

# 6. PHASE 4 --- CHARACTER MOVEMENT

If I request an animated character, implement actual articulated
movement.

Do not assume that moving the root group alone is sufficient.

Use coordinated body movement where the hierarchy supports it:

-   Head and neck.
-   Torso and hips.
-   Shoulders, arms, elbows, and wrists.
-   Hands.
-   Legs, knees, ankles, and feet.
-   Flexible or secondary elements where appropriate.

For each requested action, use meaningful motion phases:

1.  Initial pose.
2.  Anticipation.
3.  Main action.
4.  Contact or interaction, if applicable.
5.  Follow-through.
6.  Recovery.

Avoid stiff, robotic movement when the action requires natural
articulation.

Do not add elaborate animation if I request a static model. A simple
preview idle may be included only when it is useful and does not alter
the requested character.

------------------------------------------------------------------------

# 7. PHASE 5 --- CAMERA AND PREVIEW STAGE

Create a clean character inspection stage.

Requirements:

-   Show the entire character by default.
-   Use a camera angle that clearly communicates the design.
-   Avoid accidental cropping.
-   Keep the character centered and properly scaled.
-   Use a clean background.
-   Provide front, side, and three-quarter inspection where practical.
-   If requested, implement a genuinely transparent canvas background.
-   Do not add unrelated cards, timers, HUD, labels, or decorative UI.

The character asset must remain reusable. Do not embed it into a film
scene or game arena unless I explicitly request that.

------------------------------------------------------------------------

# 8. PHASE 6 --- CREATE THE DOWNLOADABLE HTML

The primary deliverable is:

`target_character.html`

It must contain the actual Three.js implementation, not a static
screenshot or an image embedded as the character.

If the platform supports file generation:

-   Create the HTML file.
-   Attach it or provide a verified download link.
-   Ensure the file contains the complete implementation.
-   Do not claim that a file was created unless it actually exists.

If the platform cannot create downloadable files, provide the complete
HTML source in one code block and explicitly state that it has not been
packaged as a downloadable file.

Do not use an image-generation tool to satisfy this request. I am asking
for a 3D HTML implementation.

------------------------------------------------------------------------

# 9. PHASE 7 --- VALIDATION

Validate the output as far as the platform allows.

Report each item as `PASS`, `FAIL`, `BLOCKED`, or `NOT_TESTED`.

### Visual fidelity

-   [ ] Main silhouette matches the supplied image.
-   [ ] Head and body proportions are consistent.
-   [ ] Face and distinctive features are present.
-   [ ] Costume and accessories are present.
-   [ ] Color distribution is consistent.
-   [ ] No important visible design feature was omitted.

### Geometry

-   [ ] Body parts are connected correctly.
-   [ ] No unintended floating geometry.
-   [ ] No severe intersections.
-   [ ] Character has correct scale and orientation.
-   [ ] Pivots are suitable for future articulation.

### Runtime

-   [ ] HTML contains actual Three.js geometry and rendering code.
-   [ ] HTML opens in the intended browser, if execution is available.
-   [ ] Dependencies load.
-   [ ] No critical runtime errors.
-   [ ] Character is visible and correctly framed.

### Source baseline

If canonical HTML was attached: - \[ \] Source was actually inspected. -
\[ \] Reused conventions are identified. - \[ \] Original files remain
unchanged.

If no canonical HTML was attached: - Mark exact source-level matching as
`NOT_VERIFIED`. - Do not block character creation because of this.

Do not mark browser or visual tests as `PASS` if you did not actually
run and inspect the result.

------------------------------------------------------------------------

# 10. FINAL RESPONSE FORMAT

After implementation, report:

1.  Character features reconstructed from the image.
2.  Important assumptions for unseen surfaces.
3.  How the 3D geometry and hierarchy were constructed.
4.  Animation included, if requested.
5.  Whether an existing TSA HTML baseline was supplied and inspected.
6.  Validation results and limitations.
7.  The actual downloadable HTML file.

The HTML file is the main result. Keep the explanation concise and make
the download easy to find.

------------------------------------------------------------------------

# 11. USER REQUEST TEMPLATE

Use this optional template after attaching the target image:

``` text
TARGET CHARACTER
Name (if known):
Reference image: attached
Details that must be preserved:

BUILD
Static or animated:
Required animation:
Important body-part movement:

PRESENTATION
Aspect ratio:
Background:
Transparent background: Yes / No
Preferred camera view:

OUTPUT
Create a standalone Three.js HTML file.
Provide the actual downloadable HTML.
Do not generate a replacement image.
```

The user may leave fields blank. Do not ask for information that can be
reasonably read from the image.

------------------------------------------------------------------------

# 12. FOLLOW-UP CORRECTION PROMPTS

### If the AI asks for canonical HTML even though the PNG is attached

> The attached PNG is the target character source. Existing HTML
> examples are optional implementation references, not a prerequisite.
> Proceed with image-based Three.js character construction using the TSA
> baseline defined in this prompt. Do not stop because no old HTML file
> is attached.

### If the AI only describes the image

> Stop describing and implement. Build the character as actual Three.js
> geometry and materials in a standalone HTML file. The image is a
> visual reference, not the requested output.

### If the AI generates another image

> I did not request image generation. I requested a 3D character
> implementation using HTML and Three.js. Build the geometry, materials,
> hierarchy, and renderer in the HTML file.

### If the AI creates a generic character

> Compare the result feature by feature with the attached image.
> Identify omitted or incorrectly reconstructed silhouette, proportions,
> face, colors, costume, and distinctive details. Correct the actual
> Three.js geometry. Do not replace the model with another generated
> picture.

### If the AI provides code but no file

> Create the complete HTML as a real downloadable file if your platform
> supports file generation. If not, state that limitation and provide
> the complete source code as a fallback.

------------------------------------------------------------------------

# 13. FINAL TSA RULE

**The supplied image defines the character. The established TSA examples
define the implementation baseline when available.**

The AI must build the character from the image---not demand an old HTML
file before starting.

If an old HTML reference is attached, inspect and reuse its proven
construction conventions. If it is not attached, continue with the TSA
implementation rules in this document and be honest that exact
source-level matching has not been verified.

The required result is a real, reusable Three.js character in a
downloadable HTML file---not a description, not a replacement image, and
not a generic approximation.

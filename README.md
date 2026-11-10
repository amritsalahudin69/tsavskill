# TSA VSkills

TSA VSkills organizes video-production guidance into a parent skill, operation capabilities, and visual-style skills. These project skills provide instructions and selection guidance; their presence does not itself provide a renderer or video-generation engine.

## Current maturity

Three project skills are installed under `.github/skills/`:

- **`vskills`** — parent/orchestration guidance for selecting production modes and composing an operation capability with an optional visual style.
- **`vidmindi`** — Miniature Diorama visual-style guidance; it affects presentation without replacing the user's scene.
- **`scene-production`** — instruction capability for implementing and validating user-defined browser scenes, including HTML/Three.js workflows.

From the repository root, `copilot skill list` was verified to list all three project skills in the observed GitHub Copilot CLI **1.0.108** environment. This is an observed environment, not a minimum-version requirement. Discovery does not prove automatic parent routing or scene execution.

Parent composition was tested manually with a user-defined delivery-truck scene. The parent selected `scene-production` and `vidmindi` while preserving the requested truck, bridge, and mountain village. This does not demonstrate a universal automatic router.

## Installation — GitHub Copilot CLI

### Prerequisites

- GitHub Copilot CLI, to discover and invoke the skills.
- Git, if using the manual clone-and-copy method.
- A GitHub CLI version that supports `gh skill`, only if trying the optional remote commands. GitHub CLI and Copilot CLI are separate tools and are not interchangeable.

### Method A: GitHub CLI (unverified for this repository)

The `gh skill` commands below are examples only. Remote preview/install has not been tested end-to-end for this repository; it requires the corresponding skill files to be available remotely. Check the current GitHub CLI help and verify discovery in the target project after any install.

This repository stores skills under `.github/skills/`, a hidden directory. The examples include `--allow-hidden-dirs`; confirm that option is supported by the installed GitHub CLI:

```bash
gh skill preview amritsalahudin69/tsavskill vskills --allow-hidden-dirs
gh skill install amritsalahudin69/tsavskill vskills --allow-hidden-dirs
```

```bash
gh skill preview amritsalahudin69/tsavskill vidmindi --allow-hidden-dirs
gh skill install amritsalahudin69/tsavskill vidmindi --allow-hidden-dirs
gh skill preview amritsalahudin69/tsavskill scene-production --allow-hidden-dirs
gh skill install amritsalahudin69/tsavskill scene-production --allow-hidden-dirs
```

GitHub CLI may select a host-specific installation location. That may differ from this repository's `.github/skills/` layout; verify the installed location and discovery in the target project.

### Method B: Manual project installation

The commands below illustrate copying selected skill directories into a target project's `.github/skills/`. This cross-project installation workflow has not been validated on a fresh target. Do not copy the whole repository into a skill directory or copy local TSA development records.

WSL/Linux, from the directory where you want the repository clone:

```bash
git clone https://github.com/amritsalahudin69/tsavskill.git
mkdir -p /path/to/target-project/.github/skills
cp -R tsavskill/.github/skills/vskills /path/to/target-project/.github/skills/
cp -R tsavskill/.github/skills/vidmindi /path/to/target-project/.github/skills/
cp -R tsavskill/.github/skills/scene-production /path/to/target-project/.github/skills/
```

In Windows PowerShell, use the equivalent commands:

```powershell
git clone https://github.com/amritsalahudin69/tsavskill.git
New-Item -ItemType Directory -Force -Path "C:\path\to\target-project\.github\skills"
Copy-Item -Recurse ".\tsavskill\.github\skills\vskills" "C:\path\to\target-project\.github\skills\"
Copy-Item -Recurse ".\tsavskill\.github\skills\vidmindi" "C:\path\to\target-project\.github\skills\"
Copy-Item -Recurse ".\tsavskill\.github\skills\scene-production" "C:\path\to\target-project\.github\skills\"
```

### Local discovery

From this repository root, run:

```bash
copilot skill list
```

This command was verified here in Copilot CLI 1.0.108. In another target project, run it from that project's root to check discovery; cross-project installation has not been independently tested.

### Prompt-based invocation

Ask Copilot to use the skill in a prompt, for example:

```text
Use the vskills parent skill to explain the available capabilities.
```

```text
Use scene-production to implement my user-defined scene as HTML/Three.js,
and apply vidmindi's Miniature Diorama presentation guidance.
```

These are prompt-based selection examples. Native `/vidmindi` and `/scene-production` slash-command registration has not been verified; do not treat those names as standalone shell commands.

### Troubleshooting

- **Skill not listed:** Run `copilot skill list` from the target project root; confirm the skill is under `.github/skills/<skill-name>/SKILL.md`.
- **Wrong installation directory:** GitHub CLI may use `.agents/skills/` at project scope. Use manual copying for the `.github/skills/` layout, or verify that the chosen location is discovered by your Copilot CLI version.
- **Invalid metadata:** Check that `SKILL.md` has YAML frontmatter with a `name` and `description`, and that the name matches the skill directory.
- **Running from a different project:** Project skills are scoped to the project. Start Copilot CLI from the directory containing the installed skill path.
- **Missing project skill:** Confirm that the skill directory and `SKILL.md` are present, then run `copilot skill list` from the project root.
- **Unsupported command:** Check the current `copilot` or `gh` CLI help; the remote `gh skill` examples above are unverified for this repository.

## Production modes and visual styles

The design separates production mode (output type), operation capability (work performed), and visual style (presentation):

- **Standalone Animation** — one autonomous animation; duration is user-defined.
- **Modular Film** — scenes intended for assembly; the 15-minute limit applies to the complete film, not each scene.
- **Character Asset** — a reusable character asset.

`vidmindi` supplies Miniature Diorama visual-style guidance. Other visual styles are unimplemented. A visual style does not itself provide a scene-production engine.

## Current capability status

**Composition model:** `vskills` guides selection of a production capability and, when requested, an optional primary visual style. For an HTML/Three.js scene, `scene-production` provides the implementation workflow; `vidmindi` may supply Miniature Diorama presentation guidance. The user's scene remains authoritative.

**Parent composition:** A manual composition test selected `scene-production` and `vidmindi` for a user-defined truck/bridge/village request. This was an orchestration check, not an automatic universal routing test.

**Lunar Outpost fixture:** Static and local HTTP checks previously passed. The user reported manual browser PASS for rendering, visible rover and habitat, actual 3D volume, recognizable Miniature Diorama appearance, rover movement and wheel rotation, and no critical DevTools Console errors. These are user-observed results, not agent-automated browser tests; agent browser automation and automated motion capture remain incomplete.

**Miniature Railway fixture:** Static checks and a local HTTP smoke test passed. Browser runtime, visual fidelity, and rendered motion have not been verified.

Both fixtures use Three.js **0.187.0** from jsDelivr and require network access to load the CDN dependency. Their results demonstrate only the checks stated above; they do not establish arbitrary-scene reliability.

**Limitations:** `scene-production` is an instruction capability, not a generic scene generator. No universal automatic router, video-generation engine, or MP4 exporter is implemented. Native `/vidmindi` and `/scene-production` slash-command registration is unverified.

## Licensing and attribution

There is no confirmed project `LICENSE` file or selected project license. Redistribution rights and attribution for original source prompts and protocol materials remain unresolved. Do not infer permission to redistribute them from their presence in the working tree.

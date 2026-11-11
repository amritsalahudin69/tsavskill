# TSA VSkills

TSA VSkills is a **general browser-based visual-production skill system** for AI coding agents. The parent `vskills` skill is the entry point. It distinguishes **production mode**, **operation capability**, and optional **visual style**. The nine styles are presentation add-ons, not the whole purpose of TSA VSkills.

## Main capability

- `vskills` — choose a mode and appropriate capability, preserve the user’s subject and canonical sources, and apply an optional visual style.
- `scene-production` — produce user-defined standalone HTML scenes with Three.js or Canvas 2D. It includes two renderer workflow references and a Python standard-library structural validator.
- Modes described by the parent: standalone animation, modular film, and reusable character asset. **Only scene-production is presently packaged as an operational child skill**; character creation, source-video breakdown, modular film assembly and video export are *not* implemented as separate automatic capabilities in this release.

## Optional visual styles

| Skill | Style | Renderer approach |
| --- | --- | --- |
| `vidmindi` | Miniature Diorama | Three.js |
| `vidps2` | Retro PS2 | Three.js |
| `vidpixel` | Pixel Art | Canvas 2D |
| `vidcomic` | Comic Book | Canvas 2D |
| `vidbrick` | Toy Brick | Three.js |
| `vidclay` | Claymation | Three.js |
| `vidpaper` | Paper Cutout | Canvas 2D |
| `vidlowpoly` | Low-Poly 3D | Three.js |
| `vidriso` | Risograph | Canvas 2D |

Retro Anime 2D is retired and not distributed. All nine listed styles have previously been manually accepted in development fixtures; that is not a guarantee for arbitrary new scenes.

## Installation / use

Copy `.github/skills/` into the **root of your own Copilot CLI project**, preserving its nested files. Start the CLI in that project and run `copilot skill list` to verify discovery. If the host does not automatically load a skill, explicitly ask it to read `.github/skills/vskills/SKILL.md`, `.github/skills/scene-production/SKILL.md`, and the chosen optional style’s `SKILL.md`.

Example request: “Use TSA VSkills `scene-production` with `vidlowpoly` style to implement a Three.js HTML animation of a cable car traversing a mountain valley. Keep the scene content and duration I specified. Validate syntax, static structure and actual browser display separately.”

Aliases such as `/vidlowpoly` are prompt conventions, **not verified native CLI slash commands**.

## Validation

```bash
python3 .github/skills/scene-production/scripts/validate_scene.py --renderer threejs path/to/scene.html
python3 .github/skills/scene-production/scripts/validate_scene.py --renderer canvas2d path/to/scene.html
python3 -m http.server 8765 --bind 127.0.0.1
```

Structural checks do **not** prove browser rendering, visual quality or movement. Open the scene in a browser for acceptance. The `tests/fixtures/` folder provides optional development examples and regression references; none is a required input to create a new user-defined scene. Most Three.js fixtures use internet-hosted dependencies, so offline runtime support is not assured.

## Release boundary

This distribution contains the working skill instructions, renderer references, validator, and examples. It excludes pre-skill raw prompt collections, duplicate source protocols, experimental/retired visual attempts, working-state ledgers, and `.git` history. No scene-generation executable, MP4 exporter, native slash command registration, or universally proven character/film assembly pipeline is claimed.

## License

No license has been selected in the provided repository snapshot. Choose a license and check rights for content before public publication. Absence of a license does not automatically authorize reuse.

<div align="center">

# TSA VSkills

### Build browser-based 2D & 3D scenes with AI coding agents

**Main TSA production skill · Image-to-3D character workflow · Canonical character integration · Nine optional visual styles**

[Install](#-quick-start--install-di-github-AI Agent-cli) · [Core workflows](#-workflow-utama-tsa-vskills) · [Skill catalog](#-skill-yang-tersedia) · [Visual styles](#-contoh-penggunaan-di-AI Agent-cli) · [Combine](#-kombinasi-skill) · [Troubleshooting](#-troubleshooting)

</div>

---

> **TSA VSkills bukan hanya paket sembilan gaya visual.** `vskills` adalah skill utama untuk mengarahkan pekerjaan produksi visual berbasis browser. `scene-production` menangani implementasi HTML/Three.js/Canvas 2D; sembilan `vid*` adalah gaya tampilan opsional. Subjek, karakter, cerita, kamera, dan aksi tetap mengikuti instruksi pengguna.

## ✨ Highlights

- **Scene milik pengguna, bukan template tetap.** Jelaskan objek, lingkungan, aksi, kamera, durasi, dan hasil yang kamu inginkan.
- **True 3D or 2D.** Gunakan Three.js untuk geometri volumetrik 3D; Canvas 2D ketika memang sesuai dengan scene.
- **Image-to-3D character workflow.** Pengguna dapat memberikan PNG/JPG sebagai referensi visual untuk membuat karakter Three.js volumetrik, dengan wajah, mata, mulut, proporsi dan pivot yang dapat diperiksa. Ini workflow yang diarahkan `vskills`, **bukan child skill mandiri yang sudah divalidasi end-to-end**.
- **Canonical-source integration.** Ketika HTML karakter/model asli diberikan, agent harus membaca implementasi aktual dan mempertahankan geometri, hierarchy, material, wajah dan pivot—bukan membuat karakter yang sekadar mirip.
- **Scene-first workflow.** Produksi scene dengan satu kemampuan operasional dan, jika dibutuhkan, satu gaya visual utama.
- **Evidence-based validation.** Pemeriksaan source dan Python bukan pengganti browser, animasi, dan visual acceptance.
- **Examples included.** Fixture HTML di `tests/fixtures/` dapat dijadikan contoh dan pemeriksaan regresi.

**Cakupan dan batas rilis:** `vskills` adalah pengarah utama yang mencakup permintaan karakter, integrasi sumber karakter, dan produksi scene; `scene-production` adalah child skill implementasi HTML/Three.js/Canvas 2D yang tersedia. Pembuatan karakter 3D dari gambar dan integrasinya dapat diminta melalui prompt di bawah, tetapi **belum tersedia sebagai child skill khusus atau workflow end-to-end yang terbukti pada paket publik**. `vskills` juga menguraikan jalur modular film, video breakdown, dan scene assembly pada tingkat perencanaan. Tidak ada jaminan kualitas otomatis, MP4 export, atau visual PASS tanpa pengujian.

## 🔗 Official repository

- **GitHub:** https://github.com/amritsalahudin69/tsavskill/
- **HTTPS clone:** `https://github.com/amritsalahudin69/tsavskill.git`
- **SSH clone:** `git@github.com:amritsalahudin69/tsavskill.git`
- **GitHub CLI:** `gh repo clone amritsalahudin69/tsavskill`

## 🚀 Quick start — install di GitHub AI Agent CLI

**Persyaratan:** GitHub AI Agent CLI yang sudah terpasang dan login, Git, serta folder proyek tempat kamu ingin menggunakan skills. Untuk menjalankan preview dibutuhkan browser; Python 3 digunakan untuk validator yang disertakan.

### Opsi A — install menggunakan prompt agent + link GitHub

1. Buka terminal di **root proyek tujuan**, lalu jalankan `AI Agent` untuk masuk ke GitHub AI Agent CLI.
2. Tempel instruksi berikut **sebagai pesan biasa di sesi AI Agent CLI** (bukan perintah shell):

```text
Install TSA VSkills from this GitHub repository:
https://github.com/amritsalahudin69/tsavskill

Read the repository's README and inspect its .github/skills/ directories.
Install the complete vskills, scene-production, and nine vid* skills into
.github/skills/ in my CURRENT project, preserving each skill's nested
references and scripts. Do not alter unrelated existing skills or files.
If a target skill already exists, show the conflict before overwriting.
Do not install the project's test fixtures as skills.

After copying, reload skills with /skills reload if supported, then verify
with /skills list (or AI Agent skill list from the terminal). Check all 11
names: vskills, scene-production, vidmindi, vidps2, vidpixel, vidcomic,
vidbrick, vidclay, vidpaper, vidlowpoly, vidriso.

Report the actual files installed, exact destination, detected skills,
missing dependencies, and any commands you could not execute. Never claim
installation PASS without verifying the local files and discovery result.
```

> Memberikan **link GitHub saja tidak otomatis memasang skill**. Agent perlu menyalin direktori skill ke lokasi yang didukung, lalu memverifikasi discovery. Agent mungkin meminta persetujuan sebelum menjalankan shell command atau menimpa file.

### Opsi B — install manual (paling mudah diverifikasi)

Jalankan ini dari root **proyek tujuan** (Linux / macOS / WSL; contoh di bawah tidak menghapus skills lama):

```bash
# Clone the TSA VSkills repository using HTTPS.
git clone --depth 1 https://github.com/amritsalahudin69/tsavskill.git /tmp/tsa-vskills-source

# Review conflicts before copying; do not overwrite unrelated skills.
mkdir -p .github/skills
cp -nR /tmp/tsa-vskills-source/.github/skills/. .github/skills/

# Review copied files and ensure no required references/scripts are missing.
find .github/skills -name SKILL.md -print
```

`cp -nR` menghindari penggantian file yang sudah ada, tetapi pada direktori skill yang sudah ada kamu tetap perlu memeriksa apakah salinannya lengkap dan sesuai versi. Jika ada konflik, selesaikan secara eksplisit—jangan menganggap instalasi berhasil hanya dari hasil `cp`.

**Alternatif akses repository:** Pilih salah satu cara clone sesuai autentikasi yang tersedia (semua mengarah ke repository yang sama):

```bash
# HTTPS
git clone https://github.com/amritsalahudin69/tsavskill.git

# SSH (requires a configured GitHub SSH key)
git clone git@github.com:amritsalahudin69/tsavskill.git

# GitHub CLI (requires gh installed and authenticated)
gh repo clone amritsalahudin69/tsavskill
```

Jika ingin memasang skill ke proyek lain, salin folder `.github/skills/` dari hasil clone ke `.github/skills/` di proyek tujuan; jangan mengganti file proyek yang sudah ada tanpa pemeriksaan.

**Opsional:** Jika GitHub CLI `gh skill` tersedia dalam versi yang mendukung fitur preview, periksa `gh skill --help`, `gh skill preview amritsalahudin69/tsavskill <skill>`, dan `gh skill install --help`. Dukungan repositori dengan skill dalam direktori tersembunyi `.github/skills/` mungkin membutuhkan `--allow-hidden-dirs`. Alur manual di atas tetap dapat dipakai tanpa fitur preview ini.

### Verifikasi setelah install

**Di dalam AI Agent CLI:** 

```text
/skills reload
/skills list
/skills info vskills
/skills info scene-production
/skills info vidlowpoly
```

**Di terminal biasa, di root proyek yang sama:**

```bash
AI Agent skill list
```

Harus terdeteksi **11 skill project**: `vskills`, `scene-production`, dan sembilan gaya di bawah ini. Jika kurang, cek folder kerja, path `.github/skills/<name>/SKILL.md`, dan apakah file referensi di `scene-production/` ikut tersalin.

> `/skills` membuka pengelolaan skill di AI Agent CLI; `/skills list` menampilkan daftar. Perintah dan pengalaman UI bisa berbeda menurut versi CLI. Tidak ada kebutuhan untuk mendaftarkan alias shell `/vidlowpoly` secara terpisah.

## 🧩 Skill yang tersedia

### Core capabilities

| Skill | Peran | Contoh tugas |
|---|---|---|
| **`vskills`** | **Skill utama TSA**: routing kebutuhan karakter-dari-gambar, source canonical, scene, dan opsi style | Arahkan gambar → HTML karakter → scene animasi |
| **`scene-production`** | Membuat scene HTML yang berjalan dengan Three.js atau Canvas 2D; memandu implementasi dan validasi | Animasi truk RC melewati jalan berbatu |

### Nine optional visual styles

| Skill | Style | Karakter visual | Renderer lazim |
|---|---|---|---|
| `vidmindi` | **Miniature Diorama** | Dunia miniatur, set maket, skala kecil | Three.js |
| `vidps2` | **Retro PS2** | 3D era konsol awal 2000-an | Three.js |
| `vidpixel` | **Pixel Art** | Piksel tajam, sprite, palet terbatas | Canvas 2D |
| `vidcomic` | **Comic Book** | Garis tinta, halftone, warna komik | Canvas 2D |
| `vidbrick` | **Toy Brick** | Konstruksi balok mainan, plastik, stud | Three.js |
| `vidclay` | **Claymation** | Permukaan plastisin, nuansa stop motion | Three.js |
| `vidpaper` | **Paper Cutout** | Potongan kertas bertumpuk, puppet | Canvas 2D |
| `vidlowpoly` | **Low-Poly 3D** | Geometri faceted, flat shading, bentuk 3D | Three.js |
| `vidriso` | **Risograph** | Spot ink, grain, overprint, registrasi tinta | Canvas 2D |

**Retro Anime 2D tidak tersedia:** implementasi eksperimennya sudah dipensiunkan dan bukan bagian katalog aktif.

## 🎬 Workflow utama TSA VSkills

**Mulai dari tujuan pengguna, bukan dari pilihan visual style.** TSA VSkills dapat diarahkan untuk membuat karakter 3D, mengintegrasikan karakter yang sudah ada ke scene, dan menghasilkan animasi HTML. Sembilan `vid*` hanya opsi gaya tambahan. Karena paket ini belum memiliki `character-creation/SKILL.md`, contoh image-to-3D berikut adalah **prompt untuk `vskills` + `scene-production`**, bukan slash command atau fitur terpisah yang telah terbukti otomatis.

### A. Gambar PNG/JPG → karakter 3D Three.js

**Input:** simpan gambar referensi di proyek, misalnya `assets/characters/hero.png`. Gambar menetapkan identitas visual; satu gambar saja tidak membuktikan desain sisi belakang atau topologi tersembunyi.

**Prompt di dalam AI Agent CLI** (ubah path gambar sesuai proyek):

```text
Use the /vskills skill as the main TSA production guide.
Use /scene-production for Three.js implementation.

OBJECTIVE
Build a reusable, genuinely volumetric 3D character from:
assets/characters/hero.png

SOURCE OF TRUTH
Inspect the actual reference image. Preserve the observable silhouette,
head/body proportions, eye and mouth placement, facial features, colors,
clothing and distinctive details. Separate observed details from guesses
about unseen surfaces.

IMPLEMENTATION
Create actual Three.js meshes and materials, not a flat PNG billboard.
Organize named geometry groups and meaningful independent pivots for head,
arms and legs. Make eyes and mouth visible. Do not force a box-shaped body
when the image shows a different form.

OUTPUT
Create characters/hero.html as a reusable standalone inspection scene.
Show front, side and three-quarter views; keep the character source separable
from preview camera/stage and unrelated game code.

VALIDATION
Check dependencies, syntax, browser rendering when available, visible
3D volume, face, pivots and proportions. Report NOT_TESTED when a visual
or runtime check was not actually performed. Do not claim a perfect match.
Preserve unrelated project files.
```

**Output yang diminta:** `characters/hero.html` berisi model Three.js nyata dengan preview. **Acceptance wajib manual:** inspeksi depan/samping/3⁄4; pastikan mata dan mulut ada, tubuh tidak gepeng, anggota tubuh terhubung, pivot benar, tidak ada layar kosong. Validator struktural tidak cukup untuk membuktikan kemiripan gambar. Bila model tidak memadai, koreksi geometri dan hierarkinya sebelum memakai karakter dalam film/game.

### B. HTML karakter canonical → scene animasi baru

**Input:** HTML karakter yang benar-benar sudah diterima, misalnya `characters/hero.html`. File HTML ini—bukan sekadar screenshot—menjadi **canonical implementation source** untuk scene berikutnya.

```text
Use /vskills as the main production guide and /scene-production for Three.js.

CANONICAL CHARACTER SOURCE
characters/hero.html

Read the actual HTML/JavaScript source first. Identify and reuse the real
geometry, hierarchy, pivots, materials, colors, face details, proportions,
and existing animation capabilities. Do NOT recreate a lookalike from
an image, description, or memory. Keep the original source unchanged.

SCENE
Build scenes/hero-garden.html: the same character walks through a garden,
stops by a bench, waves and walks away. Duration 15 seconds, 16:9,
tracking camera, no HUD. Integrate the source character into one coherent
Three.js scene and timeline; animate existing pivots where possible.

VALIDATION
Inspect source reuse, geometry, motion, ground contact, browser runtime
and visual fidelity separately. If the source lacks a required articulation,
report the exact limitation instead of inventing a rig or replacing it.
```

**Perbedaan yang wajib dipahami:** dalam workflow A gambar menentukan **apa yang dibangun**; dalam workflow B HTML yang sudah ada menentukan **kode dan konstruksi karakter yang harus dipertahankan**. Mengganti model lama dengan model 'mirip' bukan integrasi canonical.

### C. Gambar → karakter HTML → scene dengan style opsional

Jalankan **A** dahulu dan terima hasil karakter. Baru jalankan **B**, dengan gaya lingkungan opsional. Contoh untuk karakter yang *sudah* lolos inspeksi:

```text
Use /vskills and /scene-production. Use /vidmindi as the single primary
visual style for the NEW environment.

Read characters/hero.html as canonical Three.js character source.
Reuse its real geometry, material identity, face and limb pivots; do not
replace or restyle the character without permission.

Build scenes/hero-miniature-village.html: the accepted character crosses
a tiny wooden bridge in a miniature village, with a slow tracking camera,
12-second animation, no UI. Keep source character unchanged.
Report actual syntax, browser, and visual checks separately.
```

**Kombinasi di atas adalah** `vskills` (arahan) + `scene-production` (implementasi) + **maksimal satu gaya visual utama**. `vidmindi` memandu gaya lingkungan, bukan izin mengubah identitas canonical karakter. Tidak ada klaim bahwa semua gaya 2D kompatibel langsung dengan karakter Three.js volumetrik.

### D. Memeriksa hasil di browser

Jalankan dari root proyek:

```bash
python3 -m http.server 8765 --bind 127.0.0.1
```

Buka `http://localhost:8765/characters/hero.html` untuk inspeksi karakter atau `http://localhost:8765/scenes/hero-garden.html` untuk scene. Gunakan Console browser untuk memastikan modul dan aset termuat. Jika output merupakan scene animasi Three.js yang memenuhi kontrak validator, periksa pula:

```bash
python3 .github/skills/scene-production/scripts/validate_scene.py \
  --renderer threejs scenes/hero-garden.html
```

**Status kejujuran:** prompt di bagian ini menjelaskan cara **meminta** workflow, bukan bukti bahwa setiap agent dapat merekonstruksi karakter 3D berkualitas dari setiap gambar. Hasilnya tetap membutuhkan inspeksi dan revisi visual.

---

## 💬 Contoh penggunaan di AI Agent CLI

Setelah skill terdeteksi, ketik **prompt berikut di sesi AI Agent CLI**. Bentuk `Use the /skill-name skill ...` merujuk skill bernama itu; ini **bukan** perintah shell dan tidak menjamin setiap versi host menyediakan slash command mandiri untuk tiap skill.

### 3D compiler

| Kemampuan utama             | Panduan baru                                                         |
| --------------------------- | -------------------------------------------------------------------- |
| Image → 3D Character        | Cara menggunakan PNG/JPG untuk membuat model Three.js volumetrik     |
| 3D Character → HTML         | Membuat karakter mandiri dengan mata, mulut, tubuh 3D, dan pivot     |
| Canonical Character → Scene | Menggunakan implementasi HTML karakter asli tanpa membangun ulang    |
| Character + Visual Style    | Menggabungkan karakter yang sudah diterima dengan gaya opsional      |
| Validation                  | Cara menjalankan HTML, memeriksa wajah, geometri, pivot, dan animasi |

Setiap workflow sudah memiliki contoh prompt Copilot CLI siap salin.

### 1. Membuat karakter dari gambar
```text
Use /vskills and /scene-production.

Build a reusable volumetric Three.js character
from assets/characters/hero.png.

Preserve the actual facial features, eyes, mouth,
body proportions, costume, colors and details.

Create characters/hero.html with front, side
and three-quarter inspection views.
```

### 2. Menggunakan karakter dalam scene
```text
Use /vskills and /scene-production.

Read characters/hero.html as the canonical source.
Reuse its real geometry, hierarchy, materials
and articulation. Do not create a lookalike.

Build a 15-second Three.js garden scene with
the character walking, stopping and waving.
```

### 3. Menambahkan gaya visual
```text
Use /vskills, /scene-production and /vidmindi.

Preserve the canonical character from
characters/hero.html.

Build a miniature village environment and
animate the same character crossing a bridge.
```

###
```text

```

----------------------------------------------------------------------------------------------------------------
### 1. Gunakan skill utama tanpa menentukan gaya

```text
Use the /vskills skill. I want to create a standalone browser animation:
a small RC dump truck carries sand over a rocky mountain road.
Plan the appropriate production operation, preserve the scene brief,
then use /scene-production to implement one runnable Three.js HTML.
Duration: 15 seconds. Camera: low tracking shot. No HUD or captions.
Report actual source, runtime, and visual validation separately.
```

### 2. Miniature Diorama

```text
Use the /scene-production and /vidmindi skills.
Build a 12-second Three.js HTML animation of a miniature red train
crossing a tiny wooden bridge in a mountain village. Warm afternoon
lighting; camera slowly pushes in; no overlay. Deliver the HTML file.
```

### 3. Retro PS2

```text
Use the /scene-production and /vidps2 skills.
Create a 10-second early-2000s console-style 3D scene of a courier
riding a scooter through a coastal city. Use a third-person follow
camera, simple fog, low-resolution game-like materials. Output HTML.
```

### 4. Pixel Art

```text
Use the /scene-production and /vidpixel skills.
Create an 8-second Canvas 2D animation of a fox jumping across
stepping stones in a river. Crisp nearest-neighbor pixels, parallax
clouds, and a looping jump. Output a standalone HTML file.
```

### 5. Comic Book

```text
Use the /scene-production and /vidcomic skills.
Animate a bicycle messenger entering a busy city intersection in a
comic-book style, with bold outlines and halftone shadows. 10 seconds,
landscape 16:9, no text balloons. Output HTML.
```

### 6. Toy Brick

```text
Use the /scene-production and /vidbrick skills.
Create a Three.js construction scene in which a toy-brick crane lifts
and places a large block onto a small building. 12 seconds, clear
mechanical movement, soft studio lighting. Output HTML.
```

### 7. Claymation

```text
Use the /scene-production and /vidclay skills.
Create a 10-second claymation-style scene of a small turtle delivering
a letter through a garden. Handmade clay appearance, gentle stop-motion
movement, coherent ground contact. Output HTML.
```

### 8. Paper Cutout

```text
Use the /scene-production and /vidpaper skills.
Create a layered paper-cutout forest with a deer walking behind trees,
subtle paper shadows and moving clouds. 12 seconds, Canvas 2D, 16:9.
Output HTML.
```

### 9. Low-Poly 3D

```text
Use the /scene-production and /vidlowpoly skills.
Create a Three.js cable car traveling between two mountain stations.
Show a mechanically plausible cable/hanger connection, smooth
acceleration and deceleration, clear docking, and readable terrain.
15 seconds. Output a runnable HTML animation.
```

### 10. Risograph

```text
Use the /scene-production and /vidriso skills.
Create a 10-second Canvas 2D scene of a lighthouse signaling to a
sailboat in a coastal landscape. Limit the print to four ink colors,
with subtle halftone, grain and fixed registration offsets. Output HTML.
```

## 🔀 Kombinasi skill

**Kombinasi yang didukung secara desain:** satu *operation capability* + **nol atau satu primary visual style**, dikoordinasikan oleh `vskills` bila diperlukan. Ini bukan mencampur sembilan gaya menjadi satu efek. Contoh:

```text
Use the /vskills skill as the production guide.
Use /scene-production for implementation and /vidlowpoly as the ONLY
primary visual style.

Make a standalone 15-second Three.js scene: a yellow RC dump truck
climbs a winding hill while a second RC trailer waits near the summit.
The world should use low-poly faceted terrain and coherent physics-like
acceleration. Camera tracks from 3 meters in front of the lead truck.
No UI, titles, timer, or subtitles. Keep all objects visibly 3D.
Deliver runnable HTML and report what was actually browser-tested.
```

Untuk memakai **karakter HTML canonical milik sendiri**:

```text
Use /vskills and /scene-production, with /vidclay as the primary style.
Read the supplied character HTML source FIRST. Preserve its actual
geometry, hierarchy, facial identity, materials and limb pivots.
Integrate that implementation into a new Three.js garden scene.
Do NOT replace the character with a lookalike or a flat image.
If the supplied source cannot support the motion, explain the limitation.
```

Tidak ada klaim bahwa `vskills` memiliki mesin gabung otomatis atau bahwa dua visual style (`vidpixel` + `vidlowpoly`, misalnya) dapat dipadukan secara konsisten. **Multi-style blending** perlu spesifikasi tersendiri dan pengujian; jangan diasumsikan didukung.

## 🛠 Validasi hasil scene

Dari root proyek yang sudah memasang `scene-production`:

```bash
# For a Three.js HTML scene
python3 .github/skills/scene-production/scripts/validate_scene.py \
  --renderer threejs path/to/scene.html

# For a Canvas 2D HTML scene
python3 .github/skills/scene-production/scripts/validate_scene.py \
  --renderer canvas2d path/to/scene.html

# Preview with a local server, from the directory containing your output
python3 -m http.server 8765 --bind 127.0.0.1
```

Buka `http://localhost:8765/` dan arahkan ke file HTML yang dibuat. Uji **awal, tengah, dan akhir** animasi; periksa Console browser untuk kesalahan JavaScript, asset atau modul. HTTP `200` dan Python `PASS` **tidak membuktikan** bahwa scene berhasil dirender atau animasinya bagus. File statis tanpa animation loop juga mungkin tidak memenuhi validator yang memang ditujukan untuk scene bergerak.

## 📁 Struktur repository

```text
.github/skills/
├── vskills/SKILL.md                 # Main TSA orchestration skill
├── scene-production/
│   ├── SKILL.md
│   ├── references/                 # Three.js & Canvas 2D workflows
│   └── scripts/validate_scene.py   # Structural validator
├── vidmindi/SKILL.md
├── vidps2/SKILL.md
├── vidpixel/SKILL.md
├── vidcomic/SKILL.md
├── vidbrick/SKILL.md
├── vidclay/SKILL.md
├── vidpaper/SKILL.md
├── vidlowpoly/SKILL.md
└── vidriso/SKILL.md

tests/fixtures/                      # Optional examples/regression fixtures
README.md
```

Fixture bukan input wajib. Saat memasang skills ke proyek lain, cukup salin `.github/skills/` beserta dependensinya. Beberapa contoh Three.js memuat library dari CDN; browser mungkin memerlukan akses internet.

## 🩺 Troubleshooting

| Masalah | Langkah yang perlu dicek |
|---|---|
| Tidak muncul di `/skills list` | Jalankan `/skills reload`, pastikan CLI berjalan dari root proyek yang benar dan file berada di `.github/skills/<name>/SKILL.md`. |
| Hanya 9 skills muncul | Periksa apakah `vskills` dan `scene-production` ikut dipasang; total paket adalah **11 project skills**. |
| `/vidlowpoly` tidak dikenali sebagai perintah | Gunakan prompt `Use the /vidlowpoly skill ...`; jangan menganggap alias sebagai shell command. |
| Agent tidak mengikuti style | Sebutkan nama skill secara eksplisit dan pastikan `SKILL.md` tersedia serta skill aktif. |
| Browser blank / WebGL gagal | Periksa Console, jalankan local HTTP server, verifikasi import Three.js, path asset dan modul. |
| Validator Python PASS, animasi buruk | Lakukan penilaian visual manual. Validator struktural tidak menilai kualitas estetika atau kontinuitas gerak. |
| Output hanya deskripsi, bukan HTML | Minta agent membuat file HTML nyata dan melaporkan path yang terverifikasi; jangan terima klaim file dibuat tanpa bukti. |
| Instalasi menimpa skill lain | Review konflik; jangan menjalankan overwrite otomatis terhadap proyek pengguna. |

## 📚 Referensi resmi GitHub AI Agent CLI

- [Adding agent skills for GitHub AI Agent CLI](https://docs.github.com/en/AI Agent/how-tos/AI Agent-cli/customize-AI Agent/add-skills)
- [GitHub AI Agent CLI commands (`/skills`)](https://docs.github.com/en/AI Agent/reference/AI Agent-cli-reference/cli-command-reference)
- [GitHub CLI `gh skill install` (preview)](https://cli.github.com/manual/gh_skill_install)

## 📌 Project status and release notes

- **Main skill:** `vskills` — instruction-based production guidance and capability selection.
- **Operational child:** `scene-production` — HTML scene implementation using Three.js / Canvas 2D.
- **Visual children:** nine optional styles, accepted on their development fixtures. New scenes still require validation.
- **Not packaged as separately verified standalone capabilities:** automatic image-to-3D character generation, video source breakdown, full multi-scene film assembly, MP4 encoding/export, or automated visual approval. The character workflows above are guided production requests and must be individually validated.
- **License:** no license was present in the supplied snapshot. Repository ownership and reuse permissions should be clarified before an open-source release.

---

<div align="center">

**TSA VSkills — your scene, your characters, your direction.**

*Pick a production operation. Add a visual style if you want one. Verify the result in the browser.*

</div>

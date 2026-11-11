<div align="center">

# TSA VSkills

### Build browser-based 2D & 3D scenes with AI coding agents

**One production workflow · Nine optional visual styles · User-defined stories and characters**

[Getting started](#-quick-start--install-di-github-copilot-cli) · [Skill catalog](#-skill-yang-tersedia) · [CLI examples](#-contoh-penggunaan-di-copilot-cli) · [Combine skills](#-kombinasi-skill) · [Troubleshooting](#-troubleshooting)

</div>

---

> **TSA VSkills bukan hanya paket sembilan gaya visual.** `vskills` adalah skill utama untuk mengarahkan pekerjaan produksi visual berbasis browser. `scene-production` menangani implementasi HTML/Three.js/Canvas 2D; sembilan `vid*` adalah gaya tampilan opsional. Subjek, karakter, cerita, kamera, dan aksi tetap mengikuti instruksi pengguna.

## ✨ Highlights

- **Scene milik pengguna, bukan template tetap.** Jelaskan objek, lingkungan, aksi, kamera, durasi, dan hasil yang kamu inginkan.
- **True 3D or 2D.** Gunakan Three.js untuk geometri volumetrik 3D; Canvas 2D ketika memang sesuai dengan scene.
- **Canonical-source aware.** Ketika HTML karakter/model asli diberikan, agent diminta membaca implementasi aktual dan menjaga identitas serta konstruksinya; bukan membuat karakter yang sekadar mirip.
- **Scene-first workflow.** Produksi scene dengan satu kemampuan operasional dan, jika dibutuhkan, satu gaya visual utama.
- **Evidence-based validation.** Pemeriksaan source dan Python bukan pengganti browser, animasi, dan visual acceptance.
- **Examples included.** Fixture HTML di `tests/fixtures/` dapat dijadikan contoh dan pemeriksaan regresi.

**Batas kemampuan rilis ini:** `scene-production` adalah child skill operasional yang sudah dikemas. `vskills` juga menjelaskan mode *standalone animation*, *modular film*, dan *character asset*, serta rute konseptual untuk character creation, video breakdown, integrasi canonical character, dan scene assembly. Itu **belum berarti** semua operasi tersebut tersedia sebagai child skill otomatis terpisah. Tidak ada klaim bahwa paket ini otomatis menghasilkan MP4 atau menjamin kualitas visual setiap scene.

## 🔗 Official repository

- **GitHub:** https://github.com/amritsalahudin69/tsavskill/
- **HTTPS clone:** `https://github.com/amritsalahudin69/tsavskill.git`
- **SSH clone:** `git@github.com:amritsalahudin69/tsavskill.git`
- **GitHub CLI:** `gh repo clone amritsalahudin69/tsavskill`

## 🚀 Quick start — install di GitHub Copilot CLI

**Persyaratan:** GitHub Copilot CLI yang sudah terpasang dan login, Git, serta folder proyek tempat kamu ingin menggunakan skills. Untuk menjalankan preview dibutuhkan browser; Python 3 digunakan untuk validator yang disertakan.

### Opsi A — install menggunakan prompt agent + link GitHub

1. Buka terminal di **root proyek tujuan**, lalu jalankan `copilot` untuk masuk ke GitHub Copilot CLI.
2. Tempel instruksi berikut **sebagai pesan biasa di sesi Copilot CLI** (bukan perintah shell):

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
with /skills list (or copilot skill list from the terminal). Check all 11
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

**Di dalam Copilot CLI:** 

```text
/skills reload
/skills list
/skills info vskills
/skills info scene-production
/skills info vidlowpoly
```

**Di terminal biasa, di root proyek yang sama:**

```bash
copilot skill list
```

Harus terdeteksi **11 skill project**: `vskills`, `scene-production`, dan sembilan gaya di bawah ini. Jika kurang, cek folder kerja, path `.github/skills/<name>/SKILL.md`, dan apakah file referensi di `scene-production/` ikut tersalin.

> `/skills` membuka pengelolaan skill di Copilot CLI; `/skills list` menampilkan daftar. Perintah dan pengalaman UI bisa berbeda menurut versi CLI. Tidak ada kebutuhan untuk mendaftarkan alias shell `/vidlowpoly` secara terpisah.

## 🧩 Skill yang tersedia

### Core capabilities

| Skill | Peran | Contoh tugas |
|---|---|---|
| **`vskills`** | **Induk / orchestrator**: memahami mode produksi, memilih operasi, menjaga scene dan source canonical, mengarahkan opsi style | Pilih workflow untuk video HTML dari karakter yang sudah ada |
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

## 💬 Contoh penggunaan di Copilot CLI

Setelah skill terdeteksi, ketik **prompt berikut di sesi Copilot CLI**. Bentuk `Use the /skill-name skill ...` merujuk skill bernama itu; ini **bukan** perintah shell dan tidak menjamin setiap versi host menyediakan slash command mandiri untuk tiap skill.

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

## 📚 Referensi resmi GitHub Copilot CLI

- [Adding agent skills for GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/add-skills)
- [GitHub Copilot CLI commands (`/skills`)](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference)
- [GitHub CLI `gh skill install` (preview)](https://cli.github.com/manual/gh_skill_install)

## 📌 Project status and release notes

- **Main skill:** `vskills` — instruction-based production guidance and capability selection.
- **Operational child:** `scene-production` — HTML scene implementation using Three.js / Canvas 2D.
- **Visual children:** nine optional styles, accepted on their development fixtures. New scenes still require validation.
- **Not packaged as automatic standalone capabilities:** video source breakdown, full character-generation pipeline, multi-scene film assembly, MP4 encoding/export, or automated visual approval.
- **License:** no license was present in the supplied snapshot. Repository ownership and reuse permissions should be clarified before an open-source release.

---

<div align="center">

**TSA VSkills — your scene, your characters, your direction.**

*Pick a production operation. Add a visual style if you want one. Verify the result in the browser.*

</div>

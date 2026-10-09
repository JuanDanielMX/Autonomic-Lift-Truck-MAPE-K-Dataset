# Minimal Dataset — MAPE-K Autonomic Intralogistics Mobile Robot

GitHub-ready minimal dataset and reproducibility package for manuscript **machines-4629373**, *Bridging Smart Factory and Industry 5.0: A MAPE-K Autonomic Intralogistics Mobile Robot*.

## Purpose

This package consolidates the project data, software, experimental media, and reproducibility materials supporting the central findings of the manuscript. The repository distinguishes only between **project-owned materials** and **third-party dependencies**. Third-party source code is not presented as project-owned work.

## Data Availability Statement

> The raw data supporting the conclusions of this article will be made available by the authors on request.

This repository provides the minimal supporting dataset requested during editorial processing and is publicly hosted on GitHub for dissemination.

## Repository structure

```text
.
├── README.md
├── DATASET_MANIFEST.csv
├── CITATION.cff
├── SHA256SUMS.txt
├── data/
│   ├── literature_review/
│   └── experimental/
├── evidence/
│   ├── videos/
│   ├── previews/
│   └── online/
├── node-red/
├── analysis/
├── software/
│   └── project/
└── docs/
```

## What is included

### Literature-review support

- Documented search strings for Scopus, Web of Science, and IEEE Xplore.
- Machine-readable project mappings corresponding to manuscript Tables 2–4.

### Self-Configuration

- RViz mapping demonstration video.
- Project mapping scripts.
- Full online project demonstration video.
- Third-party RRT/SLAM dependencies are identified separately and are not copied into the repository as project-owned code.

### Self-Healing

- Dashboard demonstrations showing speed and green/red alert states.
- Node-RED logic using the project Boolean rule:

```text
StatusAlert = A AND NOT B
```

where `A` is the odometry-derived Boolean condition and `B` is the scan/LiDAR-derived Boolean condition.
- Full online project demonstration video.

### Self-Optimization

- Machine-readable Table 6 values for the 10 paired experimental runs.
- Verification script reproducing the means, approximately 12.4% relative improvement, paired t-statistic, p-value, and 95% confidence interval.
- Two dashboard videos.
- Node-RED speed law:

```text
Sf = 0.02 + 0.02 B
```

- Full online project demonstration video.

### Self-Protection

- SLAM/obstacle-avoidance video.
- Machine-readable Table 7 original/encrypted/decrypted validation examples.
- Node-RED AES-256-CBC encryption/decryption implementation.
- Full online project demonstration video.
- **The project passkey is not distributed.** For repository/testing use, the AES flow reads a replacement 32-byte key from the `AES_KEY` environment variable.

## Full online project videos

- **Self-Configuration:** https://www.youtube.com/watch?v=UP7f2WfFX3w
- **Self-Healing:** https://www.youtube.com/watch?v=N2gSVEovKTU
- **Self-Optimization:** https://www.youtube.com/watch?v=NeClK5fzg9U
- **Self-Protection:** https://www.youtube.com/watch?v=GViusdlDCVo

The same links are provided in `evidence/online/README.md` and `data/experimental/online_video_links.csv`.

## Verify the Self-Optimization statistics

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r analysis/requirements.txt
python analysis/verify_self_optimization.py
```

Expected values are approximately:

```text
fixed mean = 25.9 min
modulated mean = 29.1 min
mean difference = 3.2 min
relative improvement = 12.4%
t(9) = 5.58
p ≈ 0.00034
95% CI ≈ 1.90 to 4.50 min
```

## Node-RED

Import `node-red/flows.json` and read `node-red/README.md` before running it. The MQTT broker is configured as `localhost:1883` by default and should be changed for the target environment.

For repository/testing use, configure a fresh random 32-byte AES key in the environment. The flow has no embedded/default key and rejects a missing or incorrectly sized value:

```bash
export AES_KEY="$(openssl rand -hex 16)"
```

## Ownership and third-party dependencies

All bundled project data, scripts, flows, media, analysis files, and documentation are treated as project-owned materials. Third-party software dependencies are listed separately in `software/THIRD_PARTY.md` and should be obtained from their original sources under their corresponding licenses.

See also:

- `docs/PROJECT_NOTES.md`
- `docs/EVIDENCE_MAP.md`
- `DATASET_MANIFEST.csv`

## License

Project-owned research data, CSV files, documentation, figures, images, and experimental media are licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Project-developed software in `analysis/`, `node-red/`, and `software/project/` is licensed under the MIT License; each directory contains the complete MIT license text in `LICENSE`. Documentation and CSV files in those directories remain under CC BY 4.0.

Third-party dependencies retain their respective licenses and are not relicensed. See [LICENSE.md](LICENSE.md) for the complete licensing structure and [software/THIRD_PARTY.md](software/THIRD_PARTY.md) and [software/DEPENDENCIES.csv](software/DEPENDENCIES.csv) for dependency information.

## Authors

Juan Daniel Marín-Segura; Luis Antonio Carrillo-Martinez; Debbie Hernández; Froylan Cortes-Santacruz; Jesus Anselmo Fortoul-Diaz.

## Manuscript

Manuscript ID: `machines-4629373`

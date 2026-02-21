# models-cellcycle

Curated collection of **cell cycle** simulation models for the **biosim** platform. This repository contains comprehensive computational models of cell cycle regulation, including G1/S and G2/M transitions, checkpoint control, cyclin-CDK dynamics, and cell cycle oscillators across yeast and mammalian systems.

## What's Inside

### Models (64 packages)

Each model is a self-contained simulation component with a `model.yaml` manifest.

**Cell Cycle** — molecular regulation of cell division, checkpoints, and cell cycle progression:

#### Classic Cell Cycle Models
- `cellcycle-sbml-tyson1991-cell-cycle-2-var` — Classic 2-variable Tyson cell cycle model
- `cellcycle-sbml-tyson1991-cell-cycle-6-var` — Extended 6-variable Tyson cell cycle model
- `cellcycle-sbml-novak1993-cell-cycle-m-phase-control` — M-phase control mechanisms
- `cellcycle-sbml-novak1997-cell-cycle` — Comprehensive Novak cell cycle model
- `cellcycle-sbml-gardner1998-cell-cycle-goldbeter` — Goldbeter's minimal cascade model
- `cellcycle-sbml-norel1990-mpf-and-cyclin-oscillations` — MPF and cyclin oscillatory dynamics

#### Mammalian Cell Cycle Models
- `cellcycle-sbml-csikasz-nagy2006-mammalian-cell-cycle-model` — Integrated mammalian cell cycle regulation
- `cellcycle-sbml-gerard2009-an-integrated-mammalian-cell-cycle-mo` — Comprehensive mammalian cell cycle model
- `cellcycle-sbml-gerard2010-progression-of-mammalian-cell-cycle-b` — Mammalian cell cycle progression
- `cellcycle-sbml-abroudi2017-mammalian-cell-cycle-control-model` — Modern mammalian control network
- `cellcycle-sbml-weis2014-data-driven-mammalian-cell-cycle-model` — Data-driven mammalian model
- `cellcycle-sbml-traynard2016-mammalian-cell-cycle-regulation-log` — Logical model of mammalian regulation

#### Yeast Cell Cycle Models
- `cellcycle-sbml-chen2000-cellcycle` — Budding yeast cell cycle dynamics
- `cellcycle-sbml-chen2004-cell-cycle-regulation` — Yeast cell cycle regulatory network
- `cellcycle-sbml-kaizu2010-buddingyeastcellcycle-map` — Comprehensive budding yeast MAP model
- `cellcycle-sbml-li2008-caulobacter-cell-cycle` — Caulobacter cell cycle control
- `cellcycle-sbml-li2009-assymetric-caulobacter-cell-cycle` — Asymmetric Caulobacter division
- `cellcycle-sbml-novak1998-mathematical-model-of-fission-yeast-ce` — Fission yeast cell cycle
- `cellcycle-sbml-muenzner2019-yeast-cell-cycle-control-network` — Updated yeast control network

#### G1/S Transition Models
- `cellcycle-sbml-bai2003-g1phaseregulation` — G1 phase regulatory mechanisms
- `cellcycle-sbml-barr2016-all-or-nothing-g1-s-transition` — Bistable G1/S switch
- `cellcycle-sbml-swat2004-mammalian-g1-s-transition` — Mammalian restriction point control
- `cellcycle-sbml-chiorino2002-g1-s-transition-model` — G1/S transition dynamics
- `cellcycle-sbml-hatzimanikatis1999-regulation-of-the-g1-s-transi` — G1/S regulatory network
- `cellcycle-sbml-kollarovic2016-cell-fate-decision-at-g1-s-transi` — Cell fate decisions at G1/S
- `cellcycle-sbml-novak2004-a-model-for-restriction-point-control` — Restriction point model
- `cellcycle-sbml-dong2018-e2f-dynamics-in-g1-phase` — E2F transcription factor dynamics

#### Checkpoint Control Models
- `cellcycle-sbml-aguda1999-g2-dna-damage-checkpoint` — G2 DNA damage checkpoint activation
- `cellcycle-sbml-ibrahim2008-mitotic-spindle-assembly-checkpoint` — Spindle assembly checkpoint (SAC)
- `cellcycle-sbml-ciliberto2003-morphogenesis-checkpoint` — Morphogenesis checkpoint in yeast
- `cellcycle-sbml-caydasi2012-inhibition-of-tem1-by-the-gap-comple` — Tem1 GAP complex regulation
- `cellcycle-sbml-caydasi2012-regulation-of-tem1-by-the-gap-comple` — Tem1 checkpoint regulation

#### CDK-Cyclin Dynamics
- `cellcycle-sbml-morris2002-cellcycle-cdk2cyclin` — CDK2-cyclin oscillations
- `cellcycle-sbml-ciliberto2003-cycline-cdk2-timer-in-the-cell-cyc` — CDK2 timer mechanism
- `cellcycle-sbml-ferrel2011-cdk1-and-apc-regulation-in-cell-cycle` — CDK1 and APC/C regulation
- `cellcycle-sbml-ferrel2011-autonomous-biochemical-oscillator-in` — Autonomous CDK oscillator
- `cellcycle-sbml-pomerening2005-model-of-the-xenopus-cdc2-apc-sys` — Xenopus Cdc2-APC system

#### Environmental Response & Adaptation
- `cellcycle-sbml-bedessem2014-hif-1-a-mediated-response-to-hypoxi` — HIF-1α hypoxia response
- `cellcycle-sbml-zhang2018-cell-cycle-commitment-in-hypoxia` — Cell cycle commitment under hypoxia
- `cellcycle-sbml-jaiswal2017-cell-cycle-arrest` — Cell cycle arrest mechanisms
- `cellcycle-sbml-moreno2019-stochastic-model-of-g1-arrest-due-to` — Stochastic G1 arrest model
- `cellcycle-sbml-barrack2014-calcium-cell-cycle-coupling-cyclin-d` — Calcium-cell cycle coupling (cyclin D)
- `cellcycle-sbml-barrack2014-calcium-cell-cycle-coupling-rs-depen` — Calcium-cell cycle coupling (RS-dependent)

#### Size & Growth Control
- `cellcycle-sbml-model-of-budding-yeast-critical-cell-size-depend` — Critical cell size control
- `cellcycle-sbml-conradie2010-rpcontrol-cellcycle` — Ribosomal protein control
- `cellcycle-sbml-tsai2014-cell-cycle-duration-control-by-oscillat` — Duration control by oscillators

#### Specialized & Disease Models
- `cellcycle-sbml-sizek2023-mitochondrial-dysfunction-associated-s` — Mitochondrial dysfunction and senescence
- `cellcycle-sbml-lang2024-cell-cycle-model-explains-compartment-r` — Compartment-resolved cell cycle model
- `cellcycle-sbml-deboeck2021-modular-approach-to-modeling-the-cel` — Modular cell cycle framework
- `cellcycle-sbml-henze2017-a-dynamical-model-for-activating-and-s` — Activating and silencing dynamics

**Note:** This repository contains 64 models total. The above represents key categories and examples. For a complete list, see the `models/` directory.

## Layout

```
models-cellcycle/
├── models/<model-slug>/     # One model package per folder, each with model.yaml
├── libs/                    # Shared helper code for curated models
├── templates/model-pack/    # Starter template for new model packs
├── scripts/                 # Manifest and entrypoint validation scripts
├── docs/                    # Governance documentation
└── .github/workflows/       # CI/CD pipeline
```

## How It Works

### Model Interface

Every model implements the `biosim.BioModule` interface:

- **`inputs()`** — declares named input signals the module consumes
- **`outputs()`** — declares named output signals the module produces
- **`advance_to(t)`** — advances the model's internal state to time `t`

Most curated models include Python source under `src/` and are wired together via `space.yaml` in composed simulations without additional code.

### Model Standards

All models in this repository:
- Use SBML (Systems Biology Markup Language) format
- Are sourced from BioModels and other curated repositories
- Include tellurium runtime for SBML execution
- Provide `state` output for monitoring simulation results
- Support configurable timesteps via `min_dt` parameter

### Running Models

Models are loaded and executed by the `biosim-platform`. The platform reads `model.yaml`, instantiates the model from its entrypoint, and runs the simulation loop at the configured timestep for the specified duration.

Individual models can be integrated into larger composed simulations by wiring their outputs to other models' inputs, enabling multi-scale cellular modeling.

## Getting Started

### Prerequisites

- Python 3.11+
- `biosim` framework

### Install biosim

```bash
pip install "biosim @ git+https://github.com/BioSimulant/biosim.git@main"
```

### Create a New Model

1. Copy `templates/model-pack/` to `models/<your-model-slug>/`
2. Edit `model.yaml` with metadata, entrypoint, and pinned dependencies
3. Implement your module (subclass `biosim.BioModule` or use a built-in pack)
4. Add cell cycle-specific tags and categorization
5. Validate: `python scripts/validate_manifests.py && python scripts/check_entrypoints.py`

### Using Models in Spaces

To integrate cell cycle models into larger simulations:

1. Reference models by `manifest_path` (e.g., `models/cellcycle-sbml-tyson1991-cell-cycle-6-var/model.yaml`)
2. Wire model outputs to inputs of other models in your space configuration
3. Compose multi-scale simulations combining cell cycle with metabolism, signaling, or gene regulation
4. Configure runtime parameters and simulation duration

## Linking in biosim-platform

- Models can be linked with explicit paths:
  - `models/cellcycle-sbml-gerard2009-an-integrated-mammalian-cell-cycle-mo/model.yaml`
- Models can be composed with other domain models (signaling, metabolism, etc.) in multi-scale simulations

## External Repos

External authors can keep models in independent repositories and link them directly in `biosim-platform`. This repository is curated, not exclusive.

## Validation & CI

Three scripts enforce repository integrity on every push:

| Script | Purpose |
|--------|---------|
| `scripts/validate_manifests.py` | Schema validation for all model.yaml files |
| `scripts/check_entrypoints.py` | Verifies Python entrypoints are importable and callable |
| `scripts/check_public_boundary.sh` | Prevents business-sensitive content in this public repo |

The CI pipeline (`.github/workflows/ci.yml`) runs: **secret scan** → **manifest validation** → **smoke sandbox** (Docker).

## Contributing

- All dependencies must use exact version pinning (`==`)
- Model slugs use kebab-case with domain prefix (`cellcycle-sbml-`)
- Models must follow the `biosim.BioModule` interface
- SBML models use tellurium runtime for execution
- Pre-commit hooks enforce trailing whitespace, EOF newlines, YAML syntax, and secret detection
- See [docs/PUBLIC_INTERNAL_BOUNDARY.md](docs/PUBLIC_INTERNAL_BOUNDARY.md) for content policy

## Domain-Specific Notes

**Cell Cycle Focus Areas:**
- **Classic Models**: Foundational models from Tyson, Novak, Goldbeter establishing oscillatory dynamics
- **G1/S Transition**: Restriction point control, E2F dynamics, and commitment to division
- **G2/M Transition**: Entry into mitosis, CDK1 activation, and checkpoint control
- **Checkpoint Control**: DNA damage, spindle assembly, morphogenesis checkpoints
- **CDK-Cyclin Oscillators**: Autonomous biochemical oscillators driving cell cycle progression
- **Organism-Specific Models**: Yeast (budding/fission), mammalian, Xenopus, Caulobacter systems
- **Environmental Coupling**: Hypoxia, stress, calcium signaling effects on cell cycle
- **Size & Growth Control**: Critical cell size, ribosomal protein regulation, growth-division coupling

**Common Model Types:**
- Ordinary differential equation (ODE) models of regulatory networks
- Bistable switches and hysteresis in cell cycle transitions
- Limit cycle oscillators for autonomous cell cycle progression
- Stochastic models of checkpoint activation and cell fate decisions
- Modular frameworks combining multiple cell cycle phases

## License

This repository is dual-licensed:

- **Code** (scripts, templates, Python modules): Apache-2.0 (`LICENSE-CODE.txt`)
- **Model/content** (manifests, docs, wiring/config): CC BY 4.0 (`LICENSE-CONTENT.txt`)

Attribution guidance: `ATTRIBUTION.md`

# ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2 Lab

Single-model lab wrapper for ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2. Computational modeling and the theory of nonlinear dynamical systems allow one to not simply describe the events of the cell cycle, but also to understand why these events occur, just as the theory of. It can be used to explore cell-cycle regulation dynamics and compare checkpoint behavior across conditions.

This lab is a single-model Biosimulant wrapper for a cell-cycle simulation. The captured run uses the lab defaults and renders the model outputs as dark-mode visualizations for quick inspection and README embedding.

## Model Context

Computational modeling and the theory of nonlinear dynamical systems allow one to not simply describe the events of the cell cycle, but also to understand why these events occur, just as the theory of. It can be used to explore cell-cycle regulation dynamics and compare checkpoint behavior across conditions.

- Core model: ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2
- Runtime used by the lab: duration 10, step 1
- Controllable inputs: none declared
- Primary outputs: CDK1 Active
- Tags: cellcycle, sbml, biomodels_ebi, faithful

## Output Visualizations

The images below were generated from a Biosimulant lab run in dark mode. Each capture corresponds to one rendered visualization from the run output panel.

<!-- BIOSIMULANT_VISUALS_START -->

### 1. Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2 

Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2  visualization captured from the dark-mode Biosimulant run for ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2 Lab.

![ferrel2011 autonomous biochemical oscillator in cell cycle in xenopus laevis v2 ](assets/01-ferrel2011-autonomous-biochemical-oscillator-in-cell-cycle-in-xenopus-laevis-v2-.png)

### 2. Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2 

Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2  visualization captured from the dark-mode Biosimulant run for ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2 Lab.

![ferrel2011 autonomous biochemical oscillator in cell cycle in xenopus laevis v2 ](assets/02-ferrel2011-autonomous-biochemical-oscillator-in-cell-cycle-in-xenopus-laevis-v2-.png)

### 3. Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2 

Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2  visualization captured from the dark-mode Biosimulant run for ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2 Lab.

![ferrel2011 autonomous biochemical oscillator in cell cycle in xenopus laevis v2 ](assets/03-ferrel2011-autonomous-biochemical-oscillator-in-cell-cycle-in-xenopus-laevis-v2-.png)

### 4. Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2 

Ferrel2011 Autonomous Biochemical Oscillator In Cell Cycle In Xenopus Laevis V2  visualization captured from the dark-mode Biosimulant run for ferrel2011 - autonomous biochemical oscillator in cell cycle in Xenopus laevis v2 Lab.

![ferrel2011 autonomous biochemical oscillator in cell cycle in xenopus laevis v2 ](assets/04-ferrel2011-autonomous-biochemical-oscillator-in-cell-cycle-in-xenopus-laevis-v2-.png)

<!-- BIOSIMULANT_VISUALS_END -->

## How to Read This Run

Use the time-course plots to see transient and steady-state behavior, the range or snapshot charts to identify the variables with the strongest response, and any phase-portrait view to inspect coupled regulator movement through the simulated trajectory. For this cell-cycle lab, the most useful comparison is usually between checkpoint, commitment, and mitotic-exit variables because those signals define where the simulated system sits in the cycle.

## Inputs

| Input | Context |
| --- | --- |
| - | No entries declared in `lab.yaml`. |

## Outputs

| Output | Context |
| --- | --- |
| CDK1 Active | Tracks CDK1 Active in the lab model via `cellcycle_sbml_ferrel2011_autonomous_biochemical_oscillator_in_biomd0000000936_model.cdk1_active`. |

## Lab Files

- `lab.yaml` defines the Biosimulant lab wrapper, exposed inputs, outputs, and runtime settings.
- `wiring-layout.json` stores the canvas layout used by the lab UI.
- `models/core/model.yaml` contains the wrapped simulation model metadata.
- `models/core/README.md` contains the source model notes and provenance.
- `models/visualisation/model.yaml` defines the visualization model used to render the run outputs.
- `assets/` contains the generated dark-mode visualization captures embedded above.

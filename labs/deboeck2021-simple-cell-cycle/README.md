# DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model Lab

Single-model lab wrapper for DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model. Models the production and degradation of cyclin B that drives the early embryonic cell cycle.Cyclin B is degraded by APC/C. The activity of APC/C is modeled not through biochemical interactions, but t.

This lab is a single-model Biosimulant wrapper for a cell-cycle simulation. The captured run uses the lab defaults and renders the model outputs as dark-mode visualizations for quick inspection and README embedding.

## Model Context

Models the production and degradation of cyclin B that drives the early embryonic cell cycle.Cyclin B is degraded by APC/C. The activity of APC/C is modeled not through biochemical interactions, but t.

- Core model: DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model
- Runtime used by the lab: duration 10, step 1
- Controllable inputs: none declared
- Primary outputs: Cyclin CDK
- Tags: cellcycle, sbml, biomodels_ebi, faithful

## Output Visualizations

The images below were generated from a Biosimulant lab run in dark mode. Each capture corresponds to one rendered visualization from the run output panel.

<!-- BIOSIMULANT_VISUALS_START -->

### 1. Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model 

Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model  visualization captured from the dark-mode Biosimulant run for DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model Lab.

![deboeck2021 modular approach to modeling the cell cycle simple cell cycle model ](assets/01-deboeck2021-modular-approach-to-modeling-the-cell-cycle-simple-cell-cycle-model-.png)

### 2. Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model 

Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model  visualization captured from the dark-mode Biosimulant run for DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model Lab.

![deboeck2021 modular approach to modeling the cell cycle simple cell cycle model ](assets/02-deboeck2021-modular-approach-to-modeling-the-cell-cycle-simple-cell-cycle-model-.png)

### 3. Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model 

Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model  visualization captured from the dark-mode Biosimulant run for DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model Lab.

![deboeck2021 modular approach to modeling the cell cycle simple cell cycle model ](assets/03-deboeck2021-modular-approach-to-modeling-the-cell-cycle-simple-cell-cycle-model-.png)

### 4. Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model 

Deboeck2021 Modular Approach To Modeling The Cell Cycle Simple Cell Cycle Model  visualization captured from the dark-mode Biosimulant run for DeBoeck2021 - Modular approach to modeling the cell cycle, simple cell cycle model Lab.

![deboeck2021 modular approach to modeling the cell cycle simple cell cycle model ](assets/04-deboeck2021-modular-approach-to-modeling-the-cell-cycle-simple-cell-cycle-model-.png)

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
| Cyclin CDK | Tracks Cyclin CDK in the lab model via `cellcycle_sbml_deboeck2021_modular_approach_to_modeling_the_cel_biomd0000001079_model.cyclin_cdk`. |

## Lab Files

- `lab.yaml` defines the Biosimulant lab wrapper, exposed inputs, outputs, and runtime settings.
- `wiring-layout.json` stores the canvas layout used by the lab UI.
- `models/core/model.yaml` contains the wrapped simulation model metadata.
- `models/core/README.md` contains the source model notes and provenance.
- `models/visualisation/model.yaml` defines the visualization model used to render the run outputs.
- `assets/` contains the generated dark-mode visualization captures embedded above.

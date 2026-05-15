# Tyson1991 - Cell Cycle 6 var Lab

Single-model lab wrapper for Tyson1991 - Cell Cycle 6 var. Tyson1991 - Cell Cycle 6 var Mathematical model of the interactions of cdc2 and cyclin. This model is described in the article: Modeling the cell division cycle: cdc2 and cyclin interactions.

This lab is a single-model Biosimulant wrapper for a cell-cycle simulation. The captured run uses the lab defaults and renders the model outputs as dark-mode visualizations for quick inspection and README embedding.

## Model Context

Tyson1991 - Cell Cycle 6 var Mathematical model of the interactions of cdc2 and cyclin. This model is described in the article: Modeling the cell division cycle: cdc2 and cyclin interactions.

- Core model: Tyson1991 - Cell Cycle 6 var
- Runtime used by the lab: duration 10, step 1
- Controllable inputs: Total Cyclin, Total Cdc2
- Primary outputs: Cdc2k, Cdc2k P, Phosphorylated Cyclin Cdc2, Phosphorylated Cyclin Cdc2 P, Cyclin, Phosphorylated Cyclin
- Tags: cellcycle, sbml, biomodels_ebi, faithful

## Output Visualizations

The images below were generated from a Biosimulant lab run in dark mode. Each capture corresponds to one rendered visualization from the run output panel.

<!-- BIOSIMULANT_VISUALS_START -->

### 1. Tyson1991 Cell Cycle 6 Var Lab Run Interpretation

Run interpretation view that anchors the captured simulation: it summarizes the lab purpose, runtime, and how to read the generated cell-cycle outputs.

![tyson1991 cell cycle 6 var lab run interpretation](assets/01-tyson1991-cell-cycle-6-var-lab-run-interpretation.png)

### 2. Tyson1991 Cell Cycle 6 Var Mitotic Switch And Exit

Mitotic switch and exit view, capturing late-cycle regulators and the transition out of mitosis.

![tyson1991 cell cycle 6 var mitotic switch and exit](assets/02-tyson1991-cell-cycle-6-var-mitotic-switch-and-exit.png)

### 3. Tyson1991 Cell Cycle 6 Var Largest Activity Ranges

Largest activity ranges chart, ranking the variables with the widest simulated movement so the dominant responses are easy to spot.

![tyson1991 cell cycle 6 var largest activity ranges](assets/03-tyson1991-cell-cycle-6-var-largest-activity-ranges.png)

### 4. Tyson1991 Cell Cycle 6 Var Final State Snapshot

Final state snapshot, comparing the end-of-run values for the selected cell-cycle variables.

![tyson1991 cell cycle 6 var final state snapshot](assets/04-tyson1991-cell-cycle-6-var-final-state-snapshot.png)

### 5. Tyson1991 Cell Cycle 6 Var Activity Phase Portrait

Activity phase portrait, showing pairwise movement between selected variables across the simulated trajectory.

![tyson1991 cell cycle 6 var activity phase portrait](assets/05-tyson1991-cell-cycle-6-var-activity-phase-portrait.png)

<!-- BIOSIMULANT_VISUALS_END -->

## How to Read This Run

Use the time-course plots to see transient and steady-state behavior, the range or snapshot charts to identify the variables with the strongest response, and any phase-portrait view to inspect coupled regulator movement through the simulated trajectory. For this cell-cycle lab, the most useful comparison is usually between checkpoint, commitment, and mitotic-exit variables because those signals define where the simulated system sits in the cycle.

## Inputs

| Input | Context |
| --- | --- |
| Total Cyclin | Controls Total Cyclin in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.total_cyclin`. |
| Total Cdc2 | Controls Total Cdc2 in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.total_cdc2`. |

## Outputs

| Output | Context |
| --- | --- |
| Cdc2k | Tracks Cdc2k in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.cdc2k`. |
| Cdc2k P | Tracks Cdc2k P in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.cdc2k_p`. |
| Phosphorylated Cyclin Cdc2 | Tracks Phosphorylated Cyclin Cdc2 in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.phosphorylated_cyclin_cdc2`. |
| Phosphorylated Cyclin Cdc2 P | Tracks Phosphorylated Cyclin Cdc2 P in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.phosphorylated_cyclin_cdc2_p`. |
| Cyclin | Tracks Cyclin in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.cyclin`. |
| Phosphorylated Cyclin | Tracks Phosphorylated Cyclin in the lab model via `cellcycle_sbml_tyson1991_cell_cycle_6_var_biomd0000000005_model.phosphorylated_cyclin`. |

## Lab Files

- `lab.yaml` defines the Biosimulant lab wrapper, exposed inputs, outputs, and runtime settings.
- `wiring-layout.json` stores the canvas layout used by the lab UI.
- `models/core/model.yaml` contains the wrapped simulation model metadata.
- `models/core/README.md` contains the source model notes and provenance.
- `models/visualisation/model.yaml` defines the visualization model used to render the run outputs.
- `assets/` contains the generated dark-mode visualization captures embedded above.

# Li2009- Assymetric Caulobacter cell cycle Lab

Single-model lab wrapper for Li2009- Assymetric Caulobacter cell cycle. The asymmetric cell division cycle of Caulobacter crescentus is orchestrated by an elaborate gene-protein regulatory network, centered on three major control proteins, DnaA, GcrA and CtrA. It can be used to explore cell-cycle regulation dynamics and compare checkpoint behavior across conditions.

This lab is a single-model Biosimulant wrapper for a cell-cycle simulation. The captured run uses the lab defaults and renders the model outputs as dark-mode visualizations for quick inspection and README embedding.

## Model Context

The asymmetric cell division cycle of Caulobacter crescentus is orchestrated by an elaborate gene-protein regulatory network, centered on three major control proteins, DnaA, GcrA and CtrA. It can be used to explore cell-cycle regulation dynamics and compare checkpoint behavior across conditions.

- Core model: Li2009- Assymetric Caulobacter cell cycle
- Runtime used by the lab: duration 10, step 1
- Controllable inputs: Ks,DNA A1, Ks,DNA A2, Kd,DnaA, Ji DNA Active GcrA, Phosphorylated Ja DNA CtrA, Ja,Fts Q,DNA
- Primary outputs: DnaA replication initiator, GcrA transcriptional regulator, CtrA cell-cycle regulator, Phosphorylated CtrA, DivK polarity regulator, Phosphorylated DivK, Model state I, Ccr Model state M, Hcori, Hctr A, and 20 more
- Tags: cellcycle, sbml, biomodels_ebi, faithful

## Output Visualizations

The images below were generated from a Biosimulant lab run in dark mode. Each capture corresponds to one rendered visualization from the run output panel.

<!-- BIOSIMULANT_VISUALS_START -->

### 1. Li2009 Assymetric Caulobacter Cell Cycle Lab Run Interpretation

Run interpretation view that anchors the captured simulation: it summarizes the lab purpose, runtime, and how to read the generated cell-cycle outputs.

![li2009 assymetric caulobacter cell cycle lab run interpretation](assets/01-li2009-assymetric-caulobacter-cell-cycle-lab-run-interpretation.png)

### 2. Li2009 Assymetric Caulobacter Cell Cycle Growth Dna And Division Markers

Growth, DNA, and division markers, linking mass accumulation and replication signals to cell-cycle state changes.

![li2009 assymetric caulobacter cell cycle growth dna and division markers](assets/02-li2009-assymetric-caulobacter-cell-cycle-growth-dna-and-division-markers.png)

### 3. Li2009 Assymetric Caulobacter Cell Cycle Largest Activity Ranges

Largest activity ranges chart, ranking the variables with the widest simulated movement so the dominant responses are easy to spot.

![li2009 assymetric caulobacter cell cycle largest activity ranges](assets/03-li2009-assymetric-caulobacter-cell-cycle-largest-activity-ranges.png)

### 4. Li2009 Assymetric Caulobacter Cell Cycle Final State Snapshot

Final state snapshot, comparing the end-of-run values for the selected cell-cycle variables.

![li2009 assymetric caulobacter cell cycle final state snapshot](assets/04-li2009-assymetric-caulobacter-cell-cycle-final-state-snapshot.png)

### 5. Li2009 Assymetric Caulobacter Cell Cycle Activity Phase Portrait

Activity phase portrait, showing pairwise movement between selected variables across the simulated trajectory.

![li2009 assymetric caulobacter cell cycle activity phase portrait](assets/05-li2009-assymetric-caulobacter-cell-cycle-activity-phase-portrait.png)

<!-- BIOSIMULANT_VISUALS_END -->

## How to Read This Run

Use the time-course plots to see transient and steady-state behavior, the range or snapshot charts to identify the variables with the strongest response, and any phase-portrait view to inspect coupled regulator movement through the simulated trajectory. For this cell-cycle lab, the most useful comparison is usually between checkpoint, commitment, and mitotic-exit variables because those signals define where the simulated system sits in the cycle.

## Inputs

| Input | Context |
| --- | --- |
| Ks,DNA A1 | Controls Ks,DNA A1 in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.ks_dna_a1`. |
| Ks,DNA A2 | Controls Ks,DNA A2 in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.ks_dna_a2`. |
| Kd,DnaA | Controls Kd,DnaA in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.kd_dna_a`. |
| Ji DNA Active GcrA | Controls Ji DNA Active GcrA in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.ji_dna_active_gcr_a`. |
| Phosphorylated Ja DNA CtrA | Controls Phosphorylated Ja DNA CtrA in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.phosphorylated_ja_dna_ctr_a`. |
| Ja,Fts Q,DNA | Controls Ja,Fts Q,DNA in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.ja_fts_q_dna`. |

## Outputs

| Output | Context |
| --- | --- |
| DnaA replication initiator | Tracks DnaA replication initiator in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.dna_a_replication_initiator`. |
| GcrA transcriptional regulator | Tracks GcrA transcriptional regulator in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.gcr_a_transcriptional_regulator`. |
| CtrA cell-cycle regulator | Tracks CtrA cell-cycle regulator in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.ctr_a_cell_cycle_regulator`. |
| Phosphorylated CtrA | Tracks Phosphorylated CtrA in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.phosphorylated_ctr_a`. |
| DivK polarity regulator | Tracks DivK polarity regulator in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.div_k_polarity_regulator`. |
| Phosphorylated DivK | Tracks Phosphorylated DivK in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.phosphorylated_div_k`. |
| Model state I | Tracks Model state I in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.model_state_i`. |
| Ccr Model state M | Tracks Ccr Model state M in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.ccr_model_state_m`. |
| Hcori | Tracks Hcori in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.hcori`. |
| Hctr A | Tracks Hctr A in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.hctr_a`. |
| Hccr Model state M | Tracks Hccr Model state M in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.hccr_model_state_m`. |
| Hfts Model state Z | Tracks Hfts Model state Z in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.hfts_model_state_z`. |
| Replication initiation state | Tracks Replication initiation state in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.replication_initiation_state`. |
| DNA replication state | Tracks DNA replication state in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.dna_replication_state`. |
| Division event counter | Tracks Division event counter in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.division_event_counter`. |
| Pod JL | Tracks Pod JL in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.pod_jl`. |
| Phosphorylated Per | Tracks Phosphorylated Per in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.phosphorylated_per`. |
| Div J | Tracks Div J in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.div_j`. |
| Phosphorylated Cck A | Tracks Phosphorylated Cck A in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.phosphorylated_cck_a`. |
| Cpd Model state R | Tracks Cpd Model state R in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.cpd_model_state_r`. |
| Rcd A | Tracks Rcd A in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.rcd_a`. |
| Phosphorylated Par AAD | Tracks Phosphorylated Par AAD in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.phosphorylated_par_aad`. |
| Fts Model state Z | Tracks Fts Model state Z in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.fts_model_state_z`. |
| Z-ring | Tracks Z-ring in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.z_ring`. |
| Cck Active Tot | Tracks Cck Active Tot in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.cck_active_tot`. |
| Cpd Model state R Tot | Tracks Cpd Model state R Tot in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.cpd_model_state_r_tot`. |
| Par Active Tot | Tracks Par Active Tot in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.par_active_tot`. |
| Cell elongation state | Tracks Cell elongation state in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.cell_elongation_state`. |
| Model state Z (Z) | Tracks Model state Z (Z) in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.model_state_z_z`. |
| Fts Q | Tracks Fts Q in the lab model via `cellcycle_sbml_li2009_assymetric_caulobacter_cell_cycle_biomd0000000727_model.fts_q`. |

## Lab Files

- `lab.yaml` defines the Biosimulant lab wrapper, exposed inputs, outputs, and runtime settings.
- `wiring-layout.json` stores the canvas layout used by the lab UI.
- `models/core/model.yaml` contains the wrapped simulation model metadata.
- `models/core/README.md` contains the source model notes and provenance.
- `models/visualisation/model.yaml` defines the visualization model used to render the run outputs.
- `assets/` contains the generated dark-mode visualization captures embedded above.

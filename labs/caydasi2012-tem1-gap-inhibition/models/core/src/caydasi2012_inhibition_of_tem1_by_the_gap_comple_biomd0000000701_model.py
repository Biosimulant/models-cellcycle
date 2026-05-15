# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Caydasi2012 - Inhibition of Tem1 by the GAP complex in Spindle Position Checkpoint.

Source: biomodels_ebi:BIOMD0000000701
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000701
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlCaydasi2012InhibitionOfTem1ByTheGapComplexIn(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Caydasi2012 - Inhibition of Tem1 by the GAP complex in Spindle Position Checkpoint."""

    _SBML_ID = 'BIOMD0000000701'
    _TITLE = 'Caydasi2012 - Inhibition of Tem1 by the GAP complex in Spindle Position Checkpoint'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'SPB_B',
        'SPB_T',
        'Bfa1',
        'Bfa1P4',
        'Bfa1P5',
        'Tem1GTP',
        'Tem1GDP',
        'B_Bfa1',
        'B_Bfa1P4',
        'B_Bfa1P5',
        'T_Tem1GTP',
        'T_Tem1GDP',
        'B_Bfa1_Tem1GTP',
        'B_Bfa1P4_Tem1GTP',
        'B_Bfa1P5_Tem1GTP',
        'B_Bfa1_Tem1GDP',
        'B_Bfa1P4_Tem1GDP',
        'B_Bfa1P5_Tem1GDP',
        'Bfa1_Tem1GTP',
        'Bfa1P4_Tem1GTP',
        'Bfa1P5_Tem1GTP',
        'Bfa1_Tem1GDP',
        'Bfa1P4_Tem1GDP',
        'Bfa1P5_Tem1GDP',
    ]
    _SPECIES_LABELS = {
        'SPB_B': 'Model state B',
        'SPB_T': 'Model state T',
        'Bfa1': 'Bfa1 spindle checkpoint GAP',
        'Bfa1P4': 'Bfa1 phosphorylated state P4',
        'Bfa1P5': 'Bfa1 phosphorylated state P5',
        'Tem1GTP': 'Phosphorylated Tem1GT',
        'Tem1GDP': 'Phosphorylated Tem1GD',
        'B_Bfa1': 'B Bfa1',
        'B_Bfa1P4': 'B Bfa1P4',
        'B_Bfa1P5': 'B Bfa1P5',
        'T_Tem1GTP': 'Phosphorylated T Tem1GT',
        'T_Tem1GDP': 'Phosphorylated T Tem1GD',
        'B_Bfa1_Tem1GTP': 'Phosphorylated B Bfa1 Tem1GT',
        'B_Bfa1P4_Tem1GTP': 'Phosphorylated B Bfa1P4 Tem1GT',
        'B_Bfa1P5_Tem1GTP': 'Phosphorylated B Bfa1P5 Tem1GT',
        'B_Bfa1_Tem1GDP': 'Phosphorylated B Bfa1 Tem1GD',
        'B_Bfa1P4_Tem1GDP': 'Phosphorylated B Bfa1P4 Tem1GD',
        'B_Bfa1P5_Tem1GDP': 'Phosphorylated B Bfa1P5 Tem1GD',
        'Bfa1_Tem1GTP': 'Phosphorylated Bfa1 Tem1GT',
        'Bfa1P4_Tem1GTP': 'Phosphorylated Bfa1P4 Tem1GT',
        'Bfa1P5_Tem1GTP': 'Phosphorylated Bfa1P5 Tem1GT',
        'Bfa1_Tem1GDP': 'Phosphorylated Bfa1 Tem1GD',
        'Bfa1P4_Tem1GDP': 'Phosphorylated Bfa1P4 Tem1GD',
        'Bfa1P5_Tem1GDP': 'Phosphorylated Bfa1P5 Tem1GD',
    }
    _PARAMETER_INPUTS = {
        'active_bfa1_at_the_spb': ('Active_Bfa1_at_the_SPB', 0.0, 'native SBML value', 'Controls Active Bfa1 At The SPB. Maps to SBML symbol `Active_Bfa1_at_the_SPB`.'),
        'active_bfa1_at_the_cytosol': ('Active_Bfa1_at_the_Cytosol', 0.0, 'native SBML value', 'Controls Active Bfa1 At The Cytosol. Maps to SBML symbol `Active_Bfa1_at_the_Cytosol`.'),
        'active_tem1_at_the_spb': ('Active_Tem1_at_the_SPB', 0.0, 'native SBML value', 'Controls Active Tem1 At The SPB. Maps to SBML symbol `Active_Tem1_at_the_SPB`.'),
        'active_tem1_in_the_cytosol': ('Active_Tem1_in_the_Cytosol', 2.9568714765000005e-10, 'native SBML value', 'Controls Active Tem1 In The Cytosol. Maps to SBML symbol `Active_Tem1_in_the_Cytosol`.'),
        'inactive_bfa1_at_the_spb': ('Inactive_Bfa1_at_the_SPB', 4.51479948255e-16, 'native SBML value', 'Controls Inactive Bfa1 At The SPB. Maps to SBML symbol `Inactive_Bfa1_at_the_SPB`.'),
        'inactive_bfa1_in_the_cytosol': ('Inactive_Bfa1_in_the_cytosol', 1.2224947245000003e-10, 'native SBML value', 'Controls Inactive Bfa1 In The Cytosol. Maps to SBML symbol `Inactive_Bfa1_in_the_cytosol`.'),
    }
    _HEADLINE_OUTPUTS = {
        'model_state_b': ('SPB_B', 'native SBML value', 'Tracks Model state B. Maps to SBML symbol `SPB_B`.'),
        'model_state_t': ('SPB_T', 'native SBML value', 'Tracks Model state T. Maps to SBML symbol `SPB_T`.'),
        'bfa1_spindle_checkpoint_gap': ('Bfa1', 'native SBML value', 'Tracks Bfa1 spindle checkpoint GAP. Maps to SBML symbol `Bfa1`.'),
        'bfa1_phosphorylated_state_p4': ('Bfa1P4', 'native SBML value', 'Tracks Bfa1 phosphorylated state P4. Maps to SBML symbol `Bfa1P4`.'),
        'bfa1_phosphorylated_state_p5': ('Bfa1P5', 'native SBML value', 'Tracks Bfa1 phosphorylated state P5. Maps to SBML symbol `Bfa1P5`.'),
        'phosphorylated_tem1gt': ('Tem1GTP', 'native SBML value', 'Tracks Phosphorylated Tem1GT. Maps to SBML symbol `Tem1GTP`.'),
        'phosphorylated_tem1gd': ('Tem1GDP', 'native SBML value', 'Tracks Phosphorylated Tem1GD. Maps to SBML symbol `Tem1GDP`.'),
        'b_bfa1': ('B_Bfa1', 'native SBML value', 'Tracks B Bfa1. Maps to SBML symbol `B_Bfa1`.'),
        'b_bfa1p4': ('B_Bfa1P4', 'native SBML value', 'Tracks B Bfa1P4. Maps to SBML symbol `B_Bfa1P4`.'),
        'b_bfa1p5': ('B_Bfa1P5', 'native SBML value', 'Tracks B Bfa1P5. Maps to SBML symbol `B_Bfa1P5`.'),
        'phosphorylated_t_tem1gt': ('T_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated T Tem1GT. Maps to SBML symbol `T_Tem1GTP`.'),
        'phosphorylated_t_tem1gd': ('T_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated T Tem1GD. Maps to SBML symbol `T_Tem1GDP`.'),
        'phosphorylated_b_bfa1_tem1gt': ('B_Bfa1_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated B Bfa1 Tem1GT. Maps to SBML symbol `B_Bfa1_Tem1GTP`.'),
        'phosphorylated_b_bfa1p4_tem1gt': ('B_Bfa1P4_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated B Bfa1P4 Tem1GT. Maps to SBML symbol `B_Bfa1P4_Tem1GTP`.'),
        'phosphorylated_b_bfa1p5_tem1gt': ('B_Bfa1P5_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated B Bfa1P5 Tem1GT. Maps to SBML symbol `B_Bfa1P5_Tem1GTP`.'),
        'phosphorylated_b_bfa1_tem1gd': ('B_Bfa1_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated B Bfa1 Tem1GD. Maps to SBML symbol `B_Bfa1_Tem1GDP`.'),
        'phosphorylated_b_bfa1p4_tem1gd': ('B_Bfa1P4_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated B Bfa1P4 Tem1GD. Maps to SBML symbol `B_Bfa1P4_Tem1GDP`.'),
        'phosphorylated_b_bfa1p5_tem1gd': ('B_Bfa1P5_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated B Bfa1P5 Tem1GD. Maps to SBML symbol `B_Bfa1P5_Tem1GDP`.'),
        'phosphorylated_bfa1_tem1gt': ('Bfa1_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated Bfa1 Tem1GT. Maps to SBML symbol `Bfa1_Tem1GTP`.'),
        'phosphorylated_bfa1p4_tem1gt': ('Bfa1P4_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated Bfa1P4 Tem1GT. Maps to SBML symbol `Bfa1P4_Tem1GTP`.'),
        'phosphorylated_bfa1p5_tem1gt': ('Bfa1P5_Tem1GTP', 'native SBML value', 'Tracks Phosphorylated Bfa1P5 Tem1GT. Maps to SBML symbol `Bfa1P5_Tem1GTP`.'),
        'phosphorylated_bfa1_tem1gd': ('Bfa1_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated Bfa1 Tem1GD. Maps to SBML symbol `Bfa1_Tem1GDP`.'),
        'phosphorylated_bfa1p4_tem1gd': ('Bfa1P4_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated Bfa1P4 Tem1GD. Maps to SBML symbol `Bfa1P4_Tem1GDP`.'),
        'phosphorylated_bfa1p5_tem1gd': ('Bfa1P5_Tem1GDP', 'native SBML value', 'Tracks Phosphorylated Bfa1P5 Tem1GD. Maps to SBML symbol `Bfa1P5_Tem1GDP`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000701.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Caydasi2012InhibitionOfTem1ByTheGapCompleBiomd0000000701Model = SbmlCaydasi2012InhibitionOfTem1ByTheGapComplexIn

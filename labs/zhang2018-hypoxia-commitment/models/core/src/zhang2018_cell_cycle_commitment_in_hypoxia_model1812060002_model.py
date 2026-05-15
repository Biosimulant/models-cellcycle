# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Zhang2018 - Cell cycle commitment in hypoxia.

Source: biomodels_ebi:MODEL1812060002
Original: https://www.ebi.ac.uk/biomodels/MODEL1812060002
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlZhang2018CellCycleCommitmentInHypoxia(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Zhang2018 - Cell cycle commitment in hypoxia."""

    _SBML_ID = 'MODEL1812060002'
    _TITLE = 'Zhang2018 - Cell cycle commitment in hypoxia'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'Hif1a_Myc',
        'Hif2a_Myc',
        'E2F',
        'cycD_p_p',
        'cycD',
        'cycE',
        'RbP',
        'Rb_nP',
        'Myc',
        'E2F_RB',
        'Rb',
        'p_p',
        'cycE_p_p',
        'DEG',
        'Hif1a',
        'Hif2a',
    ]
    _SPECIES_LABELS = {
        'Hif1a_Myc': 'HIF-1 alpha Myc',
        'Hif2a_Myc': 'HIF-2 alpha Myc',
        'E2F': 'E2F transcription factor',
        'cycD_p_p': 'Double-phosphorylated Cyclin D',
        'cycD': 'Cyclin D',
        'cycE': 'Cyclin E',
        'RbP': 'Phosphorylated Rb',
        'Rb_nP': 'Unphosphorylated Rb',
        'Myc': 'Myc transcription factor',
        'E2F_RB': 'E2F Rb',
        'Rb': 'Rb tumor suppressor',
        'p_p': 'Double phosphorylation signal',
        'cycE_p_p': 'Double-phosphorylated Cyclin E',
        'DEG': 'Oxygen-dependent degradation factor',
        'Hif1a': 'HIF-1 alpha',
        'Hif2a': 'HIF-2 alpha',
    }
    _PARAMETER_INPUTS = {
        'oxygen': ('O2', 2.0, 'dimensionless', 'Controls Oxygen. Maps to SBML symbol `O2`.'),
    }
    _HEADLINE_OUTPUTS = {
        'hif_1_alpha_myc': ('Hif1a_Myc', 'native SBML value', 'Tracks HIF-1 alpha Myc. Maps to SBML symbol `Hif1a_Myc`.'),
        'hif_2_alpha_myc': ('Hif2a_Myc', 'native SBML value', 'Tracks HIF-2 alpha Myc. Maps to SBML symbol `Hif2a_Myc`.'),
        'e2f_transcription_factor': ('E2F', 'native SBML value', 'Tracks E2F transcription factor. Maps to SBML symbol `E2F`.'),
        'double_phosphorylated_cyclin_d': ('cycD_p_p', 'native SBML value', 'Tracks Double-phosphorylated Cyclin D. Maps to SBML symbol `cycD_p_p`.'),
        'cyclin_d': ('cycD', 'native SBML value', 'Tracks Cyclin D. Maps to SBML symbol `cycD`.'),
        'cyclin_e': ('cycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `cycE`.'),
        'phosphorylated_rb': ('RbP', 'native SBML value', 'Tracks Phosphorylated Rb. Maps to SBML symbol `RbP`.'),
        'unphosphorylated_rb': ('Rb_nP', 'native SBML value', 'Tracks Unphosphorylated Rb. Maps to SBML symbol `Rb_nP`.'),
        'myc_transcription_factor': ('Myc', 'native SBML value', 'Tracks Myc transcription factor. Maps to SBML symbol `Myc`.'),
        'e2f_rb': ('E2F_RB', 'native SBML value', 'Tracks E2F Rb. Maps to SBML symbol `E2F_RB`.'),
        'rb_tumor_suppressor': ('Rb', 'native SBML value', 'Tracks Rb tumor suppressor. Maps to SBML symbol `Rb`.'),
        'double_phosphorylation_signal': ('p_p', 'native SBML value', 'Tracks Double phosphorylation signal. Maps to SBML symbol `p_p`.'),
        'double_phosphorylated_cyclin_e': ('cycE_p_p', 'native SBML value', 'Tracks Double-phosphorylated Cyclin E. Maps to SBML symbol `cycE_p_p`.'),
        'oxygen_dependent_degradation_factor': ('DEG', 'dimensionless', 'Tracks Oxygen-dependent degradation factor. Maps to SBML symbol `DEG`.'),
        'hif_1_alpha': ('Hif1a', 'native SBML value', 'Tracks HIF-1 alpha. Maps to SBML symbol `Hif1a`.'),
        'hif_2_alpha': ('Hif2a', 'native SBML value', 'Tracks HIF-2 alpha. Maps to SBML symbol `Hif2a`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1812060002.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Zhang2018CellCycleCommitmentInHypoxiaModel1812060002Model = SbmlZhang2018CellCycleCommitmentInHypoxia

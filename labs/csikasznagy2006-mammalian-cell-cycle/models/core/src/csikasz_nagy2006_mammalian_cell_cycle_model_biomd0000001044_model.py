# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Csikasz-Nagy2006 - Mammalian Cell Cycle model.

Source: biomodels_ebi:BIOMD0000001044
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000001044
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlCsikaszNagy2006MammalianCellCycleModel(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Csikasz-Nagy2006 - Mammalian Cell Cycle model."""

    _SBML_ID = 'BIOMD0000001044'
    _TITLE = 'Csikasz-Nagy2006 - Mammalian Cell Cycle model'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'APCP',
        'BCKI',
        'Cdc20A',
        'Cdc20i',
        'Cdh1',
        'CKI',
        'CycA',
        'CycB',
        'CycE',
        'Mass',
        'pB',
        'pBCKI',
        'TriA',
        'TriE',
    ]
    _SPECIES_LABELS = {
        'APCP': 'Phosphorylated APC/C/C',
        'BCKI': 'B-type cyclin CDK inhibitor',
        'Cdc20A': 'Active Cdc20',
        'Cdc20i': 'Inactive Cdc20',
        'Cdh1': 'Cdh1 APC/C activator',
        'CKI': 'Cyclin-dependent kinase inhibitor',
        'CycA': 'Cyclin A',
        'CycB': 'Cyclin B',
        'CycE': 'Cyclin E',
        'Mass': 'Cell mass',
        'pB': 'P B',
        'pBCKI': 'P BCKI',
        'TriA': 'Tri A',
        'TriE': 'Tri E',
    }
    _PARAMETER_INPUTS = {
        'apc_c': ('APC', 0.32837343215942405, 'native SBML value', 'Controls APC/C. Maps to SBML symbol `APC`.'),
        'cdc14': ('Cdc14', 0.660586714744568, 'native SBML value', 'Controls Cdc14. Maps to SBML symbol `Cdc14`.'),
        'total_cdc20_apc_c_activator': ('Cdc20T', 0.67914024181664, 'native SBML value', 'Controls Total Cdc20 APC/C activator. Maps to SBML symbol `Cdc20T`.'),
        'phosphorylated_cdc25': ('Cdc25P', 0.1002052901971687, 'native SBML value', 'Controls Phosphorylated Cdc25. Maps to SBML symbol `Cdc25P`.'),
        'inactive_cdh1': ('Cdh1i', 0.0007642507553099476, 'native SBML value', 'Controls Inactive Cdh1. Maps to SBML symbol `Cdh1i`.'),
        'total_cyclin_dependent_kinase_inhibitor': ('CKIT', 0.624287813901901, 'native SBML value', 'Controls Total cyclin-dependent kinase inhibitor. Maps to SBML symbol `CKIT`.'),
    }
    _HEADLINE_OUTPUTS = {
        'phosphorylated_apc_c_c': ('APCP', 'native SBML value', 'Tracks Phosphorylated APC/C/C. Maps to SBML symbol `APCP`.'),
        'b_type_cyclin_cdk_inhibitor': ('BCKI', 'native SBML value', 'Tracks B-type cyclin CDK inhibitor. Maps to SBML symbol `BCKI`.'),
        'active_cdc20': ('Cdc20A', 'native SBML value', 'Tracks Active Cdc20. Maps to SBML symbol `Cdc20A`.'),
        'inactive_cdc20': ('Cdc20i', 'native SBML value', 'Tracks Inactive Cdc20. Maps to SBML symbol `Cdc20i`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'cyclin_dependent_kinase_inhibitor': ('CKI', 'native SBML value', 'Tracks Cyclin-dependent kinase inhibitor. Maps to SBML symbol `CKI`.'),
        'cyclin_a': ('CycA', 'native SBML value', 'Tracks Cyclin A. Maps to SBML symbol `CycA`.'),
        'cyclin_b': ('CycB', 'native SBML value', 'Tracks Cyclin B. Maps to SBML symbol `CycB`.'),
        'cyclin_e': ('CycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `CycE`.'),
        'cell_mass': ('Mass', 'native SBML value', 'Tracks Cell mass. Maps to SBML symbol `Mass`.'),
        'p_b': ('pB', 'native SBML value', 'Tracks P B. Maps to SBML symbol `pB`.'),
        'p_bcki': ('pBCKI', 'native SBML value', 'Tracks P BCKI. Maps to SBML symbol `pBCKI`.'),
        'tri_a': ('TriA', 'native SBML value', 'Tracks Tri A. Maps to SBML symbol `TriA`.'),
        'tri_e': ('TriE', 'native SBML value', 'Tracks Tri E. Maps to SBML symbol `TriE`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000001044.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
CsikaszNagy2006MammalianCellCycleModelBiomd0000001044Model = SbmlCsikaszNagy2006MammalianCellCycleModel

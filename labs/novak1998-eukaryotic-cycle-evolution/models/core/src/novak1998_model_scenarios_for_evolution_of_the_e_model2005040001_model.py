# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Novak1998-Model scenarios for evolution of the eukaryotic cell cycle..

Source: biomodels_ebi:MODEL2005040001
Original: https://www.ebi.ac.uk/biomodels/MODEL2005040001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlNovak1998ModelScenariosForEvolutionOfTheEukaryotic(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Novak1998-Model scenarios for evolution of the eukaryotic cell cycle.."""

    _SBML_ID = 'MODEL2005040001'
    _TITLE = 'Novak1998-Model scenarios for evolution of the eukaryotic cell cycle.'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CDK',
        'APC',
        'size',
        'ACTt',
        'ACT',
        'CKI',
        'TRI',
    ]
    _SPECIES_LABELS = {
        'CDK': 'Cyclin-dependent kinase activity',
        'APC': 'APC/C/C',
        'size': 'Size',
        'ACTt': 'Total active regulatory state',
        'ACT': 'Active regulatory state',
        'CKI': 'Cyclin-dependent kinase inhibitor',
        'TRI': 'Trimer complex',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cyclin_dependent_kinase_activity': ('CDK', 'native SBML value', 'Tracks Cyclin-dependent kinase activity. Maps to SBML symbol `CDK`.'),
        'apc_c_c': ('APC', 'native SBML value', 'Tracks APC/C/C. Maps to SBML symbol `APC`.'),
        'size': ('size', 'native SBML value', 'Tracks Size. Maps to SBML symbol `size`.'),
        'total_active_regulatory_state': ('ACTt', 'native SBML value', 'Tracks Total active regulatory state. Maps to SBML symbol `ACTt`.'),
        'active_regulatory_state': ('ACT', 'native SBML value', 'Tracks Active regulatory state. Maps to SBML symbol `ACT`.'),
        'cyclin_dependent_kinase_inhibitor': ('CKI', 'native SBML value', 'Tracks Cyclin-dependent kinase inhibitor. Maps to SBML symbol `CKI`.'),
        'trimer_complex': ('TRI', 'native SBML value', 'Tracks Trimer complex. Maps to SBML symbol `TRI`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2005040001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Novak1998ModelScenariosForEvolutionOfTheEModel2005040001Model = SbmlNovak1998ModelScenariosForEvolutionOfTheEukaryotic

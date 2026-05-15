# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Novak2004 - A Model for Restriction Point Control of the Mammalian Cell Cycle.

Source: biomodels_ebi:MODEL2006080001
Original: https://www.ebi.ac.uk/biomodels/MODEL2006080001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlNovak2004AModelForRestrictionPointControlOfThe(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Novak2004 - A Model for Restriction Point Control of the Mammalian Cell Cycle."""

    _SBML_ID = 'MODEL2006080001'
    _TITLE = 'Novak2004 - A Model for Restriction Point Control of the Mammalian Cell Cycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'ERG',
        'DRG',
        'cycD',
        'cycD_Kip1',
        'cycE',
        'cycE_Kip1',
        'cycA',
        'cycA_Kip1',
        'Kip1',
        'E2F',
        'cycB',
        'Cdh1',
        'cdc20T',
        'Cdc20',
        'PPX',
        'IEP',
        'GM',
        'mass',
    ]
    _SPECIES_LABELS = {
        'ERG': 'Early response gene module',
        'DRG': 'Delayed response gene module',
        'cycD': 'Cyclin D',
        'cycD_Kip1': 'Cyclin D:Kip1',
        'cycE': 'Cyclin E',
        'cycE_Kip1': 'Cyclin E:Kip1',
        'cycA': 'Cyclin A',
        'cycA_Kip1': 'Cyclin A:Kip1',
        'Kip1': 'Kip1 CDK inhibitor',
        'E2F': 'E2F transcription factor',
        'cycB': 'Cyclin B',
        'Cdh1': 'Cdh1 APC/C activator',
        'cdc20T': 'Cdc20T',
        'Cdc20': 'Cdc20 APC/C activator',
        'PPX': 'PPX phosphatase',
        'IEP': 'Phosphorylated IE',
        'GM': 'Model state GM',
        'mass': 'Mass',
    }
    _PARAMETER_INPUTS = {
        'e2ft': ('E2FT', 5.0, 'native SBML value', 'Controls E2FT. Maps to SBML symbol `E2FT`.'),
        'pp1t': ('PP1T', 1.0, 'native SBML value', 'Controls PP1T. Maps to SBML symbol `PP1T`.'),
        'rb_t': ('RbT', 10.0, 'native SBML value', 'Controls Rb T. Maps to SBML symbol `RbT`.'),
        'cyclin_et': ('cycET', 0.0, 'native SBML value', 'Controls Cyclin ET. Maps to SBML symbol `cycET`.'),
        'pp1a': ('PP1A', 1.0, 'native SBML value', 'Controls PP1A. Maps to SBML symbol `PP1A`.'),
        'rb_hypo': ('Rb_hypo', 10.0, 'native SBML value', 'Controls Rb Hypo. Maps to SBML symbol `Rb_hypo`.'),
    }
    _HEADLINE_OUTPUTS = {
        'early_response_gene_module': ('ERG', 'native SBML value', 'Tracks Early response gene module. Maps to SBML symbol `ERG`.'),
        'delayed_response_gene_module': ('DRG', 'native SBML value', 'Tracks Delayed response gene module. Maps to SBML symbol `DRG`.'),
        'cyclin_d': ('cycD', 'native SBML value', 'Tracks Cyclin D. Maps to SBML symbol `cycD`.'),
        'cyclin_d_kip1': ('cycD_Kip1', 'native SBML value', 'Tracks Cyclin D:Kip1. Maps to SBML symbol `cycD_Kip1`.'),
        'cyclin_e': ('cycE', 'native SBML value', 'Tracks Cyclin E. Maps to SBML symbol `cycE`.'),
        'cyclin_e_kip1': ('cycE_Kip1', 'native SBML value', 'Tracks Cyclin E:Kip1. Maps to SBML symbol `cycE_Kip1`.'),
        'cyclin_a': ('cycA', 'native SBML value', 'Tracks Cyclin A. Maps to SBML symbol `cycA`.'),
        'cyclin_a_kip1': ('cycA_Kip1', 'native SBML value', 'Tracks Cyclin A:Kip1. Maps to SBML symbol `cycA_Kip1`.'),
        'kip1_cdk_inhibitor': ('Kip1', 'native SBML value', 'Tracks Kip1 CDK inhibitor. Maps to SBML symbol `Kip1`.'),
        'e2f_transcription_factor': ('E2F', 'native SBML value', 'Tracks E2F transcription factor. Maps to SBML symbol `E2F`.'),
        'cyclin_b': ('cycB', 'native SBML value', 'Tracks Cyclin B. Maps to SBML symbol `cycB`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'native SBML value', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'cdc20t': ('cdc20T', 'native SBML value', 'Tracks Cdc20T. Maps to SBML symbol `cdc20T`.'),
        'cdc20_apc_c_activator': ('Cdc20', 'native SBML value', 'Tracks Cdc20 APC/C activator. Maps to SBML symbol `Cdc20`.'),
        'ppx_phosphatase': ('PPX', 'native SBML value', 'Tracks PPX phosphatase. Maps to SBML symbol `PPX`.'),
        'phosphorylated_ie': ('IEP', 'native SBML value', 'Tracks Phosphorylated IE. Maps to SBML symbol `IEP`.'),
        'model_state_gm': ('GM', 'native SBML value', 'Tracks Model state GM. Maps to SBML symbol `GM`.'),
        'mass': ('mass', 'native SBML value', 'Tracks Mass. Maps to SBML symbol `mass`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL2006080001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Novak2004AModelForRestrictionPointControlModel2006080001Model = SbmlNovak2004AModelForRestrictionPointControlOfThe

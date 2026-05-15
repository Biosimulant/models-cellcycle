# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Conradie2010_RPControl_CellCycle.

Source: biomodels_ebi:BIOMD0000000265
Original: https://www.ebi.ac.uk/biomodels/BIOMD0000000265
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlConradie2010RpcontrolCellcycle(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Conradie2010_RPControl_CellCycle."""

    _SBML_ID = 'BIOMD0000000265'
    _TITLE = 'Conradie2010_RPControl_CellCycle'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'CDc20',
        'CDh1',
        'CYCA',
        'CYCB',
        'CYCD',
        'CYCE',
        'DRG',
        'var2',
        'var5',
        'ERG',
        'GM',
        'var1',
        'CDc20T',
        'MASS',
        'P27',
        'CA',
        'CD',
        'CE',
        'var3',
        'var6',
        'IEP',
        'PPX',
        'var4',
    ]
    _SPECIES_LABELS = {
        'CDc20': 'Cdc20',
        'CDh1': 'Cdh1',
        'CYCA': 'Cyclin A:CDK2',
        'CYCB': 'Cyclin B:CDK2',
        'CYCD': 'Cyclin D:CDK2',
        'CYCE': 'Cyclin E:CDK2',
        'DRG': 'Delayed response gene module',
        'var2': 'E2F',
        'var5': 'E2F:Rb',
        'ERG': 'Early response gene module',
        'GM': 'General Machinery For Protein Synthesis',
        'var1': 'Hypophosphorylated Rb',
        'CDc20T': 'Inactive Cdc20',
        'MASS': 'Cell mass',
        'P27': 'p27 CDK inhibitor',
        'CA': 'P27:cyclin A:CDK2',
        'CD': 'P27:cyclin D:CDK2',
        'CE': 'P27:cyclin E:CDK2',
        'var3': 'Phosphorylated E2F',
        'var6': 'Phosphorylated E2F:Rb',
        'IEP': 'Phosphorylated IE',
        'PPX': 'PPX phosphatase',
        'var4': 'Retinoblastoma Protein (Rb)',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'cdc20': ('CDc20', 'native SBML value', 'Tracks Cdc20. Maps to SBML symbol `CDc20`.'),
        'cdh1': ('CDh1', 'native SBML value', 'Tracks Cdh1. Maps to SBML symbol `CDh1`.'),
        'cyclin_a_cdk2': ('CYCA', 'native SBML value', 'Tracks Cyclin A:CDK2. Maps to SBML symbol `CYCA`.'),
        'cyclin_b_cdk2': ('CYCB', 'native SBML value', 'Tracks Cyclin B:CDK2. Maps to SBML symbol `CYCB`.'),
        'cyclin_d_cdk2': ('CYCD', 'native SBML value', 'Tracks Cyclin D:CDK2. Maps to SBML symbol `CYCD`.'),
        'cyclin_e_cdk2': ('CYCE', 'native SBML value', 'Tracks Cyclin E:CDK2. Maps to SBML symbol `CYCE`.'),
        'delayed_response_gene_module': ('DRG', 'native SBML value', 'Tracks Delayed response gene module. Maps to SBML symbol `DRG`.'),
        'e2f': ('var2', 'native SBML value', 'Tracks E2F. Maps to SBML symbol `var2`.'),
        'e2f_rb': ('var5', 'native SBML value', 'Tracks E2F:Rb. Maps to SBML symbol `var5`.'),
        'early_response_gene_module': ('ERG', 'native SBML value', 'Tracks Early response gene module. Maps to SBML symbol `ERG`.'),
        'general_machinery_for_protein_synthesis': ('GM', 'native SBML value', 'Tracks General Machinery For Protein Synthesis. Maps to SBML symbol `GM`.'),
        'hypophosphorylated_rb': ('var1', 'native SBML value', 'Tracks Hypophosphorylated Rb. Maps to SBML symbol `var1`.'),
        'inactive_cdc20': ('CDc20T', 'native SBML value', 'Tracks Inactive Cdc20. Maps to SBML symbol `CDc20T`.'),
        'cell_mass': ('MASS', 'native SBML value', 'Tracks Cell mass. Maps to SBML symbol `MASS`.'),
        'p27_cdk_inhibitor': ('P27', 'native SBML value', 'Tracks p27 CDK inhibitor. Maps to SBML symbol `P27`.'),
        'p27_cyclin_a_cdk2': ('CA', 'native SBML value', 'Tracks P27:cyclin A:CDK2. Maps to SBML symbol `CA`.'),
        'p27_cyclin_d_cdk2': ('CD', 'native SBML value', 'Tracks P27:cyclin D:CDK2. Maps to SBML symbol `CD`.'),
        'p27_cyclin_e_cdk2': ('CE', 'native SBML value', 'Tracks P27:cyclin E:CDK2. Maps to SBML symbol `CE`.'),
        'phosphorylated_e2f': ('var3', 'native SBML value', 'Tracks Phosphorylated E2F. Maps to SBML symbol `var3`.'),
        'phosphorylated_e2f_rb': ('var6', 'native SBML value', 'Tracks Phosphorylated E2F:Rb. Maps to SBML symbol `var6`.'),
        'phosphorylated_ie': ('IEP', 'native SBML value', 'Tracks Phosphorylated IE. Maps to SBML symbol `IEP`.'),
        'ppx_phosphatase': ('PPX', 'native SBML value', 'Tracks PPX phosphatase. Maps to SBML symbol `PPX`.'),
        'retinoblastoma_protein_rb': ('var4', 'native SBML value', 'Tracks Retinoblastoma Protein (Rb). Maps to SBML symbol `var4`.'),
    }

    def __init__(self, model_path: str = 'data/BIOMD0000000265.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Conradie2010RpcontrolCellcycleBiomd0000000265Model = SbmlConradie2010RpcontrolCellcycle

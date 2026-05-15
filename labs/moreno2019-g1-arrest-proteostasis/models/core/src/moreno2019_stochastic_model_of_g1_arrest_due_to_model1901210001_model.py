# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Moreno2019 - Stochastic model of G1 arrest due to proteostasis decline delimits replicative lifespan in yeast.

Source: biomodels_ebi:MODEL1901210001
Original: https://www.ebi.ac.uk/biomodels/MODEL1901210001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlMoreno2019StochasticModelOfG1ArrestDueTo(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Moreno2019 - Stochastic model of G1 arrest due to proteostasis decline delimits replicative lifespan in yeast."""

    _SBML_ID = 'MODEL1901210001'
    _TITLE = 'Moreno2019 - Stochastic model of G1 arrest due to proteostasis decline delimits replicative lifespan in yeast'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'species'
    _OBSERVABLES = [
        'Prot',
        'YP',
        'Ydj1',
        'ProtF',
        'ProtM',
        'Oli',
        'Agg',
        'YOAgg',
        'YM',
        'YO',
        'Cln3',
        'YC',
        'Cln3F',
        'Whi5',
        'Whi5i',
    ]
    _SPECIES_LABELS = {
        'Prot': 'Protein load',
        'YP': 'Model state YP',
        'Ydj1': 'Ydj1 chaperone',
        'ProtF': 'Prot F',
        'ProtM': 'Prot Model state M',
        'Oli': 'Oligomerized proteostasis species',
        'Agg': 'Protein aggregate burden',
        'YOAgg': 'Ydj1-oligomer aggregate complex',
        'YM': 'Model state YM',
        'YO': 'Model state YO',
        'Cln3': 'Cln3 Start cyclin',
        'YC': 'Model state YC',
        'Cln3F': 'Folded Cln3 Start cyclin',
        'Whi5': 'Whi5 Start inhibitor',
        'Whi5i': 'Inactive Whi5 Start inhibitor',
    }
    _PARAMETER_INPUTS = {
        'hsp104': ('Hsp104', 1.24e-06, 'native SBML value', 'Controls Hsp104. Maps to SBML symbol `Hsp104`.'),
    }
    _HEADLINE_OUTPUTS = {
        'protein_load': ('Prot', 'native SBML value', 'Tracks Protein load. Maps to SBML symbol `Prot`.'),
        'model_state_yp': ('YP', 'native SBML value', 'Tracks Model state YP. Maps to SBML symbol `YP`.'),
        'ydj1_chaperone': ('Ydj1', 'native SBML value', 'Tracks Ydj1 chaperone. Maps to SBML symbol `Ydj1`.'),
        'prot_f': ('ProtF', 'native SBML value', 'Tracks Prot F. Maps to SBML symbol `ProtF`.'),
        'prot_model_state_m': ('ProtM', 'native SBML value', 'Tracks Prot Model state M. Maps to SBML symbol `ProtM`.'),
        'oligomerized_proteostasis_species': ('Oli', 'native SBML value', 'Tracks Oligomerized proteostasis species. Maps to SBML symbol `Oli`.'),
        'protein_aggregate_burden': ('Agg', 'native SBML value', 'Tracks Protein aggregate burden. Maps to SBML symbol `Agg`.'),
        'ydj1_oligomer_aggregate_complex': ('YOAgg', 'native SBML value', 'Tracks Ydj1-oligomer aggregate complex. Maps to SBML symbol `YOAgg`.'),
        'model_state_ym': ('YM', 'native SBML value', 'Tracks Model state YM. Maps to SBML symbol `YM`.'),
        'model_state_yo': ('YO', 'native SBML value', 'Tracks Model state YO. Maps to SBML symbol `YO`.'),
        'cln3_start_cyclin': ('Cln3', 'native SBML value', 'Tracks Cln3 Start cyclin. Maps to SBML symbol `Cln3`.'),
        'model_state_yc': ('YC', 'native SBML value', 'Tracks Model state YC. Maps to SBML symbol `YC`.'),
        'folded_cln3_start_cyclin': ('Cln3F', 'native SBML value', 'Tracks Folded Cln3 Start cyclin. Maps to SBML symbol `Cln3F`.'),
        'whi5_start_inhibitor': ('Whi5', 'native SBML value', 'Tracks Whi5 Start inhibitor. Maps to SBML symbol `Whi5`.'),
        'inactive_whi5_start_inhibitor': ('Whi5i', 'native SBML value', 'Tracks Inactive Whi5 Start inhibitor. Maps to SBML symbol `Whi5i`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1901210001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Moreno2019StochasticModelOfG1ArrestDueToModel1901210001Model = SbmlMoreno2019StochasticModelOfG1ArrestDueTo

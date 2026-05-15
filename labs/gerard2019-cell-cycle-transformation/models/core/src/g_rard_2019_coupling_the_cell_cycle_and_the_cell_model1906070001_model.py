# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Gérard - 2019 - Coupling the cell cycle and the cell transformation networks (SBML).

Source: biomodels_ebi:MODEL1906070001
Original: https://www.ebi.ac.uk/biomodels/MODEL1906070001
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlGerard2019CouplingTheCellCycleAndTheCell(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Gérard - 2019 - Coupling the cell cycle and the cell transformation networks (SBML)."""

    _SBML_ID = 'MODEL1906070001'
    _TITLE = 'Gérard - 2019 - Coupling the cell cycle and the cell transformation networks (SBML)'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'NFKB',
        'LIN28',
        'let7',
        'mIL6',
        'mIL6let7',
        'IL6',
        'mRas',
        'mRaslet7',
        'Ras',
        'STAT3',
        'miR21',
        'mPTEN',
        'miRmpten',
        'PTEN',
        'mMd',
        'Md',
        'mMdlet7',
        'E2F',
        'mMe',
        'Me',
        'mMelet7',
        'mMa',
        'Ma',
        'mMalet7',
        'mMb',
        'Mb',
        'mMblet7',
        'APC',
        'Let7TOT',
        'NFKBi',
        't',
    ]
    _SPECIES_LABELS = {
        'NFKB': 'NF-kB = 0 00045',
        'LIN28': 'LIN28 = 0 34',
        'let7': 'let-7 = 40',
        'mIL6': 'Model state M IL6 = 0 0003',
        'mIL6let7': 'Model state M IL6let7',
        'IL6': 'IL6 = 0 001',
        'mRas': 'Model state M Ras = 0 00001',
        'mRaslet7': 'Model state M Raslet7',
        'Ras': 'Ras = 0 0001',
        'STAT3': 'STAT3 = 0 0001',
        'miR21': 'Mi Model state R21 = 0 0003',
        'mPTEN': 'Model state M PTEN = 0 01',
        'miRmpten': 'Mi Rmpten',
        'PTEN': 'PTEN = 0 17',
        'mMd': 'Model state M Md',
        'Md': 'Md = 0 01',
        'mMdlet7': 'Model state M Mdlet7',
        'E2F': 'E2F transcription factor',
        'mMe': 'Model state M Me',
        'Me': 'Me = 0 01',
        'mMelet7': 'Model state M Melet7',
        'mMa': 'Model state M Ma',
        'Ma': 'Ma = 0 01',
        'mMalet7': 'Model state M Malet7',
        'mMb': 'Model state M Mb',
        'Mb': 'Mb = 0 01',
        'mMblet7': 'Model state M Mblet7',
        'APC': 'APC/C/C = 0 01',
        'Let7TOT': 'Total let-7 microRNA',
        'NFKBi': 'Inactive NF-kB',
        't': 'Model Time',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'nf_k_b_0_00045': ('NFKB', 'dimensionless', 'Tracks NF-kB = 0 00045. Maps to SBML symbol `NFKB`.'),
        'lin28_0_34': ('LIN28', 'dimensionless', 'Tracks LIN28 = 0 34. Maps to SBML symbol `LIN28`.'),
        'let_7_40': ('let7', 'dimensionless', 'Tracks let-7 = 40. Maps to SBML symbol `let7`.'),
        'model_state_m_il6_0_0003': ('mIL6', 'dimensionless', 'Tracks Model state M IL6 = 0 0003. Maps to SBML symbol `mIL6`.'),
        'model_state_m_il6let7': ('mIL6let7', 'dimensionless', 'Tracks Model state M IL6let7. Maps to SBML symbol `mIL6let7`.'),
        'il6_0_001': ('IL6', 'dimensionless', 'Tracks IL6 = 0 001. Maps to SBML symbol `IL6`.'),
        'model_state_m_ras_0_00001': ('mRas', 'dimensionless', 'Tracks Model state M Ras = 0 00001. Maps to SBML symbol `mRas`.'),
        'model_state_m_raslet7': ('mRaslet7', 'dimensionless', 'Tracks Model state M Raslet7. Maps to SBML symbol `mRaslet7`.'),
        'ras_0_0001': ('Ras', 'dimensionless', 'Tracks Ras = 0 0001. Maps to SBML symbol `Ras`.'),
        'stat3_0_0001': ('STAT3', 'dimensionless', 'Tracks STAT3 = 0 0001. Maps to SBML symbol `STAT3`.'),
        'mi_model_state_r21_0_0003': ('miR21', 'dimensionless', 'Tracks Mi Model state R21 = 0 0003. Maps to SBML symbol `miR21`.'),
        'model_state_m_pten_0_01': ('mPTEN', 'dimensionless', 'Tracks Model state M PTEN = 0 01. Maps to SBML symbol `mPTEN`.'),
        'mi_rmpten': ('miRmpten', 'dimensionless', 'Tracks Mi Rmpten. Maps to SBML symbol `miRmpten`.'),
        'pten_0_17': ('PTEN', 'dimensionless', 'Tracks PTEN = 0 17. Maps to SBML symbol `PTEN`.'),
        'model_state_m_md': ('mMd', 'dimensionless', 'Tracks Model state M Md. Maps to SBML symbol `mMd`.'),
        'md_0_01': ('Md', 'dimensionless', 'Tracks Md = 0 01. Maps to SBML symbol `Md`.'),
        'model_state_m_mdlet7': ('mMdlet7', 'dimensionless', 'Tracks Model state M Mdlet7. Maps to SBML symbol `mMdlet7`.'),
        'e2f_transcription_factor': ('E2F', 'dimensionless', 'Tracks E2F transcription factor. Maps to SBML symbol `E2F`.'),
        'model_state_m_me': ('mMe', 'dimensionless', 'Tracks Model state M Me. Maps to SBML symbol `mMe`.'),
        'me_0_01': ('Me', 'dimensionless', 'Tracks Me = 0 01. Maps to SBML symbol `Me`.'),
        'model_state_m_melet7': ('mMelet7', 'dimensionless', 'Tracks Model state M Melet7. Maps to SBML symbol `mMelet7`.'),
        'model_state_m_ma': ('mMa', 'dimensionless', 'Tracks Model state M Ma. Maps to SBML symbol `mMa`.'),
        'ma_0_01': ('Ma', 'dimensionless', 'Tracks Ma = 0 01. Maps to SBML symbol `Ma`.'),
        'model_state_m_malet7': ('mMalet7', 'dimensionless', 'Tracks Model state M Malet7. Maps to SBML symbol `mMalet7`.'),
        'model_state_m_mb': ('mMb', 'dimensionless', 'Tracks Model state M Mb. Maps to SBML symbol `mMb`.'),
        'mb_0_01': ('Mb', 'dimensionless', 'Tracks Mb = 0 01. Maps to SBML symbol `Mb`.'),
        'model_state_m_mblet7': ('mMblet7', 'dimensionless', 'Tracks Model state M Mblet7. Maps to SBML symbol `mMblet7`.'),
        'apc_c_c_0_01': ('APC', 'dimensionless', 'Tracks APC/C/C = 0 01. Maps to SBML symbol `APC`.'),
        'total_let_7_micro_rna': ('Let7TOT', 'dimensionless', 'Tracks Total let-7 microRNA. Maps to SBML symbol `Let7TOT`.'),
        'inactive_nf_k_b': ('NFKBi', 'dimensionless', 'Tracks Inactive NF-kB. Maps to SBML symbol `NFKBi`.'),
        'model_time': ('t', 'dimensionless', 'Tracks Model Time. Maps to SBML symbol `t`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL1906070001.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
GRard2019CouplingTheCellCycleAndTheCellModel1906070001Model = SbmlGerard2019CouplingTheCellCycleAndTheCell

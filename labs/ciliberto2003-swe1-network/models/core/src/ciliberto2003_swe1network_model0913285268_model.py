# SPDX-FileCopyrightText: 2025-present Demi <bjaiye1@gmail.com>
#
# SPDX-License-Identifier: MIT
"""TelluriumSBMLBioModule wrapper for Ciliberto2003_Swe1Network.

Source: biomodels_ebi:MODEL0913285268
Original: https://www.ebi.ac.uk/biomodels/MODEL0913285268
"""
from __future__ import annotations

from typing import Any, Optional

from biosim.contrib.sbml import TelluriumSBMLBioModule


class SbmlCiliberto2003Swe1network(TelluriumSBMLBioModule):
    """BioModule wrapper for SBML model: Ciliberto2003_Swe1Network."""

    _SBML_ID = 'MODEL0913285268'
    _TITLE = 'Ciliberto2003_Swe1Network'
    _TIME_UNIT = 'model_time'
    _OBSERVABLE_STRATEGY = 'rate_rules'
    _OBSERVABLES = [
        'Clb2',
        'PClb2',
        'Trim',
        'PTrim',
        'Mcm_a',
        'Sic1',
        'Mih1_a',
        'IE_a',
        'Cdc20_a',
        'Cdc20',
        'Cdh1_a',
        'Cln',
        'SBF_a',
        'Swe1',
        'PSwe1',
        'Swe1M',
        'PSwe1M',
        'BE',
        'M',
        'BUD',
        'Cdh1',
        'IE',
        'Mcm',
        'Mih1',
        'SBF',
        'Swe1_total',
        'kmih',
        'kswe',
    ]
    _SPECIES_LABELS = {
        'Clb2': 'Clb2 mitotic cyclin',
        'PClb2': 'Phosphorylated Clb2',
        'Trim': 'Trimer complex',
        'PTrim': 'Phosphorylated trimer complex',
        'Mcm_a': 'Mcm A',
        'Sic1': 'Sic1 CDK inhibitor',
        'Mih1_a': 'Mih1 A',
        'IE_a': 'IE A',
        'Cdc20_a': 'Cdc20 A',
        'Cdc20': 'Cdc20 APC/C activator',
        'Cdh1_a': 'Cdh1 A',
        'Cln': 'G1 cyclin pool',
        'SBF_a': 'SBF A',
        'Swe1': 'Swe1 inhibitory kinase',
        'PSwe1': 'Phosphorylated Swe1',
        'Swe1M': 'Membrane-associated Swe1',
        'PSwe1M': 'Membrane-associated phosphorylated Swe1',
        'BE': 'Model state BE',
        'M': 'Model state M (M)',
        'BUD': 'Budding index',
        'Cdh1': 'Cdh1 APC/C activator',
        'IE': 'Model state IE',
        'Mcm': 'MCM replication licensing complex',
        'Mih1': 'Mih1 activating phosphatase',
        'SBF': 'SBF transcription factor',
        'Swe1_total': 'Swe1 Total',
        'kmih': 'Kmih',
        'kswe': 'Kswe',
    }
    _PARAMETER_INPUTS = {}
    _HEADLINE_OUTPUTS = {
        'clb2_mitotic_cyclin': ('Clb2', 'dimensionless', 'Tracks Clb2 mitotic cyclin. Maps to SBML symbol `Clb2`.'),
        'phosphorylated_clb2': ('PClb2', 'dimensionless', 'Tracks Phosphorylated Clb2. Maps to SBML symbol `PClb2`.'),
        'trimer_complex': ('Trim', 'dimensionless', 'Tracks Trimer complex. Maps to SBML symbol `Trim`.'),
        'phosphorylated_trimer_complex': ('PTrim', 'dimensionless', 'Tracks Phosphorylated trimer complex. Maps to SBML symbol `PTrim`.'),
        'mcm_a': ('Mcm_a', 'dimensionless', 'Tracks Mcm A. Maps to SBML symbol `Mcm_a`.'),
        'sic1_cdk_inhibitor': ('Sic1', 'dimensionless', 'Tracks Sic1 CDK inhibitor. Maps to SBML symbol `Sic1`.'),
        'mih1_a': ('Mih1_a', 'dimensionless', 'Tracks Mih1 A. Maps to SBML symbol `Mih1_a`.'),
        'ie_a': ('IE_a', 'dimensionless', 'Tracks IE A. Maps to SBML symbol `IE_a`.'),
        'cdc20_a': ('Cdc20_a', 'dimensionless', 'Tracks Cdc20 A. Maps to SBML symbol `Cdc20_a`.'),
        'cdc20_apc_c_activator': ('Cdc20', 'dimensionless', 'Tracks Cdc20 APC/C activator. Maps to SBML symbol `Cdc20`.'),
        'cdh1_a': ('Cdh1_a', 'dimensionless', 'Tracks Cdh1 A. Maps to SBML symbol `Cdh1_a`.'),
        'g1_cyclin_pool': ('Cln', 'dimensionless', 'Tracks G1 cyclin pool. Maps to SBML symbol `Cln`.'),
        'sbf_a': ('SBF_a', 'dimensionless', 'Tracks SBF A. Maps to SBML symbol `SBF_a`.'),
        'swe1_inhibitory_kinase': ('Swe1', 'dimensionless', 'Tracks Swe1 inhibitory kinase. Maps to SBML symbol `Swe1`.'),
        'phosphorylated_swe1': ('PSwe1', 'dimensionless', 'Tracks Phosphorylated Swe1. Maps to SBML symbol `PSwe1`.'),
        'membrane_associated_swe1': ('Swe1M', 'dimensionless', 'Tracks Membrane-associated Swe1. Maps to SBML symbol `Swe1M`.'),
        'membrane_associated_phosphorylated_swe1': ('PSwe1M', 'dimensionless', 'Tracks Membrane-associated phosphorylated Swe1. Maps to SBML symbol `PSwe1M`.'),
        'model_state_be': ('BE', 'dimensionless', 'Tracks Model state BE. Maps to SBML symbol `BE`.'),
        'model_state_m_m': ('M', 'dimensionless', 'Tracks Model state M (M). Maps to SBML symbol `M`.'),
        'budding_index': ('BUD', 'dimensionless', 'Tracks Budding index. Maps to SBML symbol `BUD`.'),
        'cdh1_apc_c_activator': ('Cdh1', 'dimensionless', 'Tracks Cdh1 APC/C activator. Maps to SBML symbol `Cdh1`.'),
        'model_state_ie': ('IE', 'dimensionless', 'Tracks Model state IE. Maps to SBML symbol `IE`.'),
        'mcm_replication_licensing_complex': ('Mcm', 'dimensionless', 'Tracks MCM replication licensing complex. Maps to SBML symbol `Mcm`.'),
        'mih1_activating_phosphatase': ('Mih1', 'dimensionless', 'Tracks Mih1 activating phosphatase. Maps to SBML symbol `Mih1`.'),
        'sbf_transcription_factor': ('SBF', 'dimensionless', 'Tracks SBF transcription factor. Maps to SBML symbol `SBF`.'),
        'swe1_total': ('Swe1_total', 'dimensionless', 'Tracks Swe1 Total. Maps to SBML symbol `Swe1_total`.'),
        'kmih': ('kmih', 'first_order_rate_constant', 'Tracks Kmih. Maps to SBML symbol `kmih`.'),
        'kswe': ('kswe', 'first_order_rate_constant', 'Tracks Kswe. Maps to SBML symbol `kswe`.'),
    }

    def __init__(self, model_path: str = 'data/MODEL0913285268.xml', integration_step: float = 0.01) -> None:
        super().__init__(model_path=model_path, integration_step=integration_step)

    def inputs(self):
        specs = super().inputs()
        specs.pop("integration_step", None)
        return specs


# Canonical alias for stable entrypoint naming.
Ciliberto2003Swe1networkModel0913285268Model = SbmlCiliberto2003Swe1network

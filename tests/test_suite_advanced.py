"""
Runs all advanced tests included in the tests folder.

This script creates and runs all tests considered in the "advanced" tests groups,
as opposed to "basic" tests.
"""

import pytest

common_adv_path = r"tests/common/common_advanced"
pop_adv_path = r"tests/population/population_advanced"
org_adv_path = r"tests/organism/organism_advanced"
analysis_adv_path = r"tests/analysis/analysis_advanced"

pytest.main(["-v", "-s", common_adv_path, pop_adv_path, org_adv_path, analysis_adv_path])



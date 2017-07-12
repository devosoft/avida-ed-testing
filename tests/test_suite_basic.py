"""
Runs all basic tests included in the tests folder.

This script creates and runs all tests considered in the "basic" tests groups,
as opposed to "advanced" tests.
"""

import pytest

common_basic_path = r"tests/common/common_basic"
pop_basic_path = r"tests/population/population_basic"
org_basic_path = r"tests/organism/organism_basic"
analysis_basic_path = r"tests/analysis/analysis_basic"

pytest.main(["-v", "-s", common_basic_path, pop_basic_path, org_basic_path, analysis_basic_path])




"""
Runs all advanced tests included in the tests folder.

This script creates and runs all tests considered in the "advanced" tests groups
as opposed to "basic" tests.
"""

import pytest
import sys

if __name__ == "__main__":
    common_adv_path = r"tests/common/common_advanced"
    pop_adv_path = r"tests/population/population_advanced"
    org_adv_path = r"tests/organism/organism_advanced"
    analysis_adv_path = r"tests/analysis/analysis_advanced"

    pytest_args = ["-v",
                   "--junitxml=./output/junit_xml/junit_xml.log",
                   "--html=./output/html_report/html_report.html",
                   "--self-contained-html",
                   common_adv_path,
                   pop_adv_path,
                   org_adv_path,
                   analysis_adv_path]

    pytest_args.extend(sys.argv)
    pytest.main(pytest_args)



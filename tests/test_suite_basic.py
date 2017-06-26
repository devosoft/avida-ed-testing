"""
Runs all basis tests included in the tests folder.

This script creates and runs all tests considered in the "basic" tests groups,
as opposed to "advanced" tests.
"""

import unittest
import os

from tests.common import common_basic
from tests.population import population_basic
from tests.organism import organism_basic
from tests.analysis import analysis_basic

common_basic_path = r"tests/common/common_basic"
pop_basic_path = r"tests/population/population_basic"
org_basic_path = r"tests/organism/organism_basic"
analysis_basic_path = r"tests/analysis/analysis_basic"

test_pattern = "*_test.py"
tld = os.path.abspath(os.path.join(os.getcwd(), os.pardir))

common_basic_tests = unittest.TestLoader().\
    discover(start_dir=common_basic_path,
             top_level_dir=tld,
             pattern=test_pattern)

pop_basic_tests = unittest.TestLoader().\
    discover(start_dir=pop_basic_path,
             top_level_dir=tld,
             pattern=test_pattern)

org_basic_tests = unittest.TestLoader().\
    discover(start_dir=org_basic_path,
             top_level_dir=tld,
             pattern=test_pattern)

analysis_basic_tests = unittest.TestLoader().\
    discover(start_dir=analysis_basic_path,
             top_level_dir=tld,
             pattern=test_pattern)

basic_test_suite = unittest.TestSuite([common_basic_tests,
                                       pop_basic_tests,
                                       org_basic_tests,
                                       analysis_basic_tests])

unittest.TextTestRunner(verbosity=2).run(basic_test_suite)



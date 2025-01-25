from pathlib import Path
from robot.api import TestSuite
import pytest

@pytest.fixture
def test_data_dir() -> Path:
    return (Path(__file__).parent.parent / "test_data").resolve()

@pytest.fixture
def robot_test_case_skip_suite(test_data_dir) -> TestSuite:
    suite_file =  test_data_dir / "skip_test_case.robot"
    suite = TestSuite.from_file_system(suite_file)
    return suite

def test_after_failed_test_other_tests_should_be_skipped(robot_test_case_skip_suite, tmp_path):
    temp_output = tmp_path / "output.xml"
    result = robot_test_case_skip_suite.run(output=temp_output)
    assert result.suite.name == "Skip Test Case"
    passed_test = result.suite.tests[0]
    assert passed_test.status == "PASS"
    failed_test = result.suite.tests[1]
    assert failed_test.status == "FAIL" 
    skipped_tests = result.suite.tests[2:]
    assert [test.status == "SKIP" for test in skipped_tests]
from pathlib import Path
from robot.api import TestSuite
import pytest


@pytest.fixture
def test_data_dir() -> Path:
    return (Path(__file__).parent.parent / "test_data").resolve()


@pytest.fixture
def suite_one(test_data_dir) -> TestSuite:
    suite_file = test_data_dir / "skip_test_case_01.robot"
    suite = TestSuite.from_file_system(suite_file)
    return suite


@pytest.fixture
def suite_two(test_data_dir) -> TestSuite:
    suite_file = test_data_dir / "skip_test_case_02.robot"
    suite = TestSuite.from_file_system(suite_file)
    return suite


@pytest.fixture
def suite_all_tests_skipped(test_data_dir) -> TestSuite:
    suite_file = test_data_dir / "skip_suite.robot"
    suite = TestSuite.from_file_system(suite_file)
    return suite


def test_whole_suite_should_be_skipped_when_parent_setup_fail(
    suite_all_tests_skipped, tmp_path
):
    temp_output = tmp_path / "output.xml"
    result = suite_all_tests_skipped.run(output=temp_output)
    assert result.suite.name == "Skip Suite"
    skipped_tests = result.suite.tests
    for test in skipped_tests:
        assert test.status == "SKIP"


def test_after_failed_test_other_tests_should_be_skipped(suite_one, tmp_path):
    temp_output = tmp_path / "output.xml"
    result = suite_one.run(output=temp_output)
    assert result.suite.name == "Skip Test Case 01"
    passed_test = result.suite.tests[0]
    assert passed_test.status == "PASS"
    failed_test = result.suite.tests[1]
    assert failed_test.status == "FAIL"
    skipped_tests = result.suite.tests[2:]
    for test in skipped_tests:
        assert test.status == "SKIP"


def test_another_suite_should_be_executed_if_previous_suite_has_failed(
    suite_two, tmp_path
):
    temp_output = tmp_path / "output.xml"
    result = suite_two.run(output=temp_output)
    assert result.suite.name == "Skip Test Case 02"
    passed_tests = result.suite.tests[:2]
    for test in passed_tests:
        assert test.status == "PASS"
    failed_test = result.suite.tests[2]
    assert failed_test.status == "FAIL"
    skipped_tests = result.suite.tests[3:]
    for test in skipped_tests:
        assert test.status == "SKIP"

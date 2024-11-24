"""
This module contains end-to-end tests for the DataProcessor class.
"""

from pathlib import Path
from test.sample_data.e2e_sample_data.e2e_expected_results import e2e_expected_results
from src.utils.validation import validate_rp_entity_ids
from src.document_processor import DataProcessor
from src.utils.logging import log
from src.helpers.data_loader import load_json_data
from src.helpers.teardown import teardown


FILE_WITH_ERRORS_PATH_NON_RAR = "test/sample_data/e2e_sample_data/file_with_errors"
FILE_WITHOUT_ERRORS_PATH_NON_RAR = "test/sample_data/e2e_sample_data/file_without_errors"
FILE_WITH_ERRORS_PATH_RAR = "test/sample_data/e2e_sample_data/file_with_errors.rar"
FILE_WITHOUT_ERRORS_PATH_RAR = "test/sample_data/e2e_sample_data/file_without_errors.rar"


def test_e2e_document_analytics_without_errors_rar():
    """
    End-to-end test for the DataProcessor class using a rar file without errors.
    Ensures the log file is deleted after the test.
    """
    file_path = FILE_WITHOUT_ERRORS_PATH_RAR
    log_directory = "logs"
    log_file_path = Path(log_directory) / f"{Path(file_path).stem}.rar_logs.txt"
    data, temp_dir = load_json_data(file_path) # pylint: disable=unused-variable
    analytics = DataProcessor(data)
    results = analytics.process_analytics()
    expected_results = e2e_expected_results["without_errors"]
    assert (
        results == expected_results
    ), f"Failed E2E test without errors: {results} != {expected_results}"
    log(results, validate_rp_entity_ids(data), Path(file_path).name, log_directory)

    if log_file_path.exists():
        log_file_path.unlink()

    # Ensure the log file is deleted after the test
    if log_file_path.exists():
        teardown({"log_file_path": log_file_path})


def test_e2e_document_analytics_with_errors_rar():
    """
    End-to-end test for the DataProcessor class using a rar file with errors.
    Ensures the log file is deleted after the test.
    """
    file_path = FILE_WITH_ERRORS_PATH_RAR
    log_directory = "logs"
    log_file_path = Path(log_directory) / f"{Path(file_path).stem}.rar_logs.txt"
    data, temp_dir = load_json_data(file_path) # pylint: disable=unused-variable
    analytics = DataProcessor(data)
    results = analytics.process_analytics()
    expected_results = e2e_expected_results["with_errors"]
    assert (
        results == expected_results
    ), f"Failed E2E test with errors: {results} != {expected_results}"
    log(results, validate_rp_entity_ids(data), Path(file_path).name, log_directory)

    if log_file_path.exists():
        log_file_path.unlink()

    # Ensure the log file is deleted after the test
    if log_file_path.exists():
        teardown({"log_file_path": log_file_path})


def test_e2e_document_analytics_with_errors_non_rar():
    """
    End-to-end test for the DataProcessor class using a non rar file with errors.
    """
    file_path = FILE_WITH_ERRORS_PATH_NON_RAR
    log_directory = "logs"
    log_file_path = Path(log_directory) / f"{Path(file_path).stem}_logs.txt"
    data = load_json_data(file_path)
    analytics = DataProcessor(data)
    results = analytics.process_analytics()
    expected_results = e2e_expected_results["with_errors"]
    assert (
        results == expected_results
    ), f"Failed E2E test with errors: {results} != {expected_results}"
    log(results, validate_rp_entity_ids(data), Path(file_path).name, log_directory)

    if log_file_path.exists():
        log_file_path.unlink()

    # Ensure the log file is deleted after the test
    if log_file_path.exists():
        teardown({"log_file_path": log_file_path})


def test_e2e_document_analytics_without_errors_non_rar():
    """
    End-to-end test for the DataProcessor class using a non rar file without errors.
    """
    file_path = FILE_WITHOUT_ERRORS_PATH_NON_RAR
    log_directory = "logs"
    log_file_path = Path(log_directory) / f"{Path(file_path).stem}_logs.txt"
    data = load_json_data(file_path)
    analytics = DataProcessor(data)
    results = analytics.process_analytics()
    expected_results = e2e_expected_results["without_errors"]
    assert (
        results == expected_results
    ), f"Failed E2E test without errors: {results} != {expected_results}"
    log(results, validate_rp_entity_ids(data), Path(file_path).name, log_directory)

    if log_file_path.exists():
        log_file_path.unlink()

    # Ensure the log file is deleted after the test
    if log_file_path.exists():
        teardown({"log_file_path": log_file_path})

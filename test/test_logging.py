"""
This module contains tests for the format_rp_entity_id_logs function.
"""

from test.sample_data.logging_sample_data.format_rp_entity_id_logs_sample_data import (
    format_rp_entity_id_logs_sample_data,
)  # pylint: disable=E0611
from test.sample_data.logging_sample_data.format_process_data_logs_sample_data import (
    format_process_data_logs_sample_data,
)  # pylint: disable=E0611
import os
import logging
import pytest
from src.utils.logging import format_rp_entity_id_logs, format_process_data_logs, setup_logging


@pytest.mark.parametrize("scenario", list(format_rp_entity_id_logs_sample_data.keys()))
def test_format_rp_entity_id_logs(scenario):
    """
    Tests the format_rp_entity_id_logs function with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    errors = format_rp_entity_id_logs_sample_data[scenario]["errors"]
    expected_result = format_rp_entity_id_logs_sample_data[scenario]["expected_result"]
    result = format_rp_entity_id_logs(errors)
    assert result == expected_result, f"Failed on scenario '{scenario}'"


@pytest.mark.parametrize("scenario", list(format_process_data_logs_sample_data.keys()))
def test_format_process_data_logs(scenario):
    """
    Tests the format_process_data_logs function with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    results = format_process_data_logs_sample_data[scenario]["results"]
    expected_result = format_process_data_logs_sample_data[scenario]["expected_result"]
    result = format_process_data_logs(results)
    assert result == expected_result, f"Failed on scenario '{scenario}'"


def test_setup_logging_creates_log_directory_and_file(mocker):
    """
    Test that the setup_logging function creates the log directory and log file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
    """
    log_filename = "test_log.log"
    log_directory = os.path.join(os.getcwd(), "logs")
    log_file_path = os.path.join(log_directory, log_filename)

    # Mock os.makedirs to ensure it is called
    mock_makedirs = mocker.patch("os.makedirs")

    # Define a custom function to use as the side effect for os.path.exists
    def mock_exists(path):
        if path == log_directory:
            return False  # Simulate that the directory doesn't exist
        if path == log_file_path:
            return False  # Simulate that the log file doesn't exist
        return False

    # Mock os.path.exists to use the custom function as the side effect
    mock_exists = mocker.patch("os.path.exists", side_effect=mock_exists)

    # Mock open to prevent actual file operations and simulate the file creation
    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    # Call the setup_logging function
    setup_logging(log_directory, log_filename)

    # Assertions for log directory creation
    # Verify that os.makedirs was called exactly once with the log_directory as its argument
    mock_makedirs.assert_called_once_with(log_directory)

    # Verify that the open function was called exactly once with the correct arguments
    # This ensures that setup_logging attempts to create or append to the log file.
    # The "a" mode stands for "append", meaning the log file is opened for writing at the end of the file if it exists.
    mock_open.assert_called_once_with(log_file_path, "a", encoding=None, errors=None)

    # Clean up by removing handlers to avoid side effects on other tests
    # Get the root logger
    logger = logging.getLogger()
    # Iterate over a copy of the list of handlers and remove each one
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)


def test_setup_logging_creates_log_file(mocker):
    """
    Test that the setup_logging function creates the log file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
    """
    log_filename = "test_log.log"
    log_directory = os.path.join(os.getcwd(), "logs")
    log_file_path = os.path.join(log_directory, log_filename)

    # Mock os.makedirs to ensure it is called
    mock_makedirs = mocker.patch("os.makedirs")

    # Define a custom function to use as the side effect for os.path.exists
    def mock_exists(path):
        if path == log_directory:
            return False  # Simulate that the directory doesn't exist
        if path == log_file_path:
            return False  # Simulate that the log file doesn't exist
        return False

    # Mock os.path.exists to use the custom function as the side effect
    mock_exists = mocker.patch("os.path.exists", side_effect=mock_exists)

    # Mock open to prevent actual file operations and simulate the file creation
    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    # Call the setup_logging function
    setup_logging(log_directory, log_filename)

    # Assertions for log directory creation
    # Verify that os.makedirs was called exactly once with the log_directory as its argument
    mock_makedirs.assert_called_once_with(log_directory)

    # Verify that the open function was called exactly once with the correct arguments
    # This ensures that setup_logging attempts to create or append to the log file.
    # The "a" mode stands for "append", meaning the log file is opened for writing at the end of the file if it exists.
    mock_open.assert_called_once_with(log_file_path, "a", encoding=None, errors=None)

    # Clean up by removing handlers to avoid side effects on other tests
    # Get the root logger
    logger = logging.getLogger()
    # Iterate over a copy of the list of handlers and remove each one
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)


def test_setup_logging_adds_separator_to_existing_log_file(mocker):
    """
    Test that the setup_logging function adds a separator to an existing log file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
    """
    log_filename = "test_log.log"
    log_directory = os.path.join(os.getcwd(), "logs")
    log_file_path = os.path.join(log_directory, log_filename)

    # Mock os.makedirs to ensure it is called
    mock_makedirs = mocker.patch("os.makedirs")  # pylint: disable=unused-variable

    # Define a custom function to use as the side effect for os.path.exists
    def mock_exists(path):
        if path == log_directory:
            return True  # Simulate that the directory exists
        if path == log_file_path:
            return True  # Simulate that the log file exists
        return False

    # Mock os.path.exists to use the custom function as the side effect
    mock_exists = mocker.patch("os.path.exists", side_effect=mock_exists)

    # Mock open to simulate file operations
    mock_open = mocker.patch("builtins.open", mocker.mock_open())

    # Call the setup_logging function
    setup_logging(log_directory, log_filename)

    # Ensure that the separator was written to the existing log file
    mock_open().write.assert_any_call("\n\n-----\n\n")

    # Clean up by removing handlers to avoid side effects on other tests
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

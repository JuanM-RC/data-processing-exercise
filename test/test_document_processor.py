"""
This module contains tests for the DataProcessor class.
"""

from test.sample_data.processor_sample_data.process_analytics_sample_data import (
    process_analytics_sample_data,
)
from test.sample_data.processor_sample_data.count_distinct_stories_sample_data import (
    count_distinct_stories_sample_data,
)
from test.sample_data.processor_sample_data.initialize_document_record_sample_data import (
    initialize_document_record_sample_data,
)
from test.sample_data.processor_sample_data.identify_invalid_document_ids_sample_data import (
    identify_invalid_document_ids_sample_data,
)
from test.sample_data.processor_sample_data.check_and_log_document_count_sample_data import (
    check_and_log_document_count_sample_data,
)
from test.sample_data.processor_sample_data.handle_document_count_sample_data import (
    handle_document_count_sample_data,
)
from test.sample_data.processor_sample_data.validate_index_sample_data import (
    validate_index_sample_data,
)
from test.sample_data.processor_sample_data.handle_duplicates_sample_data import (
    handle_duplicates_sample_data,
)
from test.sample_data.processor_sample_data.identify_missing_indices_sample_data import (
    identify_missing_indices_sample_data,
)
from test.sample_data.processor_sample_data.get_field_sample_data import get_field_sample_data


import pytest
from src.document_processor import DataProcessor


@pytest.fixture
def document_analytics():
    """
    Fixture to initialize the DataProcessor object with a mock of document_records.
    """
    return DataProcessor([])  # Assuming no data initially, but document_records is being tested.


@pytest.mark.parametrize(
    "scenario", list(count_distinct_stories_sample_data.keys())  # Dynamically get all scenario keys
)
def test_count_distinct_stories(scenario):
    """
    Tests the count_distinct_stories method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = count_distinct_stories_sample_data[scenario]["sample_data"]
    expected_distinct_stories = count_distinct_stories_sample_data[scenario]["expected_results"][
        "distinct_stories_count"
    ]
    processor = DataProcessor(sample_data)
    assert processor.count_distinct_stories() == expected_distinct_stories


@pytest.mark.parametrize("scenario", list(initialize_document_record_sample_data.keys()))
def test_initialize_document_record(scenario):
    """
    Tests the initialize_document_record method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = initialize_document_record_sample_data[scenario]["sample_data"]
    expected_results = initialize_document_record_sample_data[scenario]["expected_results"]

    # Create an instance of DataProcessor with an empty list
    # This is because the initialize_document_record method does not depend on the initial data
    processor = DataProcessor([])

    # Iterate over each document ID in the sample data and test the initialization
    # The zip function is used to pair each document ID with its corresponding expected result
    for document_id, expected in zip(sample_data, expected_results):
        # Call the initialize_document_record method with the document ID
        result = processor.initialize_document_record(document_id)

        # Assert that the method's result matches the expected result
        assert (
            result == expected
        ), f"Failed on scenario '{scenario}' with document_id '{document_id}'"


@pytest.mark.parametrize("scenario", list(identify_invalid_document_ids_sample_data.keys()))
def test_identify_invalid_document_ids(scenario):
    """
    Tests the identify_invalid_document_ids method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = identify_invalid_document_ids_sample_data[scenario]["sample_data"]
    expected_results = identify_invalid_document_ids_sample_data[scenario]["expected_results"]
    processor = DataProcessor(sample_data)
    processor.identify_invalid_document_ids()
    actual_results = processor.results["indexing_errors"].get("invalid_document_ids")
    assert actual_results == expected_results, f"Failed on scenario '{scenario}'"


@pytest.mark.parametrize(
    "scenario",
    list(check_and_log_document_count_sample_data.keys()),
)
def test_check_and_log_document_count(scenario):
    """
    Tests the check_and_log_document_count method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = check_and_log_document_count_sample_data[scenario]["sample_data"]
    expected_results = check_and_log_document_count_sample_data[scenario]["expected_results"]
    processor = DataProcessor([])
    for data in sample_data:
        processor.check_and_log_document_count(data["record_count"], data["document_id"])
    actual_results = processor.results.get("invalid_document_counts")
    assert (
        actual_results == expected_results["invalid_document_counts"]
    ), f"Failed on scenario '{scenario}'"


@pytest.mark.parametrize(
    "scenario", list(handle_document_count_sample_data.keys())  # Dynamically get all scenario keys
)
def test_handle_document_count(scenario):
    """
    Tests the handle_document_count method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = handle_document_count_sample_data[scenario]["sample_data"]
    expected_results = handle_document_count_sample_data[scenario]["expected_results"]

    # Initialize the DataProcessor class with an empty document_records
    # and results dictionary
    processor = DataProcessor([])
    processor.document_records = {
        doc["document_id"]: {"expected_count": None} for doc in sample_data
    }
    for data in sample_data:
        processor.handle_document_count(data["record_count"], data["document_id"])

    actual_document_records = {
        doc_id: {"expected_count": rec["expected_count"]}
        for doc_id, rec in processor.document_records.items()
    }
    actual_indexing_errors = processor.results.get("indexing_errors")
    assert (
        actual_document_records == expected_results["document_records"]
    ), f"Failed on scenario '{scenario}' (document_records)"
    assert (
        actual_indexing_errors == expected_results["indexing_errors"]
    ), f"Failed on scenario '{scenario}' (indexing_errors)"


@pytest.mark.parametrize(
    "scenario",
    list(validate_index_sample_data.keys()),
)
def test_validate_index(scenario):
    """
    Tests the validate_index method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = validate_index_sample_data[scenario]["sample_data"]
    expected_results = validate_index_sample_data[scenario]["expected_results"]

    # Initialize the DataProcessor class with an empty document_records
    # and results dictionary
    processor = DataProcessor([])
    processor.document_records = {
        doc["document_id"]: {"expected_count": doc["expected_count"], "logged_out_of_range": set()}
        for doc in sample_data
    }
    actual_valid = []
    for data in sample_data:
        result = processor.validate_index(data["record_index"], data["document_id"])
        actual_valid.append(result)
    actual_indexing_errors = processor.results.get("indexing_errors")
    assert actual_valid == expected_results["valid"], f"Failed on scenario '{scenario}' (valid)"
    assert (
        actual_indexing_errors == expected_results["indexing_errors"]
    ), f"Failed on scenario '{scenario}' (indexing_errors)"


@pytest.mark.parametrize("scenario", list(handle_duplicates_sample_data.keys()))
def test_handle_duplicates(scenario):
    """
    Tests the handle_duplicates method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = handle_duplicates_sample_data[scenario]["sample_data"]
    expected_results = handle_duplicates_sample_data[scenario]["expected_results"]

    # Initialize the DataProcessor class with an empty document_records dictionary
    processor = DataProcessor([])
    processor.document_records = {
        doc["document_id"]: {
            "data": {},
            "indices": set(),
            "identical_duplicates": {},
            "different_duplicates": {},
        }
        for doc in sample_data
    }
    for data in sample_data:
        processor.handle_duplicates(data["record"], data["record_index"], data["document_id"])

    actual_document_records = processor.document_records
    actual_identical_duplicates = processor.results.get("identical_duplicates", {})
    actual_different_duplicates = processor.results.get("different_duplicates", {})

    assert (
        actual_document_records == expected_results["document_records"]
    ), f"Failed on scenario '{scenario}' (document_records)"
    assert actual_identical_duplicates == expected_results.get(
        "identical_duplicates", {}
    ), f"Failed on scenario '{scenario}' (identical_duplicates)"
    assert actual_different_duplicates == expected_results.get(
        "different_duplicates", {}
    ), f"Failed on scenario '{scenario}' (different_duplicates)"


@pytest.mark.parametrize(
    "scenario",
    list(identify_missing_indices_sample_data.keys()),
)
def test_identify_missing_indices(scenario):
    """
    Tests the identify_missing_indices method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = identify_missing_indices_sample_data[scenario]["sample_data"]
    expected_results = identify_missing_indices_sample_data[scenario]["expected_results"]
    processor = DataProcessor([])
    processor.document_records = sample_data
    processor.identify_missing_indices()
    actual_missing = processor.results.get("missing")
    actual_extra_indices = processor.results.get("extra_indices")
    assert (
        actual_missing == expected_results["missing"]
    ), f"Failed on scenario '{scenario}' (missing)"
    assert (
        actual_extra_indices == expected_results["extra_indices"]
    ), f"Failed on scenario '{scenario}' (extra_indices)"


@pytest.mark.parametrize(
    "scenario",
    list(get_field_sample_data.keys()),
)
def test_get_field(scenario):
    """
    Tests the get_field method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = get_field_sample_data[scenario]["sample_data"]
    expected_result = get_field_sample_data[scenario]["expected_result"]
    processor = DataProcessor([])
    result = processor.get_field(sample_data["record"], sample_data["field_name"])
    assert result == expected_result, f"Failed on scenario '{scenario}'"


# This one is at the end because it integrates all the others.


@pytest.mark.parametrize(
    # Dynamically get all scenario keys
    "scenario",
    list(process_analytics_sample_data.keys()),
)
def test_process_analytics(scenario):
    """
    Tests the process_analytics method of the DataProcessor class with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = process_analytics_sample_data[scenario]["sample_data"]
    expected_results = process_analytics_sample_data[scenario]["expected_results"]
    processor = DataProcessor(sample_data)
    actual_results = processor.process_analytics()
    assert actual_results == expected_results, f"Failed on scenario '{scenario}'"

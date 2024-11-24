"""
This module contains tests for the validators module.
"""

from test.sample_data.validator_sample_data.check_missing_rp_entity_id_sample_data import (
    check_missing_rp_entity_id_sample_data,
)
from test.sample_data.validator_sample_data.validate_rp_entity_id_format_sample_data import (
    validate_rp_entity_id_format_sample_data,
)
from test.sample_data.validator_sample_data.validate_rp_document_id_sample_data import (
    validate_rp_document_id_sample_data,
)
from test.sample_data.validator_sample_data.validate_rp_entity_ids_sample_data import (
    validate_rp_entity_ids_sample_data,
)
import pytest
from src.utils.validation import (
    validate_rp_document_id,
    validate_rp_entity_ids,
    check_missing_rp_entity_id,
    validate_rp_entity_id_format,
)


@pytest.mark.parametrize("scenario", list(validate_rp_document_id_sample_data.keys()))
def test_validate_rp_document_id(scenario):
    """
    Tests the validate_rp_document_id function with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = validate_rp_document_id_sample_data[scenario]["sample_data"]
    expected_result = validate_rp_document_id_sample_data[scenario]["expected_result"]
    result = validate_rp_document_id(sample_data)
    assert result == expected_result, f"Failed for scenario: {scenario}"


@pytest.mark.parametrize("scenario", list(check_missing_rp_entity_id_sample_data.keys()))
def test_check_missing_rp_entity_id(scenario):
    """
    Tests the check_missing_rp_entity_id function with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = check_missing_rp_entity_id_sample_data[scenario]["sample_data"]
    expected_result = check_missing_rp_entity_id_sample_data[scenario]["expected_result"]
    result = check_missing_rp_entity_id(sample_data)
    assert result == expected_result, f"Failed for scenario: {scenario}"


# @pytest.mark.parametrize(
#     "scenario", list(check_empty_rp_entity_id_sample_data.keys())
# )
# def test_check_empty_rp_entity_id(scenario):
#     """
#     Tests the check_empty_rp_entity_id function with various scenarios.

#     Args:
#         scenario (str): The scenario name to test.
#     """
#     sample_data = check_empty_rp_entity_id_sample_data[scenario]["sample_data"]
#     expected_result = check_empty_rp_entity_id_sample_data[scenario]["expected_result"]
#     result = check_empty_rp_entity_id(sample_data)
#     assert result == expected_result, f"Failed for scenario: {scenario}"


@pytest.mark.parametrize("scenario", list(validate_rp_entity_id_format_sample_data.keys()))
def test_validate_rp_entity_id_format(scenario):
    """
    Tests the validate_rp_entity_id_format function with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = validate_rp_entity_id_format_sample_data[scenario]["sample_data"]
    expected_result = validate_rp_entity_id_format_sample_data[scenario]["expected_result"]
    result = validate_rp_entity_id_format(
        sample_data["rp_entity_id"], sample_data["rp_document_id"], sample_data["document_index"]
    )
    assert result == expected_result, f"Failed for scenario: {scenario}"


@pytest.mark.parametrize("scenario", list(validate_rp_entity_ids_sample_data.keys()))
def test_validate_rp_entity_ids(scenario):
    """
    Tests the validate_rp_entity_ids function with various scenarios.

    Args:
        scenario (str): The scenario name to test.
    """
    sample_data = validate_rp_entity_ids_sample_data[scenario]["sample_data"]
    expected_result = validate_rp_entity_ids_sample_data[scenario]["expected_result"]
    result = validate_rp_entity_ids(sample_data)
    assert result == expected_result, f"Failed for scenario: {scenario}"

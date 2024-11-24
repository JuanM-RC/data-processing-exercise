"""
This module contains sample data for testing the validate_rp_document_id function.
"""

validate_rp_document_id_sample_data = {
    "rp_document_id_none": {
        "sample_data": {"RP_DOCUMENT_ID": None, "DOCUMENT_RECORD_INDEX": 1},
        "expected_result": (None, None, 1),
    },
    "rp_document_id_empty_string": {
        "sample_data": {"RP_DOCUMENT_ID": "", "DOCUMENT_RECORD_INDEX": 2},
        "expected_result": ("", None, 2),
    },
    "rp_document_id_valid_string": {
        "sample_data": {"RP_DOCUMENT_ID": "DOC123", "DOCUMENT_RECORD_INDEX": 3},
        "expected_result": None,
    },
    "rp_document_id_missing": {
        "sample_data": {"DOCUMENT_RECORD_INDEX": 4},
        "expected_result": (None, None, 4),
    },
    "rp_document_id_non_empty_string": {
        "sample_data": {"RP_DOCUMENT_ID": "DOC456", "DOCUMENT_RECORD_INDEX": 5},
        "expected_result": None,
    },
    "rp_document_id_whitespace_string": {
        "sample_data": {"RP_DOCUMENT_ID": "   ", "DOCUMENT_RECORD_INDEX": 6},
        "expected_result": (None, None, 6),
    },
    "rp_document_id_mixed_case_string": {
        "sample_data": {"RP_DOCUMENT_ID": "Doc789", "DOCUMENT_RECORD_INDEX": 7},
        "expected_result": None,
    },
    "rp_document_id_special_characters": {
        "sample_data": {"RP_DOCUMENT_ID": "DOC@#1", "DOCUMENT_RECORD_INDEX": 8},
        "expected_result": None,
    },
    "rp_document_id_boolean_true": {
        "sample_data": {"RP_DOCUMENT_ID": True, "DOCUMENT_RECORD_INDEX": 9},
        "expected_result": (None, None, 9),
    },
    "rp_document_id_boolean_false": {
        "sample_data": {"RP_DOCUMENT_ID": False, "DOCUMENT_RECORD_INDEX": 10},
        "expected_result": (None, None, 10),
    },
    "rp_document_id_numeric_value": {
        "sample_data": {"RP_DOCUMENT_ID": 12345, "DOCUMENT_RECORD_INDEX": 11},
        "expected_result": None,
    },
    "rp_document_id_list": {
        "sample_data": {"RP_DOCUMENT_ID": ["DOC123"], "DOCUMENT_RECORD_INDEX": 12},
        "expected_result": None,
    },
    "rp_document_id_dictionary": {
        "sample_data": {"RP_DOCUMENT_ID": {"id": "DOC123"}, "DOCUMENT_RECORD_INDEX": 13},
        "expected_result": None,
    },
    "rp_document_id_none_missing_index": {
        "sample_data": {"RP_DOCUMENT_ID": None},
        "expected_result": (None, None, None),
    },
    "rp_document_id_empty_string_missing_index": {
        "sample_data": {"RP_DOCUMENT_ID": ""},
        "expected_result": ("", None, None),
    },
    "rp_document_id_valid_string_missing_index": {
        "sample_data": {"RP_DOCUMENT_ID": "DOC123"},
        "expected_result": None,
    },
}

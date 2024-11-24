"""
This module contains sample data for testing the check_missing_rp_entity_id function.
"""

check_missing_rp_entity_id_sample_data = {
    "rp_entity_id_none": {
        "sample_data": {
            "RP_ENTITY_ID": None,
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 1,
        },
        "expected_result": (None, "DOC123", 1),
    },
    "rp_entity_id_missing": {
        "sample_data": {"RP_DOCUMENT_ID": "DOC123", "DOCUMENT_RECORD_INDEX": 2},
        "expected_result": (None, "DOC123", 2),
    },
    "rp_entity_id_valid": {
        "sample_data": {
            "RP_ENTITY_ID": "ENT123",
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 3,
        },
        "expected_result": None,
    },
    "rp_entity_id_empty_string": {
        "sample_data": {"RP_ENTITY_ID": "", "RP_DOCUMENT_ID": "DOC123", "DOCUMENT_RECORD_INDEX": 4},
        "expected_result": None,
    },
    "rp_entity_id_whitespace_string": {
        "sample_data": {
            "RP_ENTITY_ID": "   ",
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 5,
        },
        "expected_result": None,
    },
    "rp_entity_id_boolean_true": {
        "sample_data": {
            "RP_ENTITY_ID": True,
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 6,
        },
        "expected_result": None,
    },
    "rp_entity_id_boolean_false": {
        "sample_data": {
            "RP_ENTITY_ID": False,
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 7,
        },
        "expected_result": None,
    },
    "rp_entity_id_numeric_value": {
        "sample_data": {
            "RP_ENTITY_ID": 12345,
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 8,
        },
        "expected_result": None,
    },
    "rp_entity_id_list": {
        "sample_data": {
            "RP_ENTITY_ID": ["ENT123"],
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 9,
        },
        "expected_result": None,
    },
    "rp_entity_id_dictionary": {
        "sample_data": {
            "RP_ENTITY_ID": {"id": "ENT123"},
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 10,
        },
        "expected_result": None,
    },
    "rp_entity_id_special_characters": {
        "sample_data": {
            "RP_ENTITY_ID": "ENT@#1",
            "RP_DOCUMENT_ID": "DOC123",
            "DOCUMENT_RECORD_INDEX": 11,
        },
        "expected_result": None,
    },
}

"""
This module contains sample data for testing the validate_rp_entity_id_format function.
"""

validate_rp_entity_id_format_sample_data = {
    "valid_rp_entity_id": {
        "sample_data": {"rp_entity_id": "ABC123", "rp_document_id": "DOC001", "document_index": 1},
        "expected_result": None,
    },
    "invalid_rp_entity_id_length": {
        "sample_data": {"rp_entity_id": "ABC12", "rp_document_id": "DOC002", "document_index": 2},
        "expected_result": ("ABC12", "DOC002", 2),
    },
    "invalid_rp_entity_id_characters": {
        "sample_data": {"rp_entity_id": "ABC@#1", "rp_document_id": "DOC003", "document_index": 3},
        "expected_result": ("ABC@#1", "DOC003", 3),
    },
    "rp_entity_id_whitespace": {
        "sample_data": {"rp_entity_id": "   ", "rp_document_id": "DOC004", "document_index": 4},
        "expected_result": ("", "DOC004", 4),
    },
    "rp_entity_id_mixed_case": {
        "sample_data": {"rp_entity_id": "AbC123", "rp_document_id": "DOC005", "document_index": 5},
        "expected_result": ("AbC123", "DOC005", 5),
    },
    "rp_entity_id_numeric": {
        "sample_data": {"rp_entity_id": 123456, "rp_document_id": "DOC006", "document_index": 6},
        "expected_result": None,
    },
    "rp_entity_id_boolean_true": {
        "sample_data": {"rp_entity_id": True, "rp_document_id": "DOC007", "document_index": 7},
        "expected_result": ("True", "DOC007", 7),
    },
    "rp_entity_id_boolean_false": {
        "sample_data": {"rp_entity_id": False, "rp_document_id": "DOC008", "document_index": 8},
        "expected_result": ("False", "DOC008", 8),
    },
    "rp_entity_id_none": {
        "sample_data": {"rp_entity_id": None, "rp_document_id": "DOC009", "document_index": 9},
        "expected_result": ("None", "DOC009", 9),
    },
    "rp_entity_id_float_Invalid": {
        "sample_data": {"rp_entity_id": 123.456, "rp_document_id": "DOC010", "document_index": 10},
        "expected_result": ("123.456", "DOC010", 10),
    },
}

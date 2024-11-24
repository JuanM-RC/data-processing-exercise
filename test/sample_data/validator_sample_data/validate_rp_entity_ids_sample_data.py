"""
This module contains sample data for testing the validate_rp_entity_ids function.
"""

validate_rp_entity_ids_sample_data = {
    "all_valid_records": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC001", "RP_ENTITY_ID": "ABC123", "DOCUMENT_RECORD_INDEX": 1},
            {"RP_DOCUMENT_ID": "DOC002", "RP_ENTITY_ID": "DEF456", "DOCUMENT_RECORD_INDEX": 2},
            {"RP_DOCUMENT_ID": "DOC003", "RP_ENTITY_ID": "GHI789", "DOCUMENT_RECORD_INDEX": 3},
            {"RP_DOCUMENT_ID": "DOC005", "RP_ENTITY_ID": 123456, "DOCUMENT_RECORD_INDEX": 4},
        ],
        "expected_result": [],
    },
    "invalid_rp_document_id": {
        "sample_data": [
            {"RP_DOCUMENT_ID": None, "RP_ENTITY_ID": "ABC123", "DOCUMENT_RECORD_INDEX": 1},
            {"RP_DOCUMENT_ID": "", "RP_ENTITY_ID": "DEF456", "DOCUMENT_RECORD_INDEX": 2},
        ],
        "expected_result": [
            (None, None, 1),
            ("", None, 2),
        ],
    },
    "missing_rp_entity_id": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC001", "RP_ENTITY_ID": None, "DOCUMENT_RECORD_INDEX": 1},
            {"RP_DOCUMENT_ID": "DOC002", "DOCUMENT_RECORD_INDEX": 2},
        ],
        "expected_result": [
            (None, "DOC001", 1),
            (None, "DOC002", 2),
        ],
    },
    "empty_rp_entity_id": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC001", "RP_ENTITY_ID": "", "DOCUMENT_RECORD_INDEX": 1},
        ],
        "expected_result": [
            ("", "DOC001", 1),
        ],
    },
    "invalid_rp_entity_id_format": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC001", "RP_ENTITY_ID": "ABC12", "DOCUMENT_RECORD_INDEX": 1},
            {"RP_DOCUMENT_ID": "DOC002", "RP_ENTITY_ID": "ABC@#1", "DOCUMENT_RECORD_INDEX": 2},
            {"RP_DOCUMENT_ID": "DOC003", "RP_ENTITY_ID": "   ", "DOCUMENT_RECORD_INDEX": 3},
            {"RP_DOCUMENT_ID": "DOC004", "RP_ENTITY_ID": "AbC123", "DOCUMENT_RECORD_INDEX": 4},
            {"RP_DOCUMENT_ID": "DOC005", "RP_ENTITY_ID": True, "DOCUMENT_RECORD_INDEX": 5},
            {"RP_DOCUMENT_ID": "DOC006", "RP_ENTITY_ID": False, "DOCUMENT_RECORD_INDEX": 6},
            {"RP_DOCUMENT_ID": "DOC007", "RP_ENTITY_ID": None, "DOCUMENT_RECORD_INDEX": 7},
            {"RP_DOCUMENT_ID": "DOC008", "RP_ENTITY_ID": 123.456, "DOCUMENT_RECORD_INDEX": 8},
        ],
        "expected_result": [
            ("ABC12", "DOC001", 1),
            ("ABC@#1", "DOC002", 2),
            ("", "DOC003", 3),
            ("AbC123", "DOC004", 4),
            ("True", "DOC005", 5),
            ("False", "DOC006", 6),
            (None, "DOC007", 7),
            ("123.456", "DOC008", 8),
        ],
    },
}

"""
This module contains sample data for testing the format_rp_entity_id_logs function.
"""

format_rp_entity_id_logs_sample_data = {
    "no_errors": {
        "errors": [],
        "expected_result": "",
    },
    "missing_and_invalid_ids": {
        "errors": [
            (None, "DOC123", 1),
            ("INVALID_ID_1", "DOC123", 2),
            ("INVALID_ID_2", "DOC456", 3),
        ],
        "expected_result": (
            "--- RP Entity ID Validation Logs ---\n"
            "\nDocument ID DOC123:\n"
            "    - Missing RP_ENTITY_ID at index 1\n"
            "    - Invalid RP_ENTITY_ID: 'INVALID_ID_1' at index 2\n"
            "\nDocument ID DOC456:\n"
            "    - Invalid RP_ENTITY_ID: 'INVALID_ID_2' at index 3"
        ),
    },
    "only_missing_ids": {
        "errors": [
            (None, "DOC123", 1),
            (None, "DOC456", 2),
        ],
        "expected_result": (
            "--- RP Entity ID Validation Logs ---\n"
            "\nDocument ID DOC123:\n"
            "    - Missing RP_ENTITY_ID at index 1\n"
            "\nDocument ID DOC456:\n"
            "    - Missing RP_ENTITY_ID at index 2"
        ),
    },
    "only_invalid_ids": {
        "errors": [
            ("INVALID_ID_1", "DOC123", 1),
            ("INVALID_ID_2", "DOC456", 2),
        ],
        "expected_result": (
            "--- RP Entity ID Validation Logs ---\n"
            "\nDocument ID DOC123:\n"
            "    - Invalid RP_ENTITY_ID: 'INVALID_ID_1' at index 1\n"
            "\nDocument ID DOC456:\n"
            "    - Invalid RP_ENTITY_ID: 'INVALID_ID_2' at index 2"
        ),
    },
}

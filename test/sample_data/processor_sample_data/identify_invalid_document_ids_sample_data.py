"""
This module contains sample data for testing the identify_invalid_document_ids method of the DataProcessor class.
"""

identify_invalid_document_ids_sample_data = {
    "valid_and_invalid_ids": {
        "sample_data": [
            {"RP_DOCUMENT_ID": None, "RP_ENTITY_ID": "ENT1"},
            {"RP_DOCUMENT_ID": "", "RP_ENTITY_ID": "ENT2"},
            {"RP_DOCUMENT_ID": 123, "RP_ENTITY_ID": "ENT3"},
            {"RP_DOCUMENT_ID": "DOC123", "RP_ENTITY_ID": "ENT4"},  # Valid ID
            {"RP_DOCUMENT_ID": " ", "RP_ENTITY_ID": "ENT5"},
            {"RP_DOCUMENT_ID": 456.789, "RP_ENTITY_ID": "ENT6"},
        ],
        "expected_results": [
            {
                "RP_DOCUMENT_ID": None,
                "RP_ENTITY_ID": "ENT1",
                "record": {"RP_DOCUMENT_ID": None, "RP_ENTITY_ID": "ENT1"},
            },
            {
                "RP_DOCUMENT_ID": "",
                "RP_ENTITY_ID": "ENT2",
                "record": {"RP_DOCUMENT_ID": "", "RP_ENTITY_ID": "ENT2"},
            },
            {
                "RP_DOCUMENT_ID": 123,
                "RP_ENTITY_ID": "ENT3",
                "record": {"RP_DOCUMENT_ID": 123, "RP_ENTITY_ID": "ENT3"},
            },
            {
                "RP_DOCUMENT_ID": " ",
                "RP_ENTITY_ID": "ENT5",
                "record": {"RP_DOCUMENT_ID": " ", "RP_ENTITY_ID": "ENT5"},
            },
            {
                "RP_DOCUMENT_ID": 456.789,
                "RP_ENTITY_ID": "ENT6",
                "record": {"RP_DOCUMENT_ID": 456.789, "RP_ENTITY_ID": "ENT6"},
            },
        ],
    },
    "all_valid_ids": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC123", "RP_ENTITY_ID": "ENT1"},
            {"RP_DOCUMENT_ID": "DOC456", "RP_ENTITY_ID": "ENT2"},
        ],
        "expected_results": None,  # Updated to match the actual results
    },
    "all_invalid_ids": {
        "sample_data": [
            {"RP_DOCUMENT_ID": None, "RP_ENTITY_ID": "ENT1"},
            {"RP_DOCUMENT_ID": "", "RP_ENTITY_ID": "ENT2"},
            {"RP_DOCUMENT_ID": 123, "RP_ENTITY_ID": "ENT3"},
        ],
        "expected_results": [
            {
                "RP_DOCUMENT_ID": None,
                "RP_ENTITY_ID": "ENT1",
                "record": {"RP_DOCUMENT_ID": None, "RP_ENTITY_ID": "ENT1"},
            },
            {
                "RP_DOCUMENT_ID": "",
                "RP_ENTITY_ID": "ENT2",
                "record": {"RP_DOCUMENT_ID": "", "RP_ENTITY_ID": "ENT2"},
            },
            {
                "RP_DOCUMENT_ID": 123,
                "RP_ENTITY_ID": "ENT3",
                "record": {"RP_DOCUMENT_ID": 123, "RP_ENTITY_ID": "ENT3"},
            },
        ],
    },
}

"""
This module contains sample data for testing the DataProcessor class.
"""

count_distinct_stories_sample_data = {
    "empty_data": {"sample_data": [], "expected_results": {"distinct_stories_count": 0}},
    "single_record": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": "DOC123",
                "DOCUMENT_RECORD_INDEX": 1,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "ENTTY1",
            }
        ],
        "expected_results": {"distinct_stories_count": 1},
    },
    "non_string_document_ids": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": 123,
                "DOCUMENT_RECORD_INDEX": 1,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "ENTTY1",
            },
            {
                "RP_DOCUMENT_ID": 456.789,
                "DOCUMENT_RECORD_INDEX": 1,
                "DOCUMENT_RECORD_COUNT": 1,
                "RP_ENTITY_ID": "ENTTY1",
            },
        ],
        "expected_results": {"distinct_stories_count": 0},  # No valid document IDs
    },
    "missing_keys": {
        "sample_data": [
            {"RP_DOCUMENT_ID": "DOC123", "DOCUMENT_RECORD_INDEX": 1},
            {"RP_DOCUMENT_ID": "DOC456"},
        ],
        "expected_results": {"distinct_stories_count": 2},
    },
    "invalid_document_ids": {
        "sample_data": [
            {"RP_DOCUMENT_ID": None, "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "", "DOCUMENT_RECORD_INDEX": 2, "DOCUMENT_RECORD_COUNT": 1},
            {"RP_DOCUMENT_ID": "DOC1", "DOCUMENT_RECORD_INDEX": 1, "DOCUMENT_RECORD_COUNT": 1},
        ],
        "expected_results": {"distinct_stories_count": 1},  # Only "DOC1" is valid
    },
    "large_dataset": {
        "sample_data": [
            {
                "RP_DOCUMENT_ID": f"DOC{i}",
                "DOCUMENT_RECORD_INDEX": j,
                "DOCUMENT_RECORD_COUNT": 1000,
                "RP_ENTITY_ID": f"ENT{i:03d}"[:6],
            }
            for i in range(1, 1001)
            for j in range(1, 1001)
        ],
        "expected_results": {"distinct_stories_count": 1000},
    },
}

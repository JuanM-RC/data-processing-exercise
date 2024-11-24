"""
This module contains sample data for testing the check_and_log_document_count method of the DataProcessor class.
"""

check_and_log_document_count_sample_data = {
    "valid_counts": {
        "sample_data": [
            {"record_count": 5, "document_id": "DOC1"},
            {"record_count": "10", "document_id": "DOC2"},
        ],
        "expected_results": {"invalid_document_counts": {}},
    },
    "invalid_counts": {
        "sample_data": [
            {"record_count": 0, "document_id": "DOC1"},
            {"record_count": -1, "document_id": "DOC2"},
            {"record_count": "0", "document_id": "DOC3"},
            {"record_count": "abc", "document_id": "DOC4"},
            {"record_count": 5.5, "document_id": "DOC5"},
            {"record_count": "", "document_id": "DOC6"},
            {"record_count": "   ", "document_id": "DOC7"},
            {"record_count": None, "document_id": "DOC8"},
            {"record_count": True, "document_id": "DOC9"},
            {"record_count": "@#$%", "document_id": "DOC10"},
        ],
        "expected_results": {
            "invalid_document_counts": {
                "DOC1": [0],
                "DOC2": [-1],
                "DOC3": ["0"],
                "DOC4": ["abc"],
                "DOC5": [5.5],
                "DOC6": [""],
                "DOC7": ["   "],
                "DOC8": [None],
                "DOC9": [True],
                "DOC10": ["@#$%"],
            }
        },
    },
    "mixed_counts": {
        "sample_data": [
            {"record_count": 5, "document_id": "DOC1"},
            {"record_count": "abc", "document_id": "DOC2"},
            {"record_count": -1, "document_id": "DOC3"},
            {"record_count": "10", "document_id": "DOC4"},
        ],
        "expected_results": {"invalid_document_counts": {"DOC2": ["abc"], "DOC3": [-1]}},
    },
    "non_numeric_values": {
        "sample_data": [
            {"record_count": "abc", "document_id": "DOC1"},
            {"record_count": None, "document_id": "DOC2"},
            {"record_count": "@#$%", "document_id": "DOC3"},
            {"record_count": {"nested": "value"}, "document_id": "DOC4"},
            {"record_count": [1, 2, 3], "document_id": "DOC5"},
        ],
        "expected_results": {
            "invalid_document_counts": {
                "DOC1": ["abc"],
                "DOC2": [None],
                "DOC3": ["@#$%"],
                "DOC4": [{"nested": "value"}],
                "DOC5": [[1, 2, 3]],
            }
        },
    },
}

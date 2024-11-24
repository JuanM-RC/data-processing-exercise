"""
This module contains sample data for testing the handle_document_count method of the DataProcessor class.
"""

handle_document_count_sample_data = {
    "initial_count_set": {
        "sample_data": [
            {"record_count": 5, "document_id": "DOC1"},
            {"record_count": 10, "document_id": "DOC2"},
        ],
        "expected_results": {
            "document_records": {"DOC1": {"expected_count": 5}, "DOC2": {"expected_count": 10}},
            "indexing_errors": {},
        },
    },
    "count_mismatch": {
        "sample_data": [
            {"record_count": 5, "document_id": "DOC1"},
            {"record_count": 10, "document_id": "DOC2"},
            {"record_count": 7, "document_id": "DOC1"},
            {"record_count": 12, "document_id": "DOC2"},
        ],
        "expected_results": {
            "document_records": {"DOC1": {"expected_count": 5}, "DOC2": {"expected_count": 10}},
            "indexing_errors": {"DOC1": {"count_mismatch": [7]}, "DOC2": {"count_mismatch": [12]}},
        },
    },
    "no_mismatch_after_initial_set": {
        "sample_data": [
            {"record_count": 5, "document_id": "DOC1"},
            {"record_count": 5, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {"DOC1": {"expected_count": 5}},
            "indexing_errors": {},
        },
    },
    "zero_count": {
        "sample_data": [{"record_count": 0, "document_id": "DOC1"}],
        "expected_results": {
            "document_records": {"DOC1": {"expected_count": None}},
            "indexing_errors": {},
        },
    },
    "negative_count": {
        "sample_data": [{"record_count": -1, "document_id": "DOC1"}],
        "expected_results": {
            "document_records": {"DOC1": {"expected_count": None}},
            "indexing_errors": {},
        },
    },
    "non_integer_count": {
        "sample_data": [
            {"record_count": "invalid", "document_id": "DOC1"},
            {"record_count": 5.5, "document_id": "DOC2"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {"expected_count": None},
                "DOC2": {"expected_count": None},
            },
            "indexing_errors": {},
        },
    },
    "boolean_count": {
        "sample_data": [
            {"record_count": True, "document_id": "DOC1"},
            {"record_count": False, "document_id": "DOC2"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {"expected_count": None},
                "DOC2": {"expected_count": None},
            },
            "indexing_errors": {},
        },
    },
    "none_count": {
        "sample_data": [{"record_count": None, "document_id": "DOC1"}],
        "expected_results": {
            "document_records": {"DOC1": {"expected_count": None}},
            "indexing_errors": {},
        },
    },
}

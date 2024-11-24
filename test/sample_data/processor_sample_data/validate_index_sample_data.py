"""
This module contains sample data for testing the validate_index method of the DataProcessor class.
"""

validate_index_sample_data = {
    "valid_indices": {
        "sample_data": [
            {"record_index": 1, "document_id": "DOC1", "expected_count": 5},
            {"record_index": 5, "document_id": "DOC1", "expected_count": 5},
        ],
        "expected_results": {"valid": [True, True], "indexing_errors": {}},
    },
    "invalid_indices": {
        "sample_data": [
            {"record_index": 0, "document_id": "DOC1", "expected_count": 5},
            {"record_index": 6, "document_id": "DOC1", "expected_count": 5},
            {"record_index": "invalid", "document_id": "DOC1", "expected_count": 5},
            {"record_index": -1, "document_id": "DOC1", "expected_count": 5},
            {"record_index": True, "document_id": "DOC1", "expected_count": 5},
            {"record_index": "", "document_id": "DOC1", "expected_count": 5},
            {"record_index": "   ", "document_id": "DOC1", "expected_count": 5},
            {"record_index": "@#$%", "document_id": "DOC1", "expected_count": 5},
        ],
        "expected_results": {
            "valid": [False, False, False, False, False, False, False, False],
            "indexing_errors": {
                "DOC1": {
                    "out_of_range": [0, 6, -1],
                    "invalid_type": [
                        "Expected: int, Found: str for index: invalid",
                        "Expected: int, Found: bool for index: True",
                        "Expected: int, Found: str for index: ",
                        "Expected: int, Found: str for index:    ",
                        "Expected: int, Found: str for index: @#$%",
                    ],
                }
            },
        },
    },
    "mixed_indices": {
        "sample_data": [
            {"record_index": 1, "document_id": "DOC1", "expected_count": 5},
            {"record_index": "invalid", "document_id": "DOC1", "expected_count": 5},
            {"record_index": 3, "document_id": "DOC1", "expected_count": 5},
            {"record_index": 6, "document_id": "DOC1", "expected_count": 5},
        ],
        "expected_results": {
            "valid": [True, False, True, False],
            "indexing_errors": {
                "DOC1": {
                    "out_of_range": [6],
                    "invalid_type": ["Expected: int, Found: str for index: invalid"],
                }
            },
        },
    },
}

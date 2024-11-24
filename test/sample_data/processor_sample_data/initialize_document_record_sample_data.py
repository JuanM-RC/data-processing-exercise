initialize_document_record_sample_data = {
    "case_sensitivity": {
        "sample_data": ["doc123", "DOC123"],
        # Both document IDs should be valid and initialized
        "expected_results": [True, True],
    },
    "non_string_document_ids": {
        "sample_data": [123, 456.789],
        # Non-string document IDs should not be initialized
        "expected_results": [False, False],
    },
    "missing_keys": {
        "sample_data": ["DOC123", None],
        "expected_results": [True, False],  # None should not be initialized
    },
    "large_dataset": {
        "sample_data": [f"DOC{i}" for i in range(1, 1001)],
        # All should be valid and initialized
        "expected_results": [True] * 1000,
    },
    "empty_string_document_ids": {
        "sample_data": ["", "DOC123"],
        # Empty string should not be initialized
        "expected_results": [False, True],
    },
    "duplicate_document_ids": {
        "sample_data": ["DOC123", "DOC123"],
        # Duplicate IDs should be initialized only once
        "expected_results": [True, True],
    },
    "special_characters_document_ids": {
        "sample_data": ["DOC@123", "DOC#123"],
        "expected_results": [True, True],  # Special characters should be valid
    },
    "mixed_valid_invalid_document_ids": {
        "sample_data": ["DOC123", 456, None, "DOC789"],
        # Mixed valid and invalid IDs
        "expected_results": [True, False, False, True],
    },
}

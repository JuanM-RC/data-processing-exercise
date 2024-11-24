"""
This module contains sample data for testing the handle_duplicates method of the DataProcessor class.
"""

handle_duplicates_sample_data = {
    "no_duplicates": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "value2"}, "record_index": 2, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}, 2: {"field1": "value2"}},
                    "indices": {1, 2},
                    "identical_duplicates": {},
                    "different_duplicates": {},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {},
        },
    },
    "identical_duplicates": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {1: 1},
                    "different_duplicates": {},
                }
            },
            "identical_duplicates": {"DOC1": {1: 1}},
            "different_duplicates": {},
        },
    },
    "different_duplicates": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "value2"}, "record_index": 1, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
    "mixed_duplicates": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "value2"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "value1"}, "record_index": 2, "document_id": "DOC1"},
            {"record": {"field1": "value1"}, "record_index": 2, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}, 2: {"field1": "value1"}},
                    "indices": {1, 2},
                    "identical_duplicates": {2: 1},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {"DOC1": {2: 1}},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
    "duplicates_across_documents": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC2"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {},
                },
                "DOC2": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {},
                },
            },
            "identical_duplicates": {},
            "different_duplicates": {},
        },
    },
    "duplicates_with_different_data_types": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": 123}, "record_index": 1, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
    "duplicates_with_null_values": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": None}, "record_index": 1, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
    "duplicates_with_special_characters": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": "@#$%"}, "record_index": 1, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
    "duplicates_with_boolean_values": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {"record": {"field1": True}, "record_index": 1, "document_id": "DOC1"},
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
    "duplicates_with_extra_attribute": {
        "sample_data": [
            {"record": {"field1": "value1"}, "record_index": 1, "document_id": "DOC1"},
            {
                "record": {"field1": "value1", "field2": "extra"},
                "record_index": 1,
                "document_id": "DOC1",
            },
        ],
        "expected_results": {
            "document_records": {
                "DOC1": {
                    "data": {1: {"field1": "value1"}},
                    "indices": {1},
                    "identical_duplicates": {},
                    "different_duplicates": {1: 1},
                }
            },
            "identical_duplicates": {},
            "different_duplicates": {"DOC1": {1: 1}},
        },
    },
}

"""
This module serves as the entry point for the data processing and validation application.
It loads JSON data, counts distinct stories, processes analytics to find missing and duplicate entries,
and validates RP_ENTITY_IDs.
"""

import sys
from pathlib import Path
from document_processor import DataProcessor
from utils.validation import validate_rp_entity_ids
from utils.logging import log
from helpers.data_loader import load_json_data
from helpers.teardown import teardown

def main(file_path, log_directory):
    """
    Main function to load data, process analytics, and log the results.
    """
    
    if file_path.endswith(".rar"):
        data, temp_dir = load_json_data(file_path)
    else:
        data = load_json_data(file_path)
        temp_dir = None

    processor = DataProcessor(data)
    log(processor.process_analytics(), validate_rp_entity_ids(data), Path(file_path).name, log_directory)

    if temp_dir:
        teardown({"temp_dir": temp_dir})

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <path_to_file> <log_directory>")
        sys.exit(1)

    file_path = sys.argv[1]
    log_directory = sys.argv[2]
    main(file_path, log_directory)

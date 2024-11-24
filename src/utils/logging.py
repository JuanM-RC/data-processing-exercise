import logging
import os

# Set up logging configuration


import os
import logging

def setup_logging(log_directory, log_filename):
    """
    Sets up logging configuration to log messages to both the console and a log file.

    Args:
        log_directory (str): The directory where the log file will be stored.
        log_filename (str): The name of the log file where logs will be stored.
    """
    log_file_path = os.path.join(log_directory, log_filename)

    # Ensure the log directory exists
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    # Check if the log file already exists
    file_exists = os.path.exists(log_file_path)

    # If the file exists, add a separator before appending new logs
    if file_exists:
        with open(log_file_path, "a") as f:
            f.write("\n\n-----\n\n")

    logger = logging.getLogger()  # Get the root logger
    logger.setLevel(logging.INFO)  # Set the log level to INFO

    # Create handlers
    console_handler = (
        logging.StreamHandler()
    )  # For console output, we would remove it if we wanted to log only to file
    file_handler = logging.FileHandler(log_file_path, mode="a")  # For appending to file

    # Create log formatters
    formatter = logging.Formatter("%(asctime)s - %(message)s")
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def format_process_data_logs(results):
    """
    Formats the process data results into a log-friendly string.

    Args:
        results (dict): The results dictionary containing process data.

    Returns:
        str: A formatted string representing the process data logs.
    """
    log_lines = []

    # Log distinct story count from the results
    log_lines.append(f"Number of distinct stories: {results['distinct_stories_count']}")

    # Group logs for each document ID
    grouped_logs = {}

    # Missing indices (sorted numerically)
    for document_id, missing_indices in results.get("missing", {}).items():
        grouped_logs.setdefault(document_id, []).append(
            f"Missing indices: {sorted(missing_indices)}"
        )

    # Identical duplicates
    for document_id, duplicate_indices in results.get("identical_duplicates", {}).items():
        if duplicate_indices:
            duplicates = [
                f"index: {index}, repeated: {count} {'time' if count == 1 else 'times'}"
                for index, count in duplicate_indices.items()
            ]
            grouped_logs.setdefault(document_id, []).append(
                f"Identical duplicate indices: {', '.join(duplicates)}"
            )

    # Different duplicates
    for document_id, duplicate_indices in results.get("different_duplicates", {}).items():
        if duplicate_indices:
            duplicates = [
                f"index: {index}, repeated: {count} {'time' if count == 1 else 'times'}"
                for index, count in duplicate_indices.items()
            ]
            grouped_logs.setdefault(document_id, []).append(
                f"Different duplicate indices: {', '.join(duplicates)}"
            )

    # Indexing errors (Invalid Type and Out of Range errors)
    for document_id, errors in results.get("indexing_errors", {}).items():
        if "invalid_type" in errors and errors["invalid_type"]:
            invalid_type_errors = "\n        ".join(errors["invalid_type"])
            grouped_logs.setdefault(document_id, []).append(
                f"Invalid Type Errors:\n        {invalid_type_errors}"
            )

        # Sort out-of-range errors numerically
        if "out_of_range" in errors and errors["out_of_range"]:
            out_of_range_errors = sorted(errors["out_of_range"])
            out_of_range_errors_str = "\n        ".join(
                f"Out of range index: {error}" for error in out_of_range_errors
            )
            grouped_logs.setdefault(document_id, []).append(
                f"Out of Range Errors:\n        {out_of_range_errors_str}"
            )

    # Print logs grouped by document ID
    for document_id, messages in grouped_logs.items():
        log_lines.append(f"\nDocument ID {document_id}:")
        for message in messages:
            log_lines.append(f"    - {message}")

    return "\n".join(log_lines)


def format_rp_entity_id_logs(errors):
    """
    Formats the RP_ENTITY_ID validation errors into a log-friendly string.

    Args:
        errors (list): A list of tuples containing invalid RP_ENTITY_IDs and their corresponding document IDs and indices.

    Returns:
        str: A formatted string representing the RP_ENTITY_ID validation logs.
    """
    if not errors:
        return ""

    log_lines = ["--- RP Entity ID Validation Logs ---"]
    grouped_logs = {}

    # Group errors by document ID
    for error in errors:
        rp_entity_id, rp_document_id, document_index = error
        if rp_entity_id is None:
            message = f"Missing RP_ENTITY_ID at index {document_index}"
        else:
            message = f"Invalid RP_ENTITY_ID: '{rp_entity_id}' at index {document_index}"

        # Append the message to the grouped logs for each document ID
        grouped_logs.setdefault(rp_document_id, []).append(message)

    # Format the logs for each document ID
    for rp_document_id, messages in grouped_logs.items():
        log_lines.append(f"\nDocument ID {rp_document_id}:")
        for message in messages:
            log_lines.append(f"    - {message}")

    return "\n".join(log_lines)


def log(results, errors, processed_file="", log_directory=None, log_filename=None):
    """
    Logs all process data results and RP_ENTITY_ID validation errors.

    Args:
        results (dict): The results dictionary containing process data.
        errors (list): A list of tuples containing invalid RP_ENTITY_IDs and their corresponding document IDs and indices.
        processed_file (str): The name of the processed file to include in the log header.
        log_directory (str): The directory where the log file will be stored.
        log_filename (str): The name of the log file where logs will be stored. If None, defaults to '<processed_file>_logs'.
    """
    if log_filename is None:
        log_filename = f"{processed_file}_logs.txt"

    # Set up logging configuration
    setup_logging(log_directory, log_filename)

    # Call format_process_data_logs with results to get detailed logs
    process_data_logs = format_process_data_logs(results)

    # Call format_rp_entity_id_logs to log RP_ENTITY_ID issues
    rp_entity_id_logs = format_rp_entity_id_logs(errors)

    # Combine all logs into a single string and log
    # We always log process data logs because there's the story count,
    # but RP_ENTITY_ID logs are optional
    complete_logs = f"{processed_file}\n\n{process_data_logs}"
    if rp_entity_id_logs:
        complete_logs += f"\n\n{rp_entity_id_logs}"
    logging.info(complete_logs)
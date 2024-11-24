"""
This module contains functions for loading JSON data from files.
"""

import json
import os
import shutil
import tempfile
import patoolib


def create_temp_directory():
    """
    Creates a temporary directory using mkdtemp.

    Returns:
        str: The path to the created temporary directory.
    """
    temp_dir = tempfile.mkdtemp()
    return temp_dir


def extract_rar_file(rar_path, temp_dir):
    """
    Extracts a .rar file to a given temporary directory.

    Args:
        rar_path (str): The path to the .rar file.
        temp_dir (str): The path to the temporary directory where the .rar file will be extracted.

    Returns:
        str: The path to the extracted file, or None if no file is found.
    """
    try:
        # Extract the .rar file to the provided temp directory
        patoolib.extract_archive(rar_path, outdir=temp_dir)

        # Look for the extracted file in the temporary directory
        extracted_file_path = None
        for file_name in os.listdir(temp_dir):
            extracted_file_path = os.path.join(temp_dir, file_name)
            break  # Only pick the first file (or handle multiple if needed)

        return extracted_file_path if extracted_file_path else None
    except patoolib.util.PatoolError as e:
        print(f"Error extracting .rar file: {e}")
        return None


def cleanup_temp_directory(temp_dir):
    """
    Deletes the temporary directory and all its contents.

    Args:
        temp_dir (str): The directory to delete.
    """
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)  # Remove the directory and all its contents
        print(f"Deleted temporary directory: {temp_dir}")


def load_json_data(file_path):
    """
    Loads a list of JSON objects from a file. If the file is a .rar archive,
    it extracts the file from it and returns the parsed data.

    Args:
        file_path (str): The path to the JSON file or .rar file containing the JSON file.
        temp_dir (str, optional): The path to the temporary directory for extraction, if provided.

    Returns:
        tuple: A tuple containing:
            - list: A list of JSON objects loaded from the file.
            - str: The path to the temporary directory used for extraction (if any).
    """
    data = []
    temp_dir = None

    # Check if the file is a .rar file
    if file_path.endswith(".rar"):
        temp_dir = create_temp_directory()
        extracted_file_path = extract_rar_file(file_path, temp_dir)
        if not extracted_file_path:
            raise FileNotFoundError(f"No file found in the .rar archive: {file_path}")

        file_path = extracted_file_path

    # Now load the JSON data from the file
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                try:
                    data.append(json.loads(line.strip()))
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON line: {line.strip()}")
                    print(f"Error: {e}")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"No file found in the .rar archive: {file_path}") from exc
    if temp_dir:
        return data, temp_dir
    return data

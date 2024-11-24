"""
This module contains unit tests for the data_loader module, which includes functions
for loading JSON data from files, extracting files from .rar archives, and cleaning up
temporary directories.

The tests cover various scenarios, including loading JSON data from regular files and
.rar archives, handling errors such as file not found and JSON decode errors, and
ensuring proper cleanup of temporary directories.
"""

import json
import os
import tempfile
import pytest
import patoolib
from src.helpers.data_loader import load_json_data, extract_rar_file, cleanup_temp_directory

# Sample JSON data
sample_json_data = [{"key1": "value1"}, {"key2": "value2"}]


@pytest.fixture
def setup_temp_dir():
    """
    Fixture to set up and clean up a temporary directory for testing.

    Yields:
        str: The path to the temporary directory.
    """
    temp_dir = tempfile.mkdtemp()
    yield temp_dir
    cleanup_temp_directory(temp_dir)


def test_load_json_data_from_file(mocker):
    """
    Test loading JSON data from a regular file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.

    Asserts:
        The data loaded from the file matches the sample JSON data.
    """
    # Mocking the open function to simulate reading from a file. The mock will return
    # the data from `sample_json_data` as if it were read from "test.json".
    # The data contained is from the `sample_json_data` list.
    mock_open = mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data="\n".join(json.dumps(item) for item in sample_json_data)),
    )

    # Here we call the actual `load_json_data` function, which uses `open`. Since `open`
    # is mocked, the mock version of `open` is used, and it returns the mocked data
    # instead of reading from a real file. This allows us to test how `load_json_data`
    # handles the returned data.
    data = load_json_data("test.json")

    # Since we just want to know if the data is opened and read correctly, we can assert that the data is equal to the sample data.
    assert data == sample_json_data
    mock_open.assert_called_once_with("test.json", "r", encoding="utf-8")


def test_load_json_data_from_rar(mocker, setup_temp_dir):
    """
    Test loading JSON data from a .rar archive.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
        setup_temp_dir (str): The path to the temporary directory.

    Asserts:
        The data loaded from the .rar archive matches the sample JSON data.
    """
    temp_dir = setup_temp_dir  # Retrieve the temporary directory path for the test.

    # Mock the function `create_temp_directory` to simulate the creation of a temporary directory.
    # Instead of actually creating a directory, it will return the pre-defined `temp_dir` path.
    mock_create_temp_directory = mocker.patch( # pylint: disable=unused-variable
        "src.helpers.data_loader.create_temp_directory", return_value=temp_dir
    )

    # Mock the function `extract_rar_file` to simulate extracting the .rar file.
    # This simulates extracting a file called "test.rar" into the `temp_dir` and returns the path to the extracted file.
    # Note that the actual extraction process is not happening; we're mocking it to return a mock path.
    mock_extract_rar_file = mocker.patch(
        "src.helpers.data_loader.extract_rar_file",
        return_value=os.path.join(temp_dir, "extracted.json"),
    )

    # Mock the `open` function to simulate opening the extracted JSON file and reading its content.
    # Instead of actually opening a file, it returns the data from `sample_json_data` as if it were read from "extracted.json".
    # This simulates the file reading without needing the file to exist.
    mock_open = mocker.patch(
        "builtins.open",
        mocker.mock_open(read_data="\n".join(json.dumps(item) for item in sample_json_data)),
    )

    # Call the function `load_json_data("test.rar")`. Since `extract_rar_file` is mocked, it will simulate extracting
    # the .rar file and return the path to the extracted file. The `open` function is also mocked to simulate reading
    # from that extracted file and return the `sample_json_data`.
    data, temp_dir = load_json_data("test.rar")

    # Assert that the data loaded from the mock matches the expected sample data.
    # If the data is being read correctly, it should match the `sample_json_data`.
    assert data == sample_json_data

    # Ensure that the mocked `extract_rar_file` function was called once with the expected arguments:
    # - The .rar file path ("test.rar")
    # - The path to the temporary directory (`temp_dir`)
    mock_extract_rar_file.assert_called_once_with("test.rar", temp_dir)

    # Ensure that the mocked `open` function was called once to simulate opening the extracted file
    # and reading it with the expected arguments:
    # - The path to the extracted file (`os.path.join(temp_dir, "extracted.json")`)
    # - Reading mode "r" with encoding "utf-8"
    mock_open.assert_called_once_with(
        os.path.join(temp_dir, "extracted.json"), "r", encoding="utf-8"
    )


def test_cleanup_temp_directory(setup_temp_dir):
    """
    Test the cleanup_temp_directory function to ensure it deletes the temporary directory
    and its contents.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
        setup_temp_dir (str): The path to the temporary directory.

    Asserts:
        The temporary directory and its contents are deleted.
    """
    temp_dir = setup_temp_dir

    # Create some dummy files and directories inside the temp directory using custom functions
    os.makedirs(os.path.join(temp_dir, "subdir"))
    with open(os.path.join(temp_dir, "file.txt"), "w", encoding="utf-8") as f:
        f.write("dummy content")

    # Ensure the directory and its contents exist
    assert os.path.exists(temp_dir)
    assert os.path.exists(os.path.join(temp_dir, "subdir"))
    assert os.path.exists(os.path.join(temp_dir, "file.txt"))

    # Call the cleanup function
    cleanup_temp_directory(temp_dir)

    # Ensure the directory and its contents are deleted
    assert not os.path.exists(temp_dir), "The temporary directory should be deleted."


def test_extract_rar_file_error(mocker, setup_temp_dir):
    """
    Test handling of PatoolError when extracting a .rar file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
        setup_temp_dir (str): The path to the temporary directory.

    Asserts:
        The PatoolError is raised and handled correctly.
    """
    temp_dir = setup_temp_dir

    # Mocking the necessary functions
    mock_extract_archive = mocker.patch(    # pylint: disable=unused-variable
        "patoolib.extract_archive", side_effect=patoolib.util.PatoolError("Mocked error")
    )

    # Call the function
    result = extract_rar_file("test.rar", temp_dir)

    # Ensure the function handles the error correctly
    assert result is None


def test_load_json_data_no_file_found_in_rar(mocker, setup_temp_dir):
    """
    Test handling of scenario where no file is found in the .rar archive.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.
        setup_temp_dir (str): The path to the temporary directory.

    Asserts:
        The function raises a FileNotFoundError when no file is found in the .rar archive.
    """
    # Mock the `extract_rar_file` to return None (indicating no file was found in the .rar archive)
    mock_extract_rar_file = mocker.patch(
        "src.helpers.data_loader.extract_rar_file", return_value=None
    )

    # Mock the `create_temp_directory` function to return a dummy temp directory
    mock_create_temp_directory = mocker.patch(    # pylint: disable=unused-variable
        "src.helpers.data_loader.create_temp_directory", return_value=setup_temp_dir
    )

    # Test case where the file is a .rar archive and no file is extracted
    rar_path = "dummy_path/test.rar"

    # Call the function and expect a FileNotFoundError
    with pytest.raises(FileNotFoundError, match=f"No file found in the .rar archive: {rar_path}"):
        load_json_data(rar_path)

    # Ensure that `extract_rar_file` was called with the expected arguments
    mock_extract_rar_file.assert_called_once_with(rar_path, setup_temp_dir)


def test_load_json_data_file_not_found(mocker):
    """
    Test handling of FileNotFoundError when loading JSON data from a file.

    Args:
        mocker (pytest_mock.plugin.MockerFixture): The mocker fixture.

    Asserts:
        The function returns an empty list and the appropriate print message is triggered.
    """
    # Mock the `open` function to raise a FileNotFoundError
    mock_open = mocker.patch("builtins.open", side_effect=FileNotFoundError)

    # Test case where the file does not exist
    file_path = "non_existent_file.json"
    # Call the function and expect a FileNotFoundError
    with pytest.raises(FileNotFoundError, match=f"No file found in the .rar archive: {file_path}"):
        load_json_data(file_path)

    mock_open.assert_called_once_with(file_path, "r", encoding="utf-8")

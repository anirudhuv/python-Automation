# Folder Cleanup Automation

## Overview

This project provides a simple solution for automating the cleanup of unwanted folders, such as temporary folders, using Python scripts and a batch file on a Windows environment.

## Project Structure

- **spacecleaner.py**: Python script responsible for deleting unwanted folders.
- **spacecleaner.bat**: Batch file to execute the Python script.

## Prerequisites

- Python is required to run the cleanup script. Ensure that Python is installed on your system.
- The `os` module, which is part of the Python standard library, is used for folder manipulation.

## Usage

1. Customize the `spacecleaner.py` file to include the paths of unwanted folders you want to delete. Add or modify paths as needed.
2. Double-click on the `spacecleaner.bat` file to execute the cleanup script.
3. The Python script will run and delete the specified unwanted folders.

## Important Notes

- Exercise caution when specifying folder paths in the Python script to avoid unintentional deletion.
- The batch file includes a `pause` command to keep the command prompt window open after the script finishes. This allows you to review any output or error messages.

## Customization

- Update the `spacecleaner.py` file to include the paths of additional unwanted folders or customize the deletion logic.
- Adjust the batch file (`spacecleaner.bat`) based on your Python environment and script requirements.

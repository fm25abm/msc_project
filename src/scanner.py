"""
This script runs Google OSV-Scanner on the specified project and saves
the results as a JSON file.

Parameters:
    project_path (str): Path to the project to scan.
    output_file (str): Path where the JSON output will be saved.

Returns:
    bool: True if the scan completed successfully, otherwise False.
"""
import subprocess

def run_scan(project_path, output_file):

    command = [
        "osv-scanner",
        "scan",
        project_path,
        "--format",
        "json"
    ]

    try:
        with open(output_file, "w") as file:
            subprocess.run(command, stdout=file)

        print(f"Scan completed successfully.\n Results saved to {output_file}")
        return True

    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return False
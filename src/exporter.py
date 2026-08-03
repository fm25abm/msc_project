"""
Exports processed vulnerability data to a JSON file.
"""

import json


def export_results(vulnerabilities, output_path):

    with open(output_path, "w", encoding="utf-8") as file:
        json.dump(vulnerabilities, file, indent=4)

    print(f"Processed results saved to {output_path}")